# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class IEnumerableOfApplicationClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["Application"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfGetCredentialTypesForAccountClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["GetCredentialTypesForAccountResponse"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfUserThemeClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["UserTheme"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfContentItemPublicContractClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfContentItemPublicContract"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class IReadOnlyCollectionOfContentItemPublicContractClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Any
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class int64ClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: int
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfTagClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["TagResponse"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class CEListOfForumRecruitmentDetailClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["ForumRecruitmentDetail"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class DictionaryOfint32AndstringClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Mapping[str, str]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfGroupThemeClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["GroupTheme"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class booleanClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: bool
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfGroupV2CardClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["GroupV2Card"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class CEListOfGroupOptionalConversationClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["GroupOptionalConversation"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class int32ClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: int
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfGroupMemberClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfGroupMember"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfGroupBanClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfGroupBan"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfGroupMemberApplicationClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfGroupMemberApplication"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfEntityActionResultClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["EntityActionResult"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class CEListOfPartnerOfferSkuHistoryClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["PartnerOfferSkuHistoryResponse"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class IEnumerableOfUserInfoCardClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["UserInfoCard"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ReadOnlyDictionaryOfstringAndDestinyHistoricalStatsDefinitionClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Mapping[str, "DestinyHistoricalStatsDefinition"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class ListOfDestinyClanAggregateStatClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["DestinyClanAggregateStat"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class DictionaryOfuint32AndDestinyPublicMilestoneClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Mapping[str, "DestinyPublicMilestone"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfTrendingEntryClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfTrendingEntry"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfFireteamSummaryClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfFireteamSummary"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class SearchResultOfFireteamClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: "SearchResultOfFireteamResponse"
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class CEDictionaryOfstringAndstringClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Mapping[str, str]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class DictionaryOfstringAndCoreSystemClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Mapping[str, "CoreSystem"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


@dt.dataclass(frozen=True)
class CEListOfGlobalAlertClientResponse:
    error_code: "PlatformErrorCodes"
    error_status: str
    message: str
    message_data: t.Mapping[str, str]
    response: t.Sequence["GlobalAlert"]
    throttle_seconds: int
    detailed_error_trace: t.Optional[str] = None


from bungieapi.generated.components.schemas import GlobalAlert  # noqa: E402
from bungieapi.generated.components.schemas import SearchResultOfGroupBan  # noqa: E402
from bungieapi.generated.components.schemas import (  # noqa: E402
    SearchResultOfContentItemPublicContract,
    SearchResultOfFireteamResponse,
    SearchResultOfFireteamSummary,
    SearchResultOfGroupMember,
    SearchResultOfGroupMemberApplication,
    SearchResultOfTrendingEntry,
)

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.components.schemas.applications import (
    Application,
)  # noqa: E402
from bungieapi.generated.components.schemas.common.models import (
    CoreSystem,
)  # noqa: E402
from bungieapi.generated.components.schemas.config import GroupTheme  # noqa: E402
from bungieapi.generated.components.schemas.config import UserTheme  # noqa: E402
from bungieapi.generated.components.schemas.destiny.historical_stats import (
    DestinyClanAggregateStat,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.historical_stats.definitions import (
    DestinyHistoricalStatsDefinition,
)  # noqa: E402
from bungieapi.generated.components.schemas.destiny.milestones import (
    DestinyPublicMilestone,
)  # noqa: E402
from bungieapi.generated.components.schemas.entities import (
    EntityActionResult,
)  # noqa: E402
from bungieapi.generated.components.schemas.exceptions import (
    PlatformErrorCodes,
)  # noqa: E402
from bungieapi.generated.components.schemas.forum import (
    ForumRecruitmentDetail,
)  # noqa: E402
from bungieapi.generated.components.schemas.groups_v2 import GroupV2Card  # noqa: E402
from bungieapi.generated.components.schemas.groups_v2 import (
    GroupOptionalConversation,
)  # noqa: E402
from bungieapi.generated.components.schemas.tags.models.contracts import (
    TagResponse,
)  # noqa: E402
from bungieapi.generated.components.schemas.tokens import (
    PartnerOfferSkuHistoryResponse,
)  # noqa: E402
from bungieapi.generated.components.schemas.user import UserInfoCard  # noqa: E402
from bungieapi.generated.components.schemas.user.models import (
    GetCredentialTypesForAccountResponse,
)  # noqa: E402
