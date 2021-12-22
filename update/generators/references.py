import typing as t
import functools as ft
from .. import openapi as api
import itertools as it


@ft.singledispatch
def references(obj: t.Union[api.Reference, api.Schema]) -> t.Iterator[api.Reference]:
    yield from []


@references.register
def reference_reference(reference: api.Reference) -> t.Iterator[api.Reference]:
    yield reference


@references.register
def reference_object(object: api.Object) -> t.Iterator[api.Reference]:
    for child in it.chain(object.properties.values() if object.properties else [], [object.additional_properties] if object.additional_properties else []):
        yield from references(child)


@references.register
def reference_integer(integer: api.Integer) -> t.Iterator[api.Reference]:
    if integer.enum_reference:
        yield integer.enum_reference


@references.register
def reference_array(array: api.Array) -> t.Iterator[api.Reference]:
    yield from references(array.items)