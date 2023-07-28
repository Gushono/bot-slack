from slack import WebClient

from src.environment import env


class SlackClient:
    def __init__(self):  # pragma: no cover
        slack_bot_token = env.get_slack_token()
        if not slack_bot_token:
            raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")

        self.client = WebClient(slack_bot_token)

    def send_message(self, channel, message):  # pragma: no cover
        response = self.client.chat_postMessage(channel=channel, text=message)
        return response
