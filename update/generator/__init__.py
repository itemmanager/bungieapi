import typing as t
from pathlib import Path

from ..openapi import OpenApi
from .base import generator

GeneratorType = t.Literal["asyncio"]


class Generator(t.Protocol):
    def __call__(self, api: OpenApi) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
        ...


__all__ = ["generator"]
