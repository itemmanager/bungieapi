# generated by update to not change manually
import dataclasses as dt
import typing as t


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


@dt.dataclass(frozen=True)
class ContentRepresentation:
    name: str
    path: str
    validation_string: str


@dt.dataclass(frozen=True)
class CommentSummary:
    comment_count: int
    topic_id: int


from bungieapi.generated.components.schemas.content import CommentSummary  # noqa: E402
from bungieapi.generated.components.schemas.content import (
    ContentRepresentation,
)  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.user import GeneralUser  # noqa: E402
