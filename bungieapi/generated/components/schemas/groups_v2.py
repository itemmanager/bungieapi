# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum, Flag

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class GroupUserInfoCard:
    last_seen_display_name: str = dt.field(
        metadata={
            "description": "This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property."
        }
    )
    last_seen_display_name_type: "BungieMembershipType" = dt.field(
        metadata={"description": "The platform of the LastSeenDisplayName"}
    )
    applicable_membership_types: t.Sequence["BungieMembershipType"] = dt.field(
        metadata={
            "description": """The list of Membership Types indicating the platforms on which this Membership can be used.
 Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list"""
        }
    )
    bungie_global_display_name: str = dt.field(
        metadata={"description": "The bungie global display name, if set."}
    )
    cross_save_override: "BungieMembershipType" = dt.field(
        metadata={
            "description": "If there is a cross save override in effect, this value will tell you the type that is overridding this one."
        }
    )
    display_name: str = dt.field(
        metadata={
            "description": "Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API."
        }
    )
    icon_path: str = dt.field(metadata={"description": "URL the Icon if available."})
    is_public: bool = dt.field(
        metadata={"description": "If True, this is a public user membership."}
    )
    membership_id: int = dt.field(
        metadata={
            "description": "Membership ID as they user is known in the Accounts service"
        }
    )
    membership_type: "BungieMembershipType" = dt.field(
        metadata={
            "description": "Type of the membership. Not necessarily the native type."
        }
    )
    supplemental_display_name: str = dt.field(
        metadata={
            "description": "A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc."
        }
    )
    bungie_global_display_name_code: t.Optional[int] = dt.field(
        default=None,
        metadata={"description": "The bungie global display name code, if set."},
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "LastSeenDisplayName": to_json(self.last_seen_display_name),
            "LastSeenDisplayNameType": to_json(self.last_seen_display_name_type),
            "supplementalDisplayName": to_json(self.supplemental_display_name),
            "iconPath": to_json(self.icon_path),
            "crossSaveOverride": to_json(self.cross_save_override),
            "applicableMembershipTypes": to_json(self.applicable_membership_types),
            "isPublic": to_json(self.is_public),
            "membershipType": to_json(self.membership_type),
            "membershipId": to_json(self.membership_id),
            "displayName": to_json(self.display_name),
            "bungieGlobalDisplayName": to_json(self.bungie_global_display_name),
            "bungieGlobalDisplayNameCode": to_json(
                self.bungie_global_display_name_code
            ),
        }


@dt.dataclass(frozen=True)
class GroupResponse:
    alliance_status: "GroupAllianceStatus"
    allied_ids: t.Sequence[int]
    current_user_member_map: t.Mapping[str, "GroupMember"] = dt.field(
        metadata={
            "description": "This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available."
        }
    )
    current_user_memberships_inactive_for_destiny: bool = dt.field(
        metadata={
            "description": "A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save."
        }
    )
    current_user_potential_member_map: t.Mapping[
        str, "GroupPotentialMember"
    ] = dt.field(
        metadata={
            "description": "This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once."
        }
    )
    detail: "GroupV2"
    founder: "GroupMember"
    group_join_invite_count: int
    parent_group: "GroupV2"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "detail": to_json(self.detail),
            "founder": to_json(self.founder),
            "alliedIds": to_json(self.allied_ids),
            "parentGroup": to_json(self.parent_group),
            "allianceStatus": to_json(self.alliance_status),
            "groupJoinInviteCount": to_json(self.group_join_invite_count),
            "currentUserMembershipsInactiveForDestiny": to_json(
                self.current_user_memberships_inactive_for_destiny
            ),
            "currentUserMemberMap": to_json(self.current_user_member_map),
            "currentUserPotentialMemberMap": to_json(
                self.current_user_potential_member_map
            ),
        }


@dt.dataclass(frozen=True)
class GroupV2:
    about: str
    allow_chat: bool
    avatar_image_index: int
    avatar_path: str
    banner_path: str
    chat_security: "ChatSecuritySetting"
    clan_info: "GroupV2ClanInfoAndInvestment"
    conversation_id: int
    creation_date: str
    default_publicity: "GroupPostPublicity"
    enable_invitation_messaging_for_admins: bool
    features: "GroupFeatures"
    group_id: int
    group_type: "GroupType"
    homepage: "GroupHomepage"
    is_default_post_public: bool
    is_public: bool
    is_public_topic_admin_only: bool
    locale: str
    member_count: int
    membership_id_created: int
    membership_option: "MembershipOption"
    modification_date: str
    motto: str
    name: str
    tags: t.Sequence[str]
    theme: str
    ban_expire_date: t.Optional[str] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "name": to_json(self.name),
            "groupType": to_json(self.group_type),
            "membershipIdCreated": to_json(self.membership_id_created),
            "creationDate": to_json(self.creation_date),
            "modificationDate": to_json(self.modification_date),
            "about": to_json(self.about),
            "tags": to_json(self.tags),
            "memberCount": to_json(self.member_count),
            "isPublic": to_json(self.is_public),
            "isPublicTopicAdminOnly": to_json(self.is_public_topic_admin_only),
            "motto": to_json(self.motto),
            "allowChat": to_json(self.allow_chat),
            "isDefaultPostPublic": to_json(self.is_default_post_public),
            "chatSecurity": to_json(self.chat_security),
            "locale": to_json(self.locale),
            "avatarImageIndex": to_json(self.avatar_image_index),
            "homepage": to_json(self.homepage),
            "membershipOption": to_json(self.membership_option),
            "defaultPublicity": to_json(self.default_publicity),
            "theme": to_json(self.theme),
            "bannerPath": to_json(self.banner_path),
            "avatarPath": to_json(self.avatar_path),
            "conversationId": to_json(self.conversation_id),
            "enableInvitationMessagingForAdmins": to_json(
                self.enable_invitation_messaging_for_admins
            ),
            "banExpireDate": to_json(self.ban_expire_date),
            "features": to_json(self.features),
            "clanInfo": to_json(self.clan_info),
        }


class GroupType(Enum):
    GENERAL = 0
    CLAN = 1


class ChatSecuritySetting(Enum):
    GROUP = 0
    ADMINS = 1


class GroupHomepage(Enum):
    WALL = 0
    FORUM = 1
    ALLIANCE_FORUM = 2


class MembershipOption(Enum):
    REVIEWED = 0
    OPEN = 1
    CLOSED = 2


class GroupPostPublicity(Enum):
    PUBLIC = 0
    ALLIANCE = 1
    PRIVATE = 2


@dt.dataclass(frozen=True)
class GroupFeatures:
    capabilities: "Capabilities"
    host_guided_game_permission_override: "HostGuidedGamesPermissionLevel" = dt.field(
        metadata={
            "description": """Minimum Member Level allowed to host guided games
Always Allowed: Founder, Acting Founder, Admin
Allowed Overrides: None, Member, Beginner
Default is Member for clans, None for groups, although this means nothing for groups."""
        }
    )
    invite_permission_override: bool = dt.field(
        metadata={
            "description": """Minimum Member Level allowed to invite new members to group
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        }
    )
    join_level: "RuntimeGroupMemberType" = dt.field(
        metadata={
            "description": """Level to join a member at when accepting an invite, application, or joining an open clan
Default is Beginner."""
        }
    )
    maximum_members: int
    maximum_memberships_of_group_type: int = dt.field(
        metadata={
            "description": "Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership."
        }
    )
    membership_types: t.Sequence["BungieMembershipType"]
    update_banner_permission_override: bool = dt.field(
        metadata={
            "description": """Minimum Member Level allowed to update banner
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        }
    )
    update_culture_permission_override: bool = dt.field(
        metadata={
            "description": """Minimum Member Level allowed to update group culture
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "maximumMembers": to_json(self.maximum_members),
            "maximumMembershipsOfGroupType": to_json(
                self.maximum_memberships_of_group_type
            ),
            "capabilities": to_json(self.capabilities),
            "membershipTypes": to_json(self.membership_types),
            "invitePermissionOverride": to_json(self.invite_permission_override),
            "updateCulturePermissionOverride": to_json(
                self.update_culture_permission_override
            ),
            "hostGuidedGamePermissionOverride": to_json(
                self.host_guided_game_permission_override
            ),
            "updateBannerPermissionOverride": to_json(
                self.update_banner_permission_override
            ),
            "joinLevel": to_json(self.join_level),
        }


class Capabilities(Flag):
    NONE = 0
    LEADERBOARDS = 1
    CALLSIGN = 2
    OPTIONAL_CONVERSATIONS = 4
    CLAN_BANNER = 8
    D2_INVESTMENT_DATA = 16
    TAGS = 32
    ALLIANCES = 64


class HostGuidedGamesPermissionLevel(Enum):
    """Used for setting the guided game permission level override (admins and
    founders can always host guided games)."""

    NONE = 0
    BEGINNER = 1
    MEMBER = 2


class RuntimeGroupMemberType(Enum):
    """The member levels used by all V2 Groups API.

    Individual group types use their own mappings in their native
    storage (general uses BnetDbGroupMemberType and D2 clans use
    ClanMemberLevel), but they are all translated to this in the runtime
    api. These runtime values should NEVER be stored anywhere, so the
    values can be changed as necessary.
    """

    NONE = 0
    BEGINNER = 1
    MEMBER = 2
    ADMIN = 3
    ACTING_FOUNDER = 4
    FOUNDER = 5


@dt.dataclass(frozen=True)
class GroupV2ClanInfo:
    """This contract contains clan-specific group information.

    It does not include any investment data.
    """

    clan_banner_data: "ClanBanner"
    clan_callsign: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "clanCallsign": to_json(self.clan_callsign),
            "clanBannerData": to_json(self.clan_banner_data),
        }


@dt.dataclass(frozen=True)
class ClanBanner:
    decal_background_color_id: int
    decal_color_id: int
    decal_id: int
    gonfalon_color_id: int
    gonfalon_detail_color_id: int
    gonfalon_detail_id: int
    gonfalon_id: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "decalId": to_json(self.decal_id),
            "decalColorId": to_json(self.decal_color_id),
            "decalBackgroundColorId": to_json(self.decal_background_color_id),
            "gonfalonId": to_json(self.gonfalon_id),
            "gonfalonColorId": to_json(self.gonfalon_color_id),
            "gonfalonDetailId": to_json(self.gonfalon_detail_id),
            "gonfalonDetailColorId": to_json(self.gonfalon_detail_color_id),
        }


@dt.dataclass(frozen=True)
class GroupV2ClanInfoAndInvestment:
    """The same as GroupV2ClanInfo, but includes any investment data."""

    clan_banner_data: "ClanBanner"
    clan_callsign: str
    d2_clan_progressions: t.Mapping[str, "DestinyProgression"]

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "d2ClanProgressions": to_json(self.d2_clan_progressions),
            "clanCallsign": to_json(self.clan_callsign),
            "clanBannerData": to_json(self.clan_banner_data),
        }


@dt.dataclass(frozen=True)
class GroupUserBase:
    bungie_net_user_info: "UserInfoCard"
    destiny_user_info: "GroupUserInfoCard"
    group_id: int
    join_date: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "destinyUserInfo": to_json(self.destiny_user_info),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
            "joinDate": to_json(self.join_date),
        }


@dt.dataclass(frozen=True)
class GroupMember:
    bungie_net_user_info: "UserInfoCard"
    destiny_user_info: "GroupUserInfoCard"
    group_id: int
    is_online: bool
    join_date: str
    last_online_status_change: int
    member_type: "RuntimeGroupMemberType"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "memberType": to_json(self.member_type),
            "isOnline": to_json(self.is_online),
            "lastOnlineStatusChange": to_json(self.last_online_status_change),
            "groupId": to_json(self.group_id),
            "destinyUserInfo": to_json(self.destiny_user_info),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
            "joinDate": to_json(self.join_date),
        }


class GroupAllianceStatus(Enum):
    UNALLIED = 0
    PARENT = 1
    CHILD = 2


@dt.dataclass(frozen=True)
class GroupPotentialMember:
    bungie_net_user_info: "UserInfoCard"
    destiny_user_info: "GroupUserInfoCard"
    group_id: int
    join_date: str
    potential_status: "GroupPotentialMemberStatus"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "potentialStatus": to_json(self.potential_status),
            "groupId": to_json(self.group_id),
            "destinyUserInfo": to_json(self.destiny_user_info),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
            "joinDate": to_json(self.join_date),
        }


class GroupPotentialMemberStatus(Enum):
    NONE = 0
    APPLICANT = 1
    INVITEE = 2


class GroupDateRange(Enum):
    ALL = 0
    PAST_DAY = 1
    PAST_WEEK = 2
    PAST_MONTH = 3
    PAST_YEAR = 4


@dt.dataclass(frozen=True)
class GroupV2Card:
    """A small infocard of group information, usually used for when a list of
    groups are returned."""

    about: str
    avatar_path: str
    capabilities: "Capabilities"
    clan_info: "GroupV2ClanInfo"
    creation_date: str
    group_id: int
    group_type: "GroupType"
    locale: str
    member_count: int
    membership_option: "MembershipOption"
    motto: str
    name: str
    theme: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "name": to_json(self.name),
            "groupType": to_json(self.group_type),
            "creationDate": to_json(self.creation_date),
            "about": to_json(self.about),
            "motto": to_json(self.motto),
            "memberCount": to_json(self.member_count),
            "locale": to_json(self.locale),
            "membershipOption": to_json(self.membership_option),
            "capabilities": to_json(self.capabilities),
            "clanInfo": to_json(self.clan_info),
            "avatarPath": to_json(self.avatar_path),
            "theme": to_json(self.theme),
        }


@dt.dataclass(frozen=True)
class GroupSearchResponse:
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    results: t.Sequence["GroupV2Card"]
    total_results: int
    use_total_results: bool = dt.field(
        metadata={
            "description": """If useTotalResults is true, then totalResults represents an accurate count.
If False, it does not, and may be estimated/only the size of the current page.
Either way, you should probably always only trust hasMore.
This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one."""
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "results": to_json(self.results),
            "totalResults": to_json(self.total_results),
            "hasMore": to_json(self.has_more),
            "query": to_json(self.query),
            "replacementContinuationToken": to_json(
                self.replacement_continuation_token
            ),
            "useTotalResults": to_json(self.use_total_results),
        }


@dt.dataclass(frozen=True)
class GroupQuery:
    """NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes".
    If you are querying for a group, you can pass any of the properties below.
    If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):
    - groupMemberCountFilter - localeFilter - tagText
    If you pass these, you will get a useless InvalidParameters error."""

    creation_date: "GroupDateRange"
    current_page: int
    group_type: "GroupType"
    items_per_page: int
    locale_filter: str
    name: str
    request_continuation_token: str
    sort_by: "GroupSortBy"
    tag_text: str
    group_member_count_filter: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "groupType": to_json(self.group_type),
            "creationDate": to_json(self.creation_date),
            "sortBy": to_json(self.sort_by),
            "groupMemberCountFilter": to_json(self.group_member_count_filter),
            "localeFilter": to_json(self.locale_filter),
            "tagText": to_json(self.tag_text),
            "itemsPerPage": to_json(self.items_per_page),
            "currentPage": to_json(self.current_page),
            "requestContinuationToken": to_json(self.request_continuation_token),
        }


class GroupSortBy(Enum):
    NAME = 0
    DATE = 1
    POPULARITY = 2
    ID = 3


class GroupMemberCountFilter(Enum):
    ALL = 0
    ONE_TO_TEN = 1
    ELEVEN_TO_ONE_HUNDRED = 2
    GREATER_THAN_ONE_HUNDRED = 3


@dt.dataclass(frozen=True)
class GroupNameSearchRequest:
    group_name: str
    group_type: "GroupType"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupName": to_json(self.group_name),
            "groupType": to_json(self.group_type),
        }


@dt.dataclass(frozen=True)
class GroupOptionalConversation:
    chat_enabled: bool
    chat_name: str
    chat_security: "ChatSecuritySetting"
    conversation_id: int
    group_id: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "conversationId": to_json(self.conversation_id),
            "chatEnabled": to_json(self.chat_enabled),
            "chatName": to_json(self.chat_name),
            "chatSecurity": to_json(self.chat_security),
        }


@dt.dataclass(frozen=True)
class GroupEditAction:
    about: str
    callsign: str
    locale: str
    motto: str
    name: str
    tags: str
    theme: str
    allow_chat: t.Optional[bool] = None
    avatar_image_index: t.Optional[int] = None
    chat_security: t.Optional[int] = None
    default_publicity: t.Optional[int] = None
    enable_invitation_messaging_for_admins: t.Optional[bool] = None
    homepage: t.Optional[int] = None
    is_public: t.Optional[bool] = None
    is_public_topic_admin_only: t.Optional[bool] = None
    membership_option: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "about": to_json(self.about),
            "motto": to_json(self.motto),
            "theme": to_json(self.theme),
            "avatarImageIndex": to_json(self.avatar_image_index),
            "tags": to_json(self.tags),
            "isPublic": to_json(self.is_public),
            "membershipOption": to_json(self.membership_option),
            "isPublicTopicAdminOnly": to_json(self.is_public_topic_admin_only),
            "allowChat": to_json(self.allow_chat),
            "chatSecurity": to_json(self.chat_security),
            "callsign": to_json(self.callsign),
            "locale": to_json(self.locale),
            "homepage": to_json(self.homepage),
            "enableInvitationMessagingForAdmins": to_json(
                self.enable_invitation_messaging_for_admins
            ),
            "defaultPublicity": to_json(self.default_publicity),
        }


@dt.dataclass(frozen=True)
class GroupOptionsEditAction:
    host_guided_game_permission_override: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": """Minimum Member Level allowed to host guided games
Always Allowed: Founder, Acting Founder, Admin
Allowed Overrides: None, Member, Beginner
Default is Member for clans, None for groups, although this means nothing for groups."""
        },
    )
    invite_permission_override: t.Optional[bool] = dt.field(
        default=None,
        metadata={
            "description": """Minimum Member Level allowed to invite new members to group
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        },
    )
    join_level: t.Optional[int] = dt.field(
        default=None,
        metadata={
            "description": """Level to join a member at when accepting an invite, application, or joining an open clan
Default is Beginner."""
        },
    )
    update_banner_permission_override: t.Optional[bool] = dt.field(
        default=None,
        metadata={
            "description": """Minimum Member Level allowed to update banner
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        },
    )
    update_culture_permission_override: t.Optional[bool] = dt.field(
        default=None,
        metadata={
            "description": """Minimum Member Level allowed to update group culture
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups."""
        },
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "InvitePermissionOverride": to_json(self.invite_permission_override),
            "UpdateCulturePermissionOverride": to_json(
                self.update_culture_permission_override
            ),
            "HostGuidedGamePermissionOverride": to_json(
                self.host_guided_game_permission_override
            ),
            "UpdateBannerPermissionOverride": to_json(
                self.update_banner_permission_override
            ),
            "JoinLevel": to_json(self.join_level),
        }


@dt.dataclass(frozen=True)
class GroupOptionalConversationAddRequest:
    chat_name: str
    chat_security: "ChatSecuritySetting"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "chatName": to_json(self.chat_name),
            "chatSecurity": to_json(self.chat_security),
        }


@dt.dataclass(frozen=True)
class GroupOptionalConversationEditRequest:
    chat_name: str
    chat_enabled: t.Optional[bool] = None
    chat_security: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "chatEnabled": to_json(self.chat_enabled),
            "chatName": to_json(self.chat_name),
            "chatSecurity": to_json(self.chat_security),
        }


@dt.dataclass(frozen=True)
class GroupMemberLeaveResult:
    group: "GroupV2"
    group_deleted: bool

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "group": to_json(self.group),
            "groupDeleted": to_json(self.group_deleted),
        }


@dt.dataclass(frozen=True)
class GroupBanRequest:
    comment: str
    length: "IgnoreLength"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "comment": to_json(self.comment),
            "length": to_json(self.length),
        }


@dt.dataclass(frozen=True)
class GroupBan:
    bungie_net_user_info: "UserInfoCard"
    comment: str
    created_by: "UserInfoCard"
    date_banned: str
    date_expires: str
    destiny_user_info: "GroupUserInfoCard"
    group_id: int
    last_modified_by: "UserInfoCard"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "lastModifiedBy": to_json(self.last_modified_by),
            "createdBy": to_json(self.created_by),
            "dateBanned": to_json(self.date_banned),
            "dateExpires": to_json(self.date_expires),
            "comment": to_json(self.comment),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
            "destinyUserInfo": to_json(self.destiny_user_info),
        }


@dt.dataclass(frozen=True)
class GroupMemberApplication:
    bungie_net_user_info: "UserInfoCard"
    creation_date: str
    destiny_user_info: "GroupUserInfoCard"
    group_id: int
    request_message: str
    resolve_message: str
    resolve_state: "GroupApplicationResolveState"
    resolve_date: t.Optional[str] = None
    resolved_by_membership_id: t.Optional[int] = None

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "groupId": to_json(self.group_id),
            "creationDate": to_json(self.creation_date),
            "resolveState": to_json(self.resolve_state),
            "resolveDate": to_json(self.resolve_date),
            "resolvedByMembershipId": to_json(self.resolved_by_membership_id),
            "requestMessage": to_json(self.request_message),
            "resolveMessage": to_json(self.resolve_message),
            "destinyUserInfo": to_json(self.destiny_user_info),
            "bungieNetUserInfo": to_json(self.bungie_net_user_info),
        }


class GroupApplicationResolveState(Enum):
    UNRESOLVED = 0
    ACCEPTED = 1
    DENIED = 2
    RESCINDED = 3


@dt.dataclass(frozen=True)
class GroupApplicationRequest:
    message: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "message": to_json(self.message),
        }


@dt.dataclass(frozen=True)
class GroupApplicationListRequest:
    memberships: t.Sequence["UserMembership"]
    message: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "memberships": to_json(self.memberships),
            "message": to_json(self.message),
        }


class GroupsForMemberFilter(Enum):
    ALL = 0
    FOUNDED = 1
    NON_FOUNDED = 2


@dt.dataclass(frozen=True)
class GroupMembershipBase:
    group: "GroupV2"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "group": to_json(self.group),
        }


@dt.dataclass(frozen=True)
class GroupMembership:
    group: "GroupV2"
    member: "GroupMember"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "member": to_json(self.member),
            "group": to_json(self.group),
        }


@dt.dataclass(frozen=True)
class GroupMembershipSearchResponse:
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    results: t.Sequence["GroupMembership"]
    total_results: int
    use_total_results: bool = dt.field(
        metadata={
            "description": """If useTotalResults is true, then totalResults represents an accurate count.
If False, it does not, and may be estimated/only the size of the current page.
Either way, you should probably always only trust hasMore.
This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one."""
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "results": to_json(self.results),
            "totalResults": to_json(self.total_results),
            "hasMore": to_json(self.has_more),
            "query": to_json(self.query),
            "replacementContinuationToken": to_json(
                self.replacement_continuation_token
            ),
            "useTotalResults": to_json(self.use_total_results),
        }


@dt.dataclass(frozen=True)
class GetGroupsForMemberResponse:
    are_all_memberships_inactive: t.Mapping[str, bool] = dt.field(
        metadata={
            "description": """A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
 The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive."""
        }
    )
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    results: t.Sequence["GroupMembership"]
    total_results: int
    use_total_results: bool = dt.field(
        metadata={
            "description": """If useTotalResults is true, then totalResults represents an accurate count.
If False, it does not, and may be estimated/only the size of the current page.
Either way, you should probably always only trust hasMore.
This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one."""
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "areAllMembershipsInactive": to_json(self.are_all_memberships_inactive),
            "results": to_json(self.results),
            "totalResults": to_json(self.total_results),
            "hasMore": to_json(self.has_more),
            "query": to_json(self.query),
            "replacementContinuationToken": to_json(
                self.replacement_continuation_token
            ),
            "useTotalResults": to_json(self.use_total_results),
        }


@dt.dataclass(frozen=True)
class GroupPotentialMembership:
    group: "GroupV2"
    member: "GroupPotentialMember"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "member": to_json(self.member),
            "group": to_json(self.group),
        }


@dt.dataclass(frozen=True)
class GroupPotentialMembershipSearchResponse:
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    results: t.Sequence["GroupPotentialMembership"]
    total_results: int
    use_total_results: bool = dt.field(
        metadata={
            "description": """If useTotalResults is true, then totalResults represents an accurate count.
If False, it does not, and may be estimated/only the size of the current page.
Either way, you should probably always only trust hasMore.
This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one."""
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "results": to_json(self.results),
            "totalResults": to_json(self.total_results),
            "hasMore": to_json(self.has_more),
            "query": to_json(self.query),
            "replacementContinuationToken": to_json(
                self.replacement_continuation_token
            ),
            "useTotalResults": to_json(self.use_total_results),
        }


@dt.dataclass(frozen=True)
class GroupApplicationResponse:
    resolution: "GroupApplicationResolveState"

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "resolution": to_json(self.resolution),
        }


# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas import BungieMembershipType  # noqa: E402
from bungieapi.generated.components.schemas.destiny import (  # noqa: E402
    DestinyProgression,
)
from bungieapi.generated.components.schemas.ignores import IgnoreLength  # noqa: E402
from bungieapi.generated.components.schemas.queries import PagedQuery  # noqa: E402
from bungieapi.generated.components.schemas.user import UserInfoCard  # noqa: E402
from bungieapi.generated.components.schemas.user import UserMembership  # noqa: E402
