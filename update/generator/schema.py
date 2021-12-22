import functools as ft
import typing as t

from svarog.tools import camel_to_snake

from .. import openapi as api
from .literals import literal_bare


@ft.singledispatch
def generate_schema(
    schema: api.Schema, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    raise Exception(f"cannot generate type: {type(schema)} ({name})")
    # yield f"{name} = t.Any"


@generate_schema.register
def generate_object(
    object: api.Object, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:

    yield "@dt.dataclass(frozen=True)"
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
    if object.all_of:
        raise NotImplementedError("cannot generate dataclass with parent")


@generate_schema.register
def generate_integer(
    integer: api.Integer, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    if integer.enum_values:
        yield f"class {name}(Enum):"
        if integer.description:
            yield f'    """{integer.description}"""'
        for value in integer.enum_values:
            yield f"    {camel_to_snake(value.identifier).upper()} = {value.numeric_value}"
    else:
        yield f"{name} = int"


@generate_schema.register
def generate_array(
    array: api.Array, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    yield f"{name} = t.Sequence[{literal_bare(array.items, module)}]"
