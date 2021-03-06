# generated by update to not change manually
import typing as t

from bungieapi.base import BaseClient, clean_query_value
from bungieapi.forge import forge
from bungieapi.generated.components.responses import (
    CEListOfForumRecruitmentDetailClientResponse,
    ListOfTagClientResponse,
    int64ClientResponse,
)
from bungieapi.generated.components.responses.forum import PostSearchClientResponse
from bungieapi.generated.components.schemas.forum import (
    ForumPostSortEnum,
    ForumTopicsCategoryFiltersEnum,
    ForumTopicsQuickDateEnum,
    ForumTopicsSortEnum,
)


class Client(BaseClient):
    async def get_topics_paged(
        self,
        category_filter: "ForumTopicsCategoryFiltersEnum",
        group: int,
        page: int,
        page_size: int,
        quick_date: "ForumTopicsQuickDateEnum",
        sort: "ForumTopicsSortEnum",
        locales: t.Optional[str] = None,
        tagstring: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Get topics from any forum.

        Parameters:
            category_filter: A category filter
            group: The group, if any.
            locales: Comma seperated list of locales posts must match to return in the result list. Default 'en'
            page: Zero paged page number
            page_size: Unused
            quick_date: A date filter.
            sort: The sort mode.
            tagstring: The tags to search, if any.
        """
        query = {"locales": locales, "tagstring": tagstring}
        result = await self.get(
            path=f"/Forum/GetTopicsPaged/{clean_query_value(page)}/{clean_query_value(page_size)}/{clean_query_value(group)}/{clean_query_value(sort)}/{clean_query_value(quick_date)}/{clean_query_value(category_filter)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_core_topics_paged(
        self,
        category_filter: "ForumTopicsCategoryFiltersEnum",
        page: int,
        quick_date: "ForumTopicsQuickDateEnum",
        sort: "ForumTopicsSortEnum",
        locales: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Gets a listing of all topics marked as part of the core group.

        Parameters:
            category_filter: The category filter.
            locales: Comma seperated list of locales posts must match to return in the result list. Default 'en'
            page: Zero base page
            quick_date: The date filter.
            sort: The sort mode.
        """
        query = {"locales": locales}
        result = await self.get(
            path=f"/Forum/GetCoreTopicsPaged/{clean_query_value(page)}/{clean_query_value(sort)}/{clean_query_value(quick_date)}/{clean_query_value(category_filter)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_posts_threaded_paged(
        self,
        get_parent_post: bool,
        page: int,
        page_size: int,
        parent_post_id: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: "ForumPostSortEnum",
        showbanned: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Returns a thread of posts at the given parent, optionally returning
        replies to those posts as well as the original parent.

        Parameters:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
        """
        query = {"showbanned": showbanned}
        result = await self.get(
            path=f"/Forum/GetPostsThreadedPaged/{clean_query_value(parent_post_id)}/{clean_query_value(page)}/{clean_query_value(page_size)}/{clean_query_value(reply_size)}/{clean_query_value(get_parent_post)}/{clean_query_value(root_thread_mode)}/{clean_query_value(sort_mode)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_posts_threaded_paged_from_child(
        self,
        child_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: "ForumPostSortEnum",
        showbanned: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Returns a thread of posts starting at the topicId of the input
        childPostId, optionally returning replies to those posts as well as the
        original parent.

        Parameters:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
        """
        query = {"showbanned": showbanned}
        result = await self.get(
            path=f"/Forum/GetPostsThreadedPagedFromChild/{clean_query_value(child_post_id)}/{clean_query_value(page)}/{clean_query_value(page_size)}/{clean_query_value(reply_size)}/{clean_query_value(root_thread_mode)}/{clean_query_value(sort_mode)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_post_and_parent(
        self,
        child_post_id: int,
        showbanned: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Returns the post specified and its immediate parent.

        Parameters:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
        """
        query = {"showbanned": showbanned}
        result = await self.get(
            path=f"/Forum/GetPostAndParent/{clean_query_value(child_post_id)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_post_and_parent_awaiting_approval(
        self,
        child_post_id: int,
        showbanned: t.Optional[str] = None,
    ) -> PostSearchClientResponse:
        """Returns the post specified and its immediate parent of posts that
        are awaiting approval.

        Parameters:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
        """
        query = {"showbanned": showbanned}
        result = await self.get(
            path=f"/Forum/GetPostAndParentAwaitingApproval/{clean_query_value(child_post_id)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_topic_for_content(
        self,
        content_id: int,
    ) -> int64ClientResponse:
        """Gets the post Id for the given content item's comments, if it
        exists."""
        query = None
        result = await self.get(
            path=f"/Forum/GetTopicForContent/{clean_query_value(content_id)}/",
            query=query,
        )
        return forge(int64ClientResponse, result)

    async def get_forum_tag_suggestions(
        self,
        partialtag: t.Optional[str] = None,
    ) -> ListOfTagClientResponse:
        """Gets tag suggestions based on partial text entry, matching them with
        other tags previously used in the forums.

        Parameters:
            partialtag: The partial tag input to generate suggestions from.
        """
        query = {"partialtag": partialtag}
        result = await self.get(
            path="/Forum/GetForumTagSuggestions/",
            query=query,
        )
        return forge(ListOfTagClientResponse, result)

    async def get_poll(
        self,
        topic_id: int,
    ) -> PostSearchClientResponse:
        """Gets the specified forum poll.

        Parameters:
            topic_id: The post id of the topic that has the poll.
        """
        query = None
        result = await self.get(
            path=f"/Forum/Poll/{clean_query_value(topic_id)}/",
            query=query,
        )
        return forge(PostSearchClientResponse, result)

    async def get_recruitment_thread_summaries(
        self,
        request: t.Sequence[int],
    ) -> CEListOfForumRecruitmentDetailClientResponse:
        """Allows the caller to get a list of to 25 recruitment thread summary
        information objects."""
        query = None
        result = await self.post(
            path="/Forum/Recruit/Summaries/", query=query, request=request
        )
        return forge(CEListOfForumRecruitmentDetailClientResponse, result)
