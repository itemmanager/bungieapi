# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyChecklistDefinition:
    """By public demand, Checklists are loose sets of "things to do/things you
    have done" in Destiny that we were actually able to track.

    They include easter eggs you find in the world, unique chests you
    unlock, and other such data where the first time you do it is
    significant enough to be tracked, and you have the potential to "get
    them all". These may be account-wide, or may be per character. The
    status of these will be returned in related "Checklist" data coming
    down from API requests such as GetProfile or GetCharacter. Generally
    speaking, the items in a checklist can be completed in any order: we
    return an ordered list which only implies the way we are showing
    them in our own UI, and you can feel free to alter it as you wish.
    Note that, in the future, there will be something resembling the old
    D1 Record Books in at least some vague form. When that is created,
    it may be that it will supercede much or all of this Checklist data.
    It remains to be seen if that will be the case, so for now assume
    that the Checklists will still exist even after the release of D2:
    Forsaken.
    """

    display_properties: "DestinyDisplayPropertiesDefinition"
    view_action_string: str  # A localized string prompting you to view the checklist.
    scope: "DestinyScope"  # Indicates whether you will find this checklist on the Profile or Character components.
    entries: t.Sequence[
        "DestinyChecklistEntryDefinition"
    ]  # The individual checklist items. Gotta catch 'em all.
    hash: int  # The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
    index: int  # The index of the entity as it was found in the investment tables.
    redacted: bool  # If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!


@dt.dataclass(frozen=True)
class DestinyChecklistEntryDefinition:
    """The properties of an individual checklist item.

    Note that almost everything is optional: it is *highly* variable
    what kind of data we'll actually be able to return: at times we may
    have no other relationships to entities at all. Whatever UI you
    build, do it with the knowledge that any given entry might not
    actually be able to be associated with some other Destiny entity.
    """

    hash: int  # The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists.
    display_properties: "DestinyDisplayPropertiesDefinition"  # Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier.
    destination_hash: int
    location_hash: int
    bubble_hash: int  # Note that a Bubble's hash doesn't uniquely identify a "top level" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning. You can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property.
    activity_hash: int
    item_hash: int
    vendor_hash: int
    vendor_interaction_index: int
    scope: "DestinyScope"  # The scope at which this specific entry can be computed.


from bungieapi.generated.types.destiny import DestinyScope  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.definitions.common import (
    DestinyDisplayPropertiesDefinition,
)  # noqa: E402
