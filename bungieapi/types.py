import typing as t

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


class BitMaskMeta(type):
    def __new__(metacls, cls, bases, classdict, **kwds):
        fields = {}
        if bases:
            for f in list(classdict):
                if not f.startswith("_"):
                    fields[f] = classdict.pop(f)
        bitmask_class = super().__new__(metacls, cls, bases, classdict, **kwds)

        for name, value in fields.items():
            setattr(bitmask_class, name, bitmask_class(value))
        setattr(bitmask_class, "_fields", fields)
        setattr(bitmask_class, "_values", {v: k for k, v in fields.items()})
        return bitmask_class


class BitMask(metaclass=BitMaskMeta):
    _fields: t.Mapping[str, int]
    _values: t.Mapping[int, str]

    def __init__(self, value: int):
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def __or__(self, other: "BitMask") -> "BitMask":
        return self.__class__(self._value | other._value)

    def __iter__(self) -> t.Iterator["BitMask"]:
        item_value = self._value
        for value, name in sorted(self._values.items(), reverse=True):
            if value and value <= item_value:
                item_value -= value
                yield getattr(self, name)

        assert item_value == 0

    def __repr__(self):
        return " | ".join(self._values[simple._value] for simple in self)
