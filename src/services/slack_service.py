from enum import Enum

from src.client.slack_client import SlackClient


class EnumValuesSelectBoxSubject(Enum):
    DUVIDAS = "DUVIDAS"
    ACCESSO = "ACESSO"


class SlackService:
    def __init__(self, slack_client: SlackClient = None):
        self._slack_client = slack_client or SlackClient()
        self.bot_id = self._obtain_bot_id()

    def _obtain_bot_id(self) -> str:
        if self.bot_id:
            return self.bot_id

        return self._slack_client.obtain_bot_id()

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

    def is_message_from_bot(self, event: dict) -> bool:
        if not event.get("user"):
            return False

        return event.get("user") == self.bot_id
