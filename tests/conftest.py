import asyncio
import os
from datetime import datetime, timedelta

import pytest

from bungieapi.base import Token
from bungieapi.client import Client, Credentials
from bungieapi.forge import forge


@pytest.fixture
def api_key() -> str:
    return os.environ["BUNGIE_API_KEY"]


@pytest.fixture
def client_id() -> int:
    return int(os.environ["BUNGIE_API_CLIENT_ID"])


@pytest.fixture
def client_secret() -> str:
    return os.environ["BUNGIE_API_CLIENT_SECRET"]


@pytest.fixture
def application_id() -> int:
    return 40154


@pytest.fixture
def credentials(api_key) -> Credentials:
    return Credentials(api_key=api_key)


@pytest.fixture(scope="session")
def loop():
    return asyncio.new_event_loop()


async def get_token(
    client: Client, refresh_token: str, client_id: int, client_secret: str
) -> Token:
    async with client as root:
        token = await root.app.from_refresh_token(
            refresh_token, client_id=client_id, client_secret=client_secret
        )
    return token


@pytest.fixture
def user_token(request, client, loop, refresh_token, client_id, client_secret) -> Token:
    token_raw, token_ttl_str = request.config.cache.get(
        "bungieapi/user/user_token", (None, None)
    )
    if token_ttl_str:
        token_ttl = datetime.fromisoformat(token_ttl_str)
        if token_ttl < datetime.now():
            token_raw = None
    if token_raw is None:
        token = loop.run_until_complete(
            get_token(client, refresh_token, client_id, client_secret)
        )

        token_ttl = datetime.now() + timedelta(minutes=59)
        request.config.cache.set(
            "bungieapi/user/user_token", (token.to_json(), token_ttl.isoformat())
        )
    else:
        token = forge(Token, token_raw)
    return token


@pytest.fixture
def user_credentials(api_key, user_token: Token) -> Credentials:
    return Credentials(api_key=api_key, token=user_token.access_token)


@pytest.fixture
def membership_id(user_token: Token) -> int:
    return user_token.membership_id


@pytest.fixture
def client(credentials) -> Client:
    return Client(credentials=credentials)


@pytest.fixture
def user_client(user_credentials: Credentials) -> Client:
    return Client(user_credentials)


@pytest.fixture
def refresh_token() -> str:
    return os.environ["REFRESH_TOKEN"]
