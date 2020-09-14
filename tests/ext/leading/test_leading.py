from io import StringIO

from hypothesis import strategies, given

from intentionally_blank import api
from intentionally_blank.text import split_on_newlines


def test_format_leading_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["leading"])
        assert len(out_file.getvalue()) == 0


def test_airtravel_leading_unchanged(airtravel_leading_file):
    expected_text = airtravel_leading_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["leading"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text


def test_airtravel_empty_is_converted_to_airtravel_leading(airtravel_empty_file, airtravel_leading_file):
    expected_text = ''.join(airtravel_leading_file.readlines()[:-1])
    before_text = airtravel_empty_file.read()
    with StringIO(before_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["leading"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text
