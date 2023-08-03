from abc import ABC

from slack import WebClient

from src.environment import env


class SlackClientBase(ABC):
    def send_message(self, params: dict):
        pass

    def view_open(self, params: dict):
        pass

    def views_publish(self, params: dict):
        pass

    def obtain_bot_id(self):
        pass


class SlackClient(SlackClientBase):
    """
    Concrete implementation of SlackClientBase providing methods to interact with the Slack API.

    This class implements the methods to send messages, open views, publish views, and obtain the bot's user ID
    using the Slack API.

    Attributes:
        client (WebClient): An instance of the WebClient from the Slack SDK used for API communication.

    Methods:
        __init__(): Initialize the SlackClient instance with the Slack bot token.
        send_message(params: dict): Send a message using the Slack API.
        view_open(params: dict): Open a view using the Slack API.
        views_publish(params: dict): Publish a view using the Slack API.
        obtain_bot_id(): Obtain the bot's user ID using the Slack API.
    """

    def __init__(self):
        """
        Initialize the SlackClient instance with the Slack bot token.

        Raises:
            ValueError: If SLACK_BOT_TOKEN environment variable is not set.
        """
        slack_bot_token = env.get_slack_token()
        if not slack_bot_token:
            raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")
        self.client = WebClient(token=slack_bot_token)

    def send_message(self, params: dict):
        """
        Send a message using the Slack API.

        Args:
            params (dict): Parameters for sending the message.

        Returns:
            dict: API response.
        """
        response = self.client.chat_postMessage(**params)
        return response

    def view_open(self, params: dict):
        """
        Open a view using the Slack API.

        Args:
            params (dict): Parameters for opening the view.

        Returns:
            dict: API response.
        """
        response = self.client.views_open(**params)
        return response

    def views_publish(self, params: dict):
        """
        Publish a view using the Slack API.

        Args:
            params (dict): Parameters for publishing the view.

        Returns:
            dict: API response.
        """
        response = self.client.views_publish(**params)
        return response

    def obtain_bot_id(self):
        """
        Obtain the bot ID using the Slack API.

        Returns:
            str: The bot ID.
        """
        response = self.client.api_call("auth.test")
        return response["user_id"]
