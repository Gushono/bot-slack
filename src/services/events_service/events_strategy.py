from flask import Response

from src.services.events_service.events_slack_blocks import get_block_initial_message, get_home_page
from src.services.slack_service import SlackService
from src.services.utils import BaseStrategy


class OnMessageStrategy(BaseStrategy):
    """
    Strategy for handling events when a message is sent.

    This strategy handles the event when a message is sent in a specific channel.
    It verifies if the channel is valid, avoids handling message updates or deletions,
    and responds with an initial message.

    Attributes:
        allowed_channels (list[str]): List of allowed channel IDs for message handling.
    """
    allowed_channels = ["C04GL827WKX"]

    def execute(self, event: dict, slack_service: SlackService):
        """
        Execute the strategy for handling a message event.

        Args:
            event (dict): The Slack event dictionary.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            tuple[Response, int]: A tuple containing a response object and an HTTP status code.
        """
        if not self._is_valid_channel(event.get("channel")):
            return Response(), 200

        # Avoid when deleting / updating a message
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
        """
        Check if the given channel is valid for message handling.

        Args:
            channel (str): The channel ID.

        Returns:
            bool: True if the channel is valid, False otherwise.
        """
        return channel and channel in self.allowed_channels


class OnAppHomeOpenedStrategy(BaseStrategy):
    """
    Strategy for handling events when the app home is opened.

    This strategy handles the event when a user's app home is opened and publishes
    the home page view for that user.

    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for handling an app home opened event.

        Args:
            payload (dict): The payload containing information about the event.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The home page view definition.

        Raises:
            ValueError: If there is an error publishing the home page view.
        """
        home_page = get_home_page()
        response = slack_service.views_publish(
            user_id=payload["user"],
            view=home_page["view"]
        )

        if response:
            return home_page

        raise ValueError("Error publishing home page")


class OnErrorStrategy(BaseStrategy):
    """
    Strategy for handling error events.

    This strategy handles error events by printing the payload to the console.

    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for handling an error event.

        Args:
            payload (dict): The payload containing information about the error.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            tuple[Response, int]: A tuple containing a response object and an HTTP status code.
        """
        print("ERROR: " + str(payload))
        return Response(), 200
