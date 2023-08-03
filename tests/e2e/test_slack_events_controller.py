# test_your_app.py
from unittest.mock import patch


@patch("src.controller.slack_events_controller.signature_verifier.is_valid_request", return_value=True)
@patch("src.controller.slack_events_controller.handle_events", return_value=None)
def test_handle_slack_events_success(mock_handle_events, mock_is_valid_request, client):
    mock_event_data = {
        "event": {
            "type": "message",
        }
    }

    # Simulate a POST request with mocked event data
    response = client.post("/slack/events", json=mock_event_data)

    # Assert that the response is as expected
    assert response.status_code == 200
    assert response.data == b""

    # Assert that the mocked methods were called correctly
    mock_is_valid_request.assert_called_once()
    mock_handle_events.assert_called_once_with(mock_event_data["event"])


@patch("src.controller.slack_events_controller.signature_verifier.is_valid_request", return_value=False)
def test_handle_slack_events_signature_failed(mock_is_valid_request, client):
    mock_event_data = {
        "event": {
            "type": "message",
        }
    }

    # Simulate a POST request with mocked event data
    response = client.post("/slack/events", json=mock_event_data)

    # Assert that the response is as expected
    assert response.status_code == 403

    # Assert that the mocked methods were called correctly
    mock_is_valid_request.assert_called_once()
