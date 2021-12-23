# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


@dt.dataclass(frozen=True)
class ContentTypeDescription:
    allow_comments: bool
    auto_english_property_fallback: bool
    bind_identifier_to_property: str
    bound_regex: str
    bulk_uploadable: bool
    c_type: str
    content_description: str
    force_identifier_binding: bool
    name: str
    preview_image: str
    previews: t.Sequence["ContentPreview"]
    priority: int
    properties: t.Sequence["ContentTypeProperty"]
    property_sections: t.Sequence["ContentTypePropertySection"]
    reminder: str
    show_in_content_editor: bool
    suppress_cms_path: bool
    tag_metadata: t.Sequence["TagMetadataDefinition"]
    tag_metadata_items: t.Mapping[str, "TagMetadataItem"]
    type_of: str
    usage_examples: t.Sequence[str]


@dt.dataclass(frozen=True)
class ContentTypeProperty:
    attributes: t.Mapping[str, str]
    bind_to_property: str
    bound_regex: str
    child_properties: t.Sequence["ContentTypeProperty"]
    content_type_allowed: str
    datatype: "ContentPropertyDataTypeEnum"
    default_values: t.Sequence["ContentTypeDefaultValue"]
    enabled: bool
    entitytype: str
    fallback: bool
    is_combo: bool
    is_external_allowed: bool
    is_image: bool
    is_title: bool
    is_video: bool
    legal_content_types: t.Sequence[str]
    localizable: bool
    max_byte_length: int
    max_file_size: int
    max_height: int
    max_length: int
    max_width: int
    min_height: int
    min_width: int
    name: str
    order: int
    property_description: str
    property_section: str
    readable_name: str
    regexp: str
    representation_selection: t.Mapping[str, str]
    representation_validation_string: str
    required: bool
    root_property_name: str
    rss_attribute: str
    suppress_property: bool
    validate_as: str
    value: str
    visible: bool
    visible_dependency: str
    visible_on: str
    weight: int


class ContentPropertyDataTypeEnum(Enum):
    NONE = 0
    PLAINTEXT = 1
    HTML = 2
    DROPDOWN = 3
    LIST = 4
    JSON = 5
    CONTENT = 6
    REPRESENTATION = 7
    SET = 8
    FILE = 9
    FOLDER_SET = 10
    DATE = 11
    MULTILINE_PLAINTEXT = 12
    DESTINY_CONTENT = 13
    COLOR = 14


@dt.dataclass(frozen=True)
class ContentTypeDefaultValue:
    default_value: str
    when_clause: str
    when_value: str


@dt.dataclass(frozen=True)
class TagMetadataDefinition:
    datatype: str
    description: str
    is_required: bool
    items: t.Sequence["TagMetadataItem"]
    name: str
    order: int


@dt.dataclass(frozen=True)
class TagMetadataItem:
    description: str
    groups: t.Sequence[str]
    is_default: bool
    name: str
    tag_text: str


@dt.dataclass(frozen=True)
class ContentPreview:
    item_in_set: bool
    name: str
    path: str
    set_nesting: int
    set_tag: str
    use_set_id: int


@dt.dataclass(frozen=True)
class ContentTypePropertySection:
    collapsed: bool
    name: str
    readable_name: str


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.content.models import (  # noqa: E402
    ContentPreview,
    ContentPropertyDataTypeEnum,
    ContentTypeDefaultValue,
    ContentTypeProperty,
    ContentTypePropertySection,
    TagMetadataDefinition,
    TagMetadataItem,
)
