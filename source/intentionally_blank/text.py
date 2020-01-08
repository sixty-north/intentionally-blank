import re

from asq import query

LEADING_PATTERN = r"^(\s*)(.*)$"
LEADING_REGEX = re.compile(LEADING_PATTERN)


def split_indent(line):
    m = LEADING_REGEX.match(line)
    assert m is not None
    indent, text = m.groups()
    return indent, text


def is_blank_line(index, text):
    return len(text) == 0


def strip_lines(text):
    """Remove leading and trailing blank lines."""
    is_blank = lambda line: line.isspace() or not line
    return '\n'.join(
        query(text.splitlines())
            .skip_while(is_blank)
            .reverse()
            .skip_while(is_blank)
            .reverse()
    )

def chomp(s):
    """Remove any trailing carriage-return or newline terminator."""
    if s.endswith("\r\n"): return s[:-2]
    if s.endswith("\n") or s.endswith("\r"): return s[:-1]
    return s