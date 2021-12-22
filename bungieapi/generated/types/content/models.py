# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class ContentTypeDescription:
    c_type: str
    name: str
    content_description: str
    preview_image: str
    priority: int
    reminder: str
    properties: t.Sequence["ContentTypeProperty"]
    tag_metadata: t.Sequence["TagMetadataDefinition"]
    tag_metadata_items: t.Mapping[str, "TagMetadataItem"]
    usage_examples: t.Sequence[str]
    show_in_content_editor: bool
    type_of: str
    bind_identifier_to_property: str
    bound_regex: str
    force_identifier_binding: bool
    allow_comments: bool
    auto_english_property_fallback: bool
    bulk_uploadable: bool
    previews: t.Sequence["ContentPreview"]
    suppress_cms_path: bool
    property_sections: t.Sequence["ContentTypePropertySection"]


@dt.dataclass(frozen=True)
class ContentTypeProperty:
    name: str
    root_property_name: str
    readable_name: str
    value: str
    property_description: str
    localizable: bool
    fallback: bool
    enabled: bool
    order: int
    visible: bool
    is_title: bool
    required: bool
    max_length: int
    max_byte_length: int
    max_file_size: int
    regexp: str
    validate_as: str
    rss_attribute: str
    visible_dependency: str
    visible_on: str
    datatype: "ContentPropertyDataTypeEnum"
    attributes: t.Mapping[str, str]
    child_properties: t.Sequence["ContentTypeProperty"]
    content_type_allowed: str
    bind_to_property: str
    bound_regex: str
    representation_selection: t.Mapping[str, str]
    default_values: t.Sequence["ContentTypeDefaultValue"]
    is_external_allowed: bool
    property_section: str
    weight: int
    entitytype: str
    is_combo: bool
    suppress_property: bool
    legal_content_types: t.Sequence[str]
    representation_validation_string: str
    min_width: int
    max_width: int
    min_height: int
    max_height: int
    is_video: bool
    is_image: bool


ContentPropertyDataTypeEnum = t.Any


@dt.dataclass(frozen=True)
class ContentTypeDefaultValue:
    when_clause: str
    when_value: str
    default_value: str


@dt.dataclass(frozen=True)
class TagMetadataDefinition:
    description: str
    order: int
    items: t.Sequence["TagMetadataItem"]
    datatype: str
    name: str
    is_required: bool


@dt.dataclass(frozen=True)
class TagMetadataItem:
    description: str
    tag_text: str
    groups: t.Sequence[str]
    is_default: bool
    name: str


@dt.dataclass(frozen=True)
class ContentPreview:
    name: str
    path: str
    item_in_set: bool
    set_tag: str
    set_nesting: int
    use_set_id: int


@dt.dataclass(frozen=True)
class ContentTypePropertySection:
    name: str
    readable_name: str
    collapsed: bool
