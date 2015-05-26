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

import shlex
from SublimeLinter.lint import Linter, persist
import sublime
import os
import string


def get_project_folder():
    proj_file = sublime.active_window().project_file_name()
    if proj_file:
        return os.path.dirname(proj_file)
    # Use current file's folder when no project file is opened.
    return os.path.dirname( sublime.active_window().active_view().file_name() )


def apply_template(s):
    mapping = {
        "project_folder": get_project_folder()
    }
    templ = string.Template(s)
    return templ.safe_substitute(mapping)


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

    defaults = {
        'include_dirs': [],
        'extra_flags': ""
    }

    base_cmd = (
        'clang -fsyntax-only '
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
        result += apply_template( settings.get('extra_flags', '') )

        include_dirs = settings.get('include_dirs', [])

        if include_dirs:
            result += apply_template( ' '.join([' -I ' + shlex.quote(include) for include in include_dirs]) )

        return result + ' -'# read from standard input
