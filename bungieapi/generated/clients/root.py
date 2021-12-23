# generated by update to not change manually
from bungieapi.base import BaseClient
from bungieapi.forge import forge
from bungieapi.generated import clients
from bungieapi.generated.components.responses import (
    CEDictionaryOfstringAndstringClientResponse,
    CEListOfGlobalAlertClientResponse,
    DictionaryOfstringAndCoreSystemClientResponse,
)
from bungieapi.generated.components.responses.common.models import (
    CoreSettingsConfigurationClientResponse,
)


class Client(BaseClient):
    async def get_available_locales(
        self,
    ) -> CEDictionaryOfstringAndstringClientResponse:
        """List of available localization cultures."""
        query = None
        result = await self.get(path="/GetAvailableLocales/", query=query)
        return forge(CEDictionaryOfstringAndstringClientResponse, result)

    async def get_common_settings(
        self,
    ) -> CoreSettingsConfigurationClientResponse:
        """Get the common settings used by the Bungie.Net environment."""
        query = None
        result = await self.get(path="/Settings/", query=query)
        return forge(CoreSettingsConfigurationClientResponse, result)

    async def get_user_system_overrides(
        self,
    ) -> DictionaryOfstringAndCoreSystemClientResponse:
        """Get the user-specific system overrides that should be respected
        alongside common systems."""
        query = None
        result = await self.get(path="/UserSystemOverrides/", query=query)
        return forge(DictionaryOfstringAndCoreSystemClientResponse, result)

    async def get_global_alerts(
        self,
        includestreaming: bool,
    ) -> CEListOfGlobalAlertClientResponse:
        """Gets any active global alert for display in the forum banners, help
        pages, etc.

        Usually used for DOC alerts.
        Parameters:
            includestreaming: Determines whether Streaming Alerts are included in results
        """
        query = {"includestreaming": includestreaming}
        result = await self.get(path="/GlobalAlerts/", query=query)
        return forge(CEListOfGlobalAlertClientResponse, result)

    @property
    def app(self) -> clients.app.Client:
        return clients.app.Client(self._session, self._path)

    @property
    def user(self) -> clients.user.Client:
        return clients.user.Client(self._session, self._path)

    @property
    def content(self) -> clients.content.Client:
        return clients.content.Client(self._session, self._path)

    @property
    def forum(self) -> clients.forum.Client:
        return clients.forum.Client(self._session, self._path)

    @property
    def group_v2(self) -> clients.group_v2.Client:
        return clients.group_v2.Client(self._session, self._path)

    @property
    def tokens(self) -> clients.tokens.Client:
        return clients.tokens.Client(self._session, self._path)

    @property
    def destiny2(self) -> clients.destiny2.Client:
        return clients.destiny2.Client(self._session, self._path)

    @property
    def community_content(self) -> clients.community_content.Client:
        return clients.community_content.Client(self._session, self._path)

    @property
    def trending(self) -> clients.trending.Client:
        return clients.trending.Client(self._session, self._path)

    @property
    def fireteam(self) -> clients.fireteam.Client:
        return clients.fireteam.Client(self._session, self._path)

    @property
    def social(self) -> clients.social.Client:
        return clients.social.Client(self._session, self._path)
