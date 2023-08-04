from src.client.slack_client import SlackClientBase


class FakeSlackClient(SlackClientBase):
    def send_message(self, params: dict) -> dict:
        return {"message_sent": True, "message_params": params}

    def view_open(self, params: dict) -> dict:
        return {"view_opened": True, "view_params": params}

    def views_publish(self, params: dict) -> dict:
        return {"view_published": True, "view_publish_params": params}

    def obtain_bot_id(self) -> str:
        return "fake_bot_id"
