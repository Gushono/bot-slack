"""
Unit tests for the Slack events handling.
"""

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
