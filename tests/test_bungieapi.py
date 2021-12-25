import pytest

from bungieapi import Client, __version__
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
async def test_can_search_by_player_name(client: Client):
    async with client as root:
        result = await root.destiny2.search_destiny_player_by_bungie_name(
            ExactSearchRequest(display_name="the-the-whistler", display_name_code=5666),
            -1,
        )
        assert all(isinstance(r, UserInfoCard) for r in result.response)


@pytest.mark.asyncio
@pytest.mark.skip("Need token")
async def test_can_get_application_api_usage(client: Client, application_id: int):
    async with client as root:
        result = await root.app.get_application_api_usage(application_id)
        assert result.response


@pytest.mark.asyncio
async def test_can_get_global_alerts(client: Client):
    async with client as root:
        result = await root.get_global_alerts(includestreaming=True)
        assert result.error_code == PlatformErrorCodes.SUCCESS
