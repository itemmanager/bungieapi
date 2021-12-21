from os import listdir
from pathlib import Path
from radegast.cli import generate
import pytest
from click.testing import CliRunner

examples_dir = Path(__file__).parent / "examples"


@pytest.mark.parametrize("path", listdir(examples_dir))
def test_from_directories(path):
    runner = CliRunner()
    root_dir = examples_dir / path

    result = runner.invoke(
        generate, [str(root_dir / "in.json"), str(root_dir / "out.py")]
    )
    assert result.exception is None

    assert open(root_dir / "out.py").read() == open(root_dir / "expected.py").read()
