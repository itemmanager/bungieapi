# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyMetricDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    lower_value_is_better: bool
    parent_node_hashes: t.Sequence[
        int
    ]  # A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    presentation_node_type: "DestinyPresentationNodeType"
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    tracking_objective_hash: int
    trait_hashes: t.Sequence[int]
    trait_ids: t.Sequence[str]


from bungieapi.generated.components.schemas.destiny import (
    DestinyPresentationNodeType,
)  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
