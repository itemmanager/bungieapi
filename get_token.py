import asyncio
import functools as ft
import os
import ssl
import webbrowser
from uuid import uuid4

from bungieapi import Client


CLIENT_ID = int(os.environ["BUNGIE_API_CLIENT_ID"])

from aiohttp import web


async def token2():
    state = str(uuid4())
    webbrowser.open(
        f"https://www.bungie.net/en/OAuth/Authorize?response_type=code&client_id={CLIENT_ID}&state={state}"
    )
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain("keys/localhost.pem", keyfile="keys/localhost-key.pem")

    app = web.Application()
    have_code = asyncio.Event()

    async def get_code(request):
        if request.query["state"] != state:
            raise RuntimeError("oauth state check failed")
        request.query["code"]
        print(request)
        await app.cleanup()
        have_code.set()
        return web.Response(text="You can close this tab now")

    app.add_routes([web.get("/bungie-api-test", ft.partial(get_code))])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8123, ssl_context=ctx)
    await site.start()
    await have_code.wait()
    await runner.cleanup()


async def token():
    print(
        await Client.from_credentials(api_key=os.environ["BUNGIE_API_KEY"]).token(
            client_id=CLIENT_ID,
            redirect_url="https://localhost:8123/bungie-api-test",
            certfile="keys/localhost.pem",
            keyfile="keys/localhost-key.pem",
        )
    )


if __name__ == "__main__":

    asyncio.run(token())
