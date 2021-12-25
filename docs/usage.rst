=====
Usage
=====

To use BungieApi in a project::

    import os
    from bungieapi import Client

    async def get_manifest() -> DestinyManifest:
        async with Client.from_credentials(
            api_key=os.environ['BUNGIE_API_KEY']
        ) as client:
            return await (client.destiny2.get_destiny_manifest()).response

