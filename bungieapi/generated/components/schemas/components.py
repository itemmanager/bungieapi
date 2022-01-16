# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class ComponentResponse:
    """The base class for any component-returning object that may need to
    indicate information about the state of the component being returned."""

    privacy: "ComponentPrivacySetting"
    disabled: t.Optional[bool] = dt.field(
        default=None, metadata={"description": "If true, this component is disabled."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "privacy": to_json(self.privacy),
            "disabled": to_json(self.disabled),
        }


class ComponentPrivacySetting(Enum):
    """A set of flags for reason(s) why the component populated in the way that
    it did.

    Inspect the individual flags for the reasons.
    """

    NONE = 0
    PUBLIC = 1
    PRIVATE = 2
