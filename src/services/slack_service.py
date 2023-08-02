import os
from enum import Enum

from src.client.slack_client import SlackClient


class EnumValuesSelectBoxSubject(Enum):
    DUVIDAS = "DUVIDAS"
    ACCESSO = "ACESSO"


class SlackService:
    def __init__(self, slack_client: SlackClient = None):
        self._slack_client = slack_client or SlackClient()

    def send_slack_message(
            self,
            channel: str = None,
            text: str = None,
            blocks: str = None,
            thread_ts: str = None
    ):
        built_params = {}
        if channel:
            built_params["channel"] = channel
        if text:
            built_params["text"] = text
        if blocks:
            built_params["blocks"] = blocks
        if thread_ts:
            built_params["thread_ts"] = thread_ts

        return self._slack_client.send_message(built_params)

    def view_open(self, trigger_id: str = None, view: dict = None):
        built_params = {}
        if trigger_id:
            built_params["trigger_id"] = trigger_id
        if view:
            built_params["view"] = view

        return self._slack_client.view_open(built_params)

    def views_publish(self, user_id: str = None, view: dict = None):
        built_params = {}
        if user_id:
            built_params["user_id"] = user_id
        if view:
            built_params["view"] = view

        return self._slack_client.views_publish(built_params)


class SlackService1:
    def __init__(self, slack_client: SlackClient, channel=None):
        self.slack_client = slack_client
        self.channel = f"@{channel}" or "geral"

    def publish_message(self, message, user_id=None):  # pragma: no cover
        to_publish = {
            "channel": self.channel,
            "blocks": message
        }
        self.slack_client.client.chat_postMessage(**to_publish)


class WelcomeService:
    FAQ = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                """
                ¿Cuáles son los cursos que todo desarrollador de MELI necesita hacer para se considerar como capacitado?

                Todos los Devs/PLs - Ciclo de vida de Desarrollo Seguro (S-SLDC) - ESP / PORT
                Si eres un Dev/TL Frontend - Frontend Top 10
                Si eres un Dev/TL Mobile - Mobile Top 6
                Si eres un Dev/TL Backend - Meli Top 10 (Backend)

                ¿Cuál es el período de validez de los cursos?
                
                Todo los cursos de Desarrollo Seguro tienen validez de 365 dias y debemos reforzar el conocimiento todo año.
                
                ¿Hay otros cursos en la plataforma o solo los recomendados?
                
                Además de los 3 cursos recomendados para todos los Devs, hay más de 15 cursos en la plataforma y todos pueden hacer.
                
                ¿En cuál link yo me registro en la plataforma Secure Code Warrior?
                https://portal.securecodewarrior.com/#/register/526126899721, no olvides registrarte con tu correo corporativo.
                
                ¿Cuánto tiempo tengo para calificar después de registrarme en la plataforma?
                
                La licencia de Secure Code Warrior tiene una duración de 14 dias.
                Mi licencia venció pero quiero tomar más cursos, ¿cómo puedo proceder?
                Es solo registrarse de nuevo con el mismo link de registro.
                Mi licencia venció y no había terminado el curso, ¿pierdo mi avance?
                Si el curso esta finalizado, queda registrado y no se pierde. Si al vencimiento de la licencia, el curso no fue finalizado, el progreso se pierde.
                
                ¿Dónde puedo ver si ya estoy capacitad@?
                
                Puede acceder directamente a nuestros tableros:
                
                Capacitados por Usuario - Visualizar si está capacitado o no y cual fue el ultimo curso echo.
                Capacitados por Curso - Visualizar todos los cursos echos en los últimos 365 dias.
                
                Tengo el error: Tu organización tiene inicio de sesión único configurado, pero tu cuenta aún no ha sido habilitada en nuestra plataforma.
                
                Debes registrarte primero en la plataforma antes de intentar iniciar sesión. Link de registro: https://portal.securecodewarrior.com/#/register/526126899721
                
                Terminé mi curso en la plataforma, ¿cuántos días se actualiza el tablero de Tableau?
                
                Después de finalizar el curso, espere al menos 1 día hábil para que se actualice el tablero.
                
                Este año ya hice uno de los cursos recomendados, ¿debo volver a hacer?
                No será necesario, basta con consultar en Tableau el curso que queda por completar y finalizarlo.
                """
            ),
        }
    }

    START_TEXT = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to your _App's_ Slack App :tada:\n\n"
                "We're thrilled you're here. Get started by completing the steps below."
            ),
        },
    }

    DIVIDER = {"type": "divider"}

    def __init__(self, channel, user, slack_client):
        self.channel = channel
        self.user = user
        self.slack_client = slack_client
        self.icon_emoji = ":robot_face:"
        self.completed = False

    def send_welcome_message(self):
        self.slack_client.chat_postMessage(
            channel=self.channel,
            text=f"Welcome to the team, <@{self.user}>!",
            icon_emoji=self.icon_emoji
        )
        self.completed = True

    def get_message(self):
        return {
            "channel": self.channel,
            "username": "Welcome Bot",
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.START_TEXT,
                self.DIVIDER,
                *self._get_reaction_task(),
            ],
        }

    def _get_reaction_task(self):  # pragma: no cover
        checkmark = ":white_check_mark:"

        if not self.completed:
            checkmark = ":white_large_square:"

        text = f"{checkmark} *React to this message!*"

        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text,
                },
            }
        ]

    def get_home_page(self):  # pragma: no cover
        return {
            "token": os.getenv("SLACK_TOKEN"),
            "user_id": self.user,
            "view": {
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Olá, tudo bem? :wave:\n\n Sou o Bot do time de Developer Security Education :bot: - WebSec e estou aqui para te ajudar com suas principais dúvidas/problemas sobre as capacitações de Segurança de aplicações! :logo-dse: "
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

    def get_modal(self):  # pragma: no cover
        return {
            "view": {
                "type": "modal",
                "callback_id": "button_ok",
                "submit": {
                    "type": "plain_text",
                    "text": "Enviar",
                    "emoji": True
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancelar",
                    "emoji": True
                },
                "title": {
                    "type": "plain_text",
                    "text": "Ainda está com dúvida?",
                    "emoji": True
                },
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": ":wave: Hey!\n\n Não encontrou o que estava procurando com o comando /principais_duvidas`? Mande sua questão abaixo",
                            "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "input",
                        "block_id": "input_select",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Selecione seu problema",
                                "emoji": True
                            },
                            "options": [
                                {

                                    "text": {
                                        "type": "plain_text",
                                        "text": ":computer: Acesso",
                                        "emoji": True
                                    },
                                    "value": f"{EnumValuesSelectBoxSubject.ACCESSO.value}"
                                },
                                {
                                    # "block_id": "block_id",
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":question: Dúvida",
                                        "emoji": True
                                    },
                                    "value": f"{EnumValuesSelectBoxSubject.DUVIDAS.value}"
                                }
                            ],
                            "action_id": "static_select-action"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Selecione seu tipo de problema",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "Poderia nos detalhar um pouco mais o seu erro?",
                            "emoji": True
                        },
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": "input_question",
                        },

                    }
                ]
            }
        }
        # return {
        #     "type": "home",
        #     "blocks": [
        #         {
        #             "type": "section",
        #             "text": {
        #                 "type": "mrkdwn",
        #                 "text": "Welcome to the Home Tab"
        #             }
        #         }
        #     ]
        # }
