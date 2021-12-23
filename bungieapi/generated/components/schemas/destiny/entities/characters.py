# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyCharacterComponent:
    """This component contains base properties of the character.

    You'll probably want to always request this component, but hey you
    do you.
    """

    base_character_level: int  # The "base" level of your character, not accounting for any light level.
    character_id: int  # The unique identifier for the character.
    class_hash: int  # Use this hash to look up the character's DestinyClassDefinition.
    class_type: "DestinyClass"  # Mostly for historical purposes at this point, this is an enumeration for the character's class. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
    date_last_played: str  # The last date that the user played Destiny.
    emblem_background_path: str  # A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
    emblem_color: "DestinyColor"  # A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup.
    emblem_hash: int  # The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition.
    emblem_path: str  # A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
    gender_hash: int  # Use this hash to look up the character's DestinyGenderDefinition.
    gender_type: "DestinyGender"  # Mostly for historical purposes at this point, this is an enumeration for the character's Gender. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me.
    level_progression: "DestinyProgression"  # The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level.
    light: int  # The user's calculated "Light Level". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items.
    membership_id: int  # Every Destiny Profile has a membershipId. This is provided on the character as well for convenience.
    membership_type: "BungieMembershipType"  # membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values.
    minutes_played_this_session: int  # If the user is currently playing, this is how long they've been playing.
    minutes_played_total: int  # If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things.
    percent_to_next_level: float  # A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level.
    race_hash: int  # Use this hash to look up the character's DestinyRaceDefinition.
    race_type: "DestinyRace"  # Mostly for historical purposes at this point, this is an enumeration for the character's race. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
    stats: t.Mapping[
        str, int
    ]  # Your character's stats, such as Agility, Resilience, etc... *not* historical stats. You'll have to call a different endpoint for those.
    title_record_hash: int  # If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information.


@dt.dataclass(frozen=True)
class DestinyCharacterProgressionComponent:
    """This component returns anything that could be considered "Progression"
    on a user: data where the user is gaining levels, reputation, completions,
    rewards, etc..."""

    checklists: t.Mapping[
        str, t.Mapping[str, bool]
    ]  # The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition) For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
    factions: t.Mapping[
        str, "DestinyFactionProgression"
    ]  # A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.
    milestones: t.Mapping[
        str, "DestinyMilestone"
    ]  # Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.
    progressions: t.Mapping[
        str, "DestinyProgression"
    ]  # A Dictionary of all known progressions for the Character, keyed by the Progression's hash. Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.
    quests: t.Sequence[
        "DestinyQuestStatus"
    ]  # If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.  (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.)
    seasonal_artifact: "DestinyArtifactCharacterScoped"  # Data related to your progress on the current season's artifact that can vary per character.
    uninstanced_item_objectives: t.Mapping[
        str, t.Sequence["DestinyObjectiveProgress"]
    ]  # Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items.  This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.
    uninstanced_item_perks: t.Mapping[
        str, "DestinyItemPerksComponent"
    ]  # Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items. This dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.


@dt.dataclass(frozen=True)
class DestinyCharacterRenderComponent:
    """Only really useful if you're attempting to render the character's
    current appearance in 3D, this returns a bare minimum of information, pre-
    aggregated, that you'll need to perform that rendering.

    Note that you need to combine this with other 3D assets and data
    from our servers. Examine the Javascript returned by
    https://bungie.net/sharedbundle/spasm to see how we use this data,
    but be warned: the rabbit hole goes pretty deep.
    """

    custom_dyes: t.Sequence[
        "DyeReference"
    ]  # Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.
    customization: "DestinyCharacterCustomization"  # This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.
    peer_view: "DestinyCharacterPeerView"  # A minimal view of: - Equipped items - The rendering-related custom options on those equipped items Combined, that should be enough to render all of the items on the equipped character.


@dt.dataclass(frozen=True)
class DestinyCharacterActivitiesComponent:
    """This component holds activity data for a character.

    It will tell you about the character's current activity status, as
    well as activities that are available to the user.
    """

    available_activities: t.Sequence[
        "DestinyActivity"
    ]  # The list of activities that the user can play.
    current_activity_hash: int  # If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP "Activities" are just maps: it's the ActivityMode that determines what type of PVP game they're playing.
    current_activity_mode_hash: int  # If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
    current_activity_mode_hashes: t.Sequence[
        int
    ]  # If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
    current_activity_mode_type: int  # And the current activity's most specific mode type, if it can be found.
    current_activity_mode_types: t.Sequence[
        "DestinyActivityModeType"
    ]  # All Activity Modes that apply to the current activity being played, in enum form.
    current_playlist_activity_hash: int  # If the user is in a playlist, this is the hash identifier for the playlist that they chose.
    date_activity_started: str  # The last date that the user started playing an activity.
    last_completed_story_hash: int  # This will have the activity hash of the last completed story/campaign mission, in case you care about that.


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DestinyActivity  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DestinyClass  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DestinyGender  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DestinyRace  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DyeReference  # noqa: E402
from bungieapi.generated.components.schemas.destiny import (
    DestinyProgression,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.artifacts import (
    DestinyArtifactCharacterScoped,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.character import (  # noqa: E402
    DestinyCharacterCustomization,
    DestinyCharacterPeerView,
)
from bungieapi.generated.components.schemas.destiny.entities.items import (
    DestinyItemPerksComponent,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.historical_stats.definitions import (
    DestinyActivityModeType,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.milestones import (
    DestinyMilestone,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.misc import (
    DestinyColor,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.progression import (
    DestinyFactionProgression,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.quests import (  # noqa: E402
    DestinyObjectiveProgress,
    DestinyQuestStatus,
)
