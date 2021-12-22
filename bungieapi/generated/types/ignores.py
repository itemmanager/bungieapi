# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class IgnoreResponse:
    is_ignored: bool
    ignore_flags: "IgnoreStatus"


IgnoreStatus = t.Any
IgnoreLength = t.Any
