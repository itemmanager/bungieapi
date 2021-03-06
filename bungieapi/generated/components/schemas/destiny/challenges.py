# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyChallengeStatus:
    """Represents the status and other related information for a challenge that is - or was - available to a player.
    A challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play."""

    objective: "DestinyObjectiveProgress" = dt.field(
        metadata={
            "description": "The progress - including completion status - of the active challenge."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "objective": to_json(self.objective),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.quests import (  # noqa: E402
    DestinyObjectiveProgress,
)
