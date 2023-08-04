# Define the strategies in a dictionary
from src.services.interactive_service.actions_strategy import (
    SecureCodeWarriorStrategy,
    CourseLinksSecureCodeWarriorsStrategy,
    PlatformProblemSecureCodeWarriorsStrategy,
    SecurityGuardiansStrategy,
    DashboardStrategy,
    EmailStatusUpdateStrategy,
    PlatformLicenseSecureCodeWarriorsStrategy,
    SSDLCStrategy, StillNeedHelpStrategy, MyQualificationStatusStrategy, LinkDashboardHomeStrategy,
)
from src.services.slack_service import SlackService

strategies_actions = {
    "secure_code_warrior_value": SecureCodeWarriorStrategy(),
    "ssdlc_value": SSDLCStrategy(),
    "course_links_secure_code_warriors_value": CourseLinksSecureCodeWarriorsStrategy(),
    "platform_problem_secure_code_warriors_value": PlatformProblemSecureCodeWarriorsStrategy(),
    "security_guardians_value": SecurityGuardiansStrategy(),
    "dashboard_value": DashboardStrategy(),
    "email_not_in_dashboard_value": EmailStatusUpdateStrategy(),
    "status_not_updated_value": EmailStatusUpdateStrategy(),
    "platform_license_secure_code_warriors_value": PlatformLicenseSecureCodeWarriorsStrategy(),
    "need_help_value": StillNeedHelpStrategy(),
    "my_qualification_status_value": MyQualificationStatusStrategy(),
    "link_dashboard_home_value": LinkDashboardHomeStrategy(),
}


def handle_actions(payload: dict):
    """
    Handle interactive actions triggered in Slack.

    This function processes interactive action payloads, identifies the relevant action strategy based on the
    action ID, and delegates execution to the corresponding strategy handler.

    Args:
        payload (dict): The payload containing information about the interactive action.

    Returns:
        Any: The result of executing the action strategy.

    Raises:
        ValueError: If the action ID is not implemented.
    """
    action_id = payload["actions"][0]["value"]
    strategy = strategies_actions.get(action_id)

    if not strategy:
        raise ValueError(f"Action {action_id} not implemented.")

    return strategy.execute(payload=payload, slack_service=SlackService())
