# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class GroupSearchClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupSearchResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GroupClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GroupMemberLeaveResultClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupMemberLeaveResult"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GetGroupsForMemberClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GetGroupsForMemberResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GroupMembershipSearchClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupMembershipSearchResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GroupPotentialMembershipSearchClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupPotentialMembershipSearchResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class GroupApplicationClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "GroupApplicationResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


from bungieapi.generated.components.schemas.exceptions import (
    PlatformErrorCodes,
)  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.groups_v2 import GroupResponse  # noqa: E402
from bungieapi.generated.components.schemas.groups_v2 import (  # noqa: E402
    GetGroupsForMemberResponse,
    GroupApplicationResponse,
    GroupMemberLeaveResult,
    GroupMembershipSearchResponse,
    GroupPotentialMembershipSearchResponse,
    GroupSearchResponse,
)
