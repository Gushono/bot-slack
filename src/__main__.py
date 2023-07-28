"""Run flask src."""

# pylint: disable=wrong-import-position

import os

import newrelic.agent

from src import create_app

# Initialize newrelic agent before importing anything else
# The newrelic config file is hardcoded because we can't import anything before this :-(
# newrelic.agent.initialize("{}/newrelic.ini".format(os.getcwd()))

# from . import create_app

app = create_app()

if __name__ == "__main__":  # Only in dev
    app.run(host="0.0.0.0", port=8080)  # nosec
