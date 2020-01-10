from intentionally_blank.formatter import Formatter
from intentionally_blank.text import split_indent, is_blank_line


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
        active_indent = ""
        for line in lines:
            indent, text = split_indent(line)
            if not is_blank_line(indent, text):
                yield line
                active_indent = indent
            else:
                end = "\n" if line.endswith("\n") else ""
                yield f"{active_indent}{end}"
