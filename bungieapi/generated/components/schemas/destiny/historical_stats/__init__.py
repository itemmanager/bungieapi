# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportData:
    activity_details: t.Optional[
        "DestinyHistoricalStatsActivity"
    ] = None  # Details about the activity.
    entries: t.Optional[
        t.Sequence["DestinyPostGameCarnageReportEntry"]
    ] = None  # Collection of players and their data for this activity.
    period: t.Optional[str] = None  # Date and time for the activity.
    starting_phase_index: t.Optional[
        int
    ] = None  # If this activity has "phases", this is the phase at which the activity was started.
    teams: t.Optional[
        t.Sequence["DestinyPostGameCarnageReportTeamEntry"]
    ] = None  # Collection of stats for the player in this activity.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "period": to_json(self.period),
            "startingPhaseIndex": to_json(self.starting_phase_index),
            "activityDetails": to_json(self.activity_details),
            "entries": to_json(self.entries),
            "teams": to_json(self.teams),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsActivity:
    """Summary information about the activity that was played."""

    director_activity_hash: t.Optional[
        int
    ] = None  # The unique hash identifier of the DestinyActivityDefinition that was played.
    instance_id: t.Optional[
        int
    ] = None  # The unique identifier for this *specific* match that was played. This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.
    is_private: t.Optional[bool] = None  # Whether or not the match was a private match.
    membership_type: t.Optional[
        "BungieMembershipType"
    ] = None  # The Membership Type indicating the platform on which this match was played.
    mode: t.Optional[
        "DestinyActivityModeType"
    ] = None  # Indicates the most specific game mode of the activity that we could find.
    modes: t.Optional[
        t.Sequence["DestinyActivityModeType"]
    ] = None  # The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event.
    reference_id: t.Optional[
        int
    ] = None  # The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "referenceId": to_json(self.reference_id),
            "directorActivityHash": to_json(self.director_activity_hash),
            "instanceId": to_json(self.instance_id),
            "mode": to_json(self.mode),
            "modes": to_json(self.modes),
            "isPrivate": to_json(self.is_private),
            "membershipType": to_json(self.membership_type),
        }


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportEntry:
    character_id: t.Optional[
        int
    ] = None  # ID of the player's character used in the activity.
    extended: t.Optional[
        "DestinyPostGameCarnageReportExtendedData"
    ] = None  # Extended data extracted from the activity blob.
    player: t.Optional["DestinyPlayer"] = None  # Identity details of the player
    score: t.Optional[
        "DestinyHistoricalStatsValue"
    ] = None  # Score of the player if available
    standing: t.Optional[int] = None  # Standing of the player
    values: t.Optional[
        t.Mapping[str, "DestinyHistoricalStatsValue"]
    ] = None  # Collection of stats for the player in this activity.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "standing": to_json(self.standing),
            "score": to_json(self.score),
            "player": to_json(self.player),
            "characterId": to_json(self.character_id),
            "values": to_json(self.values),
            "extended": to_json(self.extended),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsValue:
    activity_id: t.Optional[
        int
    ] = None  # When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property.
    basic: t.Optional["DestinyHistoricalStatsValuePair"] = None  # Basic stat value.
    pga: t.Optional[
        "DestinyHistoricalStatsValuePair"
    ] = None  # Per game average for the statistic, if applicable
    stat_id: t.Optional[str] = None  # Unique ID for this stat
    weighted: t.Optional[
        "DestinyHistoricalStatsValuePair"
    ] = None  # Weighted value of the stat if a weight greater than 1 has been assigned.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "statId": to_json(self.stat_id),
            "basic": to_json(self.basic),
            "pga": to_json(self.pga),
            "weighted": to_json(self.weighted),
            "activityId": to_json(self.activity_id),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsValuePair:
    display_value: t.Optional[str] = None  # Localized formated version of the value.
    value: t.Optional[float] = None  # Raw value of the statistic

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "value": to_json(self.value),
            "displayValue": to_json(self.display_value),
        }


@dt.dataclass(frozen=True)
class DestinyPlayer:
    bungie_net_user_info: t.Optional[
        "UserInfoCard"
    ] = None  # Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.
    character_class: t.Optional[
        str
    ] = None  # Class of the character if applicable and available.
    character_level: t.Optional[
        int
    ] = None  # Level of the character if available. Zero if it is not available.
    clan_name: t.Optional[
        str
    ] = None  # Current clan name for the player. This value may be null or an empty string if the user does not have a clan.
    clan_tag: t.Optional[
        str
    ] = None  # Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.
    class_hash: t.Optional[int] = None
    destiny_user_info: t.Optional[
        "UserInfoCard"
    ] = None  # Details about the player as they are known in game (platform display name, Destiny emblem)
    emblem_hash: t.Optional[
        int
    ] = None  # If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).
    gender_hash: t.Optional[int] = None
    light_level: t.Optional[
        int
    ] = None  # Light Level of the character if available. Zero if it is not available.
    race_hash: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "destinyUserInfo": to_json(self.destiny_user_info),
            "characterClass": to_json(self.character_class),
            "classHash": to_json(self.class_hash),
            "raceHash": to_json(self.race_hash),
            "genderHash": to_json(self.gender_hash),
            "characterLevel": to_json(self.character_level),
            "lightLevel": to_json(self.light_level),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
            "clanName": to_json(self.clan_name),
            "clanTag": to_json(self.clan_tag),
            "emblemHash": to_json(self.emblem_hash),
        }


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportExtendedData:
    values: t.Optional[
        t.Mapping[str, "DestinyHistoricalStatsValue"]
    ] = None  # Collection of stats for the player in this activity.
    weapons: t.Optional[
        t.Sequence["DestinyHistoricalWeaponStats"]
    ] = None  # List of weapons and their perspective values.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "weapons": to_json(self.weapons),
            "values": to_json(self.values),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalWeaponStats:
    reference_id: t.Optional[
        int
    ] = None  # The hash ID of the item definition that describes the weapon.
    values: t.Optional[
        t.Mapping[str, "DestinyHistoricalStatsValue"]
    ] = None  # Collection of stats for the period.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "referenceId": to_json(self.reference_id),
            "values": to_json(self.values),
        }


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportTeamEntry:
    score: t.Optional["DestinyHistoricalStatsValue"] = None  # Score earned by the team
    standing: t.Optional[
        "DestinyHistoricalStatsValue"
    ] = None  # Team's standing relative to other teams.
    team_id: t.Optional[int] = None  # Integer ID for the team.
    team_name: t.Optional[str] = None  # Alpha or Bravo

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "teamId": to_json(self.team_id),
            "standing": to_json(self.standing),
            "score": to_json(self.score),
            "teamName": to_json(self.team_name),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboard:
    entries: t.Optional[t.Sequence["DestinyLeaderboardEntry"]] = None
    stat_id: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "statId": to_json(self.stat_id),
            "entries": to_json(self.entries),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboardEntry:
    character_id: t.Optional[
        int
    ] = None  # ID of the player's best character for the reported stat.
    player: t.Optional["DestinyPlayer"] = None  # Identity details of the player
    rank: t.Optional[
        int
    ] = None  # Where this player ranks on the leaderboard. A value of 1 is the top rank.
    value: t.Optional[
        "DestinyHistoricalStatsValue"
    ] = None  # Value of the stat for this player

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "rank": to_json(self.rank),
            "player": to_json(self.player),
            "characterId": to_json(self.character_id),
            "value": to_json(self.value),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboardResults:
    focus_character_id: t.Optional[
        int
    ] = None  # Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards.
    focus_membership_id: t.Optional[
        int
    ] = None  # Indicate the membership ID of the account that is the focal point of the provided leaderboards.
    additional: t.Mapping[str, t.Mapping[str, "DestinyLeaderboard"]] = dt.field(
        default_factory=dict
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "focusMembershipId": to_json(self.focus_membership_id),
            "focusCharacterId": to_json(self.focus_character_id),
        }


@dt.dataclass(frozen=True)
class DestinyClanAggregateStat:
    mode: t.Optional[
        "DestinyActivityModeType"
    ] = None  # The id of the mode of stats (allPvp, allPvE, etc)
    stat_id: t.Optional[str] = None  # The id of the stat
    value: t.Optional[
        "DestinyHistoricalStatsValue"
    ] = None  # Value of the stat for this player

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "mode": to_json(self.mode),
            "statId": to_json(self.stat_id),
            "value": to_json(self.value),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsByPeriod:
    all_time: t.Optional[t.Mapping[str, "DestinyHistoricalStatsValue"]] = None
    all_time_tier1: t.Optional[t.Mapping[str, "DestinyHistoricalStatsValue"]] = None
    all_time_tier2: t.Optional[t.Mapping[str, "DestinyHistoricalStatsValue"]] = None
    all_time_tier3: t.Optional[t.Mapping[str, "DestinyHistoricalStatsValue"]] = None
    daily: t.Optional[t.Sequence["DestinyHistoricalStatsPeriodGroup"]] = None
    monthly: t.Optional[t.Sequence["DestinyHistoricalStatsPeriodGroup"]] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "allTime": to_json(self.all_time),
            "allTimeTier1": to_json(self.all_time_tier1),
            "allTimeTier2": to_json(self.all_time_tier2),
            "allTimeTier3": to_json(self.all_time_tier3),
            "daily": to_json(self.daily),
            "monthly": to_json(self.monthly),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsPeriodGroup:
    activity_details: t.Optional[
        "DestinyHistoricalStatsActivity"
    ] = None  # If the period group is for a specific activity, this property will be set.
    period: t.Optional[
        str
    ] = None  # Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.
    values: t.Optional[
        t.Mapping[str, "DestinyHistoricalStatsValue"]
    ] = None  # Collection of stats for the period.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "period": to_json(self.period),
            "activityDetails": to_json(self.activity_details),
            "values": to_json(self.values),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsResults:
    additional: t.Mapping[str, "DestinyHistoricalStatsByPeriod"] = dt.field(
        default_factory=dict
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {}


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsAccountResult:
    characters: t.Optional[t.Sequence["DestinyHistoricalStatsPerCharacter"]] = None
    merged_all_characters: t.Optional["DestinyHistoricalStatsWithMerged"] = None
    merged_deleted_characters: t.Optional["DestinyHistoricalStatsWithMerged"] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "mergedDeletedCharacters": to_json(self.merged_deleted_characters),
            "mergedAllCharacters": to_json(self.merged_all_characters),
            "characters": to_json(self.characters),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsWithMerged:
    merged: t.Optional["DestinyHistoricalStatsByPeriod"] = None
    results: t.Optional[t.Mapping[str, "DestinyHistoricalStatsByPeriod"]] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "results": to_json(self.results),
            "merged": to_json(self.merged),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsPerCharacter:
    character_id: t.Optional[int] = None
    deleted: t.Optional[bool] = None
    merged: t.Optional["DestinyHistoricalStatsByPeriod"] = None
    results: t.Optional[t.Mapping[str, "DestinyHistoricalStatsByPeriod"]] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "characterId": to_json(self.character_id),
            "deleted": to_json(self.deleted),
            "results": to_json(self.results),
            "merged": to_json(self.merged),
        }


@dt.dataclass(frozen=True)
class DestinyActivityHistoryResults:
    activities: t.Optional[
        t.Sequence["DestinyHistoricalStatsPeriodGroup"]
    ] = None  # List of activities, the most recent activity first.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activities": to_json(self.activities),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalWeaponStatsData:
    weapons: t.Optional[
        t.Sequence["DestinyHistoricalWeaponStats"]
    ] = None  # List of weapons and their perspective values.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "weapons": to_json(self.weapons),
        }


@dt.dataclass(frozen=True)
class DestinyAggregateActivityResults:
    activities: t.Optional[
        t.Sequence["DestinyAggregateActivityStats"]
    ] = None  # List of all activities the player has participated in.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activities": to_json(self.activities),
        }


@dt.dataclass(frozen=True)
class DestinyAggregateActivityStats:
    activity_hash: t.Optional[
        int
    ] = None  # Hash ID that can be looked up in the DestinyActivityTable.
    values: t.Optional[
        t.Mapping[str, "DestinyHistoricalStatsValue"]
    ] = None  # Collection of stats for the player in this activity.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activityHash": to_json(self.activity_hash),
            "values": to_json(self.values),
        }


from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.historical_stats.definitions import (
    DestinyActivityModeType,
)  # noqa: E402
from bungieapi.generated.components.schemas.user import UserInfoCard  # noqa: E402
