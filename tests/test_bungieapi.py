import pytest

from bungieapi import Client, __version__
from bungieapi.generated.components.schemas import BungieMembershipType
from bungieapi.generated.components.schemas.destiny import DestinyComponentType
from bungieapi.generated.components.schemas.destiny.config import DestinyManifest
from bungieapi.generated.components.schemas.exceptions import PlatformErrorCodes
from bungieapi.generated.components.schemas.user import ExactSearchRequest, UserInfoCard


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
async def test_can_get_manifest(client: Client):
    async with client as root:
        response = await root.destiny2.get_destiny_manifest()
        assert isinstance(response.response, DestinyManifest)


@pytest.mark.asyncio
async def test_can_get_historical_stats_definition(client: Client):
    async with client as root:
        response = await root.destiny2.get_historical_stats_definition()
        assert any(
            medal_stat.medal_tier_hash.hash
            for medal_stat in response.response.values()
            if medal_stat.medal_tier_hash
        )


@pytest.mark.asyncio
async def test_can_search_by_player_name(client: Client):
    async with client as root:
        result = await root.destiny2.search_destiny_player_by_bungie_name(
            ExactSearchRequest(display_name="the-the-whistler", display_name_code=5666),
            -1,
        )
        assert all(isinstance(r, UserInfoCard) for r in result.response)


@pytest.mark.asyncio
async def test_can_get_application_api_usage(user_client: Client, application_id: int):
    async with user_client as root:
        result = await root.app.get_application_api_usage(application_id)
        assert result.response


@pytest.mark.asyncio
async def test_can_get_global_alerts(client: Client):
    async with client as root:
        result = await root.get_global_alerts(includestreaming=True)
        assert result.error_code == PlatformErrorCodes.SUCCESS


@pytest.mark.asyncio
async def test_can_get_membership_informations(user_client: Client, membership_id: int):
    async with user_client as root:
        response = await root.user.get_membership_data_for_current_user()
        assert response.response.bungie_net_user.psn_display_name == "the-the-whistler"


@pytest.mark.asyncio
async def test_can_get_characters(user_client: Client, membership_id: int):
    async with user_client as root:
        response = await root.destiny2.get_profile(
            4611686018432226653,
            membership_type=BungieMembershipType.TIGER_PSN,
            components=[
                DestinyComponentType.CHARACTERS,
                DestinyComponentType.CHARACTER_EQUIPMENT,
                DestinyComponentType.CHARACTER_ACTIVITIES,
                DestinyComponentType.PRESENTATION_NODES,
            ],
        )
        assert response.error_code == PlatformErrorCodes.SUCCESS
