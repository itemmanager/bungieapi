# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyVendorComponent:
    """This component contains essential/summary information about the
    vendor."""

    can_purchase: t.Optional[bool] = None  # If True, you can purchase from the Vendor.
    enabled: t.Optional[
        bool
    ] = None  # If True, the Vendor is currently accessible.  If False, they may not actually be visible in the world at the moment.
    next_refresh_date: t.Optional[
        str
    ] = None  # The date when this vendor's inventory will next rotate/refresh. Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different. Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.
    progression: t.Optional[
        "DestinyProgression"
    ] = None  # If the Vendor has a related Reputation, this is the Progression data that represents the character's Reputation level with this Vendor.
    seasonal_rank: t.Optional[
        int
    ] = None  # If this vendor has a seasonal rank, this will be the calculated value of that rank. How nice is that? I mean, that's pretty sweeet. It's a whole 32 bit integer.
    vendor_hash: t.Optional[
        int
    ] = None  # The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.
    vendor_location_index: t.Optional[
        int
    ] = None  # An index into the vendor definition's "locations" property array, indicating which location they are at currently. If -1, then the vendor has no known location (and you may choose not to show them in your UI as a result. I mean, it's your bag honey)

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "canPurchase": to_json(self.can_purchase),
            "progression": to_json(self.progression),
            "vendorLocationIndex": to_json(self.vendor_location_index),
            "seasonalRank": to_json(self.seasonal_rank),
            "vendorHash": to_json(self.vendor_hash),
            "nextRefreshDate": to_json(self.next_refresh_date),
            "enabled": to_json(self.enabled),
        }


@dt.dataclass(frozen=True)
class DestinyVendorCategoriesComponent:
    """A vendor can have many categories of items that they sell.

    This component will return the category information for available
    items, as well as the index into those items in the user's sale item
    list. Note that, since both the category and items are indexes, this
    data is Content Version dependent. Be sure to check that your
    content is up to date before using this data. This is an
    unfortunate, but permanent, limitation of Vendor data.
    """

    categories: t.Optional[
        t.Sequence["DestinyVendorCategory"]
    ] = None  # The list of categories for items that the vendor sells, in rendering order. These categories each point to a "display category" in the displayCategories property of the DestinyVendorDefinition, as opposed to the other categories.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "categories": to_json(self.categories),
        }


@dt.dataclass(frozen=True)
class DestinyVendorCategory:
    """Information about the category and items currently sold in that
    category."""

    display_category_index: t.Optional[
        int
    ] = None  # An index into the DestinyVendorDefinition.displayCategories property, so you can grab the display data for this category.
    item_indexes: t.Optional[
        t.Sequence[int]
    ] = None  # An ordered list of indexes into items being sold in this category (DestinyVendorDefinition.itemList) which will contain more information about the items being sold themselves. Can also be used to index into DestinyVendorSaleItemComponent data, if you asked for that data to be returned.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayCategoryIndex": to_json(self.display_category_index),
            "itemIndexes": to_json(self.item_indexes),
        }


@dt.dataclass(frozen=True)
class DestinyVendorSaleItemComponent:
    """Request this component if you want the details about an item being sold
    in relation to the character making the request: whether the character can
    buy it, whether they can afford it, and other data related to purchasing
    the item.

    Note that if you want instance, stats, etc... data for the item,
    you'll have to request additional components such as ItemInstances,
    ItemPerks etc... and acquire them from the DestinyVendorResponse's
    "items" property.
    """

    api_purchasable: t.Optional[
        bool
    ] = None  # If true, this item can be purchased through the Bungie.net API.
    augments: t.Optional[
        "DestinyVendorItemState"
    ] = None  # A flags enumeration value representing the current state of any "state modifiers" on the item being sold. These are meant to correspond with some sort of visual indicator as to the augmentation: for instance, if an item is on sale or if you already own the item in question. Determining how you want to represent these in your own app (or if you even want to) is an exercise left for the reader.
    costs: t.Optional[
        t.Sequence["DestinyItemQuantity"]
    ] = None  # A summary of the current costs of the item.
    failure_indexes: t.Optional[
        t.Sequence[int]
    ] = None  # Indexes in to the "failureStrings" lookup table in DestinyVendorDefinition for the given Vendor. Gives some more reliable failure information for why you can't purchase an item. It is preferred to use these over requiredUnlocks and unlockStatuses: the latter are provided mostly in case someone can do something interesting with it that I didn't anticipate.
    item_hash: t.Optional[
        int
    ] = None  # The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
    item_value_visibility: t.Optional[
        t.Sequence[bool]
    ] = None  # If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).
    override_next_refresh_date: t.Optional[
        str
    ] = None  # If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date. Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
    override_style_item_hash: t.Optional[
        int
    ] = None  # If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
    quantity: t.Optional[int] = None  # How much of the item you'll be getting.
    required_unlocks: t.Optional[
        t.Sequence[int]
    ] = None  # If you can't buy the item due to a complex character state, these will be hashes for DestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlocks have human readable information: it is not guaranteed that Unlocks will have human readable strings, and your application will have to handle that) Prefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes.
    sale_status: t.Optional[
        "VendorItemStatus"
    ] = None  # A flag indicating whether the requesting character can buy the item, and if not the reasons why the character can't buy it.
    unlock_statuses: t.Optional[
        t.Sequence["DestinyUnlockStatus"]
    ] = None  # If any complex unlock states are checked in determining purchasability, these will be returned here along with the status of the unlock check. Prefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes.
    vendor_item_index: t.Optional[
        int
    ] = None  # The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.  Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "saleStatus": to_json(self.sale_status),
            "requiredUnlocks": to_json(self.required_unlocks),
            "unlockStatuses": to_json(self.unlock_statuses),
            "failureIndexes": to_json(self.failure_indexes),
            "augments": to_json(self.augments),
            "itemValueVisibility": to_json(self.item_value_visibility),
            "vendorItemIndex": to_json(self.vendor_item_index),
            "itemHash": to_json(self.item_hash),
            "overrideStyleItemHash": to_json(self.override_style_item_hash),
            "quantity": to_json(self.quantity),
            "costs": to_json(self.costs),
            "overrideNextRefreshDate": to_json(self.override_next_refresh_date),
            "apiPurchasable": to_json(self.api_purchasable),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyItemQuantity,
    DestinyProgression,
    DestinyUnlockStatus,
    DestinyVendorItemState,
    VendorItemStatus,
)
from bungieapi.generated.components.schemas.destiny.entities.vendors import (
    DestinyVendorCategory,
)  # noqa: E402
