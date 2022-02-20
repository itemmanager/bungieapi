# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportData:
    activity_details: "DestinyHistoricalStatsActivity" = dt.field(
        metadata={"description": "Details about the activity."}
    )
    entries: t.Sequence["DestinyPostGameCarnageReportEntry"] = dt.field(
        metadata={
            "description": "Collection of players and their data for this activity."
        }
    )
    period: str = dt.field(metadata={"description": "Date and time for the activity."})
    teams: t.Sequence["DestinyPostGameCarnageReportTeamEntry"] = dt.field(
        metadata={"description": "Collection of stats for the player in this activity."}
    )
    activity_was_started_from_beginning: t.Optional[bool] = dt.field(
        default=None,
        metadata={
            "description": "True if the activity was started from the beginning, if that information is available."
        },
    )
    starting_phase_index: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": 'OBSOLETE - If this activity has "phases", this is the phase at which the activity was started.'
        },
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "period": to_json(self.period),
            "startingPhaseIndex": to_json(self.starting_phase_index),
            "activityWasStartedFromBeginning": to_json(
                self.activity_was_started_from_beginning
            ),
            "activityDetails": to_json(self.activity_details),
            "entries": to_json(self.entries),
            "teams": to_json(self.teams),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsActivity:
    """Summary information about the activity that was played."""

    director_activity_hash: ManifestReference["DestinyActivityDefinition"] = dt.field(
        metadata={
            "description": "The unique hash identifier of the DestinyActivityDefinition that was played."
        }
    )
    instance_id: int = dt.field(
        metadata={
            "description": """The unique identifier for this *specific* match that was played.
This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint."""
        }
    )
    is_private: bool = dt.field(
        metadata={"description": "Whether or not the match was a private match."}
    )
    membership_type: "BungieMembershipType" = dt.field(
        metadata={
            "description": "The Membership Type indicating the platform on which this match was played."
        }
    )
    mode: "DestinyActivityModeType" = dt.field(
        metadata={
            "description": "Indicates the most specific game mode of the activity that we could find."
        }
    )
    modes: t.Sequence["DestinyActivityModeType"] = dt.field(
        metadata={
            "description": "The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event."
        }
    )
    reference_id: ManifestReference["DestinyActivityDefinition"] = dt.field(
        metadata={
            "description": "The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now."
        }
    )

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
    character_id: int = dt.field(
        metadata={"description": "ID of the player's character used in the activity."}
    )
    extended: "DestinyPostGameCarnageReportExtendedData" = dt.field(
        metadata={"description": "Extended data extracted from the activity blob."}
    )
    player: "DestinyPlayer" = dt.field(
        metadata={"description": "Identity details of the player"}
    )
    score: "DestinyHistoricalStatsValue" = dt.field(
        metadata={"description": "Score of the player if available"}
    )
    standing: int = dt.field(metadata={"description": "Standing of the player"})
    values: t.Mapping[str, "DestinyHistoricalStatsValue"] = dt.field(
        metadata={"description": "Collection of stats for the player in this activity."}
    )

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
    basic: "DestinyHistoricalStatsValuePair" = dt.field(
        metadata={"description": "Basic stat value."}
    )
    pga: "DestinyHistoricalStatsValuePair" = dt.field(
        metadata={"description": "Per game average for the statistic, if applicable"}
    )
    stat_id: str = dt.field(metadata={"description": "Unique ID for this stat"})
    weighted: "DestinyHistoricalStatsValuePair" = dt.field(
        metadata={
            "description": "Weighted value of the stat if a weight greater than 1 has been assigned."
        }
    )
    activity_id: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": "When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property."
        },
    )

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
    display_value: str = dt.field(
        metadata={"description": "Localized formated version of the value."}
    )
    value: float = dt.field(metadata={"description": "Raw value of the statistic"})

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "value": to_json(self.value),
            "displayValue": to_json(self.display_value),
        }


@dt.dataclass(frozen=True)
class DestinyPlayer:
    bungie_net_user_info: "UserInfoCard" = dt.field(
        metadata={
            "description": "Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account."
        }
    )
    character_class: str = dt.field(
        metadata={"description": "Class of the character if applicable and available."}
    )
    character_level: int = dt.field(
        metadata={
            "description": "Level of the character if available. Zero if it is not available."
        }
    )
    clan_name: str = dt.field(
        metadata={
            "description": "Current clan name for the player. This value may be null or an empty string if the user does not have a clan."
        }
    )
    clan_tag: str = dt.field(
        metadata={
            "description": "Current clan tag for the player. This value may be null or an empty string if the user does not have a clan."
        }
    )
    class_hash: ManifestReference["DestinyClassDefinition"]
    destiny_user_info: "UserInfoCard" = dt.field(
        metadata={
            "description": "Details about the player as they are known in game (platform display name, Destiny emblem)"
        }
    )
    emblem_hash: ManifestReference["DestinyInventoryItemDefinition"] = dt.field(
        metadata={
            "description": "If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it)."
        }
    )
    gender_hash: ManifestReference["DestinyGenderDefinition"]
    light_level: int = dt.field(
        metadata={
            "description": "Light Level of the character if available. Zero if it is not available."
        }
    )
    race_hash: ManifestReference["DestinyRaceDefinition"]

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
    values: t.Mapping[str, "DestinyHistoricalStatsValue"] = dt.field(
        metadata={"description": "Collection of stats for the player in this activity."}
    )
    weapons: t.Sequence["DestinyHistoricalWeaponStats"] = dt.field(
        metadata={"description": "List of weapons and their perspective values."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "weapons": to_json(self.weapons),
            "values": to_json(self.values),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalWeaponStats:
    reference_id: ManifestReference["DestinyInventoryItemDefinition"] = dt.field(
        metadata={
            "description": "The hash ID of the item definition that describes the weapon."
        }
    )
    values: t.Mapping[str, "DestinyHistoricalStatsValue"] = dt.field(
        metadata={"description": "Collection of stats for the period."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "referenceId": to_json(self.reference_id),
            "values": to_json(self.values),
        }


@dt.dataclass(frozen=True)
class DestinyPostGameCarnageReportTeamEntry:
    score: "DestinyHistoricalStatsValue" = dt.field(
        metadata={"description": "Score earned by the team"}
    )
    standing: "DestinyHistoricalStatsValue" = dt.field(
        metadata={"description": "Team's standing relative to other teams."}
    )
    team_id: int = dt.field(metadata={"description": "Integer ID for the team."})
    team_name: str = dt.field(metadata={"description": "Alpha or Bravo"})

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "teamId": to_json(self.team_id),
            "standing": to_json(self.standing),
            "score": to_json(self.score),
            "teamName": to_json(self.team_name),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboard:
    entries: t.Sequence["DestinyLeaderboardEntry"]
    stat_id: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "statId": to_json(self.stat_id),
            "entries": to_json(self.entries),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboardEntry:
    character_id: int = dt.field(
        metadata={
            "description": "ID of the player's best character for the reported stat."
        }
    )
    player: "DestinyPlayer" = dt.field(
        metadata={"description": "Identity details of the player"}
    )
    rank: int = dt.field(
        metadata={
            "description": "Where this player ranks on the leaderboard. A value of 1 is the top rank."
        }
    )
    value: "DestinyHistoricalStatsValue" = dt.field(
        metadata={"description": "Value of the stat for this player"}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "rank": to_json(self.rank),
            "player": to_json(self.player),
            "characterId": to_json(self.character_id),
            "value": to_json(self.value),
        }


@dt.dataclass(frozen=True)
class DestinyLeaderboardResults:
    focus_character_id: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": "Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards."
        },
    )
    focus_membership_id: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": "Indicate the membership ID of the account that is the focal point of the provided leaderboards."
        },
    )
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
    mode: "DestinyActivityModeType" = dt.field(
        metadata={"description": "The id of the mode of stats (allPvp, allPvE, etc)"}
    )
    stat_id: str = dt.field(metadata={"description": "The id of the stat"})
    value: "DestinyHistoricalStatsValue" = dt.field(
        metadata={"description": "Value of the stat for this player"}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "mode": to_json(self.mode),
            "statId": to_json(self.stat_id),
            "value": to_json(self.value),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsByPeriod:
    all_time: t.Mapping[str, "DestinyHistoricalStatsValue"]
    all_time_tier1: t.Mapping[str, "DestinyHistoricalStatsValue"]
    all_time_tier2: t.Mapping[str, "DestinyHistoricalStatsValue"]
    all_time_tier3: t.Mapping[str, "DestinyHistoricalStatsValue"]
    daily: t.Sequence["DestinyHistoricalStatsPeriodGroup"]
    monthly: t.Sequence["DestinyHistoricalStatsPeriodGroup"]

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
    activity_details: "DestinyHistoricalStatsActivity" = dt.field(
        metadata={
            "description": "If the period group is for a specific activity, this property will be set."
        }
    )
    period: str = dt.field(
        metadata={
            "description": "Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'."
        }
    )
    values: t.Mapping[str, "DestinyHistoricalStatsValue"] = dt.field(
        metadata={"description": "Collection of stats for the period."}
    )

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
    characters: t.Sequence["DestinyHistoricalStatsPerCharacter"]
    merged_all_characters: "DestinyHistoricalStatsWithMerged"
    merged_deleted_characters: "DestinyHistoricalStatsWithMerged"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "mergedDeletedCharacters": to_json(self.merged_deleted_characters),
            "mergedAllCharacters": to_json(self.merged_all_characters),
            "characters": to_json(self.characters),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsWithMerged:
    merged: "DestinyHistoricalStatsByPeriod"
    results: t.Mapping[str, "DestinyHistoricalStatsByPeriod"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "results": to_json(self.results),
            "merged": to_json(self.merged),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalStatsPerCharacter:
    character_id: int
    deleted: bool
    merged: "DestinyHistoricalStatsByPeriod"
    results: t.Mapping[str, "DestinyHistoricalStatsByPeriod"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "characterId": to_json(self.character_id),
            "deleted": to_json(self.deleted),
            "results": to_json(self.results),
            "merged": to_json(self.merged),
        }


@dt.dataclass(frozen=True)
class DestinyActivityHistoryResults:
    activities: t.Sequence["DestinyHistoricalStatsPeriodGroup"] = dt.field(
        metadata={"description": "List of activities, the most recent activity first."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activities": to_json(self.activities),
        }


@dt.dataclass(frozen=True)
class DestinyHistoricalWeaponStatsData:
    weapons: t.Sequence["DestinyHistoricalWeaponStats"] = dt.field(
        metadata={"description": "List of weapons and their perspective values."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "weapons": to_json(self.weapons),
        }


@dt.dataclass(frozen=True)
class DestinyAggregateActivityResults:
    activities: t.Sequence["DestinyAggregateActivityStats"] = dt.field(
        metadata={
            "description": "List of all activities the player has participated in."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activities": to_json(self.activities),
        }


@dt.dataclass(frozen=True)
class DestinyAggregateActivityStats:
    activity_hash: ManifestReference["DestinyActivityDefinition"] = dt.field(
        metadata={
            "description": "Hash ID that can be looked up in the DestinyActivityTable."
        }
    )
    values: t.Mapping[str, "DestinyHistoricalStatsValue"] = dt.field(
        metadata={"description": "Collection of stats for the player in this activity."}
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "activityHash": to_json(self.activity_hash),
            "values": to_json(self.values),
        }


from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinyActivityDefinition,
    DestinyClassDefinition,
    DestinyGenderDefinition,
    DestinyInventoryItemDefinition,
    DestinyRaceDefinition,
)
from bungieapi.generated.components.schemas.destiny.historical_stats.definitions import (  # noqa: E402
    DestinyActivityModeType,
)
from bungieapi.generated.components.schemas.user import UserInfoCard  # noqa: E402
