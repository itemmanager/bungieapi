# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class IgnoreResponse:
    ignore_flags: "IgnoreStatus"
    is_ignored: bool

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "isIgnored": to_json(self.is_ignored),
            "ignoreFlags": to_json(self.ignore_flags),
        }


class IgnoreStatus(Enum):
    NOT_IGNORED = 0
    IGNORED_USER = 1
    IGNORED_GROUP = 2
    IGNORED_BY_GROUP = 4
    IGNORED_POST = 8
    IGNORED_TAG = 16
    IGNORED_GLOBAL = 32


class IgnoreLength(Enum):
    NONE = 0
    WEEK = 1
    TWO_WEEKS = 2
    THREE_WEEKS = 3
    MONTH = 4
    THREE_MONTHS = 5
    SIX_MONTHS = 6
    YEAR = 7
    FOREVER = 8
    THREE_MINUTES = 9
    HOUR = 10
    THIRTY_DAYS = 11
