import subprocess
from pathlib import Path


def reformat_directory(path: Path) -> None:
    subprocess.check_call(
        ["docformatter", str(path), "-r", "-i"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        ["autoflake", "--remove-all-unused-imports", "-i", "-r", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        ["isort", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    subprocess.check_call(
        ["black", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
