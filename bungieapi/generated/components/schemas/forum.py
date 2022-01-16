# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum

from bungieapi.json import to_json
from bungieapi.types import BitMask


class ForumTopicsCategoryFiltersEnum(BitMask):
    NONE = 0
    LINKS = 1
    QUESTIONS = 2
    ANSWERED_QUESTIONS = 4
    MEDIA = 8
    TEXT_ONLY = 16
    ANNOUNCEMENT = 32
    BUNGIE_OFFICIAL = 64
    POLLS = 128


class ForumTopicsQuickDateEnum(Enum):
    ALL = 0
    LAST_YEAR = 1
    LAST_MONTH = 2
    LAST_WEEK = 3
    LAST_DAY = 4


class ForumTopicsSortEnum(Enum):
    DEFAULT = 0
    LAST_REPLIED = 1
    MOST_REPLIED = 2
    POPULARITY = 3
    CONTROVERSIALITY = 4
    LIKED = 5
    HIGHEST_RATED = 6
    MOST_UPVOTED = 7


@dt.dataclass(frozen=True)
class PostResponse:
    is_pinned: bool
    ignore_status: "IgnoreResponse"
    is_active: bool
    is_announcement: bool
    last_reply_timestamp: str
    latest_reply_author_id: int
    latest_reply_post_id: int
    locale: str
    popularity: "ForumPostPopularity"
    thumbnail: str
    url_media_type: "ForumMediaType"
    user_has_muted_post: bool
    user_has_rated: bool
    user_rating: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "lastReplyTimestamp": to_json(self.last_reply_timestamp),
            "IsPinned": to_json(self.is_pinned),
            "urlMediaType": to_json(self.url_media_type),
            "thumbnail": to_json(self.thumbnail),
            "popularity": to_json(self.popularity),
            "isActive": to_json(self.is_active),
            "isAnnouncement": to_json(self.is_announcement),
            "userRating": to_json(self.user_rating),
            "userHasRated": to_json(self.user_has_rated),
            "userHasMutedPost": to_json(self.user_has_muted_post),
            "latestReplyPostId": to_json(self.latest_reply_post_id),
            "latestReplyAuthorId": to_json(self.latest_reply_author_id),
            "ignoreStatus": to_json(self.ignore_status),
            "locale": to_json(self.locale),
        }


class ForumMediaType(Enum):
    NONE = 0
    IMAGE = 1
    VIDEO = 2
    YOUTUBE = 3


class ForumPostPopularity(Enum):
    EMPTY = 0
    DEFAULT = 1
    DISCUSSED = 2
    COOL_STORY = 3
    HEATING_UP = 4
    HOT = 5


@dt.dataclass(frozen=True)
class PostSearchResponse:
    authors: t.Sequence["GeneralUser"]
    groups: t.Sequence["GroupResponse"]
    has_more: bool
    polls: t.Sequence["PollResponse"]
    query: "PagedQuery"
    recruitment_details: t.Sequence["ForumRecruitmentDetail"]
    related_posts: t.Sequence["PostResponse"]
    replacement_continuation_token: str
    results: t.Sequence["PostResponse"]
    searched_tags: t.Sequence["TagResponse"]
    total_results: int
    use_total_results: bool  # If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    available_pages: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "relatedPosts": to_json(self.related_posts),
            "authors": to_json(self.authors),
            "groups": to_json(self.groups),
            "searchedTags": to_json(self.searched_tags),
            "polls": to_json(self.polls),
            "recruitmentDetails": to_json(self.recruitment_details),
            "availablePages": to_json(self.available_pages),
            "results": to_json(self.results),
            "totalResults": to_json(self.total_results),
            "hasMore": to_json(self.has_more),
            "query": to_json(self.query),
            "replacementContinuationToken": to_json(
                self.replacement_continuation_token
            ),
            "useTotalResults": to_json(self.use_total_results),
        }


@dt.dataclass(frozen=True)
class PollResponse:
    results: t.Sequence["PollResult"]
    topic_id: int
    total_votes: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "topicId": to_json(self.topic_id),
            "results": to_json(self.results),
            "totalVotes": to_json(self.total_votes),
        }


@dt.dataclass(frozen=True)
class PollResult:
    answer_slot: int
    answer_text: str
    last_vote_date: str
    requesting_user_voted: bool
    votes: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "answerText": to_json(self.answer_text),
            "answerSlot": to_json(self.answer_slot),
            "lastVoteDate": to_json(self.last_vote_date),
            "votes": to_json(self.votes),
            "requestingUserVoted": to_json(self.requesting_user_voted),
        }


@dt.dataclass(frozen=True)
class ForumRecruitmentDetail:
    fireteam: t.Sequence["GeneralUser"]
    approved: bool
    intensity: "ForumRecruitmentIntensityLabel"
    kicked_player_ids: t.Sequence[int]
    microphone_required: bool
    player_slots_remaining: int
    player_slots_total: int
    tone: "ForumRecruitmentToneLabel"
    topic_id: int
    conversation_id: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "topicId": to_json(self.topic_id),
            "microphoneRequired": to_json(self.microphone_required),
            "intensity": to_json(self.intensity),
            "tone": to_json(self.tone),
            "approved": to_json(self.approved),
            "conversationId": to_json(self.conversation_id),
            "playerSlotsTotal": to_json(self.player_slots_total),
            "playerSlotsRemaining": to_json(self.player_slots_remaining),
            "Fireteam": to_json(self.fireteam),
            "kickedPlayerIds": to_json(self.kicked_player_ids),
        }


class ForumRecruitmentIntensityLabel(Enum):
    NONE = 0
    CASUAL = 1
    PROFESSIONAL = 2


class ForumRecruitmentToneLabel(Enum):
    NONE = 0
    FAMILY_FRIENDLY = 1
    ROWDY = 2


class ForumPostSortEnum(Enum):
    DEFAULT = 0
    OLDEST_FIRST = 1


class CommunityContentSortMode(Enum):
    TRENDING = 0
    LATEST = 1
    HIGHEST_RATED = 2


from bungieapi.generated.components.schemas.groups_v2 import GroupResponse  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.ignores import IgnoreResponse  # noqa: E402
from bungieapi.generated.components.schemas.queries import PagedQuery  # noqa: E402
from bungieapi.generated.components.schemas.tags.models.contracts import (  # noqa: E402
    TagResponse,
)
from bungieapi.generated.components.schemas.user import GeneralUser  # noqa: E402
