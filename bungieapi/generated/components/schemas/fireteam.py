# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


class FireteamDateRange(Enum):
    ALL = 0
    NOW = 1
    TWENTY_FOUR_HOURS = 2
    FORTY_EIGHT_HOURS = 3
    THIS_WEEK = 4


class FireteamPlatform(Enum):
    ANY = 0
    PLAYSTATION4 = 1
    XBOX_ONE = 2
    BLIZZARD = 3
    STEAM = 4
    STADIA = 5


class FireteamPublicSearchOption(Enum):
    PUBLIC_AND_PRIVATE = 0
    PUBLIC_ONLY = 1
    PRIVATE_ONLY = 2


class FireteamSlotSearch(Enum):
    NO_SLOT_RESTRICTION = 0
    HAS_OPEN_PLAYER_SLOTS = 1
    HAS_OPEN_PLAYER_OR_ALT_SLOTS = 2


@dt.dataclass(frozen=True)
class FireteamSummary:
    activity_type: int
    alternate_slot_count: int
    available_alternate_slot_count: int
    available_player_slot_count: int
    date_created: str
    date_modified: str
    date_player_modified: str
    fireteam_id: int
    group_id: int
    is_immediate: bool
    is_public: bool
    is_valid: bool
    locale: str
    owner_membership_id: int
    platform: "FireteamPlatform"
    player_slot_count: int
    scheduled_time: str
    title: str
    title_before_moderation: str


@dt.dataclass(frozen=True)
class FireteamResponse:
    alternates: t.Sequence["FireteamMember"]
    members: t.Sequence["FireteamMember"]
    summary: "FireteamSummary"


@dt.dataclass(frozen=True)
class FireteamMember:
    bungie_net_user_info: "UserInfoCard"
    character_id: int
    date_joined: str
    destiny_user_info: "FireteamUserInfoCard"
    has_microphone: bool
    last_platform_invite_attempt_date: str
    last_platform_invite_attempt_result: "FireteamPlatformInviteResult"


@dt.dataclass(frozen=True)
class FireteamUserInfoCard:
    fireteam_display_name: str
    fireteam_membership_type: "BungieMembershipType"
    applicable_membership_types: t.Sequence[
        "BungieMembershipType"
    ]  # The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
    bungie_global_display_name: str  # The bungie global display name, if set.
    bungie_global_display_name_code: int  # The bungie global display name code, if set.
    cross_save_override: "BungieMembershipType"  # If there is a cross save override in effect, this value will tell you the type that is overridding this one.
    display_name: str  # Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
    icon_path: str  # URL the Icon if available.
    is_public: bool  # If True, this is a public user membership.
    membership_id: int  # Membership ID as they user is known in the Accounts service
    membership_type: "BungieMembershipType"  # Type of the membership. Not necessarily the native type.
    supplemental_display_name: str  # A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.


class FireteamPlatformInviteResult(Enum):
    NONE = 0
    SUCCESS = 1
    ALREADY_IN_FIRETEAM = 2
    THROTTLED = 3
    SERVICE_ERROR = 4


from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.fireteam import FireteamMember  # noqa: E402
from bungieapi.generated.components.schemas.fireteam import (  # noqa: E402
    FireteamPlatform,
    FireteamPlatformInviteResult,
    FireteamSummary,
    FireteamUserInfoCard,
)
from bungieapi.generated.components.schemas.user import UserInfoCard  # noqa: E402
