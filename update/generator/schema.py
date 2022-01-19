import functools as ft
import typing as t

from .. import openapi as api
from ..tools import camel_to_snake
from .literals import literal, literal_bare


@ft.singledispatch
def generate_schema(
    schema: api.Schema, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    raise Exception(f"cannot generate type: {type(schema)} ({name})")


def linear_comment(something: t.Any) -> str:
    description = getattr(something, "description", "")
    if description:
        description = description.replace("\n", " ").replace("\r", "")
        return f" # {description}"
    return ""


def metadata(something: t.Any) -> str:
    description = getattr(something, "description", "")
    if description:
        if "\n" in description:
            return f"metadata={{'description': '''{description}'''}}"
        else:
            description = description.replace("'", r"\'")
            return f"metadata={{'description': '{description}'}}"
    return ""


@generate_schema.register
def generate_object(
    object: api.Object, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:

    yield "@dt.dataclass(frozen=True)"
    yield f"class {name}:"
    if object.description:
        yield f"    '''{object.description}'''"
    if not object.properties and not object.additional_properties:
        yield "    ..."
    if object.properties:
        required = [
            (name, property)
            for name, property in object.properties.items()
            if not property.nullable
        ]
        nullable = [
            (name, property)
            for name, property in object.properties.items()
            if property.nullable
        ]

        for name, property in sorted(required):
            if meta := metadata(property):
                yield f"    {camel_to_snake(name)}: {literal_bare(property, module)} = dt.field({meta})"
            else:
                yield f"    {camel_to_snake(name)}: {literal_bare(property, module)}"

        for name, property in sorted(nullable):
            if meta := metadata(property):
                yield f"    {camel_to_snake(name)}: {literal(property, module)} = dt.field(default=None, {meta})"
            else:
                yield f"    {camel_to_snake(name)}: {literal(property, module)} = None"

    if object.additional_properties:
        yield f"    additional: t.Mapping[str, {literal_bare(object.additional_properties, [])}]  = dt.field(default_factory=dict)"

    yield "    def to_json(self) -> t.Mapping[str, t.Any]:"
    yield "        return {"
    for name, property in (object.properties or {}).items():
        yield f'"{name}": to_json(self.{camel_to_snake(name)}),'
    yield "}"
    if object.all_of:
        raise NotImplementedError("cannot generate dataclass with parent")


@generate_schema.register
def generate_integer(
    integer: api.Integer, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    if integer.is_bitmask:
        assert integer.enum_values
        yield f"class {name}(BitMask):"
        if integer.description:
            yield f'    """{integer.description}"""'
        for value in integer.enum_values:
            yield f"    {camel_to_snake(value.identifier).upper()} = {value.numeric_value}  {linear_comment(value)}"
    elif integer.enum_values:
        yield f"class {name}(Enum):"
        if integer.description:
            yield f'    """{integer.description}"""'
        for value in integer.enum_values:
            yield f"    {camel_to_snake(value.identifier).upper()} = {value.numeric_value}  {linear_comment(value)}"
    else:
        yield f"{name} = int"


@generate_schema.register
def generate_array(
    array: api.Array, name: str, module: t.Sequence[str]
) -> t.Iterator[str]:
    yield f"{name} = t.Sequence[{literal_bare(array.items, module)}]"
