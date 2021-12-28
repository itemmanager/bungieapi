=================
Bungie Api Client
=================


.. image:: https://img.shields.io/pypi/v/bungieapi.svg
        :target: https://pypi.python.org/pypi/bungieapi

.. image:: https://github.com/itemmanager/bungieapi/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/itemmanager/bungieapi/actions/workflows/tests.yml

.. image:: https://readthedocs.org/projects/bungieapi/badge/?version=latest
        :target: https://bungieapi.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Python Client for https://github.com/Bungie-net/api/blob/master/openapi-2.json

Main features
=============
 * Typed
 * Generated directly from bungie swagger file


Usage
=====

For basic use::

    import os
    from bungieapi import Client

    async def get_manifest() -> DestinyManifest:
        async with Client.from_credentials(
            api_key=os.environ['BUNGIE_API_KEY']
        ) as client:
            return await (client.destiny2.get_destiny_manifest()).response

Requests with user tokens::

    async with with Client.from_credentials(api_key=API_KEY, token=USER_TOKEN):
        async with user_client as root:
            response = await root.user.get_membership_data_for_current_user()


Use refresh token to get user token::

    async def get_token(
        client: Client, refresh_token: str, client_id: int, client_secret: str
    ) -> Token:
        async with client as root:
            token = await root.app.from_refresh_token(
                refresh_token, client_id=client_id, client_secret=client_secret
            )
        return token

It is possible to generate token for existing bungie account::

    $> python -m bungieapi.token --help

for more details