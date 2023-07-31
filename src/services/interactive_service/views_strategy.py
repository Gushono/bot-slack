from src.services.interactive_service.actions_strategy import BaseStrategy
from src.services.interactive_service.views_slack_blocks import get_home_page
from src.services.slack_service import SlackService


class HomeStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        home_page = get_home_page(payload.get("user"))
        response = slack_service._slack_client.views_publish(
            **home_page
        )

        if response:
            return home_page
