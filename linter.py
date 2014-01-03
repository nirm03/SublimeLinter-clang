#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by nirm03
# Copyright (c) 2013 nirm03
#
# License: MIT
#

"""This module exports the Clang plugin class."""

from SublimeLinter.lint import Linter, util, persist


class Clang(Linter):

    """Provides an interface to clang."""

    syntax = ('c', 'c improved', 'c++')
    executable = 'clang'

    # We are missing out on some errors by ignoring multiline messages.
    regex = (
        r'^<stdin>:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>(error|fatal error))|(?P<warning>warning)): '
        r'(?P<message>.+)'
    )
    multiline = False

    line_col_base = (1, 1)
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {
        'include_dirs': [],
        'extra_flags': ""
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None

    base_cmd = (
        'clang -cc1 -fsyntax-only '
        '-fno-caret-diagnostics -fcxx-exceptions -Wall '
    )

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.
        """
        result = self.base_cmd

        if persist.get_syntax(self.view) == 'c++':
            result += ' -x c++ '

        settings = self.get_view_settings()
        result += settings.get('extra_flags')

        include_dirs = settings.get('include_dirs')
        if include_dirs:
            result += ' -I ' + ' -I '.join(settings.get('include_dirs'))

        return result
