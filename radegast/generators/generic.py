import typing as t
import functools as ft

from svarog.tools import camel_to_snake

from .. import openapi as api


def literal(t: t.Union[api.Reference, api.Schema]):
    literal = literal_bare(t)
    if not t.required:
        return f"t.Optional[{literal}]"
    return literal


@ft.singledispatch
def literal_bare(t: api.Schema):
    raise  NotImplementedError(f"not implemented for {type(t)}")


@literal_bare.register
def literal_object(t: api.Object):
    return 't.Any'


@literal_bare.register
def literal_int(t: api.Integer):
    return 'int'


@literal_bare.register
def literal_int(t: api.String):
    return 'str'


@literal_bare.register
def literal_int(t: api.Reference):
    return t.class_name


@literal_bare.register
def literal_bool(t: api.Boolean):
    return 'bool'


@literal_bare.register
def literal_array(t: api.Array):
    return f"t.Sequence[{literal_bare(t.items)}]"


def indentation(input: t.Sequence[str], indentation: int) -> t.Sequence[str]:
    p = indentation * "    "
    for line in input:
        yield f"{p}{line}"


def generate_response(response: api.Response, name: str) -> t.Sequence[str]:
    assert response.schema.type == api.ApiType.OBJECT
    assert isinstance(response.schema, api.Object)
    yield from generate_object(response.schema, name)


def generate_object(object: api.Object, name: str) -> t.Sequence[str]:
    yield f"@dt.dataclass(frozen=True)"
    yield f"class {name}:"
    if not object.properties and not object.additional_properties:
        yield "    ...."
    if object.properties:
        for name, property in object.properties.items():
            yield f"    {camel_to_snake(name)}: {literal_bare(property)}"