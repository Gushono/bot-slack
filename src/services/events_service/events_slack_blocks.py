def get_block_initial_message():
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":wave: Olá! Bem-vindo ao nosso canal! Estou aqui para ajudá-lo. :smiley:",
                },
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "Selecione uma das opções abaixo:"},
            },
            {"type": "divider"},
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Secure Code Warrior",
                            "emoji": True,
                        },
                        "value": "secure_code_warrior_value",
                        "action_id": "secure_code_warrior_action",
                    }
                ],
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "SSDLC", "emoji": True},
                        "value": "ssdlc_value",
                        "url": "https://learninghub-int.mercadolibre.com/courses/course-v1:it_prod+S-SDLC+2023_v2/course/",
                        "action_id": "ssdlc_action",
                    }
                ],
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Security Guardians",
                            "emoji": True,
                        },
                        "value": "security_guardians_value",
                        "action_id": "security_guardians_action",
                    }
                ],
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Dashboard",
                            "emoji": True,
                        },
                        "value": "dashboard_value",
                        "action_id": "dashboard_action",
                    }
                ],
            },
            {"type": "divider"},
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Ainda preciso de ajuda",
                            "emoji": True,
                        },
                        "value": "need_help_value",
                        "action_id": "need_help_action",
                    }
                ],
            },
        ]
    }


def get_home_page():
    return {
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
                        "capacitações de Segurança de aplicações! :logo-dse: ",
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "Você pode interagir com as seguintes opções:",
                    },
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Meu status de capacitação",
                                "emoji": True,
                            },
                            "value": "my_qualification_status_value",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Link dashboard",
                                "emoji": True,
                            },
                            "value": "link_dashboard_home_value",
                        },
                    ],
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                            "alt_text": "placeholder",
                        }
                    ],
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "*Nossos canais*"},
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "<fakelink.toChannel.com|*#guardians*>\nGuardians é o canal onde voce pode tirar duvidas... ",
                    },
                },
                {"type": "divider"},
            ],
        }
    }
