# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class ContentItemPublicContract:
    allow_comments: bool
    author: "GeneralUser"
    auto_english_property_fallback: bool
    c_type: str
    cms_path: str
    comment_summary: "CommentSummary"
    content_id: int
    creation_date: str
    has_age_gate: bool
    minimum_age: int
    modify_date: str
    properties: t.Mapping[
        str, t.Any
    ]  # Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown. As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.
    rating_image_path: str
    representations: t.Sequence["ContentRepresentation"]
    tags: t.Sequence[str]  # NOTE: Tags will always be lower case.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "contentId": to_json(self.content_id),
            "cType": to_json(self.c_type),
            "cmsPath": to_json(self.cms_path),
            "creationDate": to_json(self.creation_date),
            "modifyDate": to_json(self.modify_date),
            "allowComments": to_json(self.allow_comments),
            "hasAgeGate": to_json(self.has_age_gate),
            "minimumAge": to_json(self.minimum_age),
            "ratingImagePath": to_json(self.rating_image_path),
            "author": to_json(self.author),
            "autoEnglishPropertyFallback": to_json(self.auto_english_property_fallback),
            "properties": to_json(self.properties),
            "representations": to_json(self.representations),
            "tags": to_json(self.tags),
            "commentSummary": to_json(self.comment_summary),
        }


@dt.dataclass(frozen=True)
class ContentRepresentation:
    name: str
    path: str
    validation_string: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "path": to_json(self.path),
            "validationString": to_json(self.validation_string),
        }


@dt.dataclass(frozen=True)
class CommentSummary:
    comment_count: int
    topic_id: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "topicId": to_json(self.topic_id),
            "commentCount": to_json(self.comment_count),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.user import GeneralUser  # noqa: E402
