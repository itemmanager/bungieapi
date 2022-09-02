# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum, Flag

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class BungieFriendListResponse:
    friends: t.Sequence["BungieFriend"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "friends": to_json(self.friends),
        }


@dt.dataclass(frozen=True)
class BungieFriend:
    bungie_global_display_name: str
    bungie_net_user: "GeneralUser"
    last_seen_as_bungie_membership_type: "BungieMembershipType"
    last_seen_as_membership_id: int
    online_status: "PresenceStatus"
    online_title: "PresenceOnlineStateFlags"
    relationship: "FriendRelationshipState"
    bungie_global_display_name_code: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "lastSeenAsMembershipId": to_json(self.last_seen_as_membership_id),
            "lastSeenAsBungieMembershipType": to_json(
                self.last_seen_as_bungie_membership_type
            ),
            "bungieGlobalDisplayName": to_json(self.bungie_global_display_name),
            "bungieGlobalDisplayNameCode": to_json(
                self.bungie_global_display_name_code
            ),
            "onlineStatus": to_json(self.online_status),
            "onlineTitle": to_json(self.online_title),
            "relationship": to_json(self.relationship),
            "bungieNetUser": to_json(self.bungie_net_user),
        }


class PresenceStatus(Enum):
    OFFLINE_OR_UNKNOWN = 0
    ONLINE = 1


class PresenceOnlineStateFlags(Flag):
    NONE = 0
    DESTINY1 = 1
    DESTINY2 = 2


class FriendRelationshipState(Enum):
    UNKNOWN = 0
    FRIEND = 1
    INCOMING_REQUEST = 2
    OUTGOING_REQUEST = 3


@dt.dataclass(frozen=True)
class BungieFriendRequestListResponse:
    incoming_requests: t.Sequence["BungieFriend"]
    outgoing_requests: t.Sequence["BungieFriend"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "incomingRequests": to_json(self.incoming_requests),
            "outgoingRequests": to_json(self.outgoing_requests),
        }


class PlatformFriendType(Enum):
    UNKNOWN = 0
    XBOX = 1
    PSN = 2
    STEAM = 3
    EGS = 4


@dt.dataclass(frozen=True)
class PlatformFriendResponse:
    current_page: int
    has_more: bool
    items_per_page: int
    platform_friends: t.Sequence["PlatformFriend"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "itemsPerPage": to_json(self.items_per_page),
            "currentPage": to_json(self.current_page),
            "hasMore": to_json(self.has_more),
            "platformFriends": to_json(self.platform_friends),
        }


@dt.dataclass(frozen=True)
class PlatformFriend:
    bungie_global_display_name: str
    friend_platform: "PlatformFriendType"
    platform_display_name: str
    bungie_global_display_name_code: t.Optional[int] = None
    bungie_net_membership_id: t.Optional[int] = None
    destiny_membership_id: t.Optional[int] = None
    destiny_membership_type: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "platformDisplayName": to_json(self.platform_display_name),
            "friendPlatform": to_json(self.friend_platform),
            "destinyMembershipId": to_json(self.destiny_membership_id),
            "destinyMembershipType": to_json(self.destiny_membership_type),
            "bungieNetMembershipId": to_json(self.bungie_net_membership_id),
            "bungieGlobalDisplayName": to_json(self.bungie_global_display_name),
            "bungieGlobalDisplayNameCode": to_json(
                self.bungie_global_display_name_code
            ),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402
from bungieapi.generated.components.schemas.user import GeneralUser  # noqa: E402
