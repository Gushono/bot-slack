from src.services.interactive_service.interactive_slack_blocks import (
    get_blocks_send_messages_to_analysts, get_direct_thread_link,
    get_blocks_dashboard,
    get_block_secure_code_warrior,
    get_blocks_links_secure_code_warriors,
    build_markdown_text_for_principais_duvidas
)
from src.services.slack_service import SlackService


class BaseStrategy:
    def execute(self, payload: dict, slack_service: SlackService):
        pass


class SecureCodeWarriorStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        blocks_secure_code_warriors = get_block_secure_code_warrior()

        response = slack_service.send_slack_message(
            blocks=blocks_secure_code_warriors['blocks'],
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class SSDLCStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        # Acknowledge the message
        link_ssdlc = "google.com.br"
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=f"Você foi redirecionado para o curso <{link_ssdlc}|SSDLC>.",
        )

        return response


class CourseLinksSecureCodeWarriorsStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        blocks_links_secure_code_warriors = get_blocks_links_secure_code_warriors()

        response = slack_service.send_slack_message(
            blocks=blocks_links_secure_code_warriors['blocks'],
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class PlatformProblemSecureCodeWarriorsStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        md_faq = build_markdown_text_for_principais_duvidas()
        response = slack_service.send_slack_message(
            blocks=md_faq,
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"]
        )

        return response


class SecurityGuardiansStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        channel_name = "canal-guardians"
        channel_link = f"slack://channel?team=T04HCSY9YQ0&id=C05KFKUHXSQ"
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=f"Acesse o canal <{channel_link}|#{channel_name}> para mais informações",
        )

        return response


class DashboardStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        blocks_dashboard = get_blocks_dashboard()

        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            blocks=blocks_dashboard['blocks'],
        )

        return response


class EmailStatusUpdateStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        thread_link = get_direct_thread_link(payload)
        blocks_messages_specialist = get_blocks_send_messages_to_analysts(
            user=payload["user"]["username"],
            subject=payload['actions'][0]['value'],
            message="Usuário solicitou ajuda no grupo a respeito do dashboard, segue link da thread: " + thread_link,
        )

        response_message_to_specialist = slack_service.send_slack_message(
            channel="#bot_duvidas",
            blocks=blocks_messages_specialist['blocks'],
        )

        response_message_to_user_in_thread = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text="Enviamos mensagem para os nossos especialistas, em breve entraremos em contato com você por aqui!",
        )

        print("Response message to bot channel to specialist")
        print(response_message_to_specialist)
        print("Response message to user in thread")
        print(response_message_to_user_in_thread)

        return response_message_to_specialist


class PlatformLicenseSecureCodeWarriorsStrategy(BaseStrategy):
    def execute(self, payload: dict, slack_service: SlackService):
        link_workspace = "google.com.br"
        response = slack_service.send_slack_message(
            thread_ts=payload["message"]["thread_ts"],
            channel=payload["channel"]["id"],
            text=f"Você foi redirecionado para o workplace <{link_workspace}|Workplace> para mais informações.",
        )
        return response
