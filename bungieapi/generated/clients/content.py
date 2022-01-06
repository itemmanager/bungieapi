# generated by update to not change manually
import typing as t

from bungieapi.base import BaseClient, clean_query_value
from bungieapi.forge import forge
from bungieapi.generated.components.responses import (
    IReadOnlyCollectionOfContentItemPublicContractClientResponse,
    SearchResultOfContentItemPublicContractClientResponse,
)
from bungieapi.generated.components.responses.content import (
    ContentItemPublicContractClientResponse,
)
from bungieapi.generated.components.responses.content.models import (
    ContentTypeDescriptionClientResponse,
)


class Client(BaseClient):
    async def get_content_type(
        self,
        type: str,
    ) -> ContentTypeDescriptionClientResponse:
        """Gets an object describing a particular variant of content."""
        query = None
        result = await self.get(
            path=f"/Content/GetContentType/{clean_query_value(type)}/",
            query=query,
        )
        return forge(ContentTypeDescriptionClientResponse, result)

    async def get_content_by_id(
        self,
        id: int,
        locale: str,
        head: t.Optional[bool] = None,
    ) -> ContentItemPublicContractClientResponse:
        """Returns a content item referenced by id
        Parameters:
            head: false"""
        query = {"head": head}
        result = await self.get(
            path=f"/Content/GetContentById/{clean_query_value(id)}/{clean_query_value(locale)}/",
            query=query,
        )
        return forge(ContentItemPublicContractClientResponse, result)

    async def get_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        head: t.Optional[bool] = None,
    ) -> ContentItemPublicContractClientResponse:
        """Returns the newest item that matches a given tag and Content Type.

        Parameters:
            head: Not used.
        """
        query = {"head": head}
        result = await self.get(
            path=f"/Content/GetContentByTagAndType/{clean_query_value(tag)}/{clean_query_value(type)}/{clean_query_value(locale)}/",
            query=query,
        )
        return forge(ContentItemPublicContractClientResponse, result)

    async def search_content_with_text(
        self,
        locale: str,
        ctype: t.Optional[str] = None,
        currentpage: t.Optional[int] = None,
        head: t.Optional[bool] = None,
        searchtext: t.Optional[str] = None,
        source: t.Optional[str] = None,
        tag: t.Optional[str] = None,
    ) -> SearchResultOfContentItemPublicContractClientResponse:
        """Gets content based on querystring information passed in.

        Provides basic search and text search capabilities.
        Parameters:
            ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
            currentpage: Page number for the search results, starting with page 1.
            head: Not used.
            searchtext: Word or phrase for the search.
            source: For analytics, hint at the part of the app that triggered the search. Optional.
            tag: Tag used on the content to be searched.
        """
        query = {
            "ctype": ctype,
            "currentpage": currentpage,
            "head": head,
            "searchtext": searchtext,
            "source": source,
            "tag": tag,
        }
        result = await self.get(
            path=f"/Content/Search/{clean_query_value(locale)}/",
            query=query,
        )
        return forge(SearchResultOfContentItemPublicContractClientResponse, result)

    async def search_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        currentpage: t.Optional[int] = None,
        head: t.Optional[bool] = None,
        itemsperpage: t.Optional[int] = None,
    ) -> SearchResultOfContentItemPublicContractClientResponse:
        """Searches for Content Items that match the given Tag and Content
        Type.

        Parameters:
            currentpage: Page number for the search results starting with page 1.
            head: Not used.
            itemsperpage: Not used.
        """
        query = {"currentpage": currentpage, "head": head, "itemsperpage": itemsperpage}
        result = await self.get(
            path=f"/Content/SearchContentByTagAndType/{clean_query_value(tag)}/{clean_query_value(type)}/{clean_query_value(locale)}/",
            query=query,
        )
        return forge(SearchResultOfContentItemPublicContractClientResponse, result)

    async def search_help_articles(
        self,
        searchtext: str,
        size: str,
    ) -> IReadOnlyCollectionOfContentItemPublicContractClientResponse:
        """Search for Help Articles."""
        query = None
        result = await self.get(
            path=f"/Content/SearchHelpArticles/{clean_query_value(searchtext)}/{clean_query_value(size)}/",
            query=query,
        )
        return forge(
            IReadOnlyCollectionOfContentItemPublicContractClientResponse, result
        )
