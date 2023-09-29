import pytest

from src.services.interactive_service.actions_strategy import SecureCodeWarriorStrategy, SSDLCStrategy, \
    CourseLinksSecureCodeWarriorsStrategy, PlatformProblemSecureCodeWarriorsStrategy, SecurityGuardiansStrategy, \
    DashboardStrategy, EmailStatusUpdateStrategy, PlatformLicenseSecureCodeWarriorsStrategy, StillNeedHelpStrategy
from src.services.slack_service import SlackService
from tests.fake_slack_client import FakeSlackClient

fake_slack_service = SlackService(slack_client=FakeSlackClient())

container_payload = {"container": {"channel_id": "123"}, "message": {"thread_ts": "123.456"}, "user": {"username": "test_user"},"actions": [{"action_id": "email_not_in_dashboard_action", "value": "email_not_in_dashboard_value"}], "channel": {"id": "123"}}
generic_payload = {"message": {"thread_ts": "123", "text": "generic"}, "channel": {"id": "123"}}


@pytest.mark.parametrize(
    "strategy, payload, expected_result",
    [
        (SecureCodeWarriorStrategy, generic_payload, ["blocks", "channel", "thread_ts"]),
        (SSDLCStrategy, generic_payload, ["channel", "thread_ts"]),
        (CourseLinksSecureCodeWarriorsStrategy, generic_payload, ["blocks", "channel", "thread_ts"]),
        (PlatformProblemSecureCodeWarriorsStrategy, generic_payload, ["blocks", "channel", "thread_ts"]),
        (SecurityGuardiansStrategy, generic_payload, ["text", "channel", "thread_ts"]),
        (DashboardStrategy, generic_payload, ["blocks", "channel", "thread_ts"]),
        (EmailStatusUpdateStrategy, container_payload, ["channel", "text", "thread_ts"]),
        (PlatformLicenseSecureCodeWarriorsStrategy, generic_payload, ["channel", "text", "thread_ts"]),
        (StillNeedHelpStrategy, container_payload, ["channel", "text", "thread_ts"]),

    ]

)
def test_all_strategies(strategy, payload, expected_result):
    strategy = strategy()
    result_strategy = strategy.execute(
        payload=payload,
        slack_service=fake_slack_service
    )

    assert all([key in result_strategy["message_params"] for key in expected_result])


def test_secure_code_warriors_strategy():
    strategy = SecureCodeWarriorStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["blocks"] == [{'type': 'section', 'text': {'type': 'mrkdwn',
                                                                                        'text': 'Você selecionou as opções de secure code warriors! Segue abaixo as opções:'}},
                                                           {'type': 'divider'}, {'type': 'actions', 'elements': [
            {'type': 'button', 'text': {'type': 'plain_text', 'text': 'Link Cursos', 'emoji': True},
             'value': 'course_links_secure_code_warriors_value',
             'action_id': 'course_links_secure_code_warriors_action'}]}, {'type': 'actions', 'elements': [
            {'type': 'button', 'text': {'type': 'plain_text', 'text': 'Problema Plataforma', 'emoji': True},
             'value': 'platform_problem_secure_code_warriors_value',
             'action_id': 'platform_problem_secure_code_warriors_action'}]}, {'type': 'actions', 'elements': [
            {'type': 'button', 'text': {'type': 'plain_text', 'text': 'Licença plataforma', 'emoji': True},
             'value': 'platform_license_secure_code_warriors_value',
             'url': 'https://meli.workplace.com/groups/539467037029524/permalink/1076399480002941/',
             'action_id': 'platform_license_secure_code_warriors_actions'}]}, {'type': 'divider'}]
    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_ssdlc_strategy():
    strategy = SSDLCStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"
    assert result_strategy["message_params"]["text"] == "Você foi redirecionado para o curso <https://learninghub-int.mercadolibre.com/courses/course-v1:it_prod+S-SDLC+2023_v2/course/|SSDLC>."


def test_course_links_secure_code_warriors_strategy():
    strategy = CourseLinksSecureCodeWarriorsStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["blocks"] == [{'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*<https://portal.securecodewarrior.com/#/courses/course-list/fb42f853-8bc4-414e-941c-b58ddd6d87f0|MELI Top 5 Backend / Machine Learning (Recomendado)>*'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*<https://portal.securecodewarrior.com/#/courses/course-list/a1bcb123-6c47-468f-9983-5321ea36abd9|MELI Top 5 Frontend (Recomendado)>*'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*<https://portal.securecodewarrior.com/#/courses/course-list/0f8343e9-23e5-4db1-87c2-747ded0a3f92|MELI Top 5 Mobile (Recomendado)>*'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*<https://portal.securecodewarrior.com/#/courses/course-list/ef7ba068-fef0-47d8-87f2-6fd0116c082d|MELI Top 4 Data Science / FDA (Recomendado)>*'}}]
    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_platform_problem_secure_code_warriors_strategy():
    strategy = PlatformProblemSecureCodeWarriorsStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )
    assert result_strategy["message_params"]["blocks"] == [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Cuáles son los cursos que todo desarrollador de MELI necesita hacer para se considerar como capacitado?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '> • Todos los Devs/PLs - Ciclo de vida de Desarrollo Seguro (S-SLDC) - ESP / PORT\n> • Si eres un Dev/TL Frontend - Frontend Top 10\n> • Si eres un Dev/TL Mobile - Mobile Top 6\n> • Si eres un Dev/TL Backend - Meli Top 10 (Backend)'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Cuál es el período de validez de los cursos?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Todo los cursos de Desarrollo Seguro tienen validez de 365 dias y debemos reforzar el conocimiento todo año.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Hay otros cursos en la plataforma o solo los recomendados?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Además de los 3 cursos recomendados para todos los Devs, hay más de 15 cursos en la plataforma y todos pueden hacer.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿En cuál link yo me registro en la plataforma Secure Code Warrior?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>https://securecodewarrior.com/meli, no olvides registrarte con tu correo corporativo.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Cuánto tiempo tengo para calificar después de registrarme en la plataforma?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>La licencia de Secure Code Warrior tiene una duración de 14 dias.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*Mi licencia venció pero quiero tomar más cursos, ¿cómo puedo proceder?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Es solo registrarse de nuevo con el mismo link de registro.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*Mi licencia venció y no había terminado el curso, ¿pierdo mi avance?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Si el curso esta finalizado, queda registrado y no se pierde. Si al vencimiento de la licencia, el curso no fue finalizado, el progreso se pierde.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Dónde puedo ver si ya estoy capacitad@?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '> • Puede acceder directamente a nuestros tableros:\n> • Capacitados por Usuario - Visualizar si está capacitado o no y cual fue el ultimo curso echo.\n> • Capacitados por Curso - Visualizar todos los cursos echos en los últimos 365 dias.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*Tengo el error: Tu organización tiene inicio de sesión único configurado, pero tu cuenta aún no ha sido habilitada en nuestra plataforma.*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Debes registrarte primero en la plataforma antes de intentar iniciar sesión. Link de registro: https://portal.securecodewarrior.com/#/register/526126899721'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Terminé mi curso en la plataforma, ¿cuántos días se actualiza el tablero de Tableau?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>Después de finalizar el curso, espere al menos 1 día hábil para que se actualice el tablero.'}}, {'type': 'divider'}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*¿Este año ya hice uno de los cursos recomendados, ¿debo volver a hacer?*'}}, {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '>No será necesario, basta con consultar en Tableau el curso que queda por completar y finalizarlo.'}}, {'type': 'divider'}]
    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_security_guardians_strategy():
    strategy = SecurityGuardiansStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["text"] == "Acesse o canal <slack://channel?team=T04HCSY9YQ0&id=C05KFKUHXSQ|#canal-guardians> para mais informações"
    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_dashboard_strategy():
    strategy = DashboardStrategy()
    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["blocks"] == [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': 'Você selecionou as opções de dashboard! Segue abaixo as opções:'}}, {'type': 'divider'}, {'type': 'actions', 'elements': [{'type': 'button', 'text': {'type': 'plain_text', 'text': 'Meu email não está no dashboard', 'emoji': True}, 'value': 'email_not_in_dashboard_value', 'action_id': 'email_not_in_dashboard_action'}]}, {'type': 'actions', 'elements': [{'type': 'button', 'text': {'type': 'plain_text', 'text': 'Status de capacitado está desatualizado', 'emoji': True}, 'value': 'status_not_updated_value', 'action_id': 'status_not_updated_action'}]}]
    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_email_status_update_strategy():
    strategy = EmailStatusUpdateStrategy()
    result_strategy = strategy.execute(
        payload=container_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["text"] == 'Enviamos mensagem para os nossos analistas, em breve entraremos em contato com você por aqui! Caso ainda não tenha detalhado sua dúvida, por favor, escreva aqui'
    assert result_strategy["message_params"]["thread_ts"] == "123.456"


def test_platform_license_secure_code_warriors_strategy():
    strategy = PlatformLicenseSecureCodeWarriorsStrategy()

    result_strategy = strategy.execute(
        payload=generic_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["text"] == 'Você foi redirecionado para o <https://meli.workplace.com/groups/539467037029524/permalink/1076399480002941/|Workplace> para mais informações.'
    assert result_strategy["message_params"]["thread_ts"] == "123"


def test_still_need_help_strategy():
    strategy = StillNeedHelpStrategy()

    result_strategy = strategy.execute(
        payload=container_payload,
        slack_service=fake_slack_service
    )

    assert result_strategy["message_params"]["channel"] == "123"
    assert result_strategy["message_params"]["text"] == 'Enviamos mensagem para os nossos analistas, em breve entraremos em contato com você por aqui! Caso ainda não tenha detalhado sua dúvida, por favor, escreva abaixo'
    assert result_strategy["message_params"]["thread_ts"] == "123.456"



