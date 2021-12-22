import typing as t
import functools as ft

from svarog.tools import camel_to_snake

from .. import openapi as api


def literal(t: t.Union[api.Reference, api.Schema], module: t.Sequence[str]) -> str:
    if not t.required:
        return f"t.Optional[{literal_bare(t, module)}]"
    return literal_bare(t, module)


@ft.singledispatch
def literal_bare(t: t.Union[api.Reference, api.Schema], module: t.Sequence[str]) -> str:
    raise NotImplementedError(f"not implemented for {type(t)}")


@literal_bare.register
def literal_object(t: api.Object, module: t.Sequence[str]) -> str:
    if t.properties:
        raise RuntimeError('Cannot generate inline object')
    if not t.additional_properties:
        return "t.Any"
    return f"t.Mapping[str, {literal_bare(t.additional_properties, module)}]"


@literal_bare.register
def literal_int(t: api.Integer, module: t.Sequence[str]) -> str:
    if t.enum_reference:
        return literal_bare(t.enum_reference, module)
    return "int"


@literal_bare.register
def literal_str(t: api.String, module: t.Sequence[str]) -> str:
    return "str"


@literal_bare.register
def literal_reference(t: api.Reference, module: t.Sequence[str]) -> str:
    if t.local(module):
        return f'"{t.name}"'
    return t.name


@literal_bare.register
def literal_bool(t: api.Boolean, module: t.Sequence[str]) -> str:
    return "bool"


@literal_bare.register
def literal_array(t: api.Array, module: t.Sequence[str]) -> str:
    return f"t.Sequence[{literal_bare(t.items, module)}]"


@literal_bare.register
def literal_number(t: api.Number, module: t.Sequence[str]) -> str:
    return f'float'

def indentation(input: t.Iterator[str], indentation: int) -> t.Iterator[str]:
    p = indentation * "    "
    for line in input:
        yield f"{p}{line}"


def generate_response(response: api.Response, name: str) -> t.Iterator[str]:
    assert response.schema.type == api.ApiType.OBJECT
    assert isinstance(response.schema, api.Object)
    yield from generate_schema(response.schema, name, [])


@ft.singledispatch
def generate_schema(schema: api.Schema, name: str, module: t.Sequence[str]) -> t.Iterator[str]:
    yield f"{name} = t.Any"
    # raise NotImplementedError()


@generate_schema.register
def generate_object(object: api.Object, name: str, module: t.Sequence[str]) -> t.Iterator[str]:

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