# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


@dt.dataclass(frozen=True)
class TrendingCategories:
    categories: t.Sequence["TrendingCategory"]


@dt.dataclass(frozen=True)
class TrendingCategory:
    category_name: str
    entries: "SearchResultOfTrendingEntry"
    category_id: str


@dt.dataclass(frozen=True)
class TrendingEntry:
    """The list entry view for trending items.

    Returns just enough to show the item on the trending page.
    """

    weight: float  # The weighted score of this trending item.
    is_featured: bool
    identifier: str  # We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.
    entity_type: "TrendingEntryType"  # An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.
    display_name: str  # The localized "display name/article title/'primary localized identifier'" of the entity.
    tagline: str  # If the entity has a localized tagline/subtitle/motto/whatever, that is found here.
    image: str
    start_date: str
    end_date: str
    link: str
    webm_video: str  # If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
    mp4_video: str  # If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
    feature_image: str  # If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.
    items: t.Sequence[
        "TrendingEntry"
    ]  # If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.
    creation_date: str  # If the entry has a date at which it was created, this is that date.


class TrendingEntryType(Enum):
    """The known entity types that you can have returned from Trending."""

    NEWS = 0
    DESTINY_ITEM = 1
    DESTINY_ACTIVITY = 2
    DESTINY_RITUAL = 3
    SUPPORT_ARTICLE = 4
    CREATION = 5
    STREAM = 6
    UPDATE = 7
    LINK = 8
    FORUM_TAG = 9
    CONTAINER = 10
    RELEASE = 11


@dt.dataclass(frozen=True)
class TrendingDetail:
    identifier: str
    entity_type: "TrendingEntryType"
    news: "TrendingEntryNews"
    support: "TrendingEntrySupportArticle"
    destiny_item: "TrendingEntryDestinyItem"
    destiny_activity: "TrendingEntryDestinyActivity"
    destiny_ritual: "TrendingEntryDestinyRitual"
    creation: "TrendingEntryCommunityCreation"


@dt.dataclass(frozen=True)
class TrendingEntryNews:
    article: "ContentItemPublicContract"


@dt.dataclass(frozen=True)
class TrendingEntrySupportArticle:
    article: "ContentItemPublicContract"


@dt.dataclass(frozen=True)
class TrendingEntryDestinyItem:
    item_hash: int


@dt.dataclass(frozen=True)
class TrendingEntryDestinyActivity:
    activity_hash: int
    status: "DestinyPublicActivityStatus"


@dt.dataclass(frozen=True)
class TrendingEntryDestinyRitual:
    image: str
    icon: str
    title: str
    subtitle: str
    date_start: str
    date_end: str
    milestone_details: "DestinyPublicMilestone"  # A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.
    event_content: "DestinyMilestoneContent"  # A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.


@dt.dataclass(frozen=True)
class TrendingEntryCommunityCreation:
    media: str
    title: str
    author: str
    author_membership_id: int
    post_id: int
    body: str
    upvotes: int


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types import SearchResultOfTrendingEntry  # noqa: E402
from bungieapi.generated.types.content import ContentItemPublicContract  # noqa: E402
from bungieapi.generated.types.destiny.activities import (
    DestinyPublicActivityStatus,
)  # noqa: E402
from bungieapi.generated.types.destiny.milestones import (
    DestinyMilestoneContent,
)  # noqa: E402
from bungieapi.generated.types.destiny.milestones import (
    DestinyPublicMilestone,
)  # noqa: E402
