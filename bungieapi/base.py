import aiohttp


class BaseClient:
    def __init__(self, session: aiohttp.ClientSession, path: str) -> None:
        self._session = session
        self._path = path
