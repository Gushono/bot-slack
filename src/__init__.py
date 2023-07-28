"""Flask src creation."""

from flask import Flask

from src.environment import EnvironmentVariables
from src.controller.ping_controller import ping_blueprint
from src.controller.slack_events_controller import slack_events_blueprint

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = [("/", ping_blueprint), ("/", slack_events_blueprint)]


def create_app() -> Flask:
    """Create Flask src."""
    app = Flask(__name__)
    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app
