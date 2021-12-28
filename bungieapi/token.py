"""Cli tool to generate bungie api token for user."""
import argparse
import asyncio
import dataclasses as dt
import os
import ssl
import typing as t
import webbrowser
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

from aiohttp import web

from bungieapi import Client
from bungieapi.base import Token


CERT_DIR = Path(__file__).parent / "certs"


async def token(
    redirect_url: str, client_id: int, client_secret: str, api_key: str
) -> Token:
    state = str(uuid4())
    parsed = urlparse(redirect_url)
    if parsed.scheme != "https":
        raise RuntimeError("only https is allowed as redirect url scheme")
    if parsed.hostname != "localhost":
        raise RuntimeError("only localhost redirect urls are supported for now")

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(
        certfile=str(CERT_DIR / "localhost.pem"),
        keyfile=str(CERT_DIR / "localhost-key.pem"),
    )

    app = web.Application()
    have_code = asyncio.Event()

    code: t.Optional[str] = None

    async def get_code(request):
        nonlocal code
        if request.query["state"] != state:
            raise RuntimeError("oauth state check failed")
        code = request.query["code"]
        have_code.set()
        return web.Response(text="BungieApi authorized, You can close this tab now")

    app.add_routes([web.get(parsed.path, get_code)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, parsed.hostname, parsed.port, ssl_context=ctx)
    await site.start()

    webbrowser.open(
        f"https://www.bungie.net/en/OAuth/Authorize?response_type=code&client_id={client_id}&state={state}"
    )

    await have_code.wait()
    assert code
    await runner.cleanup()

    async with Client.from_credentials(api_key=api_key) as root:
        return await root.app.from_authorization_code(
            code, client_id=client_id, client_secret=client_secret
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "token",
        description="CLI tool to generate user refresh token. "
        "Redirect_url and client_id can be obtained after creating app on https://www.bungie.net/en/Application",
    )
    parser.add_argument(
        "--redirect-url", "-r", default=os.environ.get("BUNGIE_API_REDIRECT_URL")
    )
    parser.add_argument(
        "--client-id", "-c", default=os.environ.get("BUNGIE_API_CLIENT_ID"), type=int
    )
    parser.add_argument(
        "--client-secret", "-s", default=os.environ.get("BUNGIE_API_CLIENT_SECRET")
    )
    parser.add_argument("--api-key", "-a", default=os.environ.get("BUNGIE_API_KEY"))
    parser.add_argument(
        "--output",
        "-o",
        choices=["all"] + [f.name for f in dt.fields(Token)],
        default="all",
    )
    options = parser.parse_args()

    if not (redirect_url := options.redirect_url):
        raise RuntimeError(
            "redirect url not set. Please set BUNGIE_API_REDIRECT_URL or provide it as command argument"
        )
    if not (client_id := options.client_id):
        raise RuntimeError(
            "client id not set. Please set BUNGIE_API_CLIENT_ID or provide as command argument"
        )
    if not (client_secret := options.client_secret):
        raise RuntimeError(
            "client secret not set. Please set BUNGIE_API_CLIENT_SECRET= or provide it as command argument"
        )
    if not (api_key := options.api_key):
        raise RuntimeError(
            "api key is not set. PLease set BUNGIE_API_KEY= or provide as command argument"
        )
    my_token = asyncio.run(
        token(
            redirect_url=redirect_url,
            client_id=client_id,
            client_secret=client_secret,
            api_key=api_key,
        )
    )
    if options.output == "all":
        for k, v in my_token.__dict__.items():
            print(f"{k}: {v}")
    else:
        print(getattr(my_token, options.output))
