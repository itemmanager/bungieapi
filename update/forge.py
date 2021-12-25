import dataclasses as dt

from svarog import Svarog


svarog = Svarog(snake_case=True)

svarog.register_mold(
    lambda t: "forge" in t.__dict__, lambda t, data, forge: t.forge(t, data, forge)
)
svarog.add_filter(lambda t: hasattr(t, "filter"), lambda t, data: t.filter(t, data))


# TODO: client svarog to forge with force_none
svarog.add_filter(dt.is_dataclass, force_none)

forge = svarog.forge
