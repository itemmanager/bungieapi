# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyPlugSetsComponent:
    """Sockets may refer to a "Plug Set": a set of reusable plugs that may be
    shared across multiple sockets (or even, in theory, multiple sockets over
    multiple items).

    This is the set of those plugs that we came across in the users'
    inventory, along with the values for plugs in the set. Any given set
    in this component may be represented in Character and Profile-level,
    as some plugs may be Profile-level restricted, and some character-
    level restricted. (note that the ones that are even more specific
    will remain on the actual socket component itself, as they cannot be
    reused)
    """

    plugs: t.Optional[
        t.Mapping[str, t.Sequence["DestinyItemPlug"]]
    ] = None  # The shared list of plugs for each relevant PlugSet, keyed by the hash identifier of the PlugSet (DestinyPlugSetDefinition).

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "plugs": to_json(self.plugs),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.sockets import (
    DestinyItemPlug,
)  # noqa: E402
