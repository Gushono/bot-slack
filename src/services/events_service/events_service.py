import json

from flask import Response

from src.services.events_service.events_strategy import (
    OnMessageStrategy,
    OnAppHomeOpenedStrategy, OnErrorStrategy
)
from src.services.slack_service import SlackService

EVENTS_HANDLERS_STRATEGY = {
    "message": OnMessageStrategy,
    "app_home_opened": OnAppHomeOpenedStrategy,
    "error": OnErrorStrategy
}


def handle_events(event: dict) -> tuple[Response, int]:
    """
    Handle incoming Slack events.

    This function processes incoming Slack events and delegates their handling to specific strategies.

    Args:
        event (dict): The incoming Slack event dictionary.

    Returns:
        tuple[Response, int]: A tuple containing a response object and an HTTP status code.

    Raises:
        ValueError: If the event type is not implemented.
    """
    slack_service = SlackService()

    # Check if the event is from a bot or inside a thread and ignore it
    if slack_service.is_message_from_bot(event) or slack_service.is_message_inside_a_thread(event):
        return Response(), 200

    slack_service.send_slack_message(
        channel="C05KYUZ3LF2",
        text=f"Esse é o evento {json.dumps(event)}",
    )

    events_strategy_handler = EVENTS_HANDLERS_STRATEGY.get(event["type"])
    if not events_strategy_handler:
        raise ValueError(f"Event {event['type']} not implemented.")

    result = events_strategy_handler().execute(event, slack_service)
    if result is not None:
        return result

    return Response(), 200
