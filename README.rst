<<<<<<< HEAD
<<<<<<< HEAD
Bungie Api Client
-----------------

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

=======
Bungie Api
=======
Bungie Api Client
>>>>>>> b1cf740 (improve make file)
----

Python Client for https://github.com/Bungie-net/api/blob/master/openapi-2.json

Main features
====
 * Typed
 * Generated directly from bungie swagger file


Usage
====

>>> import os from bungieapi import Client
>>> async def get_manifest() -> DestinyManifest:
...     async with Client.from_credentials(api_key=os.environ['BUNGIE_API_KEY']) as client:
...         return await (client.destiny2.get_destiny_manifest()).response

<<<<<<< HEAD
Plan for future:
 - autogenerate from swagger
 - move radegast to correct place
>>>>>>> 9f87fdc (before movce to generic)
=======
>>>>>>> b1cf740 (improve make file)
