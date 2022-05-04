from io import StringIO

from intentionally_blank import api


def test_format_remove_trailing_lines_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing-lines"])
        assert len(out_file.getvalue()) == 0


def test_remove_trailing_lines_airtravel_empty_is_unchanged_example(airtravel_empty_file):
    expected_text = airtravel_empty_file.read()
    with StringIO(expected_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing-lines"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text

def test_airtravel_with_trailing_empty_lines_is_converted_to_airtravel_empty(airtravel_with_trailing_empty_lines_file, airtravel_empty_file):
    expected_text = ''.join(airtravel_empty_file.readlines())
    before_text = airtravel_with_trailing_empty_lines_file.read()
    with StringIO(before_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing-lines"])
        actual_text = out_file.getvalue()
        assert actual_text == expected_text

def test_airtravel_with_trailing_empty_lines_last_line_is_not_empty(airtravel_with_trailing_empty_lines_file, airtravel_empty_file):
    before_text = airtravel_with_trailing_empty_lines_file.read()
    with StringIO(before_text) as in_file, StringIO() as out_file:
        api.format_from_file_to_file(in_file, out_file, format_names=["remove-trailing-lines"])
        actual_text = out_file.getvalue()
        assert len(actual_text.splitlines(keepends=True)[-1].strip()) != 0
