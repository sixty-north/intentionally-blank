from io import StringIO

from hypothesis import given, strategies

from intentionally_blank import api


def test_format_empty_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["identity"])
        assert len(out_file.getvalue()) == 0


def test_airtravel_empty_unchanged(airtravel_empty_file):
    expected_text = airtravel_empty_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["identity"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


def test_airtravel_ragged_unchanged(airtravel_ragged_file):
    expected_text = airtravel_ragged_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["identity"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


@given(text=strategies.text())
def test_text_is_unchanged(text):
    with StringIO(text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["identity"])
        actual_text = out_file.getvalue()
        assert actual_text == text