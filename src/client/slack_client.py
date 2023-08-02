from slack import WebClient

from src.environment import env


class SlackClient:
    def __init__(self):
        slack_bot_token = env.get_slack_token()
        if not slack_bot_token:
            raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")

        self.client = WebClient(token=slack_bot_token)

    def send_message(self, params: dict):
        response = self.client.chat_postMessage(**params)
        return response

    def view_open(self, params: dict):
        response = self.client.views_open(**params)
        return response

    def views_publish(self, params: dict):
        response = self.client.views_publish(**params)
        return response
