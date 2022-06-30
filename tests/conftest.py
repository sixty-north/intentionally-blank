from pathlib import Path

import pytest

DATA_DIRPATH = Path(__file__).parent / "data"


@pytest.fixture()
def airtravel_empty_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_empty.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def airtravel_ragged_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_ragged.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def airtravel_without_eof_newline_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_without_eof_newline.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def airtravel_leading_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_leading.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def airtravel_trailing_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_trailing.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def airtravel_with_trailing_empty_lines_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_with_trailing_empty_lines.py.txt"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f


@pytest.fixture()
def flatten_010_filepath() -> Path:
    return DATA_DIRPATH/ "flatten_010.py"