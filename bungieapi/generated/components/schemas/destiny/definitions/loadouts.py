# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyLoadoutColorDefinition:
    color_image_path: str
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "colorImagePath": to_json(self.color_image_path),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyLoadoutIconDefinition:
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    icon_image_path: str
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "iconImagePath": to_json(self.icon_image_path),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyLoadoutNameDefinition:
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    name: str
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyLoadoutConstantsDefinition:
    black_icon_image_path: str = dt.field(
        metadata={
            "description": "This is a color-inverted version of the whiteIconImagePath."
        }
    )
    display_properties: "DestinyDisplayPropertiesDefinition"
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    loadout_color_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A list of the loadout color hashes in index order, for convenience."
        }
    )
    loadout_count_per_character: int = dt.field(
        metadata={
            "description": "The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks."
        }
    )
    loadout_icon_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A list of the loadout icon hashes in index order, for convenience."
        }
    )
    loadout_name_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A list of the loadout name hashes in index order, for convenience."
        }
    )
    loadout_preview_filter_out_socket_category_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A list of the socket category hashes to be filtered out of loadout item preview displays."
        }
    )
    loadout_preview_filter_out_socket_type_hashes: t.Sequence[int] = dt.field(
        metadata={
            "description": "A list of the socket type hashes to be filtered out of loadout item preview displays."
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    white_icon_image_path: str = dt.field(
        metadata={
            "description": "This is the same icon as the one in the display properties, offered here as well with a more descriptive name."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "whiteIconImagePath": to_json(self.white_icon_image_path),
            "blackIconImagePath": to_json(self.black_icon_image_path),
            "loadoutCountPerCharacter": to_json(self.loadout_count_per_character),
            "loadoutPreviewFilterOutSocketCategoryHashes": to_json(
                self.loadout_preview_filter_out_socket_category_hashes
            ),
            "loadoutPreviewFilterOutSocketTypeHashes": to_json(
                self.loadout_preview_filter_out_socket_type_hashes
            ),
            "loadoutNameHashes": to_json(self.loadout_name_hashes),
            "loadoutIconHashes": to_json(self.loadout_icon_hashes),
            "loadoutColorHashes": to_json(self.loadout_color_hashes),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
