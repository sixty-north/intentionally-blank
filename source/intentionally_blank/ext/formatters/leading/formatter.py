from intentionally_blank.formatter import Formatter
from intentionally_blank.les_iterables import partition_tail
from intentionally_blank.text import split_indent, is_partitioned_line_blank


class LeadingFormatter(Formatter):
    """Blank lines have leading whitespace equal to that on the previous non-blank line.
    """

    def format(self, lines):
        """
        Args:
            lines: An iterable series of strings, each with a newline terminator.

        Yields:
            An iterable series of strings, each with a newline terminator.
        """
        head, tail = partition_tail(lines, 1)

        # Process all but the last line
        active_indent = ""
        for line in head:
            indent, text = split_indent(line)
            if not is_partitioned_line_blank(indent, text):
                yield line
                active_indent = indent
            else:
                assert line.endswith("\n")
                yield f"{active_indent}\n"

        # tail will contain at most one line
        for line in tail:
            indent, text = split_indent(line)
            if not is_partitioned_line_blank(indent, text):
                yield line
            else:
                end = "\n" if line.endswith("\n") else ""
                if len(indent) != 0:
                    yield f"{active_indent}{end}"
                else:
                    yield end
