import dataclasses as dt
import typing as t

from svarog import Svarog


svarog = Svarog(snake_case=True)


def force_none(type_: t.Type, data: t.Mapping) -> t.Mapping:
    no_defaults = {
        f.name
        for f in dt.fields(type_)
        if f.default is dt.MISSING and f.default_factory is dt.MISSING  # type: ignore
    }
    not_provided = {name: None for name in no_defaults if name not in data}
    return {**not_provided, **data}


svarog.add_filter(dt.is_dataclass, force_none)

forge = svarog.forge

__all__ = ["forge"]
