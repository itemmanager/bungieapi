import functools as ft
import typing as t


@ft.singledispatch
def find_all_refs(in_: t.Any) -> t.Iterator[str]:
    yield from []


@find_all_refs.register
def find_all_refs_dict(in_: dict) -> t.Iterator[str]:
    try:
        yield in_["$ref"]
    except KeyError:
        for v in in_.values():
            yield from find_all_refs(v)


@find_all_refs.register
def find_all_refs_sequence(in_: list) -> t.Iterator[str]:
    for v in in_:
        yield from find_all_refs(v)


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return "".join(x.title() for x in components)
