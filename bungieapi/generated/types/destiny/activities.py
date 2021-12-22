# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types.destiny import DestinyItemQuantity


@dt.dataclass(frozen=True)
class DestinyPublicActivityStatus:
    """'Represents the public-facing status of an activity: any data about what
    is currently active in the Activity, regardless of an individual
    character's progress in it."""

    challenge_objective_hashes: t.Sequence[int]
    modifier_hashes: t.Sequence[int]
    reward_tooltip_items: t.Sequence[DestinyItemQuantity]
