# generated by update to not change manually
import dataclasses as dt

from bungieapi.generated.types.ignores import IgnoreResponse


@dt.dataclass(frozen=True)
class TagResponse:
    tag_text: str
    ignore_status: IgnoreResponse
