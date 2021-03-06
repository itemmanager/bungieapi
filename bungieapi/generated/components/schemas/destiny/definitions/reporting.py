# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyReportReasonCategoryDefinition:
    """If you're going to report someone for a Terms of Service violation, you
    need to choose a category and reason for the report.

    This definition holds both the categories and the reasons within
    those categories, for simplicity and my own laziness' sake. Note tha
    this means that, to refer to a Reason by reasonHash, you need a
    combination of the reasonHash *and* the associated ReasonCategory's
    hash: there are some reasons defined under multiple categories.
    """

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
    reasons: t.Mapping[str, "DestinyReportReasonDefinition"] = dt.field(
        metadata={
            "description": "The specific reasons for the report under this category."
        }
    )
    redacted: bool = dt.field(
        metadata={
            "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!"
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "displayProperties": to_json(self.display_properties),
            "reasons": to_json(self.reasons),
            "hash": to_json(self.hash),
            "index": to_json(self.index),
            "redacted": to_json(self.redacted),
        }


@dt.dataclass(frozen=True)
class DestinyReportReasonDefinition:
    """A specific reason for being banned.

    Only accessible under the related category
    (DestinyReportReasonCategoryDefinition) under which it is shown.
    Note that this means that report reasons' reasonHash are not
    globally unique: and indeed, entries like "Other" are defined under
    most categories for example.
    """

    display_properties: "DestinyDisplayPropertiesDefinition"
    reason_hash: int = dt.field(
        metadata={
            "description": "The identifier for the reason: they are only guaranteed unique under the Category in which they are found."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "reasonHash": to_json(self.reason_hash),
            "displayProperties": to_json(self.display_properties),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions.common import (  # noqa: E402
    DestinyDisplayPropertiesDefinition,
)
