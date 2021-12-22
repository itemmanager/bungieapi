import functools as ft
import typing as t

from svarog.tools import camel_to_snake

from .. import openapi as api
from .literals import literal_bare


@ft.singledispatch
def generate_schema(
    schema: api.Schema, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    yield f"{name} = t.Any"


@generate_schema.register
def generate_object(
    object: api.Object, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:

    yield f"@dt.dataclass(frozen=True)"
    yield f"class {name}:"
    if object.description:
        yield f"    ''''{object.description}'''"
    if not object.properties and not object.additional_properties:
        yield "    ..."
    if object.properties:
        for name, property in object.properties.items():
            yield f"    {camel_to_snake(name)}: {literal_bare(property, module)}"
    if object.additional_properties:
        yield f"    additional: t.Mapping[str, {literal_bare(object.additional_properties, [])}]"
