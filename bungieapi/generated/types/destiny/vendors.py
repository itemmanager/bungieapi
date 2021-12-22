# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyVendorReceipt:
    """'If a character purchased an item that is refundable, a Vendor Receipt
    will be created on the user's Destiny Profile.

    These expire after a configurable period of time, but until then can
    be used to get refunds on items. BNet does not provide the ability
    to refund a purchase *yet*, but you know.
    """

    currency_paid: t.Sequence["DestinyItemQuantity"]
    item_received: "DestinyItemQuantity"
    license_unlock_hash: int
    purchased_by_character_id: int
    refund_policy: "DestinyVendorItemRefundPolicy"
    sequence_number: int
    time_to_expiration: int
    expires_on: str


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny import DestinyItemQuantity  # noqa: E402
from bungieapi.generated.types.destiny import (
    DestinyVendorItemRefundPolicy,
)  # noqa: E402
