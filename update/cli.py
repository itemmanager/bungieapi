import json
import typing as t
import urllib.request
from pathlib import Path

import click

from .forge import forge
from .generator import generator
from .openapi import OpenApi


T = t.TypeVar("T")

OPEN_API_SPEC_URL = (
    "https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json"
)

PROJECT_ROOT = Path(__file__).parent.parent
OPEN_API_SPEC_PATH = PROJECT_ROOT / "source" / "openapi.json"
DEST_DIR = PROJECT_ROOT / "bungieapi" / "generated"


def download_url(source: str, dest: Path) -> None:
    with urllib.request.urlopen(urllib.request.Request(source)) as response:
        with open(dest, "wb") as f:
            f.write(response.read())


@click.command()
@click.option("--fetch/--no-fetch", type=click.BOOL, default=False)
def generate(fetch: bool) -> None:
    if fetch:
        download_url(OPEN_API_SPEC_URL, OPEN_API_SPEC_PATH)
    assert Path(OPEN_API_SPEC_PATH).exists()

    data = json.load(open(OPEN_API_SPEC_PATH))

    open_api = forge(OpenApi, data)

    for file_name, file_generator in generator(open_api):
        output = DEST_DIR / file_name
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "wt") as f:
            f.writelines((f"{line}\n" for line in file_generator))
