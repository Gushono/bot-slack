import os


def get_home_page(user):
    return {
        "token": os.getenv("SLACK_TOKEN"),
        "user_id": user,
        "view": {
            "type": "home",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Olá, tudo bem? :wave:\n\n "
                                "Sou o Bot do time de Developer Security Education :bot: - WebSec e estou aqui para te "
                                "ajudar com suas principais dúvidas/problemas sobre as "
                                "capacitações de Segurança de aplicações! :logo-dse: "
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "Você pode interagir com as seguintes opções:"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Meu status de capacitação",
                                "emoji": True
                            },
                            "value": "create_task"
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Link dashboard",
                                "emoji": True
                            },
                            "value": "create_project"
                        }
                    ]
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                            "alt_text": "placeholder"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Nossos canais*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "<fakelink.toChannel.com|*#guardians*>\nGuardians é o canal onde voce pode tirar duvidas... "
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }

    }
