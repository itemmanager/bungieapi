import dataclasses as dt
import typing as t

import aiohttp

from bungieapi.generated.clients.root import Client as RootClient


BASE_URL = "https://www.bungie.net"
BASE_PATH = "/Platform"


@dt.dataclass
class Credentials:
    api_key: str
    token: t.Optional[str] = None


class Client:
    _session = t.Optional[aiohttp.ClientSession]

    def __init__(
        self,
        credentials: Credentials,
        base_url: str = BASE_URL,
        trace_configs: t.Sequence[aiohttp.TraceConfig] = (),
    ) -> None:
        self._base_url = base_url
        self._session = None
        self._credentials = credentials
        self._trace_configs = trace_configs

    async def __aenter__(self) -> RootClient:
        headers = {"X-Api-Key": self._credentials.api_key}
        if self._credentials.token:
            headers["Authorization"] = f"Bearer {self._credentials.token}"

        self._session = aiohttp.ClientSession(
            base_url=self._base_url,
            headers=headers,
            trace_configs=list(self._trace_configs),
        )
        return RootClient(self._session, BASE_PATH)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        assert self._session  # type: ignore
        await self._session.close()  # type: ignore

    @classmethod
    def from_credentials(cls, api_key: str, token: t.Optional[str] = None) -> "Client":
        return cls(Credentials(api_key=api_key, token=token))
