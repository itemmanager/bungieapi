# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class ContentItemPublicContractClientResponse:
    detailed_error_trace: str
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "ContentItemPublicContract"
    throttle_seconds: int

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
class NewsArticleRssClientResponse:
    detailed_error_trace: str
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "NewsArticleRssResponse"
    throttle_seconds: int

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
from bungieapi.generated.components.schemas.content import (  # noqa: E402
    ContentItemPublicContract,
    NewsArticleRssResponse,
)
from bungieapi.generated.components.schemas.exceptions import (  # noqa: E402
    PlatformErrorCodes,
)
