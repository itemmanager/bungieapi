import typing as t


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
