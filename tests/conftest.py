import os

import pytest

from bungieapi.client import Client, Credentials


@pytest.fixture
def api_key() -> str:
    return os.environ["BUNGIE_API_KEY"]


@pytest.fixture
def credentials(api_key) -> Credentials:
    return Credentials(api_key=api_key)


@pytest.fixture
def client(credentials) -> Client:
    return Client(credentials=credentials)
