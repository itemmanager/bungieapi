# generated by update to not change manually
import dataclasses as dt


@dt.dataclass(frozen=True)
class DestinyPowerCapDefinition:
    """Defines a 'power cap' (limit) for gear items, based on the rarity tier
    and season of release."""

    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    power_cap: int  # The raw value for a power cap.
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
