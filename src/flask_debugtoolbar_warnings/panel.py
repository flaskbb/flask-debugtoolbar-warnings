# -*- utf-8 -*-
"""
    flask_debugtoolbar_warnings.panel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Warnings tracking panel

    :copyright: (c) 2018 the FlaskBB Team
    :license: MIT, see LICENSE for more details
"""

import os

import jinja2
from flask_debugtoolbar.panels import DebugPanel

from .warnings_manager import WarningsStorage, monkeypatch_warnings


class WarningsPanel(DebugPanel):
    name = "Warnings"

    def __init__(self, *args, **kwargs):
        super(WarningsPanel, self).__init__(*args, **kwargs)
        module_path = os.path.join(os.path.dirname(__file__), "templates")
        self.jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(module_path)
        )

    @property
    def has_content(self):
        return bool(WarningsStorage.count())

    def nav_title(self):
        return "Warnings"

    def nav_subtitle(self):
        count = WarningsStorage.count()
        title = "Warning" if 0 < count < 2 else "Warnings"
        return "{} {}".format(count, title)

    def title(self):
        return "Warnings Captured"

    def url(self):
        return ""

    def content(self):
        warnings = WarningsStorage.pop_all()
        return self.render(
            "warnings-panel.html", {"warnings": warnings}
        )

    def process_request(self, request):
        monkeypatch_warnings()
