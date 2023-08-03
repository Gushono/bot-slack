"""
Slack Client Module

This module provides classes for interacting with the Slack API.
"""

from abc import ABC
from asyncio import Future

from slack import WebClient
from slack_sdk.web.legacy_slack_response import LegacySlackResponse

from src.environment import env


class SlackClientBase(ABC):
    """
    Abstract base class for Slack clients.

    This class defines the interface for interacting with the Slack API.
    """

    def send_message(self, params: dict) -> dict:
        """Send a message using the Slack API."""
        raise NotImplementedError

    def view_open(self, params: dict) -> dict:
        """Open a view using the Slack API."""
        raise NotImplementedError

    def views_publish(self, params: dict) -> dict:
        """Publish a view using the Slack API."""
        raise NotImplementedError

    def obtain_bot_id(self) -> str:
        """Obtain the bot ID using the Slack API."""
        raise NotImplementedError


class SlackClient(SlackClientBase):
    """
    Concrete implementation of SlackClientBase providing methods to interact with the Slack API.
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

    def send_message(self, params: dict) -> Future | LegacySlackResponse:
        """Send a message using the Slack API."""
        response = self.client.chat_postMessage(**params)
        return response

    def view_open(self, params: dict) -> Future | LegacySlackResponse:
        """Open a view using the Slack API."""
        response = self.client.views_open(**params)
        return response

    def views_publish(self, params: dict) -> Future | LegacySlackResponse:
        """Publish a view using the Slack API."""
        response = self.client.views_publish(**params)
        return response

    def obtain_bot_id(self) -> str:
        """Obtain the bot ID using the Slack API."""
        response = self.client.api_call("auth.test")
        return response["user_id"]
