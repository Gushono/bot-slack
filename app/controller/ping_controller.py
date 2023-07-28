"""Module with ping endpoint."""
import logging

import newrelic.agent
from flask import Blueprint

ping_blueprint = Blueprint("ping", __name__)

logger = logging.getLogger(__name__)


@ping_blueprint.route("/ping")
def main() -> str:
    """Ping endpoint, used to know if the app is up."""
    newrelic.agent.ignore_transaction(flag=True)

    return "pong"
