# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


class DestinyActivityModeType(Enum):
    """For historical reasons, this list will have both D1 and D2-relevant
    Activity Modes in it.

    Please don't take this to mean that some D1-only feature is coming
    back!
    """

    NONE = 0
    STORY = 2
    STRIKE = 3
    RAID = 4
    ALL_PV_P = 5
    PATROL = 6
    ALL_PV_E = 7
    RESERVED9 = 9
    CONTROL = 10
    RESERVED11 = 11
    CLASH = 12  # Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins.
    RESERVED13 = 13
    CRIMSON_DOUBLES = 15
    NIGHTFALL = 16
    HEROIC_NIGHTFALL = 17
    ALL_STRIKES = 18
    IRON_BANNER = 19
    RESERVED20 = 20
    RESERVED21 = 21
    RESERVED22 = 22
    RESERVED24 = 24
    ALL_MAYHEM = 25
    RESERVED26 = 26
    RESERVED27 = 27
    RESERVED28 = 28
    RESERVED29 = 29
    RESERVED30 = 30
    SUPREMACY = 31
    PRIVATE_MATCHES_ALL = 32
    SURVIVAL = 37
    COUNTDOWN = 38
    TRIALS_OF_THE_NINE = 39
    SOCIAL = 40
    TRIALS_COUNTDOWN = 41
    TRIALS_SURVIVAL = 42
    IRON_BANNER_CONTROL = 43
    IRON_BANNER_CLASH = 44
    IRON_BANNER_SUPREMACY = 45
    SCORED_NIGHTFALL = 46
    SCORED_HEROIC_NIGHTFALL = 47
    RUMBLE = 48
    ALL_DOUBLES = 49
    DOUBLES = 50
    PRIVATE_MATCHES_CLASH = 51
    PRIVATE_MATCHES_CONTROL = 52
    PRIVATE_MATCHES_SUPREMACY = 53
    PRIVATE_MATCHES_COUNTDOWN = 54
    PRIVATE_MATCHES_SURVIVAL = 55
    PRIVATE_MATCHES_MAYHEM = 56
    PRIVATE_MATCHES_RUMBLE = 57
    HEROIC_ADVENTURE = 58
    SHOWDOWN = 59
    LOCKDOWN = 60
    SCORCHED = 61
    SCORCHED_TEAM = 62
    GAMBIT = 63
    ALL_PV_E_COMPETITIVE = 64
    BREAKTHROUGH = 65
    BLACK_ARMORY_RUN = 66
    SALVAGE = 67
    IRON_BANNER_SALVAGE = 68
    PV_P_COMPETITIVE = 69
    PV_P_QUICKPLAY = 70
    CLASH_QUICKPLAY = 71
    CLASH_COMPETITIVE = 72
    CONTROL_QUICKPLAY = 73
    CONTROL_COMPETITIVE = 74
    GAMBIT_PRIME = 75
    RECKONING = 76
    MENAGERIE = 77
    VEX_OFFENSIVE = 78
    NIGHTMARE_HUNT = 79
    ELIMINATION = 80
    MOMENTUM = 81
    DUNGEON = 82
    SUNDIAL = 83
    TRIALS_OF_OSIRIS = 84
    DARES = 85


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsDefinition:
    stat_id: str  # Unique programmer friendly ID for this stat
    group: "DestinyStatsGroupType"  # Statistic group
    period_types: t.Sequence["PeriodType"]  # Time periods the statistic covers
    modes: t.Sequence[
        "DestinyActivityModeType"
    ]  # Game modes where this statistic can be reported.
    category: "DestinyStatsCategoryType"  # Category for the stat.
    stat_name: str  # Display name
    stat_name_abbr: str  # Display name abbreviated
    stat_description: str  # Description of a stat if applicable.
    unit_type: "UnitType"  # Unit, if any, for the statistic
    icon_image: str  # Optional URI to an icon for the statistic
    merge_method: int  # Optional icon for the statistic
    unit_label: str  # Localized Unit Name for the stat.
    weight: int  # Weight assigned to this stat indicating its relative impressiveness.
    medal_tier_hash: int  # The tier associated with this medal - be it implicitly or explicitly.


class DestinyStatsGroupType(Enum):
    """If the enum value is > 100, it is a "special" group that cannot be
    queried for directly (special cases apply to when they are returned, and
    are not relevant in general cases)"""

    NONE = 0
    GENERAL = 1
    WEAPONS = 2
    MEDALS = 3
    RESERVED_GROUPS = 100  # This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant for filtering.
    LEADERBOARD = 101  # Only applicable while generating leaderboards.
    ACTIVITY = 102  # These will *only* be consumed by GetAggregateStatsByActivity
    UNIQUE_WEAPON = (
        103  # These are only consumed and returned by GetUniqueWeaponHistory
    )
    INTERNAL = 104


PeriodTypeArray = t.Sequence["PeriodType"]
DestinyActivityModeTypeArray = t.Sequence["DestinyActivityModeType"]


class DestinyStatsCategoryType(Enum):
    NONE = 0
    KILLS = 1
    ASSISTS = 2
    DEATHS = 3
    CRITICALS = 4
    K_DA = 5
    KD = 6
    SCORE = 7
    ENTERED = 8
    TIME_PLAYED = 9
    MEDAL_WINS = 10
    MEDAL_GAME = 11
    MEDAL_SPECIAL_KILLS = 12
    MEDAL_SPREES = 13
    MEDAL_MULTI_KILLS = 14
    MEDAL_ABILITIES = 15


class UnitType(Enum):
    NONE = 0
    COUNT = 1  # Indicates the statistic is a simple count of something.
    PER_GAME = 2  # Indicates the statistic is a per game average.
    SECONDS = 3  # Indicates the number of seconds
    POINTS = 4  # Indicates the number of points earned
    TEAM = 5  # Values represents a team ID
    DISTANCE = 6  # Values represents a distance (units to-be-determined)
    PERCENT = 7  # Ratio represented as a whole value from 0 to 100.
    RATIO = 8  # Ratio of something, shown with decimal places
    BOOLEAN = 9  # True or false
    WEAPON_TYPE = 10  # The stat is actually a weapon type.
    STANDING = 11  # Indicates victory, defeat, or something in between.
    MILLISECONDS = 12  # Number of milliseconds some event spanned. For example, race time, or lap time.
    COMPLETION_REASON = 13  # The value is a enumeration of the Completion Reason type.


class DestinyStatsMergeMethod(Enum):
    ADD = 0  # When collapsing multiple instances of the stat together, add the values.
    MIN = 1  # When collapsing multiple instances of the stat together, take the lower value.
    MAX = 2  # When collapsing multiple instances of the stat together, take the higher value.


class PeriodType(Enum):
    NONE = 0
    DAILY = 1
    ALL_TIME = 2
    ACTIVITY = 3
