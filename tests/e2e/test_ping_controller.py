"""Tests for ping views."""
from http import HTTPStatus

from flask import url_for


def test_ping(app):

    """Test for ping endpoint."""
    with app.app_context():
        response = app.test_client().get(url_for("ping.main"))
        assert response.status_code == HTTPStatus.OK
