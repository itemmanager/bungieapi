import itertools as it
import typing as t
from pathlib import Path

from svarog.tools import camel_to_snake

from update.generator.clients import client, generate_clients_init
from update.generator.imports import generate_imports
from update.generator.schema import generate_schema
from update.generator.tools import suffix, with_preamble
from update.openapi import OpenApi, TypeTree


def type_module_generator(types: TypeTree, module: t.Sequence[str]) -> t.Iterator[str]:
    yield "import typing as t"
    yield "import dataclasses as dt"

    for schema in types.child_schema():
        yield from generate_schema(schema.schema, schema.schema_name, module)
    yield ""

    imports = list(
        it.chain(
            *(
                generate_imports(schema.schema, module)
                for schema in types.child_schema()
            )
        )
    )
    if imports:
        yield "# imported at the end to do not case circular imports for type annotations"

        yield from suffix(imports, "  # noqa: E402")


def types_generator(
    path: Path, types: TypeTree
) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    module = str(path / Path(types.name)).split("/")

    if any(types.child_types()):
        yield path / Path(types.name) / Path("__init__.py"), with_preamble(
            type_module_generator(types, module)
        )
    else:
        yield path / Path(f"{types.name}.py"), with_preamble(
            type_module_generator(types, module)
        )

    for sub_type in types.child_types():
        yield from types_generator(path / Path(types.name), sub_type)


def empty() -> t.Iterator[str]:
    yield from []


def generator(api: OpenApi) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    yield Path("__init__.py"), with_preamble(empty())
    root = api.operations_tree()

    yield Path("clients") / "__init__.py", with_preamble(generate_clients_init(root))

    for operation_tree in (root, *root.child_clients()):
        yield Path(
            "clients"
        ) / f"{camel_to_snake(operation_tree.name)}.py", with_preamble(
            client(operation_tree)
        )

    yield from types_generator(Path("."), api.types_tree())
