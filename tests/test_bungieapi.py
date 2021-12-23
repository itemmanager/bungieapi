import pytest

from bungieapi import Client, __version__
from bungieapi.generated.components.schemas.destiny.config import DestinyManifest


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
        result = await root.destiny2.search_destiny_player_by_bungie_name(-1)
        assert result
