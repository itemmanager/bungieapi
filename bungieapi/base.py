import dataclasses as dt
import typing as t

import aiohttp
from aiohttp import ClientResponse

from bungieapi.forge import forge
from bungieapi.generated.components.schemas.exceptions import PlatformErrorCodes

QueryInput = t.Any  # t.Union[None, str, bool, int, t.Sequence[Enum]]


def clean_query_value(in_: QueryInput) -> str:
    raise NotImplementedError()


@dt.dataclass(frozen=True)
class ApiError:
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, t.Any]


class ApiException(Exception):
    def __init__(self, error: ApiError):
        self._error = error

    def __repr__(self):
        return repr(self._error)


class BaseClient:
    def __init__(self, session: aiohttp.ClientSession, path: str) -> None:
        self._session = session
        self._path = path

    def _clean_query(self, query: t.Mapping[str, QueryInput]) -> t.Mapping[str, str]:
        return {k: clean_query_value(v) for k, v in query.items()}

    async def handle_error(self, response: ClientResponse) -> ClientResponse:
        if response.status == 400:
            raise ApiException(forge(ApiError, await response.json()))
        response.raise_for_status()
        return response

    async def get(
        self, path: str, query: t.Optional[t.Mapping[str, QueryInput]]
    ) -> t.Mapping[str, t.Any]:
        assert path[0] == "/"
        query = self._clean_query(query) if query else {}

        async with self._session.get(f"{self._path}{path}", params=query) as response:
            response = await self.handle_error(response)
            return await response.json()

    async def post(
        self, path: str, query: t.Optional[t.Mapping[str, QueryInput]]
    ) -> t.Mapping[str, t.Any]:
        assert path[0] == "/"
        query = self._clean_query(query) if query else {}

        async with self._session.post(
            f"{self._path}{path}", params=query, json={"DisplayNamePrefix": "the-the"}
        ) as response:
            response = await self.handle_error(response)
            return await response.json()
