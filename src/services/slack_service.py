from src.client.slack_client import SlackClient


class SlackService:
    """
    A class for interacting with the Slack API.

    Args:
        slack_client (SlackClient, optional): An instance of the SlackClient class. If not provided,
            a new instance will be created.

    Attributes:
        _slack_client (SlackClient): The SlackClient instance used for API communication.
        _bot_id (str): The ID of the bot user.
    """

    def __init__(self, slack_client: SlackClient = None):
        """
        Initialize the SlackService.

        Args:
            slack_client (SlackClient, optional): An instance of the SlackClient class. If not provided,
                a new instance will be created.
        """
        self._slack_client = slack_client or SlackClient()
        self._bot_id = None

    @property
    def bot_id(self) -> str:
        """
        The ID of the bot user.
        """
        if self._bot_id is None:
            self._bot_id = self._slack_client.obtain_bot_id()
        return self._bot_id

    def send_slack_message(
            self,
            channel: str = None,
            text: str = None,
            blocks: str = None,
            thread_ts: str = None
    ):
        """
        Send a message to a Slack channel.

        Args:
            channel (str, optional): The channel to send the message to.
            text (str, optional): The text of the message.
            blocks (str, optional): The blocks of the message.
            thread_ts (str, optional): The thread timestamp if replying in a thread.
        """
        built_params = {}
        if channel:
            built_params["channel"] = channel
        if text:
            built_params["text"] = text
        if blocks:
            built_params["blocks"] = blocks
        if thread_ts:
            built_params["thread_ts"] = thread_ts

        return self._slack_client.send_message(built_params)

    def view_open(self, trigger_id: str = None, view: dict = None):
        """
        Open a view for a user triggered by a specific action.

        Args:
            trigger_id (str, optional): The unique identifier for the triggering action.
            view (dict, optional): The view definition to display.

        Returns:
            dict: The response from the Slack API.
        """
        built_params = {}
        if trigger_id:
            built_params["trigger_id"] = trigger_id
        if view:
            built_params["view"] = view

        return self._slack_client.view_open(built_params)

    def views_publish(self, user_id: str = None, view: dict = None):
        """
        Publish a view to a user.

        Args:
            user_id (str, optional): The ID of the user to whom the view will be published.
            view (dict, optional): The view definition to publish.

        Returns:
            dict: The response from the Slack API.
        """
        built_params = {}
        if user_id:
            built_params["user_id"] = user_id
        if view:
            built_params["view"] = view

        return self._slack_client.views_publish(built_params)

    def is_message_from_bot(self, event: dict) -> bool:
        """
        Check if a message event is from the bot.

        Args:
            event (dict): The Slack event.

        Returns:
            bool: True if the message is from the bot user, False otherwise.
        """
        if not event.get("user"):
            return False

        return event.get("user") == self.bot_id

    @staticmethod
    def is_message_inside_a_thread(event: dict) -> bool:
        """
        Check if a message event is inside a thread.

        Args:
            event (dict): The Slack event.

        Returns:
            bool: True if the message is inside a thread, False otherwise.
        """
        return event.get("parent_user_id") is not None
