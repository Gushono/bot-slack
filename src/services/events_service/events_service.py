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
    # "error": ErrorStrategy,
}


def handle_events(event: dict) -> tuple[Response, int]:
    slack_service = SlackService()
    if slack_service.is_message_from_bot(event):
        return Response(), 200

    if slack_service.is_message_inside_a_thread(event):
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


def handle_error(err):
    print("ERROR: " + str(err))
