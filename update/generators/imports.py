import typing as t
import functools as ft
import itertools as it

from .references import references
from .. import openapi as api

@ft.singledispatch
def generate_imports(input: t.Union[api.Operation, api.Schema], module: t.Sequence[str]):
    raise NotImplementedError()


@generate_imports.register
def generate_imports_operation(operation: api.Operation, module: t.Sequence[str]) -> t.Iterator[str]:
    for schema in it.chain( (parameter.type for parameter in operation.parameters), (operation.response.schema,)):
        yield from generate_imports_schema(schema, module)



@generate_imports.register
def generate_imports_schema(schema: api.Schema, module: t.Sequence[str]) -> t.Iterator[str]:
    for reference in references(schema):
        *ref_module, class_name = reference.class_name.split('.')
        if not reference.local(module):
            yield f"from bungieapi.generated.{'.'.join(ref_module)} import {reference.name}"
