# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyCollectibleDefinition:
    """Defines a."""

    acquisition_info: "DestinyCollectibleAcquisitionBlock"
    display_properties: "DestinyDisplayPropertiesDefinition"
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    item_hash: int
    parent_node_hashes: t.Sequence[
        int
    ]  # A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    presentation_info: "DestinyPresentationChildBlock"
    presentation_node_type: "DestinyPresentationNodeType"
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    scope: "DestinyScope"  # Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis.
    source_hash: int  # This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources. I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though. This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.
    source_string: str  # A human readable string for a hint about how to acquire the item.
    state_info: "DestinyCollectibleStateBlock"
    trait_hashes: t.Sequence[int]
    trait_ids: t.Sequence[str]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "scope": to_json(self.scope),
            "sourceString": to_json(self.source_string),
            "sourceHash": to_json(self.source_hash),
            "itemHash": to_json(self.item_hash),
            "acquisitionInfo": to_json(self.acquisition_info),
            "stateInfo": to_json(self.state_info),
            "presentationInfo": to_json(self.presentation_info),
            "presentationNodeType": to_json(self.presentation_node_type),
            "traitIds": to_json(self.trait_ids),
            "traitHashes": to_json(self.trait_hashes),
            "parentNodeHashes": to_json(self.parent_node_hashes),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyCollectibleAcquisitionBlock:
    acquire_material_requirement_hash: int
    acquire_timestamp_unlock_value_hash: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "acquireMaterialRequirementHash": to_json(
                self.acquire_material_requirement_hash
            ),
            "acquireTimestampUnlockValueHash": to_json(
                self.acquire_timestamp_unlock_value_hash
            ),
        }


@dt.dataclass(frozen=True)
class DestinyCollectibleStateBlock:
    obscured_override_item_hash: int
    requirements: "DestinyPresentationNodeRequirementsBlock"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "obscuredOverrideItemHash": to_json(self.obscured_override_item_hash),
            "requirements": to_json(self.requirements),
        }


from bungieapi.generated.components.schemas.destiny import DestinyScope  # noqa: E402
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyPresentationNodeType,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.presentation import (  # noqa: E402
    DestinyPresentationChildBlock,
    DestinyPresentationNodeRequirementsBlock,
)
