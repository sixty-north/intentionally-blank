from io import StringIO

from hypothesis import given, strategies, example

from intentionally_blank import api
from intentionally_blank.text import split_on_newlines


def test_format_empty_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format(in_file, out_file, format_names=["empty"])
        assert len(out_file.getvalue()) == 0


def test_airtravel_empty_is_unchanged_example(airtravel_empty_file):
    expected_text = airtravel_empty_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format(in_file, out_file, format_names=["empty"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text
        
        
def test_airtravel_ragged_(airtravel_ragged_file):
    with StringIO() as out_file:
        api.format(airtravel_ragged_file, out_file, format_names=["empty"])
        actual_text = out_file.getvalue()
        actual_lines = actual_text.splitlines(keepends=True)
        assert all(line == "\n" for line in actual_lines if len(line.strip()) == 0)
       
        
@given(text=strategies.text())
def test_blank_lines_are_empty(text):
    with StringIO(text) as in_file, StringIO() as out_file:
        api.format(in_file, out_file, format_names=["empty"])
        actual_text = out_file.getvalue()
        actual_lines = split_on_newlines(actual_text, keepends=True)
        assert all(line == "\n" for line in actual_lines if len(line.strip()) == 0)
