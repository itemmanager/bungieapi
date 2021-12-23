# generated by update to not change manually
from bungieapi.base import BaseClient
from bungieapi.forge import forge
from bungieapi.generated.components.responses import (
    CEListOfPartnerOfferSkuHistoryClientResponse,
    booleanClientResponse,
)


class Client(BaseClient):
    async def claim_partner_offer(
        self,
    ) -> booleanClientResponse:
        """Claim a partner offer as the authenticated user."""
        query = None
        result = await self.post(path="/Tokens/Partner/ClaimOffer/", query=query)
        return forge(booleanClientResponse, result)

    async def apply_missing_partner_offers_without_claim(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
    ) -> booleanClientResponse:
        """Apply a partner offer to the targeted user.

        This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.
        Parameters:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
        """
        query = None
        result = await self.post(
            path=f"/Tokens/Partner/ApplyMissingOffers/{partner_application_id}/{target_bnet_membership_id}/",
            query=query,
        )
        return forge(booleanClientResponse, result)

    async def get_partner_offer_sku_history(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
    ) -> CEListOfPartnerOfferSkuHistoryClientResponse:
        """Returns the partner sku and offer history of the targeted user.

        Elevated permissions are required to see users that are not yourself.
        Parameters:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
        """
        query = None
        result = await self.get(
            path=f"/Tokens/Partner/History/{partner_application_id}/{target_bnet_membership_id}/",
            query=query,
        )
        return forge(CEListOfPartnerOfferSkuHistoryClientResponse, result)
