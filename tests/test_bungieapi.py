import pytest

from bungieapi import __version__
from bungieapi import Client


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
async def test_can_get_manifest(client: Client):
    async with client as root:
        manifest = await root.destiny2.get_destiny_manifest()
        assert manifest
