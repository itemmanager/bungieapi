# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class ApiUsageClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "ApiUsage"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.applications import ApiUsage  # noqa: E402
from bungieapi.generated.components.schemas.exceptions import (
    PlatformErrorCodes,
)  # noqa: E402
