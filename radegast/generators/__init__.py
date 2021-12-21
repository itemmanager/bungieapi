import typing as t

from .asyncio import AsyncioGenerator
from ..openapi import OpenApi

GeneratorType: t.TypeAlias = t.Literal["asyncio"]


class Generator(t.Protocol):
    def generate(self, api: OpenApi) -> t.Sequence[str]:
        ...


def get(type: GeneratorType) -> Generator:
    return AsyncioGenerator()
