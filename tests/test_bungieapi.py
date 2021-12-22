import pytest

from bungieapi import Client, __version__


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
async def test_can_get_manifest(client: Client):
    async with client as root:
        manifest = await root.destiny2.get_destiny_manifest()
        assert manifest
