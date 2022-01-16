import functools as ft
import typing as t

from update import openapi as api


def literal(t: t.Union[api.Reference, api.Schema], module: t.Sequence[str]) -> str:
    if t.nullable:
        return f"t.Optional[{literal_bare(t, module)}]"
    return literal_bare(t, module)


@ft.singledispatch
def literal_bare(t: t.Union[api.Reference, api.Schema], module: t.Sequence[str]) -> str:
    raise NotImplementedError(f"not implemented for {type(t)}")


@literal_bare.register
def literal_object(t: api.Object, module: t.Sequence[str]) -> str:
    if t.properties:
        raise RuntimeError("Cannot generate inline object")
    if t.all_of:
        assert len(t.all_of) == 1
        return literal_bare(t.all_of[0], module)
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
    return f'"{t.name}"'


@literal_bare.register
def literal_bool(t: api.Boolean, module: t.Sequence[str]) -> str:
    return "bool"


@literal_bare.register
def literal_array(t: api.Array, module: t.Sequence[str]) -> str:
    return f"t.Sequence[{literal_bare(t.items, module)}]"


@literal_bare.register
def literal_number(t: api.Number, module: t.Sequence[str]) -> str:
    return "float"
