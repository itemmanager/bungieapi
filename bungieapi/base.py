import base64
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
def clean_list(in_: list) -> str:
    return ",".join(clean_query_value(v) for v in in_)


@clean_query_value.register
def clean_enum_value(in_: Enum) -> str:
    return str(in_.value)


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


@dt.dataclass
class Token:
    access_token: str
    token_type: t.Literal["Bearer"]
    expires_in: int
    refresh_token: str
    refresh_expires_in: int
    membership_id: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "accessToken": self.access_token,
            "tokenType": self.token_type,
            "expiresIn": self.expires_in,
            "refreshToken": self.refresh_token,
            "refreshExpiresIn": self.refresh_expires_in,
            "membershipId": self.membership_id,
        }


class AppClient(BaseClient):
    async def from_refresh_token(
        self, refresh_token: str, client_id: int, client_secret: str
    ) -> Token:
        """Get token and refresh token from refresh token."""
        return await self._authorize(
            grant_type="refresh_token",
            secret=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
        )

    async def from_authorization_code(
        self, code: str, client_id: int, client_secret: str
    ) -> Token:
        """Get token and refresh token from oouth code."""
        return await self._authorize(
            grant_type="authorization_code",
            secret=code,
            client_id=client_id,
            client_secret=client_secret,
        )

    async def _authorize(
        self,
        grant_type: t.Literal["authorization_code", "refresh_token"],
        secret: str,
        client_id: int,
        client_secret: str,
    ) -> Token:
        auth_token = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth_token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        path = "/App/OAuth/Token/"
        grant_type_to_name: t.Mapping[
            t.Literal["authorization_code", "refresh_token"], str
        ] = {"authorization_code": "code", "refresh_token": "refresh_token"}
        data = {
            "grant_type": grant_type,
            grant_type_to_name[grant_type]: secret,
        }
        async with aiohttp.ClientSession(
            base_url=self._session._base_url, headers=headers
        ) as session:
            async with session.post(f"{self._path}{path}", data=data) as response:
                response = await self.handle_error(response)
                result = await response.json()
        return forge(Token, result)
