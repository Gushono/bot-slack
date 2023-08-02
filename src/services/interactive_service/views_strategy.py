from src.services.interactive_service.actions_strategy import BaseStrategy
from src.services.interactive_service.views_slack_blocks import get_home_page
from src.services.slack_service import SlackService


class HomeStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        home_page = get_home_page()
        response = slack_service.views_publish(
            user_id=payload["user"],
            view=home_page["view"]
        )

        if response:
            return home_page

        raise ValueError("Error publishing home page")
