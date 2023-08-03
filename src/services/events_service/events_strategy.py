from flask import Response

from src.services.events_service.events_slack_blocks import get_block_initial_message, get_home_page
from src.services.slack_service import SlackService
from src.services.utils import BaseStrategy


class OnMessageStrategy(BaseStrategy):
    allowed_channels = ["C04GL827WKX"]

    def execute(self, event: dict, slack_service: SlackService):
        if not self._is_valid_channel(event.get("channel")):
            return Response(), 200

        if event.get("subtype"):
            return Response(), 200

        initial_message = get_block_initial_message()
        response = slack_service.send_slack_message(
            channel=event.get("channel"),
            text=event.get("text"),
            blocks=initial_message["blocks"],
            thread_ts=event.get("ts"),
        )

        return response

    def _is_valid_channel(self, channel: str) -> bool:
        return channel is not None and channel in self.allowed_channels


class OnAppHomeOpenedStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        home_page = get_home_page()
        response = slack_service.views_publish(
            user_id=payload["user"],
            view=home_page["view"]
        )

        if response:
            return home_page

        raise ValueError("Error publishing home page")


class OnErrorStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        print("ERROR: " + str(payload))
        return Response(), 200
