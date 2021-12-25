import dataclasses as dt
import typing as t

import aiohttp

from bungieapi.generated.clients.root import Client as RootClient


BASE_URL = "https://www.bungie.net"
BASE_PATH = "/Platform"


@dt.dataclass
class Credentials:
    api_key: str


class Client:
    _session = t.Optional[aiohttp.ClientSession]

    def __init__(self, credentials: Credentials, base_url: str = BASE_URL) -> None:
        self._base_url = base_url
        self._session = None
        self._credentials = credentials

    async def __aenter__(self) -> RootClient:
        self._session = aiohttp.ClientSession(
            base_url=self._base_url, headers={"X-Api-Key": self._credentials.api_key}
        )
        return RootClient(self._session, BASE_PATH)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        assert self._session  # type: ignore
        await self._session.close()  # type: ignore

    @classmethod
    def from_credentials(cls, api_key: str) -> "Client":
        return cls(Credentials(api_key=api_key))
