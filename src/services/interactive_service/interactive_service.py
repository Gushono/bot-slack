# Define the strategies in a dictionary
from src.client.slack_client import SlackClient
from src.services.interactive_service.actions_strategy import (
    SecureCodeWarriorStrategy,
    CourseLinksSecureCodeWarriorsStrategy,
    PlataformProblemSecureCodeWarriorsStrategy,
    SecurityGuardiansStrategy,
    DashboardStrategy,
    EmailStatusUpdateStrategy,
    # ClickMeStrategy
)
from src.services.slack_service import SlackService

strategies_actions = {
    'secure_code_warrior_value': SecureCodeWarriorStrategy(),
    'course_links_secure_code_warriors_value': CourseLinksSecureCodeWarriorsStrategy(),
    'plataform_problem_secure_code_warriors_value': PlataformProblemSecureCodeWarriorsStrategy(),
    'security_guardians_value': SecurityGuardiansStrategy(),
    'dashboard_value': DashboardStrategy(),
    'email_not_in_dashboard_value': EmailStatusUpdateStrategy(),
    'status_not_updated_value': EmailStatusUpdateStrategy(),
    # 'click_me_123': ClickMeStrategy(),
    # Add more strategies as needed...
}


def handle_actions(payload: dict):
    slack_service = SlackService(slack_client=SlackClient())
    action_id = payload['actions'][0]['action_id']

    strategy = strategies_actions.get(action_id)

    if not strategy:
        raise ValueError(f"Action {action_id} not implemented.")

    return strategy.execute(payload=payload, slack_service=slack_service)


def handle_view_flow(payload: dict):
    # slack_service = SlackService(slack_client=SlackClient())
    # action_id = payload['view']['callback_id']
    #
    # strategy = strategies_actions.get(action_id)
    #
    # if not strategy:
    #     raise ValueError(f"Action {action_id} not implemented.")
    #
    # return strategy.execute(payload=payload, slack_service=slack_service)
    print("Entrou no view flow")
    print(payload)
    return True
