# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyItemComponent:
    """The base item component, filled with properties that are generally
    useful to know in any item request or that don't feel worthwhile to put in
    their own component."""

    bind_status: "ItemBindStatus"  # If the item is bound to a location, it will be specified in this enum.
    bucket_hash: int  # The hash identifier for the specific inventory bucket in which the item is located.
    expiration_date: str  # If the item can expire, this is the date at which it will/did expire.
    is_wrapper: bool  # If this is true, the object is actually a "wrapper" of the object it's representing. This means that it's not the actual item itself, but rather an item that must be "opened" in game before you have and can use the item.  Wrappers are an evolution of "bundles", which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you "open" it.
    item_hash: int  # The identifier for the item's definition, which is where most of the useful static information for the item can be found.
    item_instance_id: int  # If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.
    item_value_visibility: t.Sequence[
        bool
    ]  # If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).
    location: "ItemLocation"  # An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items.
    lockable: bool  # If the item can be locked, this will indicate that state.
    metric_hash: int  # The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate.
    metric_objective: "DestinyObjectiveProgress"  # The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate.
    override_style_item_hash: int  # If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
    quantity: int  # The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it)
    state: "ItemState"  # A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted.
    tooltip_notification_indexes: t.Sequence[
        int
    ]  # If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item.
    transfer_status: "TransferStatuses"  # If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).
    version_number: int  # The version of this item, used to index into the versions list in the item definition quality block.


@dt.dataclass(frozen=True)
class DestinyItemPerksComponent:
    """Instanced items can have perks: benefits that the item bestows.

    These are related to DestinySandboxPerkDefinition, and sometimes - but not always - have human readable info. When they do, they are the icons and text that you see in an item's tooltip.
    Talent Grids, Sockets, and the item itself can apply Perks, which are then summarized here for your convenience.
    """

    perks: t.Sequence[
        "DestinyPerkReference"
    ]  # The list of perks to display in an item tooltip - and whether or not they have been activated.


@dt.dataclass(frozen=True)
class DestinyItemObjectivesComponent:
    """Items can have objectives and progression.

    When you request this block, you will obtain information about any
    Objectives and progression tied to this item.
    """

    date_completed: str  # If we have any information on when these objectives were completed, this will be the date of that completion. This won't be on many items, but could be interesting for some items that do store this information.
    flavor_objective: "DestinyObjectiveProgress"  # I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.
    objectives: t.Sequence[
        "DestinyObjectiveProgress"
    ]  # If the item has a hard association with objectives, your progress on them will be defined here.  Objectives are our standard way to describe a series of tasks that have to be completed for a reward.


@dt.dataclass(frozen=True)
class DestinyItemInstanceComponent:
    """If an item is "instanced", this will contain information about the
    item's instance that doesn't fit easily into other components.

    One might say this is the "essential" instance data for the item.
    Items are instanced if they require information or state that can
    vary. For instance, weapons are Instanced: they are given a unique
    identifier, uniquely generated stats, and can have their properties
    altered. Non-instanced items have none of these things: for
    instance, Glimmer has no unique properties aside from how much of it
    you own. You can tell from an item's definition whether it will be
    instanced or not by looking at the DestinyInventoryItemDefinition's
    definition.inventory.isInstanceItem property.
    """

    breaker_type: int  # If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details.
    breaker_type_hash: int  # If populated, this is the hash identifier for the item's breaker type. See DestinyBreakerTypeDefinition for more details.
    can_equip: bool  # If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details.
    cannot_equip_reason: "EquipFailureReason"  # If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel.
    damage_type: "DamageType"  # If the item has a damage type, this is the item's current damage type.
    damage_type_hash: int  # The current damage type's hash, so you can look up localized info and icons for it.
    energy: "DestinyItemInstanceEnergy"  # IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points.
    equip_required_level: int  # If the item cannot be equipped until you reach a certain level, that level will be reflected here.
    is_equipped: bool  # Is the item currently equipped on the given character?
    item_level: int  # The Item's "Level" has the most significant bearing on its stats, such as Light and Power.
    primary_stat: "DestinyStat"  # The item stat that we consider to be "primary" for the item. For instance, this would be "Attack" for Weapons or "Defense" for armor.
    quality: int  # The "Quality" of the item has a lesser - but still impactful - bearing on stats like Light and Power.
    unlock_hashes_required_to_equip: t.Sequence[
        int
    ]  # Sometimes, there are limitations to equipping that are represented by character-level flags called "unlocks". This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes.


@dt.dataclass(frozen=True)
class DestinyItemInstanceEnergy:
    energy_capacity: int  # The total capacity of Energy that the item currently has, regardless of if it is currently being used.
    energy_type: "DestinyEnergyType"  # This is the enum version of the Energy Type value, for convenience.
    energy_type_hash: int  # The type of energy for this item. Plugs that require Energy can only be inserted if they have the "Any" Energy Type or the matching energy type of this item. This is a reference to the DestinyEnergyTypeDefinition for the energy type, where you can find extended info about it.
    energy_unused: int  # The amount of energy still available for inserting new plugs.
    energy_used: int  # The amount of Energy currently in use by inserted plugs.


@dt.dataclass(frozen=True)
class DestinyItemRenderComponent:
    """Many items can be rendered in 3D.

    When you request this block, you will obtain the custom data needed
    to render this specific instance of the item.
    """

    art_regions: t.Mapping[
        str, int
    ]  # A dictionary for rendering gear components, with: key = Art Arrangement Region Index value = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.
    use_custom_dyes: bool  # If you should use custom dyes on this item, it will be indicated here.


@dt.dataclass(frozen=True)
class DestinyItemStatsComponent:
    """If you want the stats on an item's instanced data, get this component.
    These are stats like Attack, Defense etc... and *not* historical stats.

    Note that some stats have additional computation in-game at runtime - for instance, Magazine Size - and thus these stats might not be 100% accurate compared to what you see in-game for some stats. I know, it sucks. I hate it too.
    """

    stats: t.Mapping[
        str, "DestinyStat"
    ]  # If the item has stats that it provides (damage, defense, etc...), it will be given here.


@dt.dataclass(frozen=True)
class DestinyItemSocketsComponent:
    """Instanced items can have sockets, which are slots on the item where
    plugs can be inserted.

    Sockets are a bit complex: be sure to examine the documentation on
    the DestinyInventoryItemDefinition's "socket" block and elsewhere on
    these objects for more details.
    """

    sockets: t.Sequence[
        "DestinyItemSocketState"
    ]  # The list of all sockets on the item, and their status information.


@dt.dataclass(frozen=True)
class DestinyItemSocketState:
    """The status of a given item's socket.

    (which plug is inserted, if any: whether it is enabled, what
    "reusable" plugs can be inserted, etc...) If I had it to do over,
    this would probably have a DestinyItemPlug representing the inserted
    item instead of most of these properties. :shrug:
    """

    enable_fail_indexes: t.Sequence[
        int
    ]  # If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.
    is_enabled: bool  # Even if a plug is inserted, it doesn't mean it's enabled. This flag indicates whether the plug is active and providing its benefits.
    is_visible: bool  # A plug may theoretically provide benefits but not be visible - for instance, some older items use a plug's damage type perk to modify their own damage type. These, though they are not visible, still affect the item. This field indicates that state. An invisible plug, while it provides benefits if it is Enabled, cannot be directly modified by the user.
    plug_hash: int  # The currently active plug, if any. Note that, because all plugs are statically defined, its effect on stats and perks can be statically determined using the plug item's definition. The stats and perks can be taken at face value on the plug item as the stats and perks it will provide to the user/item.


@dt.dataclass(frozen=True)
class DestinyItemTalentGridComponent:
    """Well, we're here in Destiny 2, and Talent Grids are unfortunately still
    around.

    The good news is that they're pretty much only being used for
    certain base information on items and for Builds/Subclasses. The bad
    news is that they still suck. If you really want this information,
    grab this component. An important note is that talent grids are
    defined as such: A Grid has 1:M Nodes, which has 1:M Steps. Any
    given node can only have a single step active at one time, which
    represents the actual visual contents and effects of the Node (for
    instance, if you see a "Super Cool Bonus" node, the actual icon and
    text for the node is coming from the current Step of that node).
    Nodes can be grouped into exclusivity sets *and* as of D2,
    exclusivity groups (which are collections of exclusivity sets that
    affect each other). See DestinyTalentGridDefinition for more
    information. Brace yourself, the water's cold out there in the deep
    end.
    """

    grid_progression: "DestinyProgression"  # If the item has a progression, it will be detailed here. A progression means that the item can gain experience. Thresholds of experience are what determines whether and when a talent node can be activated.
    is_grid_complete: bool  # Indicates whether the talent grid on this item is completed, and thus whether it should have a gold border around it. Only will be true if the item actually *has* a talent grid, and only then if it is completed (i.e. every exclusive set has an activated node, and every non-exclusive set node has been activated)
    nodes: t.Sequence[
        "DestinyTalentNode"
    ]  # Detailed information about the individual nodes in the talent grid. A node represents a single visual "pip" in the talent grid or Build detail view, though each node may have multiple "steps" which indicate the actual bonuses and visual representation of that node.
    talent_grid_hash: int  # Most items don't have useful talent grids anymore, but Builds in particular still do. You can use this hash to lookup the DestinyTalentGridDefinition attached to this item, which will be crucial for understanding the node values on the item.


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.destiny import DamageType  # noqa: E402
from bungieapi.generated.components.schemas.destiny import DestinyStat  # noqa: E402
from bungieapi.generated.components.schemas.destiny import ItemBindStatus  # noqa: E402
from bungieapi.generated.components.schemas.destiny import ItemLocation  # noqa: E402
from bungieapi.generated.components.schemas.destiny import ItemState  # noqa: E402
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyEnergyType,
    DestinyProgression,
    DestinyTalentNode,
    EquipFailureReason,
    TransferStatuses,
)
from bungieapi.generated.components.schemas.destiny.entities.items import (  # noqa: E402
    DestinyItemInstanceEnergy,
    DestinyItemSocketState,
)
from bungieapi.generated.components.schemas.destiny.perks import (
    DestinyPerkReference,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.quests import (
    DestinyObjectiveProgress,
)  # noqa: E402
