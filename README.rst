Intentionally Blank
===================

Canonicalise the leading indentation of blank lines in text files.

Synopsis
--------

For the purposes of this tool, a "blank line" is a line containing only whitespace characters.

To have blank lines use the same leading whitespace intent and the most recent non-blank line, use
``--format=leading``::

  $ intentionally-blank format --format=leading infile.txt outfile.txt


To have blank lines be completely empty save for the terminating newline sequence, use
``--format=empty``::

  $ intentionally-blank format --format=empty infile.txt outfile.txt
