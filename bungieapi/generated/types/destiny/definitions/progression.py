# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyProgressionLevelRequirementDefinition:
    """'These are pre-constructed collections of data that can be used to
    determine the Level Requirement for an item given a Progression to be
    tested (such as the Character's level).

    For instance, say a character receives a new Auto Rifle, and that Auto Rifle's DestinyInventoryItemDefinition.quality.progressionLevelRequirementHash property is pointing at one of these DestinyProgressionLevelRequirementDefinitions. Let's pretend also that the progressionHash it is pointing at is the Character Level progression. In that situation, the character's level will be used to interpolate a value in the requirementCurve property. The value picked up from that interpolation will be the required level for the item.
    """

    requirement_curve: t.Sequence["InterpolationPointFloat"]
    progression_hash: int
    hash: int
    index: int
    redacted: bool


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.interpolation import (
    InterpolationPointFloat,
)  # noqa: E402
