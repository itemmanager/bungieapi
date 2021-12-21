from svarog import Svarog

svarog = Svarog(snake_case=True)

svarog.register_mold(
    lambda t: "forge" in t.__dict__, lambda t, data, forge: t.forge(t, data, forge)
)
svarog.register_filter(
    lambda t: hasattr(t, "filter"), lambda t, data, forge: t.filter(t, data, forge)
)

forge = svarog.forge
