import typing as t
from enum import Flag

from svarog.types import Forge

from bungieapi.forge import svarog


T = t.TypeVar("T")


def is_(predicate_type: t.Type) -> t.Callable[[t.Type], bool]:
    """Return type predicate to mold."""

    def _inner(t: t.Type) -> bool:
        try:
            return t.__origin__ == predicate_type
        except AttributeError:
            return False

    return _inner


class ManifestReference(t.Generic[T]):
    __slots__ = ("hash", "type")
    hash: str
    type: t.Type[T]

    def __init__(self, type: t.Type[T], hash: str):
        self.hash = hash
        self.type = type

    def __repr__(self):
        return f"<ManifestReference type={self.type!r} hash={self.hash} >"


def forge_reference(
    type_: t.Type[ManifestReference[T]], data: t.Mapping[str, t.Any], forge: Forge
) -> ManifestReference[T]:
    (reference_type,) = type_.__args__  # type: ignore
    if isinstance(reference_type, t.ForwardRef):
        reference_type = svarog._resolve_forward_ref(reference_type)

    return ManifestReference(type=reference_type, hash=str(data))


svarog.register_mold(is_(ManifestReference), forge_reference)


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
