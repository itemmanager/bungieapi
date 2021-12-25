# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyBreakerTypeDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    enum_value: "DestinyBreakerType"  # We have an enumeration for Breaker types for quick reference. This is the current definition's breaker type enum value.
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "enumValue": to_json(self.enum_value),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyBreakerType,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
