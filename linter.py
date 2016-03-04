#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ivan Sobolev
# Copyright (c) 2016 Ivan Sobolev
#
# License: MIT
#

"""This module exports the Bemlint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Bemlint(NodeLinter):
    """Provides an interface to bemlint."""

    syntax = ('html', 'txt', 'html+tt2','html+tt3')
    cmd = ('bemlint', '--format', 'compact')
    version_args = '--version'
    version_re = r'v(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.1.0'
    regex = (
        r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) - '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'bem'
