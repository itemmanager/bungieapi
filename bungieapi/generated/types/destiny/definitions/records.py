# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyRecordDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    scope: "DestinyScope"  # Indicates whether this Record's state is determined on a per-character or on an account-wide basis.
    presentation_info: "DestinyPresentationChildBlock"
    lore_hash: int
    objective_hashes: t.Sequence[int]
    record_value_style: "DestinyRecordValueStyle"
    for_title_gilding: bool
    title_info: "DestinyRecordTitleBlock"
    completion_info: "DestinyRecordCompletionBlock"
    state_info: "SchemaRecordStateBlock"
    requirements: "DestinyPresentationNodeRequirementsBlock"
    expiration_info: "DestinyRecordExpirationBlock"
    interval_info: "DestinyRecordIntervalBlock"  # Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval
    reward_items: t.Sequence[
        "DestinyItemQuantity"
    ]  # If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.  However, note that some records intentionally have "hidden" rewards. These will not be returned in this list.
    presentation_node_type: "DestinyPresentationNodeType"
    trait_ids: t.Sequence[str]
    trait_hashes: t.Sequence[int]
    parent_node_hashes: t.Sequence[
        int
    ]  # A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!


@dt.dataclass(frozen=True)
class DestinyRecordTitleBlock:
    has_title: bool
    titles_by_gender: t.Mapping[str, str]
    titles_by_gender_hash: t.Mapping[
        str, str
    ]  # For those who prefer to use the definitions.
    gilding_tracking_record_hash: int


@dt.dataclass(frozen=True)
class DestinyRecordCompletionBlock:
    partial_completion_objective_count_threshold: int  # The number of objectives that must be completed before the objective is considered "complete"
    score_value: int
    should_fire_toast: bool
    toast_style: "DestinyRecordToastStyle"


@dt.dataclass(frozen=True)
class SchemaRecordStateBlock:
    featured_priority: int
    obscured_string: str


@dt.dataclass(frozen=True)
class DestinyRecordExpirationBlock:
    """If this record has an expiration after which it cannot be earned, this
    is some information about that expiration."""

    has_expiration: bool
    description: str
    icon: str


@dt.dataclass(frozen=True)
class DestinyRecordIntervalBlock:
    interval_objectives: t.Sequence["DestinyRecordIntervalObjective"]
    interval_rewards: t.Sequence["DestinyRecordIntervalRewards"]
    original_objective_array_insertion_index: int


@dt.dataclass(frozen=True)
class DestinyRecordIntervalObjective:
    interval_objective_hash: int
    interval_score_value: int


@dt.dataclass(frozen=True)
class DestinyRecordIntervalRewards:
    interval_reward_items: t.Sequence["DestinyItemQuantity"]


from bungieapi.generated.types.destiny import DestinyItemQuantity  # noqa: E402
from bungieapi.generated.types.destiny import DestinyPresentationNodeType  # noqa: E402
from bungieapi.generated.types.destiny import DestinyRecordToastStyle  # noqa: E402
from bungieapi.generated.types.destiny import DestinyRecordValueStyle  # noqa: E402
from bungieapi.generated.types.destiny import DestinyScope  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
from bungieapi.generated.types.destiny.definitions.presentation import (
    DestinyPresentationChildBlock,
)  # noqa: E402
from bungieapi.generated.types.destiny.definitions.presentation import (
    DestinyPresentationNodeRequirementsBlock,
)  # noqa: E402
