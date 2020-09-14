from io import StringIO

import pytest

from intentionally_blank import api


def test_format_visible_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["visible"])
        assert len(out_file.getvalue()) == 0


@pytest.mark.skip("Godkjenn not ready")
def test_format_visible(airtravel_ragged_file, godkjenn):
    with StringIO() as out_file:
        api.format_from_file_to_file(airtravel_ragged_file, out_file, format_names=["visible"])
        actual_text = out_file.getvalue()
        godkjenn.verify(actual_text.encode("utf-8"))
