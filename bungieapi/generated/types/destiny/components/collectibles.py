# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyCollectiblesComponent:
    collectibles: t.Mapping[str, "DestinyCollectibleComponent"]
    collection_categories_root_node_hash: int  # The hash for the root presentation node definition of Collection categories.
    collection_badges_root_node_hash: int  # The hash for the root presentation node definition of Collection Badges.


@dt.dataclass(frozen=True)
class DestinyCollectibleComponent:
    state: "DestinyCollectibleState"


@dt.dataclass(frozen=True)
class DestinyProfileCollectiblesComponent:
    recent_collectible_hashes: t.Sequence[
        int
    ]  # The list of collectibles determined by the game as having been "recently" acquired.
    newness_flagged_collectible_hashes: t.Sequence[
        int
    ]  # The list of collectibles determined by the game as having been "recently" acquired. The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.
    collectibles: t.Mapping[str, "DestinyCollectibleComponent"]
    collection_categories_root_node_hash: int  # The hash for the root presentation node definition of Collection categories.
    collection_badges_root_node_hash: int  # The hash for the root presentation node definition of Collection Badges.


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny import DestinyCollectibleState  # noqa: E402
