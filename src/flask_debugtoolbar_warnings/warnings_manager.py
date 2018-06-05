# -*- coding: utf-8 -*-
"""
    flask_debugtoolbar_warnings.warnings_manager
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: (c) 2018 the FlaskBB Team
    :license: MIT, see LICENSE for more details
"""

import threading
import warnings
from collections import defaultdict, deque

__all__ = ("WarningsStorage", "monkeypatch_warnings")

__patched = False


class WarningsStorage(object):
    _warnings = defaultdict(list)

    @classmethod
    def push(cls, warning):
        cls._warnings[threading.currentThread()].append(warning)

    @classmethod
    def get(cls):
        return cls._warnings[threading.currentThread()][:]

    @classmethod
    def pop_all(cls):
        return cls._warnings.pop(threading.currentThread(), [])

    @classmethod
    def count(cls):
        return len(cls._warnings[threading.currentThread()])


def monkeypatch_warnings(module=warnings):
    global __patched
    if __patched:
        return

    __patched = True

    module._showwarnmsg_impl = WarningsStorage.push
    module.showwarning = module._showwarning_orig
