# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyAnimationReference:
    anim_identifier: str
    anim_name: str
    path: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "animName": to_json(self.anim_name),
            "animIdentifier": to_json(self.anim_identifier),
            "path": to_json(self.path),
        }
