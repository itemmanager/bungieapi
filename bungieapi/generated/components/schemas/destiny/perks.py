# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json
from bungieapi.types import ManifestReference


@dt.dataclass(frozen=True)
class DestinyPerkReference:
    """The list of perks to display in an item tooltip - and whether or not they have been activated.
    Perks apply a variety of effects to a character, and are generally either intrinsic to the item or provided in activated talent nodes or sockets."""

    icon_path: str = dt.field(metadata={"description": "The icon for the perk."})
    is_active: bool = dt.field(
        metadata={
            "description": "Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)"
        }
    )
    perk_hash: ManifestReference["DestinySandboxPerkDefinition"] = dt.field(
        metadata={
            "description": "The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user."
        }
    )
    visible: bool = dt.field(
        metadata={
            "description": "Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "perkHash": to_json(self.perk_hash),
            "iconPath": to_json(self.icon_path),
            "isActive": to_json(self.is_active),
            "visible": to_json(self.visible),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny.definitions import (  # noqa: E402
    DestinySandboxPerkDefinition,
)
