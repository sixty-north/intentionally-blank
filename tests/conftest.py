from pathlib import Path

import pytest

DATA_DIRPATH = Path(__file__).parent / "data"


@pytest.fixture()
def airtravel_empty_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_empty.py"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f
        
        
@pytest.fixture()
def airtravel_ragged_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_ragged.py"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f
        
        
@pytest.fixture()
def airtravel_without_eof_newline_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_without_eof_newline.py"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f
        
        
@pytest.fixture()
def airtravel_leading_file():
    airtravel_filepath = DATA_DIRPATH / "airtravel_leading.py"
    with open(airtravel_filepath, "rt", encoding="utf8") as f:
        yield f
