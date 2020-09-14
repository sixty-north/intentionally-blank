from io import StringIO

from hypothesis import given, strategies

from intentionally_blank import api


def test_format_eof_newline_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        assert len(out_file.getvalue()) == 0


def test_airtravel_without_eof_newline_is_given_eof_newline(airtravel_without_eof_newline_file):
    expected_text = airtravel_without_eof_newline_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        actual_text = out_file.getvalue()
        assert actual_text.endswith("\n")


def test_airtravel_without_eof_newline_is_identical_before_last_character(airtravel_without_eof_newline_file):
    expected_text = airtravel_without_eof_newline_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        actual_text = out_file.getvalue()
        assert actual_text[:-1] == expected_text

def test_airtravel_empty_unchanged_by_eof_newline(airtravel_empty_file):
    expected_text = airtravel_empty_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


def test_airtravel_ragged_unchanged_by_eof_newline_before_last_character(airtravel_ragged_file):
    expected_text = airtravel_ragged_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        actual_text = out_file.getvalue()
        assert actual_text[:-1] == expected_text


@given(text=strategies.text(min_size=1))
def test_eof_newline_always_ends_with_newline(text):
    with StringIO(text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["eof-newline"])
        actual_text = out_file.getvalue()
        assert actual_text.endswith("\n")