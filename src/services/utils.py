from src.services.slack_service import SlackService


class BaseStrategy:
    def execute(self, payload: dict, slack_service: SlackService):
        pass
