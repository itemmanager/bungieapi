# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class GroupSearchClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupSearchResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GroupClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GroupMemberLeaveResultClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupMemberLeaveResult"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GetGroupsForMemberClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GetGroupsForMemberResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GroupMembershipSearchClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupMembershipSearchResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GroupPotentialMembershipSearchClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupPotentialMembershipSearchResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


@dt.dataclass(frozen=True)
class GroupApplicationClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["GroupApplicationResponse"] = None
    throttle_seconds: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "Response": to_json(self.response),
            "ErrorCode": to_json(self.error_code),
            "ThrottleSeconds": to_json(self.throttle_seconds),
            "ErrorStatus": to_json(self.error_status),
            "Message": to_json(self.message),
            "MessageData": to_json(self.message_data),
            "DetailedErrorTrace": to_json(self.detailed_error_trace),
        }


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
