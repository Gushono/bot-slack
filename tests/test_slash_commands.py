from http import HTTPStatus
from unittest import mock

from flask import url_for

from app.services.slack_service import SlackService


@mock.patch.object(SlackService, "publish_message")
def test_echo_welcome(slack_service_mock, app):
    slack_service_mock.return_value = None
    with app.app_context():
        response = app.test_client().post(url_for("slack_events.principais_duvidas"), data=dict(user_id="123"))
        assert response.status_code == HTTPStatus.OK
        assert response.status_code == 200
