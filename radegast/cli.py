import io
import json
from pathlib import Path

import click
import typing as t
from radegast.generators import get
from .openapi import OpenApi
from .cleanup import reformat_file
from .svarog import forge

T = t.TypeVar("T")


@click.command()
@click.argument("open-api-spec", type=click.File("rt"))
@click.argument("output", type=click.Path())
def generate(open_api_spec: io.BufferedReader, output: Path):
    data = json.load(open_api_spec)
    generator = get("asyncio")
    with open(output, "wt") as f:
        for line in generator.generate(forge(OpenApi, data)):
            f.write(f"{line}\n")

    reformat_file(Path(output))
