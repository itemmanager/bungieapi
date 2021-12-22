# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class ContentItemPublicContract:
    content_id: int
    c_type: str
    cms_path: str
    creation_date: str
    modify_date: str
    allow_comments: bool
    has_age_gate: bool
    minimum_age: int
    rating_image_path: str
    author: "GeneralUser"
    auto_english_property_fallback: bool
    properties: t.Mapping[str, t.Any]
    representations: t.Sequence["ContentRepresentation"]
    tags: t.Sequence[str]
    comment_summary: "CommentSummary"


@dt.dataclass(frozen=True)
class ContentRepresentation:
    name: str
    path: str
    validation_string: str


@dt.dataclass(frozen=True)
class CommentSummary:
    topic_id: int
    comment_count: int


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.user import GeneralUser  # noqa: E402
