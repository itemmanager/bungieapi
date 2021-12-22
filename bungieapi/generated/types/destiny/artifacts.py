# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyArtifactProfileScoped:
    """'Represents a Seasonal Artifact and all data related to it for the
    requested Account.

    It can be combined with Character-scoped data for a full picture of
    what a character has available/has chosen, or just these settings
    can be used for overview information.
    """

    artifact_hash: int
    point_progression: "DestinyProgression"
    points_acquired: int
    power_bonus_progression: "DestinyProgression"
    power_bonus: int


@dt.dataclass(frozen=True)
class DestinyArtifactCharacterScoped:
    artifact_hash: int
    points_used: int
    reset_count: int
    tiers: t.Sequence["DestinyArtifactTier"]


@dt.dataclass(frozen=True)
class DestinyArtifactTier:
    tier_hash: int
    is_unlocked: bool
    points_to_unlock: int
    items: t.Sequence["DestinyArtifactTierItem"]


@dt.dataclass(frozen=True)
class DestinyArtifactTierItem:
    item_hash: int
    is_active: bool


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny import DestinyProgression  # noqa: E402
