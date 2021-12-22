# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyMilestoneDefinition:
    """'Milestones are an in-game concept where they're attempting to tell you
    what you can do next in-game. If that sounds a lot like Advisors in Destiny
    1, it is! So we threw out Advisors in the Destiny 2 API and tacked all of
    the data we would have put on Advisors onto Milestones instead. Each
    Milestone represents something going on in the game right now:

    - A "ritual activity" you can perform, like nightfall
    - A "special event" that may have activities related to it, like Taco Tuesday (there's no Taco Tuesday in Destiny 2)
    - A checklist you can fulfill, like helping your Clan complete all of its weekly objectives
    - A tutorial quest you can play through, like the introduction to the Crucible.
    Most of these milestones appear in game as well. Some of them are BNet only, because we're so extra. You're welcome.
    There are some important caveats to understand about how we currently render Milestones and their deficiencies. The game currently doesn't have any content that actually tells you oughtright *what* the Milestone is: that is to say, what you'll be doing. The best we get is either a description of the overall Milestone, or of the Quest that the Milestone is having you partake in: which is usually something that assumes you already know what it's talking about, like "Complete 5 Challenges". 5 Challenges for what? What's a challenge? These are not questions that the Milestone data will answer for you unfortunately.
    This isn't great, and in the future I'd like to add some custom text to give you more contextual information to pass on to your users. But for now, you can do what we do to render what little display info we do have:
    Start by looking at the currently active quest (ideally, you've fetched DestinyMilestone or DestinyPublicMilestone data from the API, so you know the currently active quest for the Milestone in question). Look up the Quests property in the Milestone Definition, and check if it has display properties. If it does, show that as the description of the Milestone. If it doesn't, fall back on the Milestone's description.
    This approach will let you avoid, whenever possible, the even less useful (and sometimes nonexistant) milestone-level names and descriptions.
    """

    display_properties: "DestinyDisplayPropertiesDefinition"
    display_preference: "DestinyMilestoneDisplayPreference"
    image: str
    milestone_type: "DestinyMilestoneType"
    recruitable: bool
    friendly_name: str
    show_in_explorer: bool
    show_in_milestones: bool
    explore_prioritizes_activity_image: bool
    has_predictable_dates: bool
    quests: t.Mapping[str, "DestinyMilestoneQuestDefinition"]
    rewards: t.Mapping[str, "DestinyMilestoneRewardCategoryDefinition"]
    vendors_display_title: str
    vendors: t.Sequence["DestinyMilestoneVendorDefinition"]
    values: t.Mapping[str, "DestinyMilestoneValueDefinition"]
    is_in_game_milestone: bool
    activities: t.Sequence["DestinyMilestoneChallengeActivityDefinition"]
    default_order: int
    hash: int
    index: int
    redacted: bool


DestinyMilestoneDisplayPreference = t.Any
DestinyMilestoneType = t.Any


@dt.dataclass(frozen=True)
class DestinyMilestoneQuestDefinition:
    """'Any data we need to figure out whether this Quest Item is the currently
    active one for the conceptual Milestone.

    Even just typing this description, I already regret it.
    """

    quest_item_hash: int
    display_properties: t.Any
    override_image: str
    quest_rewards: t.Any
    activities: t.Mapping[str, "DestinyMilestoneActivityDefinition"]
    destination_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneQuestRewardsDefinition:
    ''' 'If rewards are given in a quest - as opposed to overall in the entire Milestone - there's way less to track. We're going to simplify this contract as a result. However, this also gives us the opportunity to potentially put more than just item information into the reward data if we're able to mine it out in the future. Remember this if you come back and ask "why are quest reward items nested inside of their own class?"'''

    items: t.Sequence["DestinyMilestoneQuestRewardItem"]


@dt.dataclass(frozen=True)
class DestinyMilestoneQuestRewardItem:
    """ 'A subclass of DestinyItemQuantity, that provides not just the item and its quantity but also information that BNet can - at some point - use internally to provide more robust runtime information about the item's qualities.
    If you want it, please ask! We're just out of time to wire it up right now. Or a clever person just may do it with our existing endpoints."""

    vendor_hash: int
    vendor_item_index: int
    item_hash: int
    item_instance_id: int
    quantity: int
    has_conditional_visibility: bool


@dt.dataclass(frozen=True)
class DestinyMilestoneActivityDefinition:
    """'Milestones can have associated activities which provide additional
    information about the context, challenges, modifiers, state etc...

    related to this Milestone. Information we need to be able to return
    that data is defined here, along with Tier data to establish a
    relationship between a conceptual Activity and its difficulty levels
    and variants.
    """

    conceptual_activity_hash: int
    variants: t.Mapping[str, "DestinyMilestoneActivityVariantDefinition"]


@dt.dataclass(frozen=True)
class DestinyMilestoneActivityVariantDefinition:
    """'Represents a variant on an activity for a Milestone: a specific
    difficulty tier, or a specific activity variant for example.

    These will often have more specific details, such as an associated
    Guided Game, progression steps, tier-specific rewards, and custom
    values.
    """

    activity_hash: int
    order: int


@dt.dataclass(frozen=True)
class DestinyMilestoneRewardCategoryDefinition:
    """'The definition of a category of rewards, that contains many individual
    rewards."""

    category_hash: int
    category_identifier: str
    display_properties: t.Any
    reward_entries: t.Mapping[str, "DestinyMilestoneRewardEntryDefinition"]
    order: int


@dt.dataclass(frozen=True)
class DestinyMilestoneRewardEntryDefinition:
    """'The definition of a specific reward, which may be contained in a
    category of rewards and that has optional information about how it is
    obtained."""

    reward_entry_hash: int
    reward_entry_identifier: str
    items: t.Sequence["DestinyItemQuantity"]
    vendor_hash: int
    display_properties: t.Any
    order: int


@dt.dataclass(frozen=True)
class DestinyMilestoneVendorDefinition:
    """'If the Milestone or a component has vendors whose inventories
    could/should be displayed that are relevant to it, this will return the
    vendor in question.

    It also contains information we need to determine whether that
    vendor is actually relevant at the moment, given the user's current
    state.
    """

    vendor_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneValueDefinition:
    """'The definition for information related to a key/value pair that is
    relevant for a particular Milestone or component within the Milestone.

    This lets us more flexibly pass up information that's useful to
    someone, even if it's not necessarily us.
    """

    key: str
    display_properties: "DestinyDisplayPropertiesDefinition"


@dt.dataclass(frozen=True)
class DestinyMilestoneChallengeActivityDefinition:
    activity_hash: int
    challenges: t.Sequence["DestinyMilestoneChallengeDefinition"]
    activity_graph_nodes: t.Sequence["DestinyMilestoneChallengeActivityGraphNodeEntry"]
    phases: t.Sequence["DestinyMilestoneChallengeActivityPhase"]


@dt.dataclass(frozen=True)
class DestinyMilestoneChallengeDefinition:
    challenge_objective_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneChallengeActivityGraphNodeEntry:
    activity_graph_hash: int
    activity_graph_node_hash: int


@dt.dataclass(frozen=True)
class DestinyMilestoneChallengeActivityPhase:
    phase_hash: int


from bungieapi.generated.types.destiny import DestinyItemQuantity  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
