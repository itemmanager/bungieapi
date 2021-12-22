# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types.groups_v2 import GroupResponse
from bungieapi.generated.types.ignores import IgnoreResponse
from bungieapi.generated.types.queries import PagedQuery
from bungieapi.generated.types.tags.models.contracts import TagResponse
from bungieapi.generated.types.user import GeneralUser

ForumTopicsCategoryFiltersEnum = t.Any
ForumTopicsQuickDateEnum = t.Any
ForumTopicsSortEnum = t.Any


@dt.dataclass(frozen=True)
class PostResponse:
    last_reply_timestamp: str
    is_pinned: bool
    url_media_type: "ForumMediaType"
    thumbnail: str
    popularity: "ForumPostPopularity"
    is_active: bool
    is_announcement: bool
    user_rating: int
    user_has_rated: bool
    user_has_muted_post: bool
    latest_reply_post_id: int
    latest_reply_author_id: int
    ignore_status: IgnoreResponse
    locale: str


ForumMediaType = t.Any
ForumPostPopularity = t.Any


@dt.dataclass(frozen=True)
class PostSearchResponse:
    related_posts: t.Sequence["PostResponse"]
    authors: t.Sequence[GeneralUser]
    groups: t.Sequence[GroupResponse]
    searched_tags: t.Sequence[TagResponse]
    polls: t.Sequence["PollResponse"]
    recruitment_details: t.Sequence["ForumRecruitmentDetail"]
    available_pages: int
    results: t.Sequence["PostResponse"]
    total_results: int
    has_more: bool
    query: PagedQuery
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class PollResponse:
    topic_id: int
    results: t.Sequence["PollResult"]
    total_votes: int


@dt.dataclass(frozen=True)
class PollResult:
    answer_text: str
    answer_slot: int
    last_vote_date: str
    votes: int
    requesting_user_voted: bool


@dt.dataclass(frozen=True)
class ForumRecruitmentDetail:
    topic_id: int
    microphone_required: bool
    intensity: "ForumRecruitmentIntensityLabel"
    tone: "ForumRecruitmentToneLabel"
    approved: bool
    conversation_id: int
    player_slots_total: int
    player_slots_remaining: int
    fireteam: t.Sequence[GeneralUser]
    kicked_player_ids: t.Sequence[int]


ForumRecruitmentIntensityLabel = t.Any
ForumRecruitmentToneLabel = t.Any
ForumPostSortEnum = t.Any
CommunityContentSortMode = t.Any
