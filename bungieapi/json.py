import functools as ft
import typing as t
from enum import Enum


def to_json(obj: t.Any) -> t.Any:
    if not obj:
        return None
    if hasattr(obj, "to_json"):
        data = obj.to_json()
        if isinstance(data, dict):
            data = {k: v for k, v in data.items() if v}
        return data

    return to_json_for_simple(obj)


@ft.singledispatch
def to_json_for_simple(obj: t.Any) -> t.Any:
    return obj


@to_json_for_simple.register
def to_json_array(xs: list) -> t.Sequence:
    return [to_json(x) for x in xs]


@to_json_for_simple.register
def to_json_dict(obj: dict) -> t.Mapping:
    return {k: to_json(v) for k, v in obj}


@to_json_for_simple.register
def to_json_enum(obj: Enum) -> t.Any:
    return to_json(obj.value)
