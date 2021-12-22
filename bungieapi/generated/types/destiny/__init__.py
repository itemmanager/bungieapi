# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


@dt.dataclass(frozen=True)
class DestinyProgression:
    """'Information about a current character's status with a Progression.

    A progression is a value that can increase with activity and has
    levels. Think Character Level and Reputation Levels. Combine this
    "live" data with the related DestinyProgressionDefinition for a full
    picture of the Progression.
    """

    progression_hash: int
    daily_progress: int
    daily_limit: int
    weekly_progress: int
    weekly_limit: int
    current_progress: int
    level: int
    level_cap: int
    step_index: int
    progress_to_next_level: int
    next_level_at: int
    current_reset_count: int
    season_resets: t.Sequence["DestinyProgressionResetEntry"]
    reward_item_states: t.Sequence["DestinyProgressionRewardItemState"]


@dt.dataclass(frozen=True)
class DestinyProgressionResetEntry:
    """'Represents a season and the number of resets you had in that season.

    We do not necessarily - even for progressions with resets - track it over all seasons. So be careful and check the season numbers being returned.
    """

    season: int
    resets: int


class DestinyProgressionRewardItemState(Enum):
    """Represents the different states a progression reward item can be in."""

    NONE = 0
    INVISIBLE = 1
    EARNED = 2
    CLAIMED = 4
    CLAIM_ALLOWED = 8


class DestinyProgressionScope(Enum):
    """There are many Progressions in Destiny (think Character Level, or
    Reputation).

    These are the various "Scopes" of Progressions, which affect many things: * Where/if they are stored * How they are calculated * Where they can be used in other game logic
    """

    ACCOUNT = 0
    CHARACTER = 1
    CLAN = 2
    ITEM = 3
    IMPLICIT_FROM_EQUIPMENT = 4
    MAPPED = 5
    MAPPED_AGGREGATE = 6
    MAPPED_STAT = 7
    MAPPED_UNLOCK_VALUE = 8


class DestinyProgressionStepDisplayEffect(Enum):
    """If progression is earned, this determines whether the progression shows visual effects on the character or its item - or neither."""

    NONE = 0
    CHARACTER = 1
    ITEM = 2


@dt.dataclass(frozen=True)
class DestinyItemQuantity:
    """'Used in a number of Destiny contracts to return data about an item
    stack and its quantity.

    Can optionally return an itemInstanceId if the item is instanced - in which case, the quantity returned will be 1. If it's not... uh, let me know okay? Thanks.
    """

    item_hash: int
    item_instance_id: int
    quantity: int
    has_conditional_visibility: bool


class TierType(Enum):
    UNKNOWN = 0
    CURRENCY = 1
    BASIC = 2
    COMMON = 3
    RARE = 4
    SUPERIOR = 5
    EXOTIC = 6


class BucketScope(Enum):
    CHARACTER = 0
    ACCOUNT = 1


class BucketCategory(Enum):
    INVISIBLE = 0
    ITEM = 1
    CURRENCY = 2
    EQUIPPABLE = 3
    IGNORED = 4


class ItemLocation(Enum):
    UNKNOWN = 0
    INVENTORY = 1
    VAULT = 2
    VENDOR = 3
    POSTMASTER = 4


class DestinyStatAggregationType(Enum):
    """When a Stat (DestinyStatDefinition) is aggregated, this is the rules
    used for determining the level and formula used for aggregation.

    * CharacterAverage = apply a weighted average using the related DestinyStatGroupDefinition on the DestinyInventoryItemDefinition across the character's equipped items. See both of those definitions for details. * Character = don't aggregate: the stat should be located and used directly on the character. * Item = don't aggregate: the stat should be located and used directly on the item.
    """

    CHARACTER_AVERAGE = 0
    CHARACTER = 1
    ITEM = 2


class DestinyStatCategory(Enum):
    """At last, stats have categories.

    Use this for whatever purpose you might wish.
    """

    GAMEPLAY = 0
    WEAPON = 1
    DEFENSE = 2
    PRIMARY = 3


class EquippingItemBlockAttributes(Enum):
    NONE = 0
    EQUIP_ON_ACQUIRE = 1


class DestinyAmmunitionType(Enum):
    NONE = 0
    PRIMARY = 1
    SPECIAL = 2
    HEAVY = 3
    UNKNOWN = 4


@dt.dataclass(frozen=True)
class DyeReference:
    channel_hash: int
    dye_hash: int


class DestinyVendorProgressionType(Enum):
    """Describes the type of progression that a vendor has."""

    DEFAULT = 0
    RITUAL = 1
    NO_SEASONAL_REFRESH = 2


class VendorDisplayCategorySortOrder(Enum):
    """Display categories can have custom sort orders.

    These are the possible options.
    """

    DEFAULT = 0
    SORT_BY_TIER = 1


class DestinyVendorInteractionRewardSelection(Enum):
    """When a Vendor Interaction provides rewards, they'll either let you
    choose one or let you have all of them.

    This determines which it will be.
    """

    NONE = 0
    ONE = 1
    ALL = 2


class DestinyVendorReplyType(Enum):
    """This determines the type of reply that a Vendor will have during an
    Interaction."""

    ACCEPT = 0
    DECLINE = 1
    COMPLETE = 2


class VendorInteractionType(Enum):
    """An enumeration of the known UI interactions for Vendors."""

    UNKNOWN = 0
    UNDEFINED = 1
    QUEST_COMPLETE = 2
    QUEST_CONTINUE = 3
    REPUTATION_PREVIEW = 4
    RANK_UP_REWARD = 5
    TOKEN_TURN_IN = 6
    QUEST_ACCEPT = 7
    PROGRESS_TAB = 8
    END = 9
    START = 10


class DestinyItemSortType(Enum):
    """Determines how items are sorted in an inventory bucket."""

    ITEM_ID = 0
    TIMESTAMP = 1
    STACK_SIZE = 2


class DestinyVendorItemRefundPolicy(Enum):
    """The action that happens when the user attempts to refund an item."""

    NOT_REFUNDABLE = 0
    DELETES_ITEM = 1
    REVOKES_LICENSE = 2


class DestinyGatingScope(Enum):
    """This enumeration represents the most restrictive type of gating that is
    being performed by an entity.

    This is useful as a shortcut to avoid a lot of lookups when determining whether the gating on an Entity applies to everyone equally, or to their specific Profile or Character states.
    None = There is no gating on this item.
    Global = The gating on this item is based entirely on global game state. It will be gated the same for everyone.
    Clan = The gating on this item is at the Clan level. For instance, if you're gated by Clan level this will be the case.
    Profile = The gating includes Profile-specific checks, but not on the Profile's characters. An example of this might be when you acquire an Emblem: the Emblem will be available in your Kiosk for all characters in your Profile from that point onward.
    Character = The gating includes Character-specific checks, including character level restrictions. An example of this might be an item that you can't purchase from a Vendor until you reach a specific Character Level.
    Item = The gating includes item-specific checks. For BNet, this generally implies that we'll show this data only on a character level or deeper.
    AssumedWorstCase = The unlocks and checks being used for this calculation are of an unknown type and are used for unknown purposes. For instance, if some great person decided that an unlock value should be globally scoped, but then the game changes it using character-specific data in a way that BNet doesn't know about. Because of the open-ended potential for this to occur, many unlock checks for "globally" scoped unlock data may be assumed as the worst case unless it has been specifically whitelisted as otherwise. That sucks, but them's the breaks.
    """

    NONE = 0
    GLOBAL = 1
    CLAN = 2
    PROFILE = 3
    CHARACTER = 4
    ITEM = 5
    ASSUMED_WORST_CASE = 6


class SocketTypeActionType(Enum):
    """Indicates the type of actions that can be performed."""

    INSERT_PLUG = 0
    INFUSE_ITEM = 1
    REINITIALIZE_SOCKET = 2


class DestinySocketVisibility(Enum):
    VISIBLE = 0
    HIDDEN = 1
    HIDDEN_WHEN_EMPTY = 2
    HIDDEN_IF_NO_PLUGS_AVAILABLE = 3


class DestinySocketCategoryStyle(Enum):
    """Represents the possible and known UI styles used by the game for
    rendering Socket Categories."""

    UNKNOWN = 0
    REUSABLE = 1
    CONSUMABLE = 2
    UNLOCKABLE = 3
    INTRINSIC = 4
    ENERGY_METER = 5
    LARGE_PERK = 6
    ABILITIES = 7
    SUPERS = 8


class ActivityGraphNodeHighlightType(Enum):
    """The various known UI styles in which an item can be highlighted.

    It'll be up to you to determine what you want to show based on this
    highlighting, BNet doesn't have any assets that correspond to these
    states. And yeah, RiseOfIron and Comet have their own special
    highlight states. Don't ask me, I can't imagine they're still used.
    """

    NONE = 0
    NORMAL = 1
    HYPER = 2
    COMET = 3
    RISE_OF_IRON = 4


class DestinyUnlockValueUIStyle(Enum):
    """If you're showing an unlock value in the UI, this is the format in which
    it should be shown.

    You'll have to build your own algorithms on the client side to
    determine how best to render these options.
    """

    AUTOMATIC = 0
    FRACTION = 1
    CHECKBOX = 2
    PERCENTAGE = 3
    DATE_TIME = 4
    FRACTION_FLOAT = 5
    INTEGER = 6
    TIME_DURATION = 7
    HIDDEN = 8
    MULTIPLIER = 9
    GREEN_PIPS = 10
    RED_PIPS = 11
    EXPLICIT_PERCENTAGE = 12
    RAW_FLOAT = 13


class DestinyObjectiveGrantStyle(Enum):
    """Some Objectives provide perks, generally as part of providing some kind
    of interesting modifier for a Challenge or Quest.

    This indicates when the Perk is granted.
    """

    WHEN_INCOMPLETE = 0
    WHEN_COMPLETE = 1
    ALWAYS = 2


class DamageType(Enum):
    NONE = 0
    KINETIC = 1
    ARC = 2
    THERMAL = 3
    VOID = 4
    RAID = 5
    STASIS = 6


class DestinyActivityNavPointType(Enum):
    INACTIVE = 0
    PRIMARY_OBJECTIVE = 1
    SECONDARY_OBJECTIVE = 2
    TRAVEL_OBJECTIVE = 3
    PUBLIC_EVENT_OBJECTIVE = 4
    AMMO_CACHE = 5
    POINT_TYPE_FLAG = 6
    CAPTURE_POINT = 7
    DEFENSIVE_ENCOUNTER = 8
    GHOST_INTERACTION = 9
    KILL_AI = 10
    QUEST_ITEM = 11
    PATROL_MISSION = 12
    INCOMING = 13
    ARENA_OBJECTIVE = 14
    AUTOMATION_HINT = 15
    TRACKED_QUEST = 16


class DestinyActivityModeCategory(Enum):
    """Activity Modes are grouped into a few possible broad categories."""

    NONE = 0
    PV_E = 1
    PV_P = 2
    PV_E_COMPETITIVE = 3


class DestinyItemSubType(Enum):
    """This Enumeration further classifies items by more specific
    categorizations than DestinyItemType.

    The "Sub-Type" is where we classify and categorize items one step further in specificity: "Auto Rifle" instead of just "Weapon" for example, or "Vanguard Bounty" instead of merely "Bounty".
    These sub-types are provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit.
    NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
    """

    NONE = 0
    CRUCIBLE = 1
    VANGUARD = 2
    EXOTIC = 5
    AUTO_RIFLE = 6
    SHOTGUN = 7
    MACHINEGUN = 8
    HAND_CANNON = 9
    ROCKET_LAUNCHER = 10
    FUSION_RIFLE = 11
    SNIPER_RIFLE = 12
    PULSE_RIFLE = 13
    SCOUT_RIFLE = 14
    CRM = 16
    SIDEARM = 17
    SWORD = 18
    MASK = 19
    SHADER = 20
    ORNAMENT = 21
    FUSION_RIFLE_LINE = 22
    GRENADE_LAUNCHER = 23
    SUBMACHINE_GUN = 24
    TRACE_RIFLE = 25
    HELMET_ARMOR = 26
    GAUNTLETS_ARMOR = 27
    CHEST_ARMOR = 28
    LEG_ARMOR = 29
    CLASS_ARMOR = 30
    BOW = 31
    DUMMY_REPEATABLE_BOUNTY = 32


class DestinyGraphNodeState(Enum):
    """Represents a potential state of an Activity Graph node."""

    HIDDEN = 0
    VISIBLE = 1
    TEASER = 2
    INCOMPLETE = 3
    COMPLETED = 4


class DestinyPresentationNodeType(Enum):
    DEFAULT = 0
    CATEGORY = 1
    COLLECTIBLES = 2
    RECORDS = 3
    METRIC = 4


class DestinyScope(Enum):
    """There's a lot of places where we need to know scope on more than just a
    profile or character level.

    For everything else, there's this more generic sense of scope.
    """

    PROFILE = 0
    CHARACTER = 1


class DestinyPresentationDisplayStyle(Enum):
    """A hint for how the presentation node should be displayed when shown in a
    list.

    How you use this is your UI is up to you.
    """

    CATEGORY = 0
    BADGE = 1
    MEDALS = 2
    COLLECTIBLE = 3
    RECORD = 4


class DestinyRecordValueStyle(Enum):
    INTEGER = 0
    PERCENTAGE = 1
    MILLISECONDS = 2
    BOOLEAN = 3
    DECIMAL = 4


class DestinyGender(Enum):
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2


class DestinyRecordToastStyle(Enum):
    NONE = 0
    RECORD = 1
    LORE = 2
    BADGE = 3
    META_RECORD = 4
    MEDAL_COMPLETE = 5
    SEASON_CHALLENGE_COMPLETE = 6
    GILDED_TITLE_COMPLETE = 7


class DestinyPresentationScreenStyle(Enum):
    """A hint for what screen should be shown when this presentation node is
    clicked into.

    How you use this is your UI is up to you.
    """

    DEFAULT = 0
    CATEGORY_SETS = 1
    BADGE = 2


class PlugUiStyles(Enum):
    """If the plug has a specific custom style, this enumeration will represent
    that style/those styles."""

    NONE = 0
    MASTERWORK = 1


class PlugAvailabilityMode(Enum):
    """This enum determines whether the plug is available to be inserted.

    - Normal means that all existing rules for plug insertion apply.
    - UnavailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket does NOT match the plug category.
    - AvailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket DOES match the plug category.
    For category matching, use the plug's "plugCategoryIdentifier" property, comparing it to
    """

    NORMAL = 0
    UNAVAILABLE_IF_SOCKET_CONTAINS_MATCHING_PLUG_CATEGORY = 1
    AVAILABLE_IF_SOCKET_CONTAINS_MATCHING_PLUG_CATEGORY = 2


class DestinyEnergyType(Enum):
    """Represents the socket energy types for Armor 2.0, Ghosts 2.0, and Stasis
    subclasses."""

    ANY = 0
    ARC = 1
    THERMAL = 2
    VOID = 3
    GHOST = 4
    SUBCLASS = 5
    STASIS = 6


class SocketPlugSources(Enum):
    """Indicates how a socket is populated, and where you should look for valid
    plug data.

    This is a flags enumeration/bitmask field, as you may have to look
    in multiple sources across multiple components for valid plugs. For
    instance, a socket could have plugs that are sourced from its own
    definition, as well as plugs that are sourced from Character-scoped
    AND profile-scoped Plug Sets. Only by combining plug data for every
    indicated source will you be able to know all of the plugs available
    for a socket.
    """

    NONE = 0
    INVENTORY_SOURCED = 1
    REUSABLE_PLUG_ITEMS = 2
    PROFILE_PLUG_SET = 4
    CHARACTER_PLUG_SET = 8


class ItemPerkVisibility(Enum):
    """Indicates how a perk should be shown, or if it should be, in the game
    UI.

    Maybe useful for those of you trying to filter out internal-use-only
    perks (or for those of you trying to figure out what they do!)
    """

    VISIBLE = 0
    DISABLED = 1
    HIDDEN = 2


class SpecialItemType(Enum):
    """As you run into items that need to be classified for Milestone purposes
    in ways that we cannot infer via direct data, add a new classification here
    and use a string constant to represent it in the local item config file.

    NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
    """

    NONE = 0
    SPECIAL_CURRENCY = 1
    ARMOR = 8
    WEAPON = 9
    ENGRAM = 23
    CONSUMABLE = 24
    EXCHANGE_MATERIAL = 25
    MISSION_REWARD = 27
    CURRENCY = 29


class DestinyItemType(Enum):
    """An enumeration that indicates the high-level "type" of the item,
    attempting to iron out the context specific differences for specific
    instances of an entity.

    For instance, though a weapon may be of various weapon "Types", in DestinyItemType they are all classified as "Weapon". This allows for better filtering on a higher level of abstraction for the concept of types.
    This enum is provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit.
    NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
    I keep updating these because they're so damn convenient. I guess I shouldn't fight it.
    """

    NONE = 0
    CURRENCY = 1
    ARMOR = 2
    WEAPON = 3
    MESSAGE = 7
    ENGRAM = 8
    CONSUMABLE = 9
    EXCHANGE_MATERIAL = 10
    MISSION_REWARD = 11
    QUEST_STEP = 12
    QUEST_STEP_COMPLETE = 13
    EMBLEM = 14
    QUEST = 15
    SUBCLASS = 16
    CLAN_BANNER = 17
    AURA = 18
    MOD = 19
    DUMMY = 20
    SHIP = 21
    VEHICLE = 22
    EMOTE = 23
    GHOST = 24
    PACKAGE = 25
    BOUNTY = 26
    WRAPPER = 27
    SEASONAL_ARTIFACT = 28
    FINISHER = 29


class DestinyClass(Enum):
    TITAN = 0
    HUNTER = 1
    WARLOCK = 2
    UNKNOWN = 3


class DestinyBreakerType(Enum):
    """A plug can optionally have a "Breaker Type": a special ability that can
    affect units in unique ways.

    Activating this plug can grant one of these types.
    """

    NONE = 0
    SHIELD_PIERCING = 1
    DISRUPTION = 2
    STAGGER = 3


class DestinyProgressionRewardItemAcquisitionBehavior(Enum):
    """Represents the different kinds of acquisition behavior for progression
    reward items."""

    INSTANT = 0
    PLAYER_CLAIM_REQUIRED = 1


class ItemBindStatus(Enum):
    NOT_BOUND = 0
    BOUND_TO_CHARACTER = 1
    BOUND_TO_ACCOUNT = 2
    BOUND_TO_GUILD = 3


class TransferStatuses(Enum):
    """Whether you can transfer an item, and why not if you can't."""

    CAN_TRANSFER = 0
    ITEM_IS_EQUIPPED = 1
    NOT_TRANSFERRABLE = 2
    NO_ROOM_IN_DESTINATION = 4


class ItemState(Enum):
    """A flags enumeration/bitmask where each bit represents a different
    possible state that the item can be in that may effect how the item is
    displayed to the user and what actions can be performed against it."""

    NONE = 0
    LOCKED = 1
    TRACKED = 2
    MASTERWORK = 4


class DestinyGameVersions(Enum):
    """A flags enumeration/bitmask indicating the versions of the game that a
    given user has purchased."""

    NONE = 0
    DESTINY2 = 1
    DLC1 = 2
    DLC2 = 4
    FORSAKEN = 8
    YEAR_TWO_ANNUAL_PASS = 16
    SHADOWKEEP = 32
    BEYOND_LIGHT = 64
    ANNIVERSARY30TH = 128
    THE_WITCH_QUEEN = 256


class DestinyComponentType(Enum):
    """Represents the possible components that can be returned from Destiny
    "Get" calls such as GetProfile, GetCharacter, GetVendor etc...

    When making one of these requests, you will pass one or more of these components as a comma separated list in the "?components=" querystring parameter. For instance, if you want baseline Profile data, Character Data, and character progressions, you would pass "?components=Profiles,Characters,CharacterProgressions" You may use either the numerical or string values.
    """

    NONE = 0
    PROFILES = 100
    VENDOR_RECEIPTS = 101
    PROFILE_INVENTORIES = 102
    PROFILE_CURRENCIES = 103
    PROFILE_PROGRESSION = 104
    PLATFORM_SILVER = 105
    CHARACTERS = 200
    CHARACTER_INVENTORIES = 201
    CHARACTER_PROGRESSIONS = 202
    CHARACTER_RENDER_DATA = 203
    CHARACTER_ACTIVITIES = 204
    CHARACTER_EQUIPMENT = 205
    ITEM_INSTANCES = 300
    ITEM_OBJECTIVES = 301
    ITEM_PERKS = 302
    ITEM_RENDER_DATA = 303
    ITEM_STATS = 304
    ITEM_SOCKETS = 305
    ITEM_TALENT_GRIDS = 306
    ITEM_COMMON_DATA = 307
    ITEM_PLUG_STATES = 308
    ITEM_PLUG_OBJECTIVES = 309
    ITEM_REUSABLE_PLUGS = 310
    VENDORS = 400
    VENDOR_CATEGORIES = 401
    VENDOR_SALES = 402
    KIOSKS = 500
    CURRENCY_LOOKUPS = 600
    PRESENTATION_NODES = 700
    COLLECTIBLES = 800
    RECORDS = 900
    TRANSITORY = 1000
    METRICS = 1100
    STRING_VARIABLES = 1200


class DestinyPresentationNodeState(Enum):
    """I know this doesn't look like a Flags Enumeration/bitmask right now, but
    I assure you it is.

    This is the possible states that a Presentation Node can be in, and
    it is almost certain that its potential states will increase in the
    future. So don't treat it like a straight up enumeration.
    """

    NONE = 0
    INVISIBLE = 1
    OBSCURED = 2


class DestinyRecordState(Enum):
    """A Flags enumeration/bitmask where each bit represents a possible state
    that a Record/Triumph can be in."""

    NONE = 0
    RECORD_REDEEMED = 1
    REWARD_UNAVAILABLE = 2
    OBJECTIVE_NOT_COMPLETED = 4
    OBSCURED = 8
    INVISIBLE = 16
    ENTITLEMENT_UNOWNED = 32
    CAN_EQUIP_TITLE = 64


class DestinyCollectibleState(Enum):
    """A Flags Enumeration/bitmask where each bit represents a different state
    that the Collectible can be in.

    A collectible can be in any number of these states, and you can
    choose to use or ignore any or all of them when making your own UI
    that shows Collectible info. Our displays are going to honor them,
    but we're also the kind of people who only pretend to inhale before
    quickly passing it to the left. So, you know, do what you got to do.
    (All joking aside, please note the caveat I mention around the
    Invisible flag: there are cases where it is in the best interest of
    your users to honor these flags even if you're a "show all the data"
    person. Collector-oriented compulsion is a very unfortunate and real
    thing, and I would hate to instill that compulsion in others through
    showing them items that they cannot earn. Please consider this when
    you are making your own apps/sites.)
    """

    NONE = 0
    NOT_ACQUIRED = 1
    OBSCURED = 2
    INVISIBLE = 4
    CANNOT_AFFORD_MATERIAL_REQUIREMENTS = 8
    INVENTORY_SPACE_UNAVAILABLE = 16
    UNIQUENESS_VIOLATION = 32
    PURCHASE_DISABLED = 64


class DestinyPartyMemberStates(Enum):
    """A flags enumeration that represents a Fireteam Member's status."""

    NONE = 0
    FIRETEAM_MEMBER = 1
    POSSE_MEMBER = 2
    GROUP_MEMBER = 4
    PARTY_LEADER = 8


class DestinyGamePrivacySetting(Enum):
    """A player can choose to restrict requests to join their Fireteam to
    specific states.

    These are the possible states a user can choose.
    """

    OPEN = 0
    CLAN_AND_FRIENDS_ONLY = 1
    FRIENDS_ONLY = 2
    INVITATION_ONLY = 3
    CLOSED = 4


class DestinyJoinClosedReasons(Enum):
    """A Flags enumeration representing the reasons why a person can't join
    this user's fireteam."""

    NONE = 0
    IN_MATCHMAKING = 1
    LOADING = 2
    SOLO_MODE = 4
    INTERNAL_REASONS = 8
    DISALLOWED_BY_GAME_STATE = 16
    OFFLINE = 32768


class DestinyRace(Enum):
    HUMAN = 0
    AWOKEN = 1
    EXO = 2
    UNKNOWN = 3


@dt.dataclass(frozen=True)
class DestinyActivity:
    """'Represents the "Live" data that we can obtain about a Character's
    status with a specific Activity.

    This will tell you whether the character can participate in the
    activity, as well as some other basic mutable information. Meant to
    be combined with static DestinyActivityDefinition data for a full
    picture of the Activity.
    """

    activity_hash: int
    is_new: bool
    can_lead: bool
    can_join: bool
    is_completed: bool
    is_visible: bool
    display_level: int
    recommended_light: int
    difficulty_tier: "DestinyActivityDifficultyTier"
    challenges: t.Sequence["DestinyChallengeStatus"]
    modifier_hashes: t.Sequence[int]
    boolean_activity_options: t.Mapping[str, bool]
    loadout_requirement_index: int


class DestinyActivityDifficultyTier(Enum):
    """An enumeration representing the potential difficulty levels of an
    activity.

    Their names are... more qualitative than quantitative.
    """

    TRIVIAL = 0
    EASY = 1
    NORMAL = 2
    CHALLENGING = 3
    HARD = 4
    BRAVE = 5
    ALMOST_IMPOSSIBLE = 6
    IMPOSSIBLE = 7


@dt.dataclass(frozen=True)
class DestinyStat:
    """'Represents a stat on an item *or* Character (NOT a Historical Stat, but
    a physical attribute stat like Attack, Defense etc...)"""

    stat_hash: int
    value: int


class EquipFailureReason(Enum):
    """The reasons why an item cannot be equipped, if any.

    Many flags can be set, or "None" if
    """

    NONE = 0
    ITEM_UNEQUIPPABLE = 1
    ITEM_UNIQUE_EQUIP_RESTRICTED = 2
    ITEM_FAILED_UNLOCK_CHECK = 4
    ITEM_FAILED_LEVEL_CHECK = 8
    ITEM_NOT_ON_CHARACTER = 16


@dt.dataclass(frozen=True)
class DestinyTalentNode:
    """'I see you've come to find out more about Talent Nodes.

    I'm so sorry. Talent Nodes are the conceptual, visual nodes that
    appear on Talent Grids. Talent Grids, in Destiny 1, were found on
    almost every instanced item: they had Nodes that could be activated
    to change the properties of the item. In Destiny 2, Talent Grids
    only exist for Builds/Subclasses, and while the basic concept is the
    same (Nodes can be activated once you've gained sufficient
    Experience on the Item, and provide effects), there are some new
    concepts from Destiny 1. Examine DestinyTalentGridDefinition and its
    subordinates for more information. This is the "Live" information
    for the current status of a Talent Node on a specific item. Talent
    Nodes have many Steps, but only one can be active at any one time:
    and it is the Step that determines both the visual and the game
    state-changing properties that the Node provides. Examine this and
    DestinyTalentNodeStepDefinition carefully. *IMPORTANT NOTE* Talent
    Nodes are, unfortunately, Content Version DEPENDENT. Though they
    refer to hashes for Nodes and Steps, those hashes are not guaranteed
    to be immutable across content versions. This is a source of great
    exasperation for me, but as a result anyone using Talent Grid data
    must ensure that the content version of their static content matches
    that of the server responses before showing or making decisions
    based on talent grid data.
    """

    node_index: int
    node_hash: int
    state: "DestinyTalentNodeState"
    is_activated: bool
    step_index: int
    materials_to_upgrade: t.Sequence["DestinyMaterialRequirement"]
    activation_grid_level: int
    progress_percent: float
    hidden: bool
    node_stats_block: t.Any


class DestinyTalentNodeState(Enum):
    INVALID = 0
    CAN_UPGRADE = 1
    NO_POINTS = 2
    NO_PREREQUISITES = 3
    NO_STEPS = 4
    NO_UNLOCK = 5
    NO_MATERIAL = 6
    NO_GRID_LEVEL = 7
    SWAPPING_LOCKED = 8
    MUST_SWAP = 9
    COMPLETE = 10
    UNKNOWN = 11
    CREATION_ONLY = 12
    HIDDEN = 13


@dt.dataclass(frozen=True)
class DestinyTalentNodeStatBlock:
    """'This property has some history.

    A talent grid can provide stats on both the item it's related to and
    the character equipping the item. This returns data about those stat
    bonuses.
    """

    current_step_stats: t.Sequence["DestinyStat"]
    next_step_stats: t.Sequence["DestinyStat"]


class DestinyVendorFilter(Enum):
    """Indicates the type of filter to apply to Vendor results."""

    NONE = 0
    API_PURCHASABLE = 1


class VendorItemStatus(Enum):
    SUCCESS = 0
    NO_INVENTORY_SPACE = 1
    NO_FUNDS = 2
    NO_PROGRESSION = 4
    NO_UNLOCK = 8
    NO_QUANTITY = 16
    OUTSIDE_PURCHASE_WINDOW = 32
    NOT_AVAILABLE = 64
    UNIQUENESS_VIOLATION = 128
    UNKNOWN_ERROR = 256
    ALREADY_SELLING = 512
    UNSELLABLE = 1024
    SELLING_INHIBITED = 2048
    ALREADY_OWNED = 4096
    DISPLAY_ONLY = 8192


@dt.dataclass(frozen=True)
class DestinyUnlockStatus:
    """'Indicates the status of an "Unlock Flag" on a Character or Profile.

    These are individual bits of state that can be either set or not
    set, and sometimes provide interesting human-readable information in
    their related DestinyUnlockDefinition.
    """

    unlock_hash: int
    is_set: bool


class DestinyVendorItemState(Enum):
    """The possible states of Destiny Profile Records.

    IMPORTANT: Any given item can theoretically have many of these states simultaneously: as a result, this was altered to be a flags enumeration/bitmask for v3.2.0.
    """

    NONE = 0
    INCOMPLETE = 1
    REWARD_AVAILABLE = 2
    COMPLETE = 4
    NEW = 8
    FEATURED = 16
    ENDING = 32
    ON_SALE = 64
    OWNED = 128
    WIDE_VIEW = 256
    NEXUS_ATTENTION = 512
    SET_DISCOUNT = 1024
    PRICE_DROP = 2048
    DAILY_OFFER = 4096
    CHARITY = 8192
    SEASONAL_REWARD_EXPIRATION = 16384
    BEST_DEAL = 32768
    POPULAR = 65536
    FREE = 131072


@dt.dataclass(frozen=True)
class DestinyEquipItemResults:
    """'The results of a bulk Equipping operation performed through the Destiny
    API."""

    equip_results: t.Sequence["DestinyEquipItemResult"]


@dt.dataclass(frozen=True)
class DestinyEquipItemResult:
    """'The results of an Equipping operation performed through the Destiny
    API."""

    item_instance_id: int
    equip_status: "PlatformErrorCodes"


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.challenges import (
    DestinyChallengeStatus,
)  # noqa: E402
from bungieapi.generated.types.destiny.definitions import (
    DestinyMaterialRequirement,
)  # noqa: E402
from bungieapi.generated.types.exceptions import PlatformErrorCodes  # noqa: E402
