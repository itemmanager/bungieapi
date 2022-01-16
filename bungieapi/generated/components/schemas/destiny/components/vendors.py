# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinyVendorGroupComponent:
    """This component returns references to all of the Vendors in the response,
    grouped by categorizations that Bungie has deemed to be interesting, in the
    order in which both the groups and the vendors within that group should be
    rendered."""

    groups: t.Sequence[
        "DestinyVendorGroup"
    ]  # The ordered list of groups being returned.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groups": to_json(self.groups),
        }


@dt.dataclass(frozen=True)
class DestinyVendorGroup:
    """Represents a specific group of vendors that can be rendered in the
    recommended order.

    How do we figure out this order? It's a long story, and will likely
    get more complicated over time.
    """

    vendor_group_hash: ManifestReference["DestinyVendorGroupDefinition"]
    vendor_hashes: t.Sequence[
        int
    ]  # The ordered list of vendors within a particular group.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "vendorGroupHash": to_json(self.vendor_group_hash),
            "vendorHashes": to_json(self.vendor_hashes),
        }


@dt.dataclass(frozen=True)
class DestinyVendorBaseComponent:
    """This component contains essential/summary information about the
    vendor."""

    enabled: bool  # If True, the Vendor is currently accessible.  If False, they may not actually be visible in the world at the moment.
    next_refresh_date: str  # The date when this vendor's inventory will next rotate/refresh. Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different. Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.
    vendor_hash: ManifestReference[
        "DestinyVendorDefinition"
    ]  # The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "vendorHash": to_json(self.vendor_hash),
            "nextRefreshDate": to_json(self.next_refresh_date),
            "enabled": to_json(self.enabled),
        }


@dt.dataclass(frozen=True)
class DestinyVendorSaleItemBaseComponent:
    """The base class for Vendor Sale Item data.

    Has a bunch of character-agnostic state about the item being sold.
    Note that if you want instance, stats, etc... data for the item,
    you'll have to request additional components such as ItemInstances,
    ItemPerks etc... and acquire them from the DestinyVendorResponse's
    "items" property.
    """

    costs: t.Sequence[
        "DestinyItemQuantity"
    ]  # A summary of the current costs of the item.
    item_hash: ManifestReference[
        "DestinyInventoryItemDefinition"
    ]  # The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
    quantity: int  # How much of the item you'll be getting.
    vendor_item_index: int  # The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.  Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.
    api_purchasable: t.Optional[
        bool
    ] = None  # If true, this item can be purchased through the Bungie.net API.
    override_next_refresh_date: t.Optional[
        str
    ] = None  # If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date. Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
    override_style_item_hash: t.Optional[
        ManifestReference["DestinyInventoryItemDefinition"]
    ] = None  # If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "vendorItemIndex": to_json(self.vendor_item_index),
            "itemHash": to_json(self.item_hash),
            "overrideStyleItemHash": to_json(self.override_style_item_hash),
            "quantity": to_json(self.quantity),
            "costs": to_json(self.costs),
            "overrideNextRefreshDate": to_json(self.override_next_refresh_date),
            "apiPurchasable": to_json(self.api_purchasable),
        }


@dt.dataclass(frozen=True)
class DestinyPublicVendorComponent:
    """This component contains essential/summary information about the vendor
    from the perspective of a character-agnostic view."""

    enabled: bool  # If True, the Vendor is currently accessible.  If False, they may not actually be visible in the world at the moment.
    next_refresh_date: str  # The date when this vendor's inventory will next rotate/refresh. Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different. Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.
    vendor_hash: ManifestReference[
        "DestinyVendorDefinition"
    ]  # The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "vendorHash": to_json(self.vendor_hash),
            "nextRefreshDate": to_json(self.next_refresh_date),
            "enabled": to_json(self.enabled),
        }


@dt.dataclass(frozen=True)
class DestinyPublicVendorSaleItemComponent:
    """Has character-agnostic information about an item being sold by a vendor.

    Note that if you want instance, stats, etc... data for the item,
    you'll have to request additional components such as ItemInstances,
    ItemPerks etc... and acquire them from the DestinyVendorResponse's
    "items" property. For most of these, however, you'll have to ask for
    it in context of a specific character.
    """

    costs: t.Sequence[
        "DestinyItemQuantity"
    ]  # A summary of the current costs of the item.
    item_hash: ManifestReference[
        "DestinyInventoryItemDefinition"
    ]  # The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
    quantity: int  # How much of the item you'll be getting.
    vendor_item_index: int  # The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.  Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.
    api_purchasable: t.Optional[
        bool
    ] = None  # If true, this item can be purchased through the Bungie.net API.
    override_next_refresh_date: t.Optional[
        str
    ] = None  # If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date. Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
    override_style_item_hash: t.Optional[
        ManifestReference["DestinyInventoryItemDefinition"]
    ] = None  # If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "vendorItemIndex": to_json(self.vendor_item_index),
            "itemHash": to_json(self.item_hash),
            "overrideStyleItemHash": to_json(self.override_style_item_hash),
            "quantity": to_json(self.quantity),
            "costs": to_json(self.costs),
            "overrideNextRefreshDate": to_json(self.override_next_refresh_date),
            "apiPurchasable": to_json(self.api_purchasable),
        }


from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyItemQuantity,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinyInventoryItemDefinition,
    DestinyVendorDefinition,
    DestinyVendorGroupDefinition,
)
