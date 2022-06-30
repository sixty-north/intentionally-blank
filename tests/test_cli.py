from click.testing import CliRunner
from intentionally_blank.cli import cli

def test_list_formats_exits_with_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["list-formats"])
    assert result.exit_code == 0


def test_list_formatters_prints_newline_separated_strings():
    runner = CliRunner()
    result = runner.invoke(cli, ["list-formats"])
    output_lines = result.output.splitlines(keepends=False)
    assert len(output_lines) > 0
    assert all(len(line.split()) == 1 for line in output_lines)


def test_format_issue_2(flatten_010_filepath, tmp_path):
    runner = CliRunner()
    result = runner.invoke(cli, [
        "format",
        "--format=empty",
        "--format=eof-newline",
        str(flatten_010_filepath),
        str(tmp_path / "output.py"),
    ])
    assert result.exit_code == 0
