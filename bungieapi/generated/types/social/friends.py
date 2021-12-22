# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.generated.types import BungieMembershipType
from bungieapi.generated.types.user import GeneralUser


@dt.dataclass(frozen=True)
class BungieFriendListResponse:
    friends: t.Sequence["BungieFriend"]


@dt.dataclass(frozen=True)
class BungieFriend:
    last_seen_as_membership_id: int
    last_seen_as_bungie_membership_type: BungieMembershipType
    bungie_global_display_name: str
    bungie_global_display_name_code: int
    online_status: "PresenceStatus"
    online_title: "PresenceOnlineStateFlags"
    relationship: "FriendRelationshipState"
    bungie_net_user: GeneralUser


PresenceStatus = t.Any
PresenceOnlineStateFlags = t.Any
FriendRelationshipState = t.Any


@dt.dataclass(frozen=True)
class BungieFriendRequestListResponse:
    incoming_requests: t.Sequence["BungieFriend"]
    outgoing_requests: t.Sequence["BungieFriend"]


PlatformFriendType = t.Any


@dt.dataclass(frozen=True)
class PlatformFriendResponse:
    items_per_page: int
    current_page: int
    has_more: bool
    platform_friends: t.Sequence["PlatformFriend"]


@dt.dataclass(frozen=True)
class PlatformFriend:
    platform_display_name: str
    friend_platform: "PlatformFriendType"
    destiny_membership_id: int
    destiny_membership_type: int
    bungie_net_membership_id: int
    bungie_global_display_name: str
    bungie_global_display_name_code: int
