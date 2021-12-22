# generated by update to not change manually
import dataclasses as dt


@dt.dataclass(frozen=True)
class DestinyActivityModifierDefinition:
    """'Modifiers - in Destiny 1, these were referred to as "Skulls" - are changes that can be applied to an Activity."""

    display_properties: "DestinyDisplayPropertiesDefinition"
    hash: int
    index: int
    redacted: bool


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
