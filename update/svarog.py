import typing as t

from svarog import Svarog
from svarog.checks import has_annotated_init
from svarog.forges import _clean_annotations


svarog = Svarog(snake_case=True)

svarog.register_mold(
    lambda t: "forge" in t.__dict__, lambda t, data, forge: t.forge(t, data, forge)
)
svarog.add_filter(lambda t: hasattr(t, "filter"), lambda t, data: t.filter(t, data))


def force_none(type_: t.Type, data: t.Mapping) -> t.Mapping:
    not_provided = {
        name: None
        for name, value in _clean_annotations(type_.__init__)
        if name != "return" and name not in data
    }
    return {**not_provided, **data}


svarog.add_filter(has_annotated_init, force_none)

forge = svarog.forge
