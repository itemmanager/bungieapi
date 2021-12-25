import functools as ft
import itertools as it
import typing as t

from .. import openapi as api
from .references import references


@ft.singledispatch
def generate_imports(
    input: t.Union[api.Operation, api.Schema, api.Reference], module: t.Sequence[str]
) -> t.Iterator[str]:
    raise NotImplementedError(f"generate_imports not defined for {type(input)}")


@generate_imports.register
def generate_imports_operation(
    operation: api.Operation, module: t.Sequence[str]
) -> t.Iterator[str]:
    schema: t.Union[api.Schema, api.Reference]
    for schema in it.chain(  # type: ignore
        (parameter.schema for parameter in operation.parameters),
        (operation.response,),
        (operation.request_body,) if operation.request_body else [],
    ):
        yield from generate_imports(schema, module)


@generate_imports.register
def generate_imports_schema(
    schema: api.Schema, module: t.Sequence[str]
) -> t.Iterator[str]:
    for reference in references(schema):
        yield from generate_import(reference, module)


@generate_imports.register
def generate_import(
    reference: api.Reference, module: t.Sequence[str]
) -> t.Iterator[str]:
    *ref_module, class_name = reference.class_name.split(".")
    if not reference.local(module):
        name = reference.name
        yield f"from {'.'.join(reference.module)} import {reference.name}"
