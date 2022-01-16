# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyRecordsComponent:
    record_categories_root_node_hash: int  # The hash for the root presentation node definition of Triumph categories.
    record_seals_root_node_hash: int  # The hash for the root presentation node definition of Triumph Seals.
    records: t.Mapping[str, "DestinyRecordComponent"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "records": to_json(self.records),
            "recordCategoriesRootNodeHash": to_json(
                self.record_categories_root_node_hash
            ),
            "recordSealsRootNodeHash": to_json(self.record_seals_root_node_hash),
        }


@dt.dataclass(frozen=True)
class DestinyRecordComponent:
    interval_objectives: t.Sequence["DestinyObjectiveProgress"]
    intervals_redeemed_count: int
    objectives: t.Sequence["DestinyObjectiveProgress"]
    reward_visibilty: t.Sequence[
        bool
    ]  # If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.
    state: "DestinyRecordState"
    completed_count: t.Optional[
        int
    ] = None  # If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "state": to_json(self.state),
            "objectives": to_json(self.objectives),
            "intervalObjectives": to_json(self.interval_objectives),
            "intervalsRedeemedCount": to_json(self.intervals_redeemed_count),
            "completedCount": to_json(self.completed_count),
            "rewardVisibilty": to_json(self.reward_visibilty),
        }


@dt.dataclass(frozen=True)
class DestinyProfileRecordsComponent:
    active_score: int  # Your 'active' Triumphs score.
    legacy_score: int  # Your 'legacy' Triumphs score.
    lifetime_score: int  # Your 'lifetime' Triumphs score.
    record_categories_root_node_hash: int  # The hash for the root presentation node definition of Triumph categories.
    record_seals_root_node_hash: int  # The hash for the root presentation node definition of Triumph Seals.
    records: t.Mapping[str, "DestinyRecordComponent"]
    score: int  # Your 'active' Triumphs score, maintained for backwards compatibility.
    tracked_record_hash: t.Optional[
        int
    ] = None  # If this profile is tracking a record, this is the hash identifier of the record it is tracking.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "score": to_json(self.score),
            "activeScore": to_json(self.active_score),
            "legacyScore": to_json(self.legacy_score),
            "lifetimeScore": to_json(self.lifetime_score),
            "trackedRecordHash": to_json(self.tracked_record_hash),
            "records": to_json(self.records),
            "recordCategoriesRootNodeHash": to_json(
                self.record_categories_root_node_hash
            ),
            "recordSealsRootNodeHash": to_json(self.record_seals_root_node_hash),
        }


@dt.dataclass(frozen=True)
class DestinyCharacterRecordsComponent:
    featured_record_hashes: t.Sequence[int]
    record_categories_root_node_hash: int  # The hash for the root presentation node definition of Triumph categories.
    record_seals_root_node_hash: int  # The hash for the root presentation node definition of Triumph Seals.
    records: t.Mapping[str, "DestinyRecordComponent"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "featuredRecordHashes": to_json(self.featured_record_hashes),
            "records": to_json(self.records),
            "recordCategoriesRootNodeHash": to_json(
                self.record_categories_root_node_hash
            ),
            "recordSealsRootNodeHash": to_json(self.record_seals_root_node_hash),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyRecordState,
)
from bungieapi.generated.components.schemas.destiny.quests import (  # noqa: E402
    DestinyObjectiveProgress,
)
