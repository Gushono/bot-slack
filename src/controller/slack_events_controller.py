import json

from flask import Blueprint, request, Response, jsonify
from slack_sdk.signature import SignatureVerifier

from src.client.slack_client import SlackClient
from src.environment import env
from src.services.interactive_service.actions_slack_blocks import get_block_initial_message
from src.services.interactive_service.interactive_service import handle_actions, handle_view_flow
from src.services.interactive_service.views_strategy import HomeStrategy
from src.services.slack_service import SlackService

slack_events_blueprint = Blueprint('slack_events', __name__)

# Our src's Slack Event Adapter for receiving actions via the Events API
signature_verifier = SignatureVerifier(env.get_signing_secret())


# slack_events_adapter = SlackEventAdapter(env.get_signing_secret(), "/slack/events", slack_events_blueprint)

@slack_events_blueprint.route("/slack/events", methods=["POST"])
def handle_slack_events():
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return jsonify({"error": "Invalid request"}), 403

    events_handlers = {
        "message": handle_message,
        "app_mention": handle_mentions,
        "app_home_opened": handle_app_home_opened

    }

    data = request.get_json()
    print("this is the value")
    print(data)
    print("this is the data type")
    print(data)

    slack_service = SlackService()

    bot_id = slack_service._slack_client.client.api_call("auth.test")["user_id"]
    event_type = data.get("type")
    if "event" in data and "text" in data["event"]:
        handler = events_handlers.get(event_type)

        if not handler:
            raise ValueError(f"Handler for event {event_type} not implemented.")

        user = data["event"].get("user")

        if not user or user == bot_id:
            return Response(), 200

        event = data["event"]
        slack_service.send_slack_message(
            channel="C04GL827WKX",
            text=f"This is the event: {json.dumps(event)}",
        )

        result = handler(data)
        print(result)

        return Response(), 200

    slack_service.send_slack_message(
        channel="C04GL827WKX",
        text=f"This is the event OUT OF EVENT: {json.dumps(data)}",
    )

    return Response(), 200


# Create a SlackClient for your bot to use for Web API requests


# Example responder to bot mentions
# @slack_events_adapter.on("app_mention")  # pragma: no cover
def handle_mentions(event_data):
    print("this is the event")
    print(event_data)
    # slack_client = SlackClient()
    # event = event_data["event"]
    # slack_client.send_message(
    #     channel=event["channel"],
    #     message=f"You said:\n>{event['text']}",
    # )


# Example responder to greetings
# @slack_events_adapter.on("message")
def handle_message(event_data):
    slack_client = SlackClient()

    event = event_data["event"]
    user = event.get("user")

    print(event)

    bot_id = slack_client.client.api_call("auth.test")["user_id"]

    if not user or user == bot_id:
        return

    allowed_channels = ["C04GL827WKX"]

    if event.get("channel") is not None and event.get("channel") not in allowed_channels:
        print(event.get("channel"))
        print("Not allowed channel")
        return Response(), 200
    print("this is the event")
    print(event)

    initial_message = get_block_initial_message()
    ts_thread = event.get("ts")
    slack_client.client.chat_postMessage(
        thread_ts=ts_thread,
        channel=event["channel"],
        text=event['text'],
        blocks=initial_message['blocks']
    )


@slack_events_blueprint.route("/interactive-endpoint", methods=["POST"])
def echo_interactive():  # pragma: no cover
    payload = json.loads(request.form['payload'])
    if not payload["user"]:
        return Response(), 200

    # Actions flow
    if payload.get("actions") is not None:
        result = handle_actions(payload)
        if result is not None:
            return Response(), 200

    # View Flow
    if payload.get("view") is not None:
        result = handle_view_flow(payload)
        if result is not None:
            return Response(), 200

    print(payload)
    return {"opa": "opa"}, 200


#
# @slack_events_adapter.on("app_home_opened")
def handle_app_home_opened(event_data):
    print(event_data)
    message = event_data["event"]

    response = HomeStrategy().execute(payload=message, slack_service=SlackService())

    return Response(response), 200


# Error events
# @slack_events_adapter.on("error")
def error_handler(err):  # pragma: no cover
    print("ERROR: " + str(err))
