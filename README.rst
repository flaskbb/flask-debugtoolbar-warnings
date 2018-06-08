flask-debugtoolbar-warnings
===========================

Adds warning support for Flask-Debugtoolbar

Installation
~~~~~~~~~~~~

``flask-debugtoolbar-warnings`` is available on `pypi <https://pypi.org/project/flask-debugtoolbar-warnings/>`_
and installable with::

    pip install flask-debugtoolbar-warnings

This package supports Python 2.7, 3.4, 3.5, 3.6 (and presumably Python 3.7
and the pypy versions of these Python versions, though it is untested).

.. note::

   If you are installing this package outside of a virtual environment
   consider installing it with ``pip install --user`` rather than using
   sudo or adminstrator privileges to avoid installing it into your
   system Python.


Usage
~~~~~

After installing this package, register it into the ``flask-debugtoolbar`` loader
by setting the ``DEBUG_TB_PANELS`` configuration variable before calling
``init_app`` on the DebugToolbar object::

    app.config['DEBUG_TB_PANELS'] = [
        'flask_debugtoolbar_warnings.WarningsPanel'
    ]

.. warning::

    By setting this variable it implicity disables the other panels that are
    enabled by default, if you wish to keep those enabled set this variable
    with them set as well::

        app.config['DEBUG_TB_PANELS'] = [
            'flask_debugtoolbar.panels.versions.VersionDebugPanel',
            'flask_debugtoolbar.panels.timer.TimerDebugPanel',
            'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
            'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
            'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
            'flask_debugtoolbar.panels.template.TemplateDebugPanel',
            'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
            'flask_debugtoolbar.panels.logger.LoggingPanel',
            'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
            'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
            'flask_debugtoolbar_warnings.WarningsPanel'
        ]

After the first request through your application, this panel will begin
intercepting all warnings that are not ignored or already filtered by
being set to ``once`` or ``module``, or have been set to ``error`` (these
throw exceptions rather than pass fully through the warning machinery).


You may view these warnings in the DebugToolbar side panel under the Warnings
section. The warnings panel will display the category (e.g. what kind of warning),
filename, line number, message and source (if provided).
