# generated by update to not change manually
from bungieapi.base import BaseClient, clean_query_value
from bungieapi.forge import forge
from bungieapi.generated.components.responses import (
    SearchResultOfTrendingEntryClientResponse,
)
from bungieapi.generated.components.responses.trending import (
    TrendingCategoriesClientResponse,
    TrendingDetailClientResponse,
)
from bungieapi.generated.components.schemas.trending import TrendingEntryType


class Client(BaseClient):
    async def get_trending_categories(
        self,
    ) -> TrendingCategoriesClientResponse:
        """Returns trending items for Bungie.net, collapsed into the first page
        of items per category.

        For pagination within a category, call GetTrendingCategory.
        """
        query = None
        result = await self.get(
            path="/Trending/Categories/",
            query=query,
        )
        return forge(TrendingCategoriesClientResponse, result)

    async def get_trending_category(
        self,
        category_id: str,
        page_number: int,
    ) -> SearchResultOfTrendingEntryClientResponse:
        """Returns paginated lists of trending items for a category.

        Parameters:
            category_id: The ID of the category for whom you want additional results.
            page_number: The page # of results to return.
        """
        query = None
        result = await self.get(
            path=f"/Trending/Categories/{clean_query_value(category_id)}/{clean_query_value(page_number)}/",
            query=query,
        )
        return forge(SearchResultOfTrendingEntryClientResponse, result)

    async def get_trending_entry_detail(
        self,
        identifier: str,
        trending_entry_type: "TrendingEntryType",
    ) -> TrendingDetailClientResponse:
        """Returns the detailed results for a specific trending entry.

        Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.
        Parameters:
            identifier: The identifier for the entity to be returned.
            trending_entry_type: The type of entity to be returned.
        """
        query = None
        result = await self.get(
            path=f"/Trending/Details/{clean_query_value(trending_entry_type)}/{clean_query_value(identifier)}/",
            query=query,
        )
        return forge(TrendingDetailClientResponse, result)
