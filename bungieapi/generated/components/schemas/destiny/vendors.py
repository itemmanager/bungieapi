# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyVendorReceipt:
    """If a character purchased an item that is refundable, a Vendor Receipt
    will be created on the user's Destiny Profile.

    These expire after a configurable period of time, but until then can
    be used to get refunds on items. BNet does not provide the ability
    to refund a purchase *yet*, but you know.
    """

    currency_paid: t.Optional[
        t.Sequence["DestinyItemQuantity"]
    ] = None  # The amount paid for the item, in terms of items that were consumed in the purchase and their quantity.
    expires_on: t.Optional[
        str
    ] = None  # The date at which this receipt is rendered invalid.
    item_received: t.Optional[
        "DestinyItemQuantity"
    ] = None  # The item that was received, and its quantity.
    license_unlock_hash: t.Optional[
        int
    ] = None  # The unlock flag used to determine whether you still have the purchased item.
    purchased_by_character_id: t.Optional[
        int
    ] = None  # The ID of the character who made the purchase.
    refund_policy: t.Optional[
        "DestinyVendorItemRefundPolicy"
    ] = None  # Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details.
    sequence_number: t.Optional[int] = None  # The identifier of this receipt.
    time_to_expiration: t.Optional[
        int
    ] = None  # The seconds since epoch at which this receipt is rendered invalid.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "currencyPaid": to_json(self.currency_paid),
            "itemReceived": to_json(self.item_received),
            "licenseUnlockHash": to_json(self.license_unlock_hash),
            "purchasedByCharacterId": to_json(self.purchased_by_character_id),
            "refundPolicy": to_json(self.refund_policy),
            "sequenceNumber": to_json(self.sequence_number),
            "timeToExpiration": to_json(self.time_to_expiration),
            "expiresOn": to_json(self.expires_on),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyItemQuantity,
    DestinyVendorItemRefundPolicy,
)
