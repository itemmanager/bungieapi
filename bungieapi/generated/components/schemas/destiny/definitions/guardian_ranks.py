# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinyGuardianRankDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    foreground_image_path: str
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
    overlay_image_path: str
    overlay_mask_image_path: str
    presentation_node_hash: ManifestReference["DestinyPresentationNodeDefinition"]
    rank_number: int
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "rankNumber": to_json(self.rank_number),
            "presentationNodeHash": to_json(self.presentation_node_hash),
            "foregroundImagePath": to_json(self.foreground_image_path),
            "overlayImagePath": to_json(self.overlay_image_path),
            "overlayMaskImagePath": to_json(self.overlay_mask_image_path),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyGuardianRankConstantsDefinition:
    display_properties: "DestinyDisplayPropertiesDefinition"
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    icon_backgrounds: "DestinyGuardianRankIconBackgroundsDefinition"
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    rank_count: int
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    root_node_hash: ManifestReference["DestinyPresentationNodeDefinition"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "rankCount": to_json(self.rank_count),
            "rootNodeHash": to_json(self.root_node_hash),
            "iconBackgrounds": to_json(self.icon_backgrounds),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyGuardianRankIconBackgroundsDefinition:
    background_empty_blue_gradient_bordered_image_path: str
    background_empty_bordered_image_path: str
    background_filled_blue_bordered_image_path: str
    background_filled_blue_gradient_bordered_image_path: str
    background_filled_blue_low_alpha_image_path: str
    background_filled_blue_medium_alpha_image_path: str
    background_filled_gray_heavy_alpha_bordered_image_path: str
    background_filled_gray_medium_alpha_bordered_image_path: str
    background_filled_white_image_path: str
    background_filled_white_medium_alpha_image_path: str
    background_plate_black_alpha_image_path: str
    background_plate_black_image_path: str
    background_plate_white_image_path: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "backgroundEmptyBorderedImagePath": to_json(
                self.background_empty_bordered_image_path
            ),
            "backgroundEmptyBlueGradientBorderedImagePath": to_json(
                self.background_empty_blue_gradient_bordered_image_path
            ),
            "backgroundFilledBlueBorderedImagePath": to_json(
                self.background_filled_blue_bordered_image_path
            ),
            "backgroundFilledBlueGradientBorderedImagePath": to_json(
                self.background_filled_blue_gradient_bordered_image_path
            ),
            "backgroundFilledBlueLowAlphaImagePath": to_json(
                self.background_filled_blue_low_alpha_image_path
            ),
            "backgroundFilledBlueMediumAlphaImagePath": to_json(
                self.background_filled_blue_medium_alpha_image_path
            ),
            "backgroundFilledGrayMediumAlphaBorderedImagePath": to_json(
                self.background_filled_gray_medium_alpha_bordered_image_path
            ),
            "backgroundFilledGrayHeavyAlphaBorderedImagePath": to_json(
                self.background_filled_gray_heavy_alpha_bordered_image_path
            ),
            "backgroundFilledWhiteMediumAlphaImagePath": to_json(
                self.background_filled_white_medium_alpha_image_path
            ),
            "backgroundFilledWhiteImagePath": to_json(
                self.background_filled_white_image_path
            ),
            "backgroundPlateWhiteImagePath": to_json(
                self.background_plate_white_image_path
            ),
            "backgroundPlateBlackImagePath": to_json(
                self.background_plate_black_image_path
            ),
            "backgroundPlateBlackAlphaImagePath": to_json(
                self.background_plate_black_alpha_image_path
            ),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.presentation import (  # noqa: E402
    DestinyPresentationNodeDefinition,
)