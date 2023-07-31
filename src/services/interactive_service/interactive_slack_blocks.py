from src.enums.qa_enum import EnumQuestions, EnumAnswers


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
                        "url": "https://learninghub-int.mercadolibre.com/courses/course-v1:it_prod+S-SDLC+2023_v2/course/",
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
                            "text": "Security Guardians",
                            "emoji": True
                        },
                        "value": "security_guardians_value",
                        "action_id": "security_guardians_action"
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
                            "text": "Dashboard",
                            "emoji": True
                        },
                        "value": "dashboard_value",
                        "action_id": "dashboard_action"
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
                        "value": "platform_problem_secure_code_warriors_value",
                        "action_id": "platform_problem_secure_code_warriors_action"
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
                        "value": "platform_license_secure_code_warriors_value",
                        "url": "https://meli.workplace.com/groups/539467037029524/permalink/1076399480002941/",
                        "action_id": "platform_license_secure_code_warriors_actions"
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
                    "text": "*<https://portal.securecodewarrior.com/#/courses/course-list/fb42f853-8bc4-414e-941c-b58ddd6d87f0|MELI Top 5 Backend / Machine Learning (Recomendado)>*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<https://portal.securecodewarrior.com/#/courses/course-list/a1bcb123-6c47-468f-9983-5321ea36abd9|MELI Top 5 Frontend (Recomendado)>*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<https://portal.securecodewarrior.com/#/courses/course-list/0f8343e9-23e5-4db1-87c2-747ded0a3f92|MELI Top 5 Mobile (Recomendado)>*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<https://portal.securecodewarrior.com/#/courses/course-list/ef7ba068-fef0-47d8-87f2-6fd0116c082d|MELI Top 4 Data Science / FDA (Recomendado)>*"
                }
            }
        ]
    }


def get_blocks_dashboard():
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Você selecionou as opções de dashboard! Segue abaixo as opções:"
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
                            "text": "Meu email não está no dashboard",
                            "emoji": True
                        },
                        "value": "email_not_in_dashboard_value",
                        "action_id": "email_not_in_dashboard_action"
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
                            "text": "Status de capacitado está desatualizado",
                            "emoji": True
                        },
                        "value": "status_not_updated_value",
                        "action_id": "status_not_updated_action"
                    }
                ]
            },

        ]
    }


def get_blocks_send_messages_to_analysts(user: str, subject: str, message: str):
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*O usuário: {user} enviou a seguinte duvida:* \n"
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
    }


def get_direct_thread_link(payload):
    # Extract the channel ID and parent message timestamp from the payload
    channel_id = payload["container"]["channel_id"]
    parent_message_ts = payload["message"]["thread_ts"]

    # Replace 'YOUR_SLACK_TEAM_DOMAIN' with your Slack team's domain
    slack_team_domain = 'teste-gustavo'

    link = f"https://{slack_team_domain}.slack.com/archives/{channel_id}/p{parent_message_ts.replace('.', '')}"
    return link
