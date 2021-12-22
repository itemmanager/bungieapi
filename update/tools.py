import functools as ft
import re
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


CAMEL_RE_PRE = re.compile("(.)([A-Z][a-z]+)")
CAMEL_RE_POST = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(name: str) -> str:
    name = CAMEL_RE_PRE.sub(r"\1_\2", name)
    return CAMEL_RE_POST.sub(r"\1_\2", name).lower()
