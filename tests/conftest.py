"""Here are define pytest fixtures, hooks and plugins."""

import pytest

from src import create_app


@pytest.fixture
def app():
    """App fixture."""
    flask_app = create_app()
    flask_app.config["SERVER_NAME"] = "TESTE_SERVER"

    return flask_app
