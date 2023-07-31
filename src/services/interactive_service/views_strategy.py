from src.services.interactive_service.actions_strategy import BaseStrategy
from src.services.slack_service import SlackService


class HomeStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        modal = welcome.get_modal()
        slack_service.view_open(
            trigger_id=payload['trigger_id'],
            view=modal["view"],
        )
