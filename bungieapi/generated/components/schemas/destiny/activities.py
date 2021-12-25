# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyPublicActivityStatus:
    """Represents the public-facing status of an activity: any data about what
    is currently active in the Activity, regardless of an individual
    character's progress in it."""

    challenge_objective_hashes: t.Optional[
        t.Sequence[int]
    ] = None  # Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.
    modifier_hashes: t.Optional[
        t.Sequence[int]
    ] = None  # The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.
    reward_tooltip_items: t.Optional[
        t.Sequence["DestinyItemQuantity"]
    ] = None  # If the activity itself provides any specific "mock" rewards, this will be the items and their quantity. Why "mock", you ask? Because these are the rewards as they are represented in the tooltip of the Activity. These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "challengeObjectiveHashes": to_json(self.challenge_objective_hashes),
            "modifierHashes": to_json(self.modifier_hashes),
            "rewardTooltipItems": to_json(self.reward_tooltip_items),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (
    DestinyItemQuantity,
)  # noqa: E402
