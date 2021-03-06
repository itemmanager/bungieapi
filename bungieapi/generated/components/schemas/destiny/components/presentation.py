# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyPresentationNodesComponent:
    nodes: t.Mapping[str, "DestinyPresentationNodeComponent"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "nodes": to_json(self.nodes),
        }


@dt.dataclass(frozen=True)
class DestinyPresentationNodeComponent:
    completion_value: int = dt.field(
        metadata={
            "description": "The value at which the presentation node is considered to be completed."
        }
    )
    objective: "DestinyObjectiveProgress" = dt.field(
        metadata={
            "description": "An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes."
        }
    )
    progress_value: int = dt.field(
        metadata={
            "description": "How much of the presentation node is considered to be completed so far by the given character/profile."
        }
    )
    state: "DestinyPresentationNodeState"
    record_category_score: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": "If available, this is the current score for the record category that this node represents."
        },
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "state": to_json(self.state),
            "objective": to_json(self.objective),
            "progressValue": to_json(self.progress_value),
            "completionValue": to_json(self.completion_value),
            "recordCategoryScore": to_json(self.record_category_score),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyPresentationNodeState,
)
from bungieapi.generated.components.schemas.destiny.quests import (  # noqa: E402
    DestinyObjectiveProgress,
)
