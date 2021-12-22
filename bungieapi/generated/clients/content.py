# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types import SearchResultOfContentItemPublicContract
from bungieapi.generated.types.content import ContentItemPublicContract
from bungieapi.generated.types.content.models import ContentTypeDescription
from bungieapi.generated.types.exceptions import PlatformErrorCodes

from ...base import BaseClient


@dt.dataclass(frozen=True)
class GetContentTypeClientResponse:
    response: ContentTypeDescription
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class GetContentByIdClientResponse:
    response: ContentItemPublicContract
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class GetContentByTagAndTypeClientResponse:
    response: ContentItemPublicContract
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class SearchContentWithTextClientResponse:
    response: SearchResultOfContentItemPublicContract
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class SearchContentByTagAndTypeClientResponse:
    response: SearchResultOfContentItemPublicContract
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


@dt.dataclass(frozen=True)
class SearchHelpArticlesClientResponse:
    response: t.Any
    error_code: PlatformErrorCodes
    throttle_seconds: int
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    detailed_error_trace: str


class Client(BaseClient):
    async def get_content_type(
        self,
        type: str,
    ) -> GetContentTypeClientResponse:
        """Gets an object describing a particular variant of content."""
        ...

    async def get_content_by_id(
        self,
        id: int,
        locale: str,
        head: t.Optional[bool] = None,
    ) -> GetContentByIdClientResponse:
        """Returns a content item referenced by id."""
        ...

    async def get_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        head: t.Optional[bool] = None,
    ) -> GetContentByTagAndTypeClientResponse:
        """Returns the newest item that matches a given tag and Content
        Type."""
        ...

    async def search_content_with_text(
        self,
        locale: str,
        ctype: t.Optional[str] = None,
        currentpage: t.Optional[int] = None,
        head: t.Optional[bool] = None,
        searchtext: t.Optional[str] = None,
        source: t.Optional[str] = None,
        tag: t.Optional[str] = None,
    ) -> SearchContentWithTextClientResponse:
        """Gets content based on querystring information passed in.

        Provides basic search and text search capabilities.
        """
        ...

    async def search_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        currentpage: t.Optional[int] = None,
        head: t.Optional[bool] = None,
        itemsperpage: t.Optional[int] = None,
    ) -> SearchContentByTagAndTypeClientResponse:
        """Searches for Content Items that match the given Tag and Content
        Type."""
        ...

    async def search_help_articles(
        self,
        searchtext: str,
        size: str,
    ) -> SearchHelpArticlesClientResponse:
        """Search for Help Articles."""
        ...
