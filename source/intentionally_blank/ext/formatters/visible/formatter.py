from intentionally_blank.formatter import Formatter
from intentionally_blank.text import split_indent, is_blank_line


class VisibleWhitespaceFormatter(Formatter):
    """Display whitespace using visible characters. Fixed tab size of eight.
    """
    
    def format(self, lines):
        """
        Args:
            lines: An iterable series of strings, each with a newline terminator.
        
        Yields:
            An iterable series of strings, each with a newline terminator.
        """
        return map(transliterate_whitespace, lines)


def transliterate_whitespace(text, tab_size=8):
    return text.translate(str.maketrans({" ": "␣", "\t": "→" * tab_size, "\n": "↵\n"}))