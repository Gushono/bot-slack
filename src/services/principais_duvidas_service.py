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


def get_block_initial_message():
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":wave: Olá! Bem-vindo ao nosso canal! Estou aqui para ajudá-lo. :smiley:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Selecione uma das opções abaixo:"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Secure Code Warrior",
                            "emoji": True
                        },
                        "value": "secure_code_warrior_value",
                        "action_id": "secure_code_warrior_action"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "SSDLC",
                            "emoji": True
                        },
                        "value": "ssdlc_value",
                        "action_id": "ssdlc_action"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Outros",
                            "emoji": True
                        },
                        "value": "others_value",
                        "action_id": "others_action"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Ainda preciso de ajuda",
                            "emoji": True
                        },
                        "value": "need_help_value",
                        "action_id": "need_help_action"
                    }
                ]
            }
        ]
    }


def get_block_secure_code_warrior():
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Você selecionou as opções de secure code warriors! Segue abaixo as opções:"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Link Cursos",
                            "emoji": True
                        },
                        "value": "course_links_secure_code_warriors_value",
                        "action_id": "course_links_secure_code_warriors_action"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Problema Plataforma",
                            "emoji": True
                        },
                        "value": "plataform_problem_secure_code_warriors_value",
                        "action_id": "plataform_problem_secure_code_warriors_action"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Licença plataforma",
                            "emoji": True
                        },
                        "value": "plataform_license_secure_code_warriors_value",
                        "url": "https://google.com",
                        "action_id": "plataform_license_secure_code_warriors_actions"
                    }
                ]
            },
            {
                "type": "divider"
            }
        ]
    }


def get_blocks_links_secure_code_warriors():
    return {
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<fakeLink.toHotelPage.com|MELI TOP 5 - BACKEND>*\n★★★★★\nRated: 10.0 - Excellent"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_1.png",
                    "alt_text": "Meli top 5 backend"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<fakeLink.toHotelPage.com|MELI TOP 5 - FRONTEND>*\n★★★★★\nRated: 10.0 - Excellent"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_1.png",
                    "alt_text": "Meli top 5 frontend"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<fakeLink.toHotelPage.com|MELI TOP 5 - MOBILE>*\n★★★★★\nRated: 10.0 - Excellent"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_1.png",
                    "alt_text": "Windsor Court Hotel thumbnail"
                }
            },
            {
                "type": "divider"
            }
        ]
    }
