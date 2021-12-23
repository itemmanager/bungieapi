import itertools as it
import typing as t
from pathlib import Path

from svarog.tools import camel_to_snake

from update.generator.clients import client, generate_clients_init
from update.generator.imports import generate_imports
from update.generator.schema import generate_schema
from update.generator.tools import response_schema_name, suffix, with_preamble
from update.openapi import BindResponse, BindSchema, OpenApi, Tree


def responses_module_generator(
    tree: Tree[BindResponse], module: t.Sequence[str]
) -> t.Iterator[str]:
    yield "import typing as t"
    yield "import dataclasses as dt"
    yield "from enum import Enum"
    for bind_response in tree.child_leaf():
        yield from generate_schema(
            bind_response.response.schema,
            response_schema_name(bind_response.schema_name),
            module,
        )

    imports = list(
        it.chain(
            *(
                generate_imports(bind_response.response.schema, module)
                for bind_response in tree.child_leaf()
            )
        )
    )
    if imports:
        yield "# imported at the end to do not case circular imports for type annotations"

        yield from suffix(imports.__iter__(), "  # noqa: E402")


def schema_module_generator(
    types: Tree[BindSchema], module: t.Sequence[str]
) -> t.Iterator[str]:
    yield "import typing as t"
    yield "import dataclasses as dt"
    yield "from enum import Enum"

    for schema in types.child_leaf():
        try:
            yield from generate_schema(schema.schema, schema.schema_name, module)
        except:
            raise
    yield ""

    imports = list(
        it.chain(
            *(generate_imports(schema.schema, module) for schema in types.child_leaf())
        )
    )
    if imports:
        yield "# imported at the end to do not case circular imports for type annotations"

        yield from suffix(imports.__iter__(), "  # noqa: E402")


T = t.TypeVar("T")


def tree_generator(
    path: Path,
    tree: Tree[T],
    module_generator: t.Callable[[Tree[T], t.Sequence[str]], t.Iterator[str]],
) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    module = str(path / Path(tree.name)).split("/")

    if any(tree.child_nodes()):
        yield path / Path(tree.name) / Path("__init__.py"), with_preamble(
            module_generator(tree, module)
        )
    else:
        yield path / Path(f"{tree.name}.py"), with_preamble(
            module_generator(tree, module)
        )

    for sub_type in tree.child_nodes():
        yield from tree_generator(path / Path(tree.name), sub_type, module_generator)


def responses_generator(
    path: Path, tree: Tree[BindResponse]
) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    yield from tree_generator(path, tree, responses_module_generator)


def schemas_generator(
    path: Path, tree: Tree[BindSchema]
) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    yield from tree_generator(path, tree, schema_module_generator)


def empty() -> t.Iterator[str]:
    yield from []


def generator(api: OpenApi) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
    yield Path("__init__.py"), with_preamble(empty())
    root = api.operations_tree()

    yield Path("clients") / "__init__.py", with_preamble(generate_clients_init(root))

    for operation_tree in (root, *root.child_nodes()):
        yield Path(
            "clients"
        ) / f"{camel_to_snake(operation_tree.name)}.py", with_preamble(
            client(operation_tree)
        )

    yield Path(".") / "components" / "__init__.py", with_preamble(empty())
    yield from schemas_generator(Path(".") / "components", api.schema_tree())
    yield from responses_generator(Path(".") / "components", api.response_tree())
