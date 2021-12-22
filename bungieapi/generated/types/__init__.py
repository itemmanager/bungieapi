# generated by update to not change manually
import dataclasses as dt
import typing as t
from enum import Enum


class BungieMembershipType(Enum):
    """The types of membership the Accounts system supports.

    This is the external facing enum used in place of the internal-only
    Bungie.SharedDefinitions.MembershipType.
    """

    NONE = 0
    TIGER_XBOX = 1
    TIGER_PSN = 2
    TIGER_STEAM = 3
    TIGER_BLIZZARD = 4
    TIGER_STADIA = 5
    TIGER_DEMON = 10
    BUNGIE_NEXT = 254
    ALL = -1


class BungieCredentialType(Enum):
    """The types of credentials the Accounts system supports.

    This is the external facing enum used in place of the internal-only
    Bungie.SharedDefinitions.CredentialType.
    """

    NONE = 0
    XUID = 1
    PSNID = 2
    WLID = 3
    FAKE = 4
    FACEBOOK = 5
    GOOGLE = 8
    WINDOWS = 9
    DEMON_ID = 10
    STEAM_ID = 12
    BATTLE_NET_ID = 14
    STADIA_ID = 16
    TWITCH_ID = 18


@dt.dataclass(frozen=True)
class SearchResultOfContentItemPublicContract:
    results: t.Sequence["ContentItemPublicContract"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfPostResponse:
    results: t.Sequence["PostResponse"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


BungieMembershipTypeArray = t.Sequence["BungieMembershipType"]


@dt.dataclass(frozen=True)
class SearchResultOfGroupV2Card:
    results: t.Sequence["GroupV2Card"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfGroupMember:
    results: t.Sequence["GroupMember"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfGroupBan:
    results: t.Sequence["GroupBan"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfGroupMemberApplication:
    results: t.Sequence["GroupMemberApplication"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfGroupMembership:
    results: t.Sequence["GroupMembership"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfGroupPotentialMembership:
    results: t.Sequence["GroupPotentialMembership"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyVendorReceiptsComponent:
    data: "DestinyVendorReceiptsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyInventoryComponent:
    data: "DestinyInventoryComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyProfileComponent:
    data: "DestinyProfileComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyPlatformSilverComponent:
    data: "DestinyPlatformSilverComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyKiosksComponent:
    data: "DestinyKiosksComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyPlugSetsComponent:
    data: "DestinyPlugSetsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyProfileProgressionComponent:
    data: "DestinyProfileProgressionComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyPresentationNodesComponent:
    data: "DestinyPresentationNodesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyProfileRecordsComponent:
    data: "DestinyProfileRecordsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyProfileCollectiblesComponent:
    data: "DestinyProfileCollectiblesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyProfileTransitoryComponent:
    data: "DestinyProfileTransitoryComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyMetricsComponent:
    data: "DestinyMetricsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyStringVariablesComponent:
    data: "DestinyStringVariablesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCharacterComponent:
    data: t.Mapping[str, "DestinyCharacterComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyInventoryComponent:
    data: t.Mapping[str, "DestinyInventoryComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent:
    data: t.Mapping[str, "DestinyCharacterProgressionComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent:
    data: t.Mapping[str, "DestinyCharacterRenderComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent:
    data: t.Mapping[str, "DestinyCharacterActivitiesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyKiosksComponent:
    data: t.Mapping[str, "DestinyKiosksComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent:
    data: t.Mapping[str, "DestinyPlugSetsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyBaseItemComponentSetOfuint32:
    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent:
    data: t.Mapping[str, "DestinyItemObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent:
    data: t.Mapping[str, "DestinyItemPerksComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent:
    data: t.Mapping[str, "DestinyPresentationNodesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent:
    data: t.Mapping[str, "DestinyCharacterRecordsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent:
    data: t.Mapping[str, "DestinyCollectiblesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent:
    data: t.Mapping[str, "DestinyStringVariablesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyBaseItemComponentSetOfint64:
    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent:
    data: t.Mapping[str, "DestinyItemObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent:
    data: t.Mapping[str, "DestinyItemPerksComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyItemComponentSetOfint64:
    instances: "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent"
    render_data: "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent"
    stats: "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent"
    sockets: "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent"
    reusable_plugs: "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent"
    plug_objectives: "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent"
    talent_grids: "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent"
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent"
    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent:
    data: t.Mapping[str, "DestinyItemInstanceComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent:
    data: t.Mapping[str, "DestinyItemRenderComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent:
    data: t.Mapping[str, "DestinyItemStatsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent:
    data: t.Mapping[str, "DestinyItemSocketsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent:
    data: t.Mapping[str, "DestinyItemReusablePlugsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent:
    data: t.Mapping[str, "DestinyItemPlugObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent:
    data: t.Mapping[str, "DestinyItemTalentGridComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent:
    data: t.Mapping[str, "DestinyItemPlugComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent:
    data: t.Mapping[str, "DestinyCurrenciesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCharacterComponent:
    data: "DestinyCharacterComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCharacterProgressionComponent:
    data: "DestinyCharacterProgressionComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCharacterRenderComponent:
    data: "DestinyCharacterRenderComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCharacterActivitiesComponent:
    data: "DestinyCharacterActivitiesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCharacterRecordsComponent:
    data: "DestinyCharacterRecordsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCollectiblesComponent:
    data: "DestinyCollectiblesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyCurrenciesComponent:
    data: "DestinyCurrenciesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemComponent:
    data: "DestinyItemComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemInstanceComponent:
    data: "DestinyItemInstanceComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemObjectivesComponent:
    data: "DestinyItemObjectivesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemPerksComponent:
    data: "DestinyItemPerksComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemRenderComponent:
    data: "DestinyItemRenderComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemStatsComponent:
    data: "DestinyItemStatsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemTalentGridComponent:
    data: "DestinyItemTalentGridComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemSocketsComponent:
    data: "DestinyItemSocketsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemReusablePlugsComponent:
    data: "DestinyItemReusablePlugsComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyItemPlugObjectivesComponent:
    data: "DestinyItemPlugObjectivesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyVendorGroupComponent:
    data: "DestinyVendorGroupComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyVendorComponent:
    data: t.Mapping[str, "DestinyVendorComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent:
    data: t.Mapping[str, "DestinyVendorCategoriesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent:
    sale_items: t.Mapping[str, "DestinyVendorSaleItemComponent"]


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent:
    data: t.Mapping[str, "PersonalDestinyVendorSaleItemSetComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyBaseItemComponentSetOfint32:
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent:
    data: t.Mapping[str, "DestinyItemObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent:
    data: t.Mapping[str, "DestinyItemPerksComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyItemComponentSetOfint32:
    instances: "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent"
    render_data: "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent"
    stats: "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent"
    sockets: "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent"
    reusable_plugs: "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent"
    plug_objectives: "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent"
    talent_grids: "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent"
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent"
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent:
    data: t.Mapping[str, "DestinyItemInstanceComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent:
    data: t.Mapping[str, "DestinyItemRenderComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent:
    data: t.Mapping[str, "DestinyItemStatsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent:
    data: t.Mapping[str, "DestinyItemSocketsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent:
    data: t.Mapping[str, "DestinyItemReusablePlugsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent:
    data: t.Mapping[str, "DestinyItemPlugObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent:
    data: t.Mapping[str, "DestinyItemTalentGridComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyVendorComponent:
    data: "DestinyVendorComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SingleComponentResponseOfDestinyVendorCategoriesComponent:
    data: "DestinyVendorCategoriesComponent"
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent:
    data: t.Mapping[str, "DestinyVendorSaleItemComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent:
    data: t.Mapping[str, "DestinyPublicVendorComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent:
    sale_items: t.Mapping[str, "DestinyPublicVendorSaleItemComponent"]


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent:
    data: t.Mapping[str, "PublicDestinyVendorSaleItemSetComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DestinyItemComponentSetOfuint32:
    instances: "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent"
    render_data: "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent"
    stats: "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent"
    sockets: "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent"
    reusable_plugs: "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent"
    plug_objectives: "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent"
    talent_grids: "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent"
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent"
    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent"
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent"


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent:
    data: t.Mapping[str, "DestinyItemInstanceComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent:
    data: t.Mapping[str, "DestinyItemRenderComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent:
    data: t.Mapping[str, "DestinyItemStatsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent:
    data: t.Mapping[str, "DestinyItemSocketsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent:
    data: t.Mapping[str, "DestinyItemReusablePlugsComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent:
    data: t.Mapping[str, "DestinyItemPlugObjectivesComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent:
    data: t.Mapping[str, "DestinyItemTalentGridComponent"]
    privacy: "ComponentPrivacySetting"
    disabled: bool


@dt.dataclass(frozen=True)
class SearchResultOfDestinyEntitySearchResultItem:
    results: t.Sequence["DestinyEntitySearchResultItem"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfTrendingEntry:
    results: t.Sequence["TrendingEntry"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfFireteamSummary:
    results: t.Sequence["FireteamSummary"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class SearchResultOfFireteamResponse:
    results: t.Sequence["FireteamResponse"]
    total_results: int
    has_more: bool
    query: "PagedQuery"
    replacement_continuation_token: str
    use_total_results: bool


@dt.dataclass(frozen=True)
class GlobalAlert:
    alert_key: str
    alert_html: str
    alert_timestamp: str
    alert_link: str
    alert_level: "GlobalAlertLevel"
    alert_type: "GlobalAlertType"
    stream_info: "StreamInfo"


class GlobalAlertLevel(Enum):
    UNKNOWN = 0
    BLUE = 1
    YELLOW = 2
    RED = 3


class GlobalAlertType(Enum):
    GLOBAL_ALERT = 0
    STREAMING_ALERT = 1


@dt.dataclass(frozen=True)
class StreamInfo:
    channel_name: str


from bungieapi.generated.types.components import ComponentPrivacySetting  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.content import ContentItemPublicContract  # noqa: E402
from bungieapi.generated.types.destiny.components.collectibles import (
    DestinyCollectiblesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.collectibles import (
    DestinyProfileCollectiblesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.inventory import (
    DestinyCurrenciesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.inventory import (
    DestinyPlatformSilverComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.items import (
    DestinyItemPlugComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.items import (
    DestinyItemPlugObjectivesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.items import (
    DestinyItemReusablePlugsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.kiosks import (
    DestinyKiosksComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.metrics import (
    DestinyMetricsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.plug_sets import (
    DestinyPlugSetsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.presentation import (
    DestinyPresentationNodesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.profiles import (
    DestinyProfileProgressionComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.profiles import (
    DestinyProfileTransitoryComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.records import (
    DestinyCharacterRecordsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.records import (
    DestinyProfileRecordsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.string_variables import (
    DestinyStringVariablesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.vendors import (
    DestinyPublicVendorComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.vendors import (
    DestinyPublicVendorSaleItemComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.components.vendors import (
    DestinyVendorGroupComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.definitions import (
    DestinyEntitySearchResultItem,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.characters import (
    DestinyCharacterActivitiesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.characters import (
    DestinyCharacterComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.characters import (
    DestinyCharacterProgressionComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.characters import (
    DestinyCharacterRenderComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.inventory import (
    DestinyInventoryComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemInstanceComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemObjectivesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemPerksComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemRenderComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemSocketsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemStatsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.items import (
    DestinyItemTalentGridComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.profiles import (
    DestinyProfileComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.profiles import (
    DestinyVendorReceiptsComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.vendors import (
    DestinyVendorCategoriesComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.vendors import (
    DestinyVendorComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.entities.vendors import (
    DestinyVendorSaleItemComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.responses import (
    PersonalDestinyVendorSaleItemSetComponent,
)  # noqa: E402
from bungieapi.generated.types.destiny.responses import (
    PublicDestinyVendorSaleItemSetComponent,
)  # noqa: E402
from bungieapi.generated.types.fireteam import FireteamResponse  # noqa: E402
from bungieapi.generated.types.fireteam import FireteamSummary  # noqa: E402
from bungieapi.generated.types.forum import PostResponse  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupBan  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupMember  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupMemberApplication  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupMembership  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupPotentialMembership  # noqa: E402
from bungieapi.generated.types.groups_v2 import GroupV2Card  # noqa: E402
from bungieapi.generated.types.queries import PagedQuery  # noqa: E402
from bungieapi.generated.types.trending import TrendingEntry  # noqa: E402
