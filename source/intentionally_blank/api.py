import sys

import logging

from functools import reduce

from intentionally_blank.formatter import create_formatter, formatter_names
from intentionally_blank.les_iterables import ensure_contains

logger = logging.getLogger(__name__)

DEFAULT_TAB_SIZE = 8

def format(in_file, out_file, format_names, tab_size=None):
    tab_size = tab_size or DEFAULT_TAB_SIZE
    formatters = [create_formatter(format_name, tab_size) for format_name in ensure_contains(format_names, "identity")]
    
    logger.debug("formatters = %s", formatters)
    
    out_file.writelines(
        reduce(
            lambda lines, formatter: formatter.format(lines),
            formatters,
            in_file
        )
    )

def list_formatters(file=None):
    file = file or sys.stdout
    for name in formatter_names():
        print(name, file=file)
        
        
def describe_formatter(format_name, file=None):
    file = file or sys.stdout
    formatter = create_formatter(format_name)
    print(formatter.describe(), file=file)
