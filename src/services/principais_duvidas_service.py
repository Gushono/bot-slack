from src.enums.qa_enum import EnumQuestions, EnumAnswers
from src.services.slack_service import WelcomeService


def build_markdown_text_for_principais_duvidas():
    faq_messages = []

    for question, answer in zip(EnumQuestions, EnumAnswers):
        faq_messages.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        question.value
                    ),
                },
            }
        )
        faq_messages.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        answer.value
                    ),
                },
            },
        )
        faq_messages.append(
            {
                "type": "divider"
            },
        )

    return faq_messages


def define_answer_bot(message):  # pragma: no cover
    try:
        questions = {
            "conta bloqueada": "Nao sei te ajudar nao",
            "conta ok": "vixi mano",
            "hi": "salve mano",
            "Você torce pro nautico": "Sim, com ctz"
        }

        return questions[message]
    except Exception as ex:
        return "Nao sei o que fazer nao"


def send_welcome_message(channel, user, slack_client):  # pragma: no cover
    welcome_messages = {}

    welcome_service = WelcomeService(
        channel,
        user,
        slack_client
    )

    message = welcome_service.get_message()
    response = slack_client.chat_postMessage(**message)

    if channel not in welcome_messages:
        welcome_messages[channel] = {}

    welcome_messages[channel][user] = welcome_service
