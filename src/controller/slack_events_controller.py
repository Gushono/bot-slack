import json

from flask import Blueprint, request, Response
from slackeventsapi import SlackEventAdapter

from src.client.slack_client import SlackClient
from src.environment import env
from src.services.principais_duvidas_service import build_markdown_text_for_principais_duvidas, send_welcome_message, \
    get_block_initial_message, get_block_secure_code_warrior, get_blocks_links_secure_code_warriors, \
    get_blocks_send_messages_to_analysts, get_blocks_dashboard, get_direct_thread_link
from src.services.slack_service import WelcomeService, SlackService

slack_events_blueprint = Blueprint('slack_events', __name__)

# Our src's Slack Event Adapter for receiving actions via the Events API
slack_events_adapter = SlackEventAdapter(env.get_signing_secret(), "/slack/events", slack_events_blueprint)


# Create a SlackClient for your bot to use for Web API requests


# Example responder to bot mentions
@slack_events_adapter.on("app_mention")  # pragma: no cover
def handle_mentions(event_data):
    slack_client = SlackClient()
    event = event_data["event"]
    slack_client.send_message(
        channel=event["channel"],
        message=f"You said:\n>{event['text']}",
    )


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

    if event['text'].lower() == "start":
        send_welcome_message(f'@{user}', user=user, slack_client=slack_client.client, payload=event)
        return
    else:
        initial_message = get_block_initial_message()
        ts_thread = event.get("ts")
        slack_client.client.chat_postMessage(
            thread_ts=ts_thread,
            channel=event["channel"],
            text=event['text'],
            blocks=initial_message['blocks']
        )


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")  # pragma: no cover
def reaction_added(event_data):
    slack_client = SlackClient()
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.send_message(channel=channel, message=text)


@slack_events_blueprint.route("/principais-duvidas", methods=["POST"])
def principais_duvidas():
    data = request.form
    user = data['user_id']

    slack_service = SlackService(SlackClient(), channel=user)

    faq_messages = build_markdown_text_for_principais_duvidas()
    slack_service.publish_message(faq_messages)

    return Response(), 200


@slack_events_blueprint.route("/interactive-endpoint", methods=["POST"])
def echo_interactive():  # pragma: no cover
    data = request.form
    payload = json.loads(data['payload'])
    print("payload")
    print(payload)
    user = payload["user"]

    slack_client = SlackClient()

    if not user:
        return Response(), 200

    welcome = WelcomeService(user['id'], user=user['id'], slack_client=slack_client.client)

    if payload.get("actions") is not None:
        print("Entrou em actions")
        if payload['actions'][0]['value'] == 'secure_code_warrior_value':
            print("Entrou em secure_code_warrior_value")
            blocks_secure_code_warriors = get_block_secure_code_warrior()
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                blocks=blocks_secure_code_warriors['blocks']
            )

        if payload['actions'][0]['value'] == 'course_links_secure_code_warriors_value':
            print("Entrou em secure_code_warrior_value")
            blocks_links_secure_code_warriors = get_blocks_links_secure_code_warriors()
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                blocks=blocks_links_secure_code_warriors['blocks'],
            )
        if payload['actions'][0]['value'] == 'plataform_problem_secure_code_warriors_value':
            print("Entrou em secure_code_warrior_value")
            md_faq = build_markdown_text_for_principais_duvidas()
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                blocks=md_faq,
            )

        if payload['actions'][0]['value'] == 'security_guardians_value':
            channel_name = "canal-guardians"
            channel_link = f"slack://channel?team=T04HCSY9YQ0&id=C05KFKUHXSQ"
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                text=f"Acesse o canal <{channel_link}|#{channel_name}> para mais informações",
            )

        if payload['actions'][0]['value'] == 'dashboard_value':
            blocks_dashboard = get_blocks_dashboard()
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                blocks=blocks_dashboard['blocks'],
            )

        if payload['actions'][0]['value'] == 'email_not_in_dashboard_value' or payload['actions'][0][
            'value'] == 'status_not_updated_value':
            thread_link = get_direct_thread_link(payload)
            blocks_messages_specialist = get_blocks_send_messages_to_analysts(
                user=payload["user"]["username"],
                subject=payload['actions'][0]['value'],
                message="Usuário solicitou ajuda no grupo a respeito do dashboard, segue link da thread: " + thread_link,
            )
            slack_client.client.chat_postMessage(
                channel="#bot_duvidas",
                blocks=blocks_messages_specialist['blocks'],
            )
            slack_client.client.chat_postMessage(
                thread_ts=payload["message"]["thread_ts"],
                channel=payload["channel"]["id"],
                text="Enviamos mensagem para os nossos especialistas, em breve entraremos em contato com você por aqui!",
            )

        if payload['actions'][0]['value'] == 'click_me_123':
            print("Entrou em click_me_123")
            modal = welcome.get_modal()
            slack_client.client.views_open(
                trigger_id=payload['trigger_id'],
                view=modal["view"],

            )
            return Response(), 200

    if payload.get("view") is not None:

        if payload['view']['callback_id'] == 'button_ok':
            subject, message = format_values_slack(payload['view']['state']['values'])
            slack_client.client.chat_postMessage(
                channel="#bot_duvidas",
                blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*O usuário: {user['username']} enviou a seguinte duvida:* \n"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"> Subject: {subject.upper()}\n"
                                    f"> Message: {message}"
                        }

                    },
                    {
                        "type": "divider"
                    }
                ]

            )

            slack_client.client.chat_postMessage(
                channel=user['id'],
                text="A mensagem chegou para nossos analistas, em breve alguém te ajudará",
            )

        return Response(), 200

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
