# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class TrendingCategories:
    categories: t.Sequence["TrendingCategory"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "categories": to_json(self.categories),
        }


@dt.dataclass(frozen=True)
class TrendingCategory:
    category_id: str
    category_name: str
    entries: "SearchResultOfTrendingEntry"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "categoryName": to_json(self.category_name),
            "entries": to_json(self.entries),
            "categoryId": to_json(self.category_id),
        }


@dt.dataclass(frozen=True)
class TrendingEntry:
    """The list entry view for trending items.

    Returns just enough to show the item on the trending page.
    """

    display_name: str = dt.field(
        metadata={
            "description": "The localized \"display name/article title/'primary localized identifier'\" of the entity."
        }
    )
    entity_type: "TrendingEntryType" = dt.field(
        metadata={
            "description": "An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item."
        }
    )
    feature_image: str = dt.field(
        metadata={
            "description": "If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time."
        }
    )
    identifier: str = dt.field(
        metadata={
            "description": "We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type."
        }
    )
    image: str
    is_featured: bool
    items: t.Sequence["TrendingEntry"] = dt.field(
        metadata={
            "description": "If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header."
        }
    )
    link: str
    mp4_video: str = dt.field(
        metadata={
            "description": "If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo"
        }
    )
    tagline: str = dt.field(
        metadata={
            "description": "If the entity has a localized tagline/subtitle/motto/whatever, that is found here."
        }
    )
    webm_video: str = dt.field(
        metadata={
            "description": "If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo"
        }
    )
    weight: float = dt.field(
        metadata={"description": "The weighted score of this trending item."}
    )
    creation_date: t.Optional[str] = dt.field(
        default=None,
        metadata={
            "description": "If the entry has a date at which it was created, this is that date."
        },
    )
    end_date: t.Optional[str] = None
    start_date: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "weight": to_json(self.weight),
            "isFeatured": to_json(self.is_featured),
            "identifier": to_json(self.identifier),
            "entityType": to_json(self.entity_type),
            "displayName": to_json(self.display_name),
            "tagline": to_json(self.tagline),
            "image": to_json(self.image),
            "startDate": to_json(self.start_date),
            "endDate": to_json(self.end_date),
            "link": to_json(self.link),
            "webmVideo": to_json(self.webm_video),
            "mp4Video": to_json(self.mp4_video),
            "featureImage": to_json(self.feature_image),
            "items": to_json(self.items),
            "creationDate": to_json(self.creation_date),
        }


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
    creation: "TrendingEntryCommunityCreation"
    destiny_activity: "TrendingEntryDestinyActivity"
    destiny_item: "TrendingEntryDestinyItem"
    destiny_ritual: "TrendingEntryDestinyRitual"
    entity_type: "TrendingEntryType"
    identifier: str
    news: "TrendingEntryNews"
    support: "TrendingEntrySupportArticle"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "identifier": to_json(self.identifier),
            "entityType": to_json(self.entity_type),
            "news": to_json(self.news),
            "support": to_json(self.support),
            "destinyItem": to_json(self.destiny_item),
            "destinyActivity": to_json(self.destiny_activity),
            "destinyRitual": to_json(self.destiny_ritual),
            "creation": to_json(self.creation),
        }


@dt.dataclass(frozen=True)
class TrendingEntryNews:
    article: "ContentItemPublicContract"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "article": to_json(self.article),
        }


@dt.dataclass(frozen=True)
class TrendingEntrySupportArticle:
    article: "ContentItemPublicContract"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "article": to_json(self.article),
        }


@dt.dataclass(frozen=True)
class TrendingEntryDestinyItem:
    item_hash: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "itemHash": to_json(self.item_hash),
        }


@dt.dataclass(frozen=True)
class TrendingEntryDestinyActivity:
    activity_hash: int
    status: "DestinyPublicActivityStatus"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activityHash": to_json(self.activity_hash),
            "status": to_json(self.status),
        }


@dt.dataclass(frozen=True)
class TrendingEntryDestinyRitual:
    event_content: "DestinyMilestoneContent" = dt.field(
        metadata={
            "description": 'A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.'
        }
    )
    icon: str
    image: str
    milestone_details: "DestinyPublicMilestone" = dt.field(
        metadata={
            "description": "A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here."
        }
    )
    subtitle: str
    title: str
    date_end: t.Optional[str] = None
    date_start: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "image": to_json(self.image),
            "icon": to_json(self.icon),
            "title": to_json(self.title),
            "subtitle": to_json(self.subtitle),
            "dateStart": to_json(self.date_start),
            "dateEnd": to_json(self.date_end),
            "milestoneDetails": to_json(self.milestone_details),
            "eventContent": to_json(self.event_content),
        }


@dt.dataclass(frozen=True)
class TrendingEntryCommunityCreation:
    author: str
    author_membership_id: int
    body: str
    media: str
    post_id: int
    title: str
    upvotes: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "media": to_json(self.media),
            "title": to_json(self.title),
            "author": to_json(self.author),
            "authorMembershipId": to_json(self.author_membership_id),
            "postId": to_json(self.post_id),
            "body": to_json(self.body),
            "upvotes": to_json(self.upvotes),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas import (  # noqa: E402
    SearchResultOfTrendingEntry,
)
from bungieapi.generated.components.schemas.content import (  # noqa: E402
    ContentItemPublicContract,
)
from bungieapi.generated.components.schemas.destiny.activities import (  # noqa: E402
    DestinyPublicActivityStatus,
)
from bungieapi.generated.components.schemas.destiny.milestones import (  # noqa: E402
    DestinyMilestoneContent,
    DestinyPublicMilestone,
)
