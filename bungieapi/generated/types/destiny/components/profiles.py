# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyProfileProgressionComponent:
    """'The set of progression-related information that applies at a Profile-
    wide level for your Destiny experience.

    This differs from the Jimi Hendrix Experience because there's less
    guitars on fire. Yet. #spoileralert? This will include information
    such as Checklist info.
    """

    checklists: t.Mapping[str, t.Mapping[str, bool]]
    seasonal_artifact: "DestinyArtifactProfileScoped"


@dt.dataclass(frozen=True)
class DestinyProfileTransitoryComponent:
    """ 'This is an experimental set of data that Bungie considers to be "transitory" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it.
    This information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data."""

    party_members: t.Sequence["DestinyProfileTransitoryPartyMember"]
    current_activity: "DestinyProfileTransitoryCurrentActivity"
    joinability: "DestinyProfileTransitoryJoinability"
    tracking: t.Sequence["DestinyProfileTransitoryTrackingEntry"]
    last_orbited_destination_hash: int


@dt.dataclass(frozen=True)
class DestinyProfileTransitoryPartyMember:
    """'This is some bare minimum information about a party member in a
    Fireteam.

    Unfortunately, without great computational expense on our side we
    can only get at the data contained here. I'd like to give you a
    character ID for example, but we don't have it. But we do have these
    three pieces of information. May they help you on your quest to show
    meaningful data about current Fireteams. Notably, we don't and can't
    feasibly return info on characters. If you can, try to use just the
    data below for your UI and purposes. Only hit us with further
    queries if you absolutely must know the character ID of the
    currently playing character. Pretty please with sugar on top.
    """

    membership_id: int
    emblem_hash: int
    display_name: str
    status: "DestinyPartyMemberStates"


@dt.dataclass(frozen=True)
class DestinyProfileTransitoryCurrentActivity:
    """'If you are playing in an activity, this is some information about it.

    Note that we cannot guarantee any of this resembles what ends up in
    the PGCR in any way. They are sourced by two entirely separate
    systems with their own logic, and the one we source this data from
    should be considered non-authoritative in comparison.
    """

    start_time: str
    end_time: str
    score: float
    highest_opposing_faction_score: float
    number_of_opponents: int
    number_of_players: int


@dt.dataclass(frozen=True)
class DestinyProfileTransitoryJoinability:
    """'Some basic information about whether you can be joined, how many slots
    are left etc.

    Note that this can change quickly, so it may not actually be useful.
    But perhaps it will be in some use cases?
    """

    open_slots: int
    privacy_setting: "DestinyGamePrivacySetting"
    closed_reasons: "DestinyJoinClosedReasons"


@dt.dataclass(frozen=True)
class DestinyProfileTransitoryTrackingEntry:
    """'This represents a single "thing" being tracked by the player.

    This can point to many types of entities, but only a subset of them
    will actually have a valid hash identifier for whatever it is being
    pointed to. It's up to you to interpret what it means when various
    combinations of these entries have values being tracked.
    """

    location_hash: int
    item_hash: int
    objective_hash: int
    activity_hash: int
    questline_item_hash: int
    tracked_date: str


from bungieapi.generated.types.destiny import DestinyGamePrivacySetting  # noqa: E402
from bungieapi.generated.types.destiny import DestinyJoinClosedReasons  # noqa: E402
from bungieapi.generated.types.destiny import DestinyPartyMemberStates  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.artifacts import (
    DestinyArtifactProfileScoped,
)  # noqa: E402
