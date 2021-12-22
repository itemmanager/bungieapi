# generated by update to not change manually
import dataclasses as dt


@dt.dataclass(frozen=True)
class DestinyBreakerTypeDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    enum_value: "DestinyBreakerType"  # We have an enumeration for Breaker types for quick reference. This is the current definition's breaker type enum value.
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!


from bungieapi.generated.types.destiny import DestinyBreakerType  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
