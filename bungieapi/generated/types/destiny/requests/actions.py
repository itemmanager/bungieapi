# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types import BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyActionRequest:
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyCharacterActionRequest:
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyItemActionRequest:
    item_id: int
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyPostmasterTransferRequest:
    item_reference_hash: int
    stack_size: int
    item_id: int
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyItemSetActionRequest:
    item_ids: t.Sequence[int]
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyItemStateRequest:
    state: bool
    item_id: int
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyInsertPlugsActionRequest:
    action_token: str
    item_instance_id: int
    plug: t.Any
    character_id: int
    membership_type: BungieMembershipType


@dt.dataclass(frozen=True)
class DestinyInsertPlugsRequestEntry:
    """'Represents all of the data related to a single plug to be inserted.

    Note that, while you *can* point to a socket that represents
    infusion, you will receive an error if you attempt to do so. Come on
    guys, let's play nice.
    """

    socket_index: int
    socket_array_type: "DestinySocketArrayType"
    plug_item_hash: int


DestinySocketArrayType = t.Any


@dt.dataclass(frozen=True)
class DestinyInsertPlugsFreeActionRequest:
    plug: t.Any
    item_id: int
    character_id: int
    membership_type: BungieMembershipType
