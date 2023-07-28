"""Here are define pytest fixtures, hooks and plugins."""

import pytest

from app import create_app


@pytest.fixture
def app():
    """App fixture."""
    flask_app = create_app()
    flask_app.config["SERVER_NAME"] = "TESTE_SERVER"

    return flask_app
