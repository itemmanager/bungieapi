import sys
from pathlib import Path

import autoflake  # type: ignore
import black as black
import docformatter  # type: ignore
from isort.api import sort_file


def reformat_file(path: Path) -> None:
    docformatter._main(
        ["docformatter", "-i", str(path)], sys.stdin, sys.stderr, sys.stdin
    )
    autoflake._main(
        ["autoflake", "--in-place", "--remove-all-unused-imports", str(path)],
        sys.stdin,
        sys.stderr,
    )
    sort_file(path, quiet=True)
    black.reformat_one(
        src=path,
        fast=False,
        write_back=black.WriteBack.YES,
        mode=black.Mode(),
        report=black.Report(quiet=True),
    )
