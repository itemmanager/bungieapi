# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyMilestone:
    """'Represents a runtime instance of a user's milestone status.

    Live Milestone data should be combined with
    DestinyMilestoneDefinition data to show the user a picture of what
    is available for them to do in the game, and their status in regards
    to said "things to do." Consider it a big, wonky to-do list, or
    Advisors 3.0 for those who remember the Destiny 1 API.
    """

    milestone_hash: int
    available_quests: t.Sequence["DestinyMilestoneQuest"]
    activities: t.Sequence["DestinyMilestoneChallengeActivity"]
    values: t.Mapping[str, float]
    vendor_hashes: t.Sequence[int]
    vendors: t.Sequence["DestinyMilestoneVendor"]
    rewards: t.Sequence["DestinyMilestoneRewardCategory"]
    start_date: str
    end_date: str
    order: int


@dt.dataclass(frozen=True)
class DestinyMilestoneQuest:
    """'If a Milestone has one or more Quests, this will contain the live
    information for the character's status with one of those quests."""

    quest_item_hash: int
    status: "DestinyQuestStatus"
    activity: "DestinyMilestoneActivity"
    challenges: t.Sequence["DestinyChallengeStatus"]


@dt.dataclass(frozen=True)
class DestinyMilestoneActivity:
    """'Sometimes, we know the specific activity that the Milestone wants you
    to play.

    This entity provides additional information about that Activity and
    all of its variants. (sometimes there's only one variant, but I
    think you get the point)
    """

    activity_hash: int
    activity_mode_hash: int
    activity_mode_type: int
    modifier_hashes: t.Sequence[int]
    variants: t.Sequence["DestinyMilestoneActivityVariant"]


@dt.dataclass(frozen=True)
class DestinyMilestoneActivityVariant:
    """'Represents custom data that we know about an individual variant of an
    activity."""

    activity_hash: int
    completion_status: "DestinyMilestoneActivityCompletionStatus"
    activity_mode_hash: int
    activity_mode_type: int


@dt.dataclass(frozen=True)
class DestinyMilestoneActivityCompletionStatus:
    """'Represents this player's personal completion status for the Activity
    under a Milestone, if the activity has trackable completion and progress
    information.

    (most activities won't, or the concept won't apply. For instance, it
    makes sense to talk about a tier of a raid as being Completed or
    having progress, but it doesn't make sense to talk about a Crucible
    Playlist in those terms.
    """

    completed: bool
    phases: t.Sequence["DestinyMilestoneActivityPhase"]


@dt.dataclass(frozen=True)
class DestinyMilestoneActivityPhase:
    """'Represents whatever information we can return about an explicit phase
    in an activity.

    In the future, I hope we'll have more than just "guh, you done gone
    and did something," but for the forseeable future that's all we've
    got. I'm making it more than just a list of booleans out of that
    overly-optimistic hope.
    """

    complete: bool
    phase_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneChallengeActivity:
    activity_hash: int
    challenges: t.Sequence["DestinyChallengeStatus"]
    modifier_hashes: t.Sequence[int]
    boolean_activity_options: t.Mapping[str, bool]
    loadout_requirement_index: int
    phases: t.Sequence["DestinyMilestoneActivityPhase"]


@dt.dataclass(frozen=True)
class DestinyMilestoneVendor:
    """'If a Milestone has one or more Vendors that are relevant to it, this
    will contain information about that vendor that you can choose to show."""

    vendor_hash: int
    preview_item_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneRewardCategory:
    """'Represents a category of "summary" rewards that can be earned for the
    Milestone regardless of specific quest rewards that can be earned."""

    reward_category_hash: int
    entries: t.Sequence["DestinyMilestoneRewardEntry"]


@dt.dataclass(frozen=True)
class DestinyMilestoneRewardEntry:
    """'The character-specific data for a milestone's reward entry.

    See DestinyMilestoneDefinition for more information about Reward
    Entries.
    """

    reward_entry_hash: int
    earned: bool
    redeemed: bool


@dt.dataclass(frozen=True)
class DestinyMilestoneContent:
    """'Represents localized, extended content related to Milestones.

    This is intentionally returned by a separate endpoint and not with
    Character-level Milestone data because we do not put localized data
    into standard Destiny responses, both for brevity of response and
    for caching purposes. If you really need this data, hit the
    Milestone Content endpoint.
    """

    about: str
    status: str
    tips: t.Sequence[str]
    item_categories: t.Sequence["DestinyMilestoneContentItemCategory"]


@dt.dataclass(frozen=True)
class DestinyMilestoneContentItemCategory:
    """'Part of our dynamic, localized Milestone content is arbitrary
    categories of items.

    These are built in our content management system, and thus aren't
    the same as programmatically generated rewards.
    """

    title: str
    item_hashes: t.Sequence[int]


@dt.dataclass(frozen=True)
class DestinyPublicMilestone:
    """'Information about milestones, presented in a character state-agnostic
    manner.

    Combine this data with DestinyMilestoneDefinition to get a full
    picture of the milestone, which is basically a checklist of things
    to do in the game. Think of this as GetPublicAdvisors 3.0, for those
    who used the Destiny 1 API.
    """

    milestone_hash: int
    available_quests: t.Sequence["DestinyPublicMilestoneQuest"]
    activities: t.Sequence["DestinyPublicMilestoneChallengeActivity"]
    vendor_hashes: t.Sequence[int]
    vendors: t.Sequence["DestinyPublicMilestoneVendor"]
    start_date: str
    end_date: str
    order: int


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneQuest:
    quest_item_hash: int
    activity: "DestinyPublicMilestoneActivity"
    challenges: t.Sequence["DestinyPublicMilestoneChallenge"]


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneActivity:
    """'A milestone may have one or more conceptual Activities associated with
    it, and each of those conceptual activities could have a variety of
    variants, modes, tiers, what-have-you.

    Our attempts to determine what qualifies as a conceptual activity
    are, unfortunately, janky. So if you see missing modes or modes that
    don't seem appropriate to you, let us know and I'll buy you a beer
    if we ever meet up in person.
    """

    activity_hash: int
    modifier_hashes: t.Sequence[int]
    variants: t.Sequence["DestinyPublicMilestoneActivityVariant"]
    activity_mode_hash: int
    activity_mode_type: int


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneActivityVariant:
    """'Represents a variant of an activity that's relevant to a milestone."""

    activity_hash: int
    activity_mode_hash: int
    activity_mode_type: int


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneChallenge:
    """'A Milestone can have many Challenges.

    Challenges are just extra Objectives that provide a fun way to mix-
    up play and provide extra rewards.
    """

    objective_hash: int
    activity_hash: int


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneChallengeActivity:
    activity_hash: int
    challenge_objective_hashes: t.Sequence[int]
    modifier_hashes: t.Sequence[int]
    loadout_requirement_index: int
    phase_hashes: t.Sequence[int]
    boolean_activity_options: t.Mapping[str, bool]


@dt.dataclass(frozen=True)
class DestinyPublicMilestoneVendor:
    vendor_hash: int
    preview_item_hash: int


from bungieapi.generated.types.destiny.challenges import (
    DestinyChallengeStatus,
)  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.quests import DestinyQuestStatus  # noqa: E402
