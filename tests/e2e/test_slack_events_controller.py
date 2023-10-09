"""
Unit tests for the Slack events handling.
"""
import json
import urllib
from unittest.mock import patch

from flask import Response


@patch(
    "src.controller.slack_events_controller.signature_verifier.is_valid_request",
    return_value=True
)
@patch("src.controller.slack_events_controller.handle_events", return_value=None)
def test_handle_slack_events_success(mock_handle_events, mock_is_valid_request, client):
    """
    Test the successful handling of Slack events.

    This test mocks the is_valid_request and handle_events functions to ensure successful handling
    of incoming Slack events. It simulates a POST request with mocked event data and asserts the
    expected response and function calls.

    Args:
        mock_handle_events (Mock): Mock for the handle_events function.
        mock_is_valid_request (Mock): Mock for the is_valid_request function.
        client (FlaskClient): Flask test client.

    Returns:
        None
    """
    mock_event_data = {
        "event": {
            "type": "message",
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/slack/events", json=mock_event_data)

    # Assert that the response is as expected
    assert response.status_code == 200
    assert response.data == b""

    # Assert that the mocked methods were called correctly
    mock_is_valid_request.assert_called_once()
    mock_handle_events.assert_called_once_with(mock_event_data["event"])


@patch(
    "src.controller.slack_events_controller.signature_verifier.is_valid_request",
    return_value=False
)
def test_handle_slack_events_signature_failed(mock_is_valid_request, client):
    """
    Test handling of Slack events with failed signature verification.

    This test mocks the is_valid_request function to simulate a failed signature verification.
    It simulates a POST request with mocked event data and asserts the expected response and
    function calls.

    Args:
        mock_is_valid_request (Mock): Mock for the is_valid_request function.
        client (FlaskClient): Flask test client.

    Returns:
        None
    """
    mock_event_data = {
        "event": {
            "type": "message",
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/slack/events", json=mock_event_data)

    # Assert that the response is as expected
    assert response.status_code == 403

    # Assert that the mocked methods were called correctly
    mock_is_valid_request.assert_called_once()


@patch(
    "src.controller.slack_events_controller.signature_verifier.is_valid_request",
    return_value=True
)
@patch("src.client.slack_client.WebClient.api_call", return_value=None)
@patch("src.client.slack_client.WebClient.chat_postMessage", return_value=None)
def test_handle_slack_events_on_message_success(
        mock_chat_post_message, mock_api_call, mock_is_valid_request, client
):
    mock_event_data = {
        "event": {
            "type": "message",
            "text": "hello",
            "channel": "C1234567890",
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/slack/events", json=mock_event_data)

    # Assert that the response is as expected
    assert response.status_code == 200

    # Assert that the mocked methods were called correctly
    mock_is_valid_request.assert_called_once()


def test_handle_interactive_endpoint_success_ignore_payload_without_user(client):
    mock_payload = {
        "payload": {
            "user": None,
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/interactive-endpoint", json=mock_payload, headers=headers)

    # Assert that the response is as expected
    assert response.status_code == 200


@patch("src.client.slack_client.WebClient.api_call", return_value=None)
@patch("src.client.slack_client.WebClient.chat_postMessage", return_value=None)
def test_handle_interactive_endpoint_success(mock_post_message, mock_api_call, client):
    mock_payload = {
        "payload": {
            "user": {
                "id": "U0123456",
            },
            "message": {
                "thread_ts": "1234567890.123456",
            },
            "channel": {
                "id": "C1234567890",
            },
            "actions": [
                {
                    "action_id": "ssdlc_action",
                    "value": "ssdlc_value",
                },
            ],
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/interactive-endpoint", json=mock_payload)
    # Assert that the response is as expected
    assert response.status_code == 200


@patch("src.client.slack_client.WebClient.api_call", return_value=None)
@patch("src.client.slack_client.WebClient.chat_postMessage", return_value=True)
def test_handle_interactive_endpoint_success_returning_something(mock_post_message, mock_api_call, client):
    mock_payload = {
        "payload": {
            "user": {
                "id": "U0123456",
            },
            "message": {
                "thread_ts": "1234567890.123456",
            },
            "channel": {
                "id": "C1234567890",
            },
            "actions": [
                {
                    "action_id": "ssdlc_action",
                    "value": "ssdlc_value",
                },
            ],
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/interactive-endpoint", json=mock_payload)

    # Assert that the response is as expected
    assert response.status_code == 200


def test_handle_interactive_endpoint_failed_with_unknown_strategy(client):
    mock_payload = {
        "payload": {
            "user": {
                "id": "U0123456",
            },
            "actions": [
                {
                    "action_id": "unknown_action_id",
                    "value": "unknown_action_value",
                },
            ],
        }
    }

    # Simulate a POST request with mocked event data
    response: Response = client.post("/interactive-endpoint", json=mock_payload)

    # Assert that the response is as expected
    assert response.status_code == 500
