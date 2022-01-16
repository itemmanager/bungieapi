# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinyRecordDefinition:
    completion_info: "DestinyRecordCompletionBlock"
    display_properties: "DestinyDisplayPropertiesDefinition"
    expiration_info: "DestinyRecordExpirationBlock"
    for_title_gilding: bool
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    interval_info: "DestinyRecordIntervalBlock" = dt.field(
        metadata={
            "description": "Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval"
        }
    )
    objective_hashes: t.Sequence[int]
    parent_node_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents."
        }
    )
    presentation_info: "DestinyPresentationChildBlock"
    presentation_node_type: "DestinyPresentationNodeType"
    record_value_style: "DestinyRecordValueStyle"
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    requirements: "DestinyPresentationNodeRequirementsBlock"
    reward_items: t.Sequence["DestinyItemQuantity"] = dt.field(
        metadata={
            "description": """If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.
 However, note that some records intentionally have "hidden" rewards. These will not be returned in this list."""
        }
    )
    scope: "DestinyScope" = dt.field(
        metadata={
            "description": "Indicates whether this Record's state is determined on a per-character or on an account-wide basis."
        }
    )
    state_info: "SchemaRecordStateBlock"
    title_info: "DestinyRecordTitleBlock"
    trait_hashes: t.Sequence[int]
    trait_ids: t.Sequence[str]
    lore_hash: t.Optional[ManifestReference["DestinyLoreDefinition"]] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "scope": to_json(self.scope),
            "presentationInfo": to_json(self.presentation_info),
            "loreHash": to_json(self.lore_hash),
            "objectiveHashes": to_json(self.objective_hashes),
            "recordValueStyle": to_json(self.record_value_style),
            "forTitleGilding": to_json(self.for_title_gilding),
            "titleInfo": to_json(self.title_info),
            "completionInfo": to_json(self.completion_info),
            "stateInfo": to_json(self.state_info),
            "requirements": to_json(self.requirements),
            "expirationInfo": to_json(self.expiration_info),
            "intervalInfo": to_json(self.interval_info),
            "rewardItems": to_json(self.reward_items),
            "presentationNodeType": to_json(self.presentation_node_type),
            "traitIds": to_json(self.trait_ids),
            "traitHashes": to_json(self.trait_hashes),
            "parentNodeHashes": to_json(self.parent_node_hashes),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyRecordTitleBlock:
    has_title: bool
    titles_by_gender: t.Mapping[str, str]
    titles_by_gender_hash: t.Mapping[str, str] = dt.field(
        metadata={"description": "For those who prefer to use the definitions."}
    )
    gilding_tracking_record_hash: t.Optional[
        ManifestReference["DestinyRecordDefinition"]
    ] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "hasTitle": to_json(self.has_title),
            "titlesByGender": to_json(self.titles_by_gender),
            "titlesByGenderHash": to_json(self.titles_by_gender_hash),
            "gildingTrackingRecordHash": to_json(self.gilding_tracking_record_hash),
        }


@dt.dataclass(frozen=True)
class DestinyRecordCompletionBlock:
    score_value: int
    partial_completion_objective_count_threshold: int = dt.field(
        metadata={
            "description": 'The number of objectives that must be completed before the objective is considered "complete"'
        }
    )
    should_fire_toast: bool
    toast_style: "DestinyRecordToastStyle"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "partialCompletionObjectiveCountThreshold": to_json(
                self.partial_completion_objective_count_threshold
            ),
            "ScoreValue": to_json(self.score_value),
            "shouldFireToast": to_json(self.should_fire_toast),
            "toastStyle": to_json(self.toast_style),
        }


@dt.dataclass(frozen=True)
class SchemaRecordStateBlock:
    featured_priority: int
    obscured_string: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "featuredPriority": to_json(self.featured_priority),
            "obscuredString": to_json(self.obscured_string),
        }


@dt.dataclass(frozen=True)
class DestinyRecordExpirationBlock:
    """If this record has an expiration after which it cannot be earned, this
    is some information about that expiration."""

    description: str
    has_expiration: bool
    icon: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "hasExpiration": to_json(self.has_expiration),
            "description": to_json(self.description),
            "icon": to_json(self.icon),
        }


@dt.dataclass(frozen=True)
class DestinyRecordIntervalBlock:
    interval_objectives: t.Sequence["DestinyRecordIntervalObjective"]
    interval_rewards: t.Sequence["DestinyRecordIntervalRewards"]
    original_objective_array_insertion_index: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "intervalObjectives": to_json(self.interval_objectives),
            "intervalRewards": to_json(self.interval_rewards),
            "originalObjectiveArrayInsertionIndex": to_json(
                self.original_objective_array_insertion_index
            ),
        }


@dt.dataclass(frozen=True)
class DestinyRecordIntervalObjective:
    interval_objective_hash: ManifestReference["DestinyObjectiveDefinition"]
    interval_score_value: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "intervalObjectiveHash": to_json(self.interval_objective_hash),
            "intervalScoreValue": to_json(self.interval_score_value),
        }


@dt.dataclass(frozen=True)
class DestinyRecordIntervalRewards:
    interval_reward_items: t.Sequence["DestinyItemQuantity"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "intervalRewardItems": to_json(self.interval_reward_items),
        }


from bungieapi.generated.components.schemas.destiny import DestinyScope  # noqa: E402
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyItemQuantity,
    DestinyPresentationNodeType,
    DestinyRecordToastStyle,
    DestinyRecordValueStyle,
)
from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinyObjectiveDefinition,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.lore import (  # noqa: E402
    DestinyLoreDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.presentation import (  # noqa: E402
    DestinyPresentationChildBlock,
    DestinyPresentationNodeRequirementsBlock,
)
