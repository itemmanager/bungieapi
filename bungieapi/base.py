from enum import Enum

import aiohttp
import typing as t

QueryInput = t.Union[None, str, bool, int, t.Sequence[Enum]]


def clean_query_value(in_: QueryInput) -> str:
    raise NotImplementedError()


class BaseClient:
    def __init__(self, session: aiohttp.ClientSession, path: str) -> None:
        self._session = session
        self._path = path

    def _clean_query(self, query: t.Mapping[str, QueryInput]) -> t.Mapping[str, str]:
        return {k: clean_query_value(v) for k, v in query.items()}

    async def get(self, path: str, query: t.Optional[t.Mapping[str, QueryInput]]) -> t.Mapping[str, t.Any]:
        raise NotImplementedError()

    async def post(self, path: str, query: t.Optional[t.Mapping[str, QueryInput]]) -> t.Mapping[str, t.Any]:
        raise NotImplementedError()
