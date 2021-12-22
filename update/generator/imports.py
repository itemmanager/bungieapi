import functools as ft
import itertools as it
import typing as t

from .. import openapi as api
from .references import references


@ft.singledispatch
def generate_imports(
    input: t.Union[api.Operation, api.Schema], module: t.Sequence[str]
) -> t.Iterator[str]:
    raise NotImplementedError(f"generate_imports not defined for {type(input)}")


@generate_imports.register
def generate_imports_operation(
    operation: api.Operation, module: t.Sequence[str]
) -> t.Iterator[str]:
    for schema in it.chain(
        (parameter.type for parameter in operation.parameters),
        (operation.response.schema,),
    ):
        yield from generate_imports_schema(schema, module)


@generate_imports.register
def generate_imports_schema(
    schema: api.Schema, module: t.Sequence[str]
) -> t.Iterator[str]:
    for reference in references(schema):
        *ref_module, class_name = reference.class_name.split(".")
        if not reference.local(module):
            yield f"from bungieapi.generated.{'.'.join(ref_module)} import {reference.name}"
