# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class PartnerOfferClaimRequest:
    bungie_net_membership_id: int
    partner_offer_id: str
    transaction_id: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "PartnerOfferId": to_json(self.partner_offer_id),
            "BungieNetMembershipId": to_json(self.bungie_net_membership_id),
            "TransactionId": to_json(self.transaction_id),
        }


@dt.dataclass(frozen=True)
class PartnerOfferSkuHistoryResponse:
    all_offers_applied: bool
    claim_date: str
    localized_description: str
    localized_name: str
    sku_identifier: str
    sku_offers: t.Sequence["PartnerOfferHistoryResponse"]
    transaction_id: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "SkuIdentifier": to_json(self.sku_identifier),
            "LocalizedName": to_json(self.localized_name),
            "LocalizedDescription": to_json(self.localized_description),
            "ClaimDate": to_json(self.claim_date),
            "AllOffersApplied": to_json(self.all_offers_applied),
            "TransactionId": to_json(self.transaction_id),
            "SkuOffers": to_json(self.sku_offers),
        }


@dt.dataclass(frozen=True)
class PartnerOfferHistoryResponse:
    is_consumable: bool
    localized_description: str
    localized_name: str
    partner_offer_key: str
    quantity_applied: int
    apply_date: t.Optional[str] = None
    membership_id: t.Optional[int] = None
    membership_type: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "PartnerOfferKey": to_json(self.partner_offer_key),
            "MembershipId": to_json(self.membership_id),
            "MembershipType": to_json(self.membership_type),
            "LocalizedName": to_json(self.localized_name),
            "LocalizedDescription": to_json(self.localized_description),
            "IsConsumable": to_json(self.is_consumable),
            "QuantityApplied": to_json(self.quantity_applied),
            "ApplyDate": to_json(self.apply_date),
        }


@dt.dataclass(frozen=True)
class PartnerRewardHistoryResponse:
    partner_offers: t.Sequence["PartnerOfferSkuHistoryResponse"]
    twitch_drops: t.Sequence["TwitchDropHistoryResponse"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "PartnerOffers": to_json(self.partner_offers),
            "TwitchDrops": to_json(self.twitch_drops),
        }


@dt.dataclass(frozen=True)
class TwitchDropHistoryResponse:
    description: str
    title: str
    claim_state: t.Optional[int] = None
    created_at: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Title": to_json(self.title),
            "Description": to_json(self.description),
            "CreatedAt": to_json(self.created_at),
            "ClaimState": to_json(self.claim_state),
        }


@dt.dataclass(frozen=True)
class BungieRewardDisplay:
    objective_display_properties: "RewardDisplayProperties"
    reward_display_properties: "RewardDisplayProperties"
    user_reward_availability_model: "UserRewardAvailabilityModel"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "UserRewardAvailabilityModel": to_json(self.user_reward_availability_model),
            "ObjectiveDisplayProperties": to_json(self.objective_display_properties),
            "RewardDisplayProperties": to_json(self.reward_display_properties),
        }


@dt.dataclass(frozen=True)
class UserRewardAvailabilityModel:
    availability_model: "RewardAvailabilityModel"
    is_available_for_user: bool
    is_unlocked_for_user: bool

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "AvailabilityModel": to_json(self.availability_model),
            "IsAvailableForUser": to_json(self.is_available_for_user),
            "IsUnlockedForUser": to_json(self.is_unlocked_for_user),
        }


@dt.dataclass(frozen=True)
class RewardAvailabilityModel:
    collectible_definitions: t.Sequence["CollectibleDefinitions"]
    decrypted_token: str
    game_earn_by_date: str
    has_existing_code: bool
    has_offer: bool
    is_loyalty_reward: bool
    is_offer: bool
    offer_applied: bool
    record_definitions: t.Sequence["DestinyRecordDefinition"]
    redemption_end_date: str
    shopify_end_date: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "HasExistingCode": to_json(self.has_existing_code),
            "RecordDefinitions": to_json(self.record_definitions),
            "CollectibleDefinitions": to_json(self.collectible_definitions),
            "IsOffer": to_json(self.is_offer),
            "HasOffer": to_json(self.has_offer),
            "OfferApplied": to_json(self.offer_applied),
            "DecryptedToken": to_json(self.decrypted_token),
            "IsLoyaltyReward": to_json(self.is_loyalty_reward),
            "ShopifyEndDate": to_json(self.shopify_end_date),
            "GameEarnByDate": to_json(self.game_earn_by_date),
            "RedemptionEndDate": to_json(self.redemption_end_date),
        }


@dt.dataclass(frozen=True)
class CollectibleDefinitions:
    collectible_definition: "DestinyCollectibleDefinition"
    destiny_inventory_item_definition: "DestinyInventoryItemDefinition"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "CollectibleDefinition": to_json(self.collectible_definition),
            "DestinyInventoryItemDefinition": to_json(
                self.destiny_inventory_item_definition
            ),
        }


@dt.dataclass(frozen=True)
class RewardDisplayProperties:
    description: str
    image_path: str
    name: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Name": to_json(self.name),
            "Description": to_json(self.description),
            "ImagePath": to_json(self.image_path),
        }


from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinyInventoryItemDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.collectibles import (  # noqa: E402
    DestinyCollectibleDefinition,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.records import (  # noqa: E402
    DestinyRecordDefinition,
)
