import typing as t
from enum import Flag


T = t.TypeVar("T")


class ManifestReference(t.Generic[T]):
    __slots__ = ("hash",)

    def __init__(self, hash: int):
        self.hash = hash


F = t.TypeVar("F", bound=Flag)


def decompose(flag: F) -> t.Set[F]:
    """Decompose flag to atomic values."""
    all_values = {item.value: item.name for item in flag.__class__}
    item_value = flag.value
    result = set()
    for value, name in sorted(all_values.items(), reverse=True):
        if value and value <= item_value:
            item_value -= value
            assert name
            result.add(getattr(flag, name))
    return result
