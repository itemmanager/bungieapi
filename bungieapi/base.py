import dataclasses as dt
import functools as ft
import typing as t
from enum import Enum

import aiohttp
from aiohttp import ClientResponse

from bungieapi.forge import forge
from bungieapi.generated.components.schemas.exceptions import PlatformErrorCodes
from bungieapi.json import to_json


QueryInput = t.Any  # t.Union[None, str, bool, int, t.Sequence[Enum]]


@ft.singledispatch
def clean_query_value(in_: QueryInput) -> str:
    return str(in_)


@clean_query_value.register
def clean_enum_value(in_: Enum) -> str:
    return in_.value


@clean_query_value.register
def clean_enum_bool(in_: bool) -> str:
    return "true" if in_ else "false"


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
        return {k: clean_query_value(v) for k, v in query.items() if v is not None}

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
        self,
        path: str,
        query: t.Optional[t.Mapping[str, QueryInput]],
        request: t.Any = None,
    ) -> t.Mapping[str, t.Any]:
        assert path[0] == "/"
        query = self._clean_query(query) if query else {}

        async with self._session.post(
            f"{self._path}{path}", params=query, json=to_json(request)
        ) as response:
            response = await self.handle_error(response)
            return await response.json()
