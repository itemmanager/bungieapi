# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyMetricsComponent:
    metrics: t.Optional[t.Mapping[str, "DestinyMetricComponent"]] = None
    metrics_root_node_hash: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "metrics": to_json(self.metrics),
            "metricsRootNodeHash": to_json(self.metrics_root_node_hash),
        }


@dt.dataclass(frozen=True)
class DestinyMetricComponent:
    invisible: t.Optional[bool] = None
    objective_progress: t.Optional["DestinyObjectiveProgress"] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "invisible": to_json(self.invisible),
            "objectiveProgress": to_json(self.objective_progress),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.quests import (
    DestinyObjectiveProgress,
)  # noqa: E402
