import typing as t
from pathlib import Path

from .asyncio import asyncio_generator
from ..openapi import OpenApi

GeneratorType = t.Literal["asyncio"]


class Generator(t.Protocol):
    def __call__(self, api: OpenApi) -> t.Iterator[t.Tuple[Path, t.Iterator[str]]]:
        ...


def get(type: GeneratorType) -> Generator:
    return asyncio_generator
