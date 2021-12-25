# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyFactionProgression:
    """Mostly for historical purposes, we segregate Faction progressions from
    other progressions.

    This is just a DestinyProgression with a shortcut for finding the
    DestinyFactionDefinition of the faction related to the progression.
    """

    current_progress: int  # This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)
    current_reset_count: int  # The number of resets of this progression you've executed this season, if applicable to this progression.
    daily_limit: int  # If this progression has a daily limit, this is that limit.
    daily_progress: int  # The amount of progress earned today for this progression.
    faction_hash: int  # The hash identifier of the Faction related to this progression. Use it to look up the DestinyFactionDefinition for more rendering info.
    faction_vendor_index: int  # The index of the Faction vendor that is currently available. Will be set to -1 if no vendors are available.
    level: int  # This is the level of the progression (for instance, the Character Level).
    level_cap: int  # This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)
    next_level_at: int  # The total amount of progression (i.e. "Experience") needed in order to reach the next level.
    progress_to_next_level: int  # The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.
    progression_hash: int  # The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.
    reward_item_states: t.Sequence[
        "DestinyProgressionRewardItemState"
    ]  # Information about historical rewards for this progression, if there is any data for it.
    season_resets: t.Sequence[
        "DestinyProgressionResetEntry"
    ]  # Information about historical resets of this progression, if there is any data for it.
    step_index: int  # Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)
    weekly_limit: int  # If this progression has a weekly limit, this is that limit.
    weekly_progress: int  # The amount of progress earned toward this progression in the current week.

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "factionHash": to_json(self.faction_hash),
            "factionVendorIndex": to_json(self.faction_vendor_index),
            "progressionHash": to_json(self.progression_hash),
            "dailyProgress": to_json(self.daily_progress),
            "dailyLimit": to_json(self.daily_limit),
            "weeklyProgress": to_json(self.weekly_progress),
            "weeklyLimit": to_json(self.weekly_limit),
            "currentProgress": to_json(self.current_progress),
            "level": to_json(self.level),
            "levelCap": to_json(self.level_cap),
            "stepIndex": to_json(self.step_index),
            "progressToNextLevel": to_json(self.progress_to_next_level),
            "nextLevelAt": to_json(self.next_level_at),
            "currentResetCount": to_json(self.current_reset_count),
            "seasonResets": to_json(self.season_resets),
            "rewardItemStates": to_json(self.reward_item_states),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyProgressionResetEntry,
    DestinyProgressionRewardItemState,
)
