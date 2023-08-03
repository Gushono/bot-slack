from src.services.interactive_service.actions_slack_blocks import (
    get_blocks_send_messages_to_analysts, get_direct_thread_link,
    get_blocks_dashboard,
    get_block_secure_code_warrior,
    get_blocks_links_secure_code_warriors,
    build_markdown_text_for_principais_duvidas
)
from src.services.slack_service import SlackService
from src.services.utils import BaseStrategy


class SecureCodeWarriorStrategy(BaseStrategy):
    """
    Strategy for handling secure code warrior-related interactions.
    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for secure code warrior interactions.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        blocks_secure_code_warriors = get_block_secure_code_warrior()

        response = slack_service.send_slack_message(
            blocks=blocks_secure_code_warriors['blocks'],
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class SSDLCStrategy(BaseStrategy):
    """
    Strategy for handling SSDLC-related interactions.
    """

    COURSE_LINK = "https://learninghub-int.mercadolibre.com/courses/course-v1:it_prod+S-SDLC+2023_v2/course/"
    COURSE_NAME = "SSDLC"

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for handling SSDLC interactions.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=f"Você foi redirecionado para o curso <{self.COURSE_LINK}|{self.COURSE_NAME}>.",
        )

        return response


class CourseLinksSecureCodeWarriorsStrategy(BaseStrategy):
    """
    Strategy for handling course links for Secure Code Warriors interactions.
    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for handling course links for Secure Code Warriors interactions.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        blocks_links_secure_code_warriors = get_blocks_links_secure_code_warriors()

        response = slack_service.send_slack_message(
            blocks=blocks_links_secure_code_warriors['blocks'],
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class PlatformProblemSecureCodeWarriorsStrategy(BaseStrategy):
    """
    Strategy for handling platform problem inquiries related to Secure Code Warriors interactions.
    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for handling platform problem inquiries for Secure Code Warriors interactions.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        md_faq = build_markdown_text_for_principais_duvidas()
        response = slack_service.send_slack_message(
            blocks=md_faq,
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class SecurityGuardiansStrategy(BaseStrategy):
    """
    Strategy for providing information about the Security Guardians channel.
    """

    TEAM_ID = "T04HCSY9YQ0"
    CHANNEL_ID = "C05KFKUHXSQ"
    CHANNEL_LINK = f"slack://channel?team={TEAM_ID}&id={CHANNEL_ID}"
    CHANNEL_NAME = "canal-guardians"

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for providing information about the Security Guardians channel.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        text = f"Acesse o canal <{self.CHANNEL_LINK}|#{self.CHANNEL_NAME}> para mais informações"
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=text,
        )

        return response


class DashboardStrategy(BaseStrategy):
    """
    Strategy for providing information about the dashboard.
    """

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for providing information about the dashboard.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        blocks_dashboard = get_blocks_dashboard()
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            blocks=blocks_dashboard['blocks'],
        )

        return response


class EmailStatusUpdateStrategy(BaseStrategy):
    """
    Strategy for sending email status update messages.
    """
    # Bot duvidas channel
    BOT_CHANNEL = "C04JBNDLF16"
    RESPONSE_TO_USER = "Enviamos mensagem para os nossos analistas, em breve entraremos em contato com você por aqui!"

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for sending email status update messages.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        thread_link = get_direct_thread_link(payload)
        blocks_messages_specialist = get_blocks_send_messages_to_analysts(
            user=payload["user"]["username"],
            subject=payload['actions'][0]['value'],
            message="Usuário solicitou ajuda no grupo a respeito do dashboard, segue link da thread: " + thread_link,
        )

        response_message_to_specialist = slack_service.send_slack_message(
            channel=self.BOT_CHANNEL,
            blocks=blocks_messages_specialist['blocks'],
        )

        response_message_to_user_in_thread = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=self.RESPONSE_TO_USER,
        )

        return response_message_to_specialist and response_message_to_user_in_thread


class PlatformLicenseSecureCodeWarriorsStrategy(BaseStrategy):
    """
    Strategy for providing information about the Platform License related to Secure Code Warriors.
    """
    WORKPLACE_LINK = "https://meli.workplace.com/groups/539467037029524/permalink/1076399480002941/"

    def execute(self, payload: dict, slack_service: SlackService):
        """
        Execute the strategy for providing information about the Platform License related to Secure Code Warriors.

        Args:
            payload (dict): The payload containing information about the interaction.
            slack_service (SlackService): The SlackService instance for API interaction.

        Returns:
            dict: The API response.
        """
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=f"Você foi redirecionado para o <{self.WORKPLACE_LINK}|Workplace> para mais informações.",
        )
        return response
