from io import StringIO

from intentionally_blank import api


def test_format_visible_with_empty_string():
    with StringIO() as in_file, StringIO() as out_file:
        api.format(in_file, out_file, format_names=["visible"])
        assert len(out_file.getvalue()) == 0
