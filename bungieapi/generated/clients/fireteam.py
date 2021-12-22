# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types import (
    SearchResultOfFireteamResponse,
    SearchResultOfFireteamSummary,
)
from bungieapi.generated.types.exceptions import PlatformErrorCodes
from bungieapi.generated.types.fireteam import FireteamResponse

from ...base import BaseClient


@dt.dataclass(frozen=True)
class GetActivePrivateClanFireteamCountClientResponse:
    response: int
    error_code: "PlatformErrorCodes"
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class GetAvailableClanFireteamsClientResponse:
    response: "SearchResultOfFireteamSummary"
    error_code: "PlatformErrorCodes"
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class SearchPublicAvailableClanFireteamsClientResponse:
    response: "SearchResultOfFireteamSummary"
    error_code: "PlatformErrorCodes"
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class GetMyClanFireteamsClientResponse:
    response: "SearchResultOfFireteamResponse"
    error_code: "PlatformErrorCodes"
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class GetClanFireteamClientResponse:
    response: "FireteamResponse"
    error_code: "PlatformErrorCodes"
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


class Client(BaseClient):
    async def get_active_private_clan_fireteam_count(
        self,
        group_id: int,
    ) -> GetActivePrivateClanFireteamCountClientResponse:
        """Gets a count of all active non-public fireteams for the specified
        clan.

        Maximum value returned is 25.
        """
        ...

    async def get_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: int,
        group_id: int,
        page: int,
        platform: int,
        public_only: int,
        slot_filter: int,
        lang_filter: t.Optional[str] = None,
    ) -> GetAvailableClanFireteamsClientResponse:
        """Gets a listing of all of this clan's fireteams that are have
        available slots.

        Caller is not checked for join criteria so caching is maximized.
        """
        ...

    async def search_public_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: int,
        page: int,
        platform: int,
        slot_filter: int,
        lang_filter: t.Optional[str] = None,
    ) -> SearchPublicAvailableClanFireteamsClientResponse:
        """Gets a listing of all public fireteams starting now with open slots.

        Caller is not checked for join criteria so caching is maximized.
        """
        ...

    async def get_my_clan_fireteams(
        self,
        group_id: int,
        include_closed: bool,
        page: int,
        platform: int,
        group_filter: t.Optional[bool] = None,
        lang_filter: t.Optional[str] = None,
    ) -> GetMyClanFireteamsClientResponse:
        """Gets a listing of all fireteams that caller is an applicant, a
        member, or an alternate of."""
        ...

    async def get_clan_fireteam(
        self,
        fireteam_id: int,
        group_id: int,
    ) -> GetClanFireteamClientResponse:
        """Gets a specific fireteam."""
        ...
