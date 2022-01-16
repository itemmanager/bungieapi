import functools as ft
import itertools as it
import typing as t

from .. import openapi as api


@ft.singledispatch
def references(obj: t.Union[api.Reference, api.Schema]) -> t.Iterator[api.Reference]:
    yield from []


@references.register
def reference_reference(reference: api.Reference) -> t.Iterator[api.Reference]:
    yield reference


@references.register
def reference_object(object: api.Object) -> t.Iterator[api.Reference]:
    for child in it.chain(
        object.properties.values() if object.properties else [],
        [object.additional_properties] if object.additional_properties else [],
        object.all_of if object.all_of else [],
    ):
        yield from references(child)


@references.register
def reference_integer(integer: api.Integer) -> t.Iterator[api.Reference]:
    if integer.enum_reference:
        yield integer.enum_reference
    if integer.mapped_definition:
        yield integer.mapped_definition


@references.register
def reference_array(array: api.Array) -> t.Iterator[api.Reference]:
    yield from references(array.items)
