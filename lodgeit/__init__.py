"""
    lodgeit
    ~~~~~~~

    The lodgeit pastebin.

    :copyright: 2007 by Armin Ronacher.
    :license: BSD
"""

import subprocess

try:
    lodgeit_version = subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:7]
except Exception:
    lodgeit_version = ""
