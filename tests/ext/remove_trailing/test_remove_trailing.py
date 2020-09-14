from io import StringIO

from hypothesis import given, strategies

from intentionally_blank import api
from intentionally_blank.text import split_on_newlines


def test_format_remove_trailing_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing"])
        assert len(out_file.getvalue()) == 0


def test_airtravel_empty_is_unchanged_example(airtravel_empty_file):
    expected_text = airtravel_empty_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


def test_airtravel_trailing(airtravel_trailing_file):
    with StringIO() as out_file:
        api.format_from_file_to_file(airtravel_trailing_file, out_file, format_names=["remove-trailing"])
        actual_text = out_file.getvalue()
        actual_lines = actual_text.splitlines(keepends=False)
        assert all(line == line.rstrip() for line in actual_lines)


def test_airtravel_trailing_is_converted_to_airtravel_empty(airtravel_trailing_file, airtravel_empty_file):
    expected_text = ''.join(airtravel_empty_file.readlines())
    before_text = airtravel_trailing_file.read()
    with StringIO(before_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


@given(text=strategies.text())
def test_blank_lines_are_empty(text):
    with StringIO(text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing"])
        actual_text = out_file.getvalue()
        actual_lines = split_on_newlines(actual_text, keepends=True)
        assert all(line == "\n" for line in actual_lines if len(line.strip()) == 0)
