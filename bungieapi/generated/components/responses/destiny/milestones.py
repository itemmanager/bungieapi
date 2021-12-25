# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyMilestoneClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["DestinyMilestone"] = None
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
class DestinyMilestoneContentClientResponse:
    detailed_error_trace: t.Optional[str] = None
    error_code: t.Optional["PlatformErrorCodes"] = None
    error_status: t.Optional[str] = None
    message: t.Optional[str] = None
    message_data: t.Optional[t.Mapping[str, str]] = None
    response: t.Optional["DestinyMilestoneContent"] = None
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


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.milestones import (
    DestinyMilestone,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.milestones import (
    DestinyMilestoneContent,
)  # noqa: E402
from bungieapi.generated.components.schemas.exceptions import (
    PlatformErrorCodes,
)  # noqa: E402
