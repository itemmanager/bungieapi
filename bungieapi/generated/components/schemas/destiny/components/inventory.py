# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyPlatformSilverComponent:
    platform_silver: t.Optional[
        t.Mapping[str, "DestinyItemComponent"]
    ] = None  # If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "platformSilver": to_json(self.platform_silver),
        }


@dt.dataclass(frozen=True)
class DestinyCurrenciesComponent:
    """This component provides a quick lookup of every item the requested
    character has and how much of that item they have.

    Requesting this component will allow you to circumvent manually
    putting together the list of which currencies you have for the
    purpose of testing currency requirements on an item being purchased,
    or operations that have costs. You *could* figure this out yourself
    by doing a GetCharacter or GetProfile request and forming your own
    lookup table, but that is inconvenient enough that this feels like a
    worthwhile (and optional) redundency. Don't bother requesting it if
    you have already created your own lookup from prior
    GetCharacter/GetProfile calls.
    """

    item_quantities: t.Optional[
        t.Mapping[str, int]
    ] = None  # A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing. This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "itemQuantities": to_json(self.item_quantities),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.entities.items import (
    DestinyItemComponent,
)  # noqa: E402
