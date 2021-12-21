import sys
from pathlib import Path
from isort.api import sort_file

import black as black
import docformatter


def reformat_file(path: Path) -> None:
    docformatter._main(
        ["docformatter", "-i", str(path)], sys.stdin, sys.stderr, sys.stdin
    )
    black.reformat_one(
        src=path,
        fast=False,
        write_back=black.WriteBack.YES,
        mode=black.Mode(),
        report=black.Report(quiet=True),
    )
    sort_file(path, quiet=True)
