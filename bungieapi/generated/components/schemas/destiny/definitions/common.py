# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyDisplayPropertiesDefinition:
    """Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information."""

    description: str
    has_icon: bool
    high_res_icon: str = dt.field(
        metadata={
            "description": "If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here."
        }
    )
    icon: str = dt.field(
        metadata={
            "description": """Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.
But usually, it will be a small square image that you can use as... well, an icon.
They are currently represented as 96px x 96px images."""
        }
    )
    icon_sequences: t.Sequence["DestinyIconSequenceDefinition"]
    name: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "description": to_json(self.description),
            "name": to_json(self.name),
            "icon": to_json(self.icon),
            "iconSequences": to_json(self.icon_sequences),
            "highResIcon": to_json(self.high_res_icon),
            "hasIcon": to_json(self.has_icon),
        }


@dt.dataclass(frozen=True)
class DestinyIconSequenceDefinition:
    frames: t.Sequence[str]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "frames": to_json(self.frames),
        }


@dt.dataclass(frozen=True)
class DestinyPositionDefinition:
    x: int
    y: int
    z: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "x": to_json(self.x),
            "y": to_json(self.y),
            "z": to_json(self.z),
        }
