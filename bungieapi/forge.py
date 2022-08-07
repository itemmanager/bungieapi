import dataclasses as dt
import typing as t

from svarog import Svarog


T = t.TypeVar("T")


class NonStrictSvarog(Svarog):
    def forge(self, type_: t.Type[T], data: t.Any) -> T:
        if data is None:
            return None  # type: ignore

        return super().forge(type_, data)


svarog = NonStrictSvarog(snake_case=True)


def force_none(type_: t.Type, data: t.Mapping) -> t.Mapping:
    no_defaults = {
        f.name
        for f in dt.fields(type_)
        if f.default is dt.MISSING and f.default_factory is dt.MISSING
    }
    not_provided = {name: None for name in no_defaults if name not in data}
    return {**not_provided, **data}


svarog.add_filter(dt.is_dataclass, force_none)

forge = svarog.forge

__all__ = ["forge"]
