import json

from flask import Blueprint, request, Response
from slackeventsapi import SlackEventAdapter

from src.client.slack_client import SlackClient
from src.environment import env
from src.services.interactive_service.interactive_service import handle_actions, handle_view_flow
from src.services.interactive_service.interactive_slack_blocks import get_block_initial_message
from src.services.slack_service import WelcomeService

slack_events_blueprint = Blueprint('slack_events', __name__)

# Our src's Slack Event Adapter for receiving actions via the Events API
slack_events_adapter = SlackEventAdapter(env.get_signing_secret(), "/slack/events", slack_events_blueprint)


# Create a SlackClient for your bot to use for Web API requests


# Example responder to bot mentions
@slack_events_adapter.on("app_mention")  # pragma: no cover
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
@slack_events_adapter.on("message")
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

    # if event['text'].lower() == "start":
    #     send_welcome_message(f'@{user}', user=user, slack_client=slack_client.client, payload=event)
    #     return
    # else:
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
        #
        # if payload['view']['callback_id'] == 'button_ok':
        #     subject, message = format_values_slack(payload['view']['state']['values'])
        #     slack_client.client.chat_postMessage(
        #         channel="#bot_duvidas",
        #         blocks=[
        #             {
        #                 "type": "section",
        #                 "text": {
        #                     "type": "mrkdwn",
        #                     "text": f"*O usuário: {user['username']} enviou a seguinte duvida:* \n"
        #                 }
        #             },
        #             {
        #                 "type": "divider"
        #             },
        #             {
        #                 "type": "section",
        #                 "text": {
        #                     "type": "mrkdwn",
        #                     "text": f"> Subject: {subject.upper()}\n"
        #                             f"> Message: {message}"
        #                 }
        #
        #             },
        #             {
        #                 "type": "divider"
        #             }
        #         ]
        #
        #     )
        #
        #     slack_client.client.chat_postMessage(
        #         channel=user['id'],
        #         text="A mensagem chegou para nossos analistas, em breve alguém te ajudará",
        #     )
        #
        # return Response(), 200

    print(payload)
    return {"opa": "opa"}, 200


@slack_events_adapter.on("app_home_opened")
def app_home_openned(event_data):  # pragma: no cover
    print(event_data)
    message = event_data["event"]
    # channel = message["channel"]
    user = message["user"]

    slack_client = SlackClient()

    welcome = WelcomeService(user, user=user, slack_client=slack_client.client)
    home_page = welcome.get_home_page()

    slack_client.client.views_publish(
        **home_page
    )

    return Response(home_page), 200


# Error events
@slack_events_adapter.on("error")
def error_handler(err):  # pragma: no cover
    print("ERROR: " + str(err))


def format_values_slack(values: dict):  # pragma: no cover
    subject = values['input_select']['static_select-action']['selected_option']['value'].lower()
    message = values['block_id']['input_question']['value']

    return subject, message
