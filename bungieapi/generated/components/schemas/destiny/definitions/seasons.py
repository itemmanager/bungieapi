# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinySeasonDefinition:
    """Defines a canonical "Season" of Destiny: a range of a few months where
    the game highlights certain challenges, provides new loot, has new Clan-
    related rewards and celebrates various seasonal events."""

    background_image_path: str
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
    preview: "DestinySeasonPreviewDefinition" = dt.field(
        metadata={
            "description": "Optional - Defines the promotional text, images, and links to preview this season."
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    season_number: int
    artifact_item_hash: t.Optional[
        ManifestReference["DestinyInventoryItemDefinition"]
    ] = None
    end_date: t.Optional[str] = None
    seal_presentation_node_hash: t.Optional[
        ManifestReference["DestinyPresentationNodeDefinition"]
    ] = None
    season_pass_hash: t.Optional[
        ManifestReference["DestinySeasonPassDefinition"]
    ] = None
    season_pass_progression_hash: t.Optional[
        ManifestReference["DestinyProgressionDefinition"]
    ] = None
    seasonal_challenges_presentation_node_hash: t.Optional[
        ManifestReference["DestinyPresentationNodeDefinition"]
    ] = None
    start_date: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "backgroundImagePath": to_json(self.background_image_path),
            "seasonNumber": to_json(self.season_number),
            "startDate": to_json(self.start_date),
            "endDate": to_json(self.end_date),
            "seasonPassHash": to_json(self.season_pass_hash),
            "seasonPassProgressionHash": to_json(self.season_pass_progression_hash),
            "artifactItemHash": to_json(self.artifact_item_hash),
            "sealPresentationNodeHash": to_json(self.seal_presentation_node_hash),
            "seasonalChallengesPresentationNodeHash": to_json(
                self.seasonal_challenges_presentation_node_hash
            ),
            "preview": to_json(self.preview),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinySeasonPreviewDefinition:
    """Defines the promotional text, images, and links to preview this
    season."""

    description: str = dt.field(
        metadata={"description": "A localized description of the season."}
    )
    images: t.Sequence["DestinySeasonPreviewImageDefinition"] = dt.field(
        metadata={
            "description": "A list of images to preview the seasonal content. Should have at least three to show."
        }
    )
    link_path: str = dt.field(
        metadata={
            "description": 'A relative path to learn more about the season. Web browsers should be automatically redirected to the user\'s Bungie.net locale. For example: "/SeasonOfTheChosen" will redirect to "/7/en/Seasons/SeasonOfTheChosen" for English users.'
        }
    )
    video_link: str = dt.field(
        metadata={
            "description": "An optional link to a localized video, probably YouTube."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "description": to_json(self.description),
            "linkPath": to_json(self.link_path),
            "videoLink": to_json(self.video_link),
            "images": to_json(self.images),
        }


@dt.dataclass(frozen=True)
class DestinySeasonPreviewImageDefinition:
    """Defines the thumbnail icon, high-res image, and video link for
    promotional images."""

    high_res_image: str = dt.field(
        metadata={
            "description": "An optional path to a high-resolution image, probably 1920x1080."
        }
    )
    thumbnail_image: str = dt.field(
        metadata={
            "description": "A thumbnail icon path to preview seasonal content, probably 480x270."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "thumbnailImage": to_json(self.thumbnail_image),
            "highResImage": to_json(self.high_res_image),
        }


@dt.dataclass(frozen=True)
class DestinySeasonPassDefinition:
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
    prestige_progression_hash: ManifestReference[
        "DestinyProgressionDefinition"
    ] = dt.field(
        metadata={
            "description": """I know what you're thinking, but I promise we're not going to duplicate and drown you. Instead, we're giving you sweet, sweet power bonuses.
 Prestige progression is further progression that you can make on the Season pass after you gain max ranks, that will ultimately increase your power/light level over the theoretical limit."""
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    reward_progression_hash: ManifestReference[
        "DestinyProgressionDefinition"
    ] = dt.field(
        metadata={
            "description": 'This is the progression definition related to the progression for the initial levels 1-100 that provide item rewards for the Season pass. Further experience after you reach the limit is provided in the "Prestige" progression referred to by prestigeProgressionHash.'
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "rewardProgressionHash": to_json(self.reward_progression_hash),
            "prestigeProgressionHash": to_json(self.prestige_progression_hash),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyEventCardDefinition:
    """Defines the properties of an 'Event Card' in Destiny 2, to coincide with
    a seasonal event for additional challenges, premium rewards, a new seal,
    and a special title.

    For example: Solstice of Heroes 2022.
    """

    color: "DestinyColor"
    display_properties: "DestinyDisplayPropertiesDefinition"
    end_time: int
    hash: int = dt.field(
        metadata={
            "description": """The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to."""
        }
    )
    images: "DestinyEventCardImages"
    index: int = dt.field(
        metadata={
            "description": "The index of the entity as it was found in the investment tables."
        }
    )
    link_redirect_path: str
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )
    seal_presentation_node_hash: ManifestReference["DestinyPresentationNodeDefinition"]
    ticket_currency_item_hash: ManifestReference["DestinyInventoryItemDefinition"]
    ticket_vendor_category_hash: int
    ticket_vendor_hash: ManifestReference["DestinyVendorDefinition"]
    triumphs_presentation_node_hash: ManifestReference[
        "DestinyPresentationNodeDefinition"
    ]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "linkRedirectPath": to_json(self.link_redirect_path),
            "color": to_json(self.color),
            "images": to_json(self.images),
            "triumphsPresentationNodeHash": to_json(
                self.triumphs_presentation_node_hash
            ),
            "sealPresentationNodeHash": to_json(self.seal_presentation_node_hash),
            "ticketCurrencyItemHash": to_json(self.ticket_currency_item_hash),
            "ticketVendorHash": to_json(self.ticket_vendor_hash),
            "ticketVendorCategoryHash": to_json(self.ticket_vendor_category_hash),
            "endTime": to_json(self.end_time),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyEventCardImages:
    card_complete_image_path: str
    card_complete_wrap_image_path: str
    card_incomplete_image_path: str
    progress_icon_image_path: str
    theme_background_image_path: str
    unowned_card_sleeve_image_path: str
    unowned_card_sleeve_wrap_image_path: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "unownedCardSleeveImagePath": to_json(self.unowned_card_sleeve_image_path),
            "unownedCardSleeveWrapImagePath": to_json(
                self.unowned_card_sleeve_wrap_image_path
            ),
            "cardIncompleteImagePath": to_json(self.card_incomplete_image_path),
            "cardCompleteImagePath": to_json(self.card_complete_image_path),
            "cardCompleteWrapImagePath": to_json(self.card_complete_wrap_image_path),
            "progressIconImagePath": to_json(self.progress_icon_image_path),
            "themeBackgroundImagePath": to_json(self.theme_background_image_path),
        }


from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinyInventoryItemDefinition,
    DestinyProgressionDefinition,
    DestinyVendorDefinition,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
from bungieapi.generated.components.schemas.destiny.definitions.presentation import (  # noqa: E402
    DestinyPresentationNodeDefinition,
)
from bungieapi.generated.components.schemas.destiny.misc import (  # noqa: E402
    DestinyColor,
)
