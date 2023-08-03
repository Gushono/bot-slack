"""Here are define pytest fixtures, hooks and plugins."""

import pytest

from src import create_app


@pytest.fixture
def app():
    app = create_app()  # Create your Flask app instance here
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
