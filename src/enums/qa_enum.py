"""
Module to define the enums of the questions and answers of the bot.
"""
from enum import Enum


class EnumQuestions(Enum):
    """
    Enumeration containing questions as values.

    Each value represents a question related to the topic.
    """

    QUESTION_1 = (
        "*¿Cuáles son los cursos que todo desarrollador de MELI necesita hacer para se"
        " considerar como capacitado?*"
    )

    QUESTION_2 = "*¿Cuál es el período de validez de los cursos?*"

    QUESTION_3 = "*¿Hay otros cursos en la plataforma o solo los recomendados?*"

    QUESTION_4 = "*¿En cuál link yo me registro en la plataforma Secure Code Warrior?*"

    QUESTION_5 = (
        "*¿Cuánto tiempo tengo para calificar después de registrarme en la plataforma?*"
    )

    QUESTION_6 = (
        "*Mi licencia venció pero quiero tomar más cursos, ¿cómo puedo proceder?*"
    )

    QUESTION_7 = (
        "*Mi licencia venció y no había terminado el curso, ¿pierdo mi avance?*"
    )

    QUESTION_8 = "*¿Dónde puedo ver si ya estoy capacitad@?*"

    QUESTION_9 = (
        "*Tengo el error: Tu organización tiene inicio de sesión único "
        "configurado, pero tu cuenta aún no ha sido habilitada en nuestra plataforma.*"
    )

    QUESTION_10 = (
        "*¿Terminé mi curso en la plataforma, ¿cuántos días se actualiza el "
        "tablero de Tableau?*"
    )

    QUESTION_11 = (
        "*¿Este año ya hice uno de los cursos recomendados, ¿debo volver a hacer?*"
    )


class EnumAnswers(Enum):
    """
    Enumeration containing answers as values.

    Each value represents an answer corresponding to the respective question.
    """

    ANSWER_1 = (
        "> • Todos los Devs/PLs - Ciclo de vida de Desarrollo Seguro (S-SLDC) - ESP / PORT\n"
        "> • Si eres un Dev/TL Frontend - Frontend Top 10\n"
        "> • Si eres un Dev/TL Mobile - Mobile Top 6\n"
        "> • Si eres un Dev/TL Backend - Meli Top 10 (Backend)"
    )

    ANSWER_2 = (
        ">Todo los cursos de Desarrollo Seguro tienen validez de 365 dias "
        "y debemos reforzar el conocimiento todo año."
    )

    ANSWER_3 = (
        ">Además de los 3 cursos recomendados para todos los Devs, hay "
        "más de 15 cursos en la plataforma y todos pueden hacer."
    )

    ANSWER_4 = ">https://securecodewarrior.com/meli, no olvides registrarte con tu correo corporativo."

    ANSWER_5 = ">La licencia de Secure Code Warrior tiene una duración de 14 dias."

    ANSWER_6 = ">Es solo registrarse de nuevo con el mismo link de registro."

    ANSWER_7 = (
        ">Si el curso esta finalizado, queda registrado y no se pierde. "
        "Si al vencimiento de la licencia, el curso no fue finalizado, el progreso se pierde."
    )

    ANSWER_8 = (
        "> • Puede acceder directamente a nuestros tableros:\n"
        "> • Capacitados por Usuario - Visualizar si está capacitado o no y "
        "cual fue el ultimo curso echo.\n"
        "> • Capacitados por Curso - Visualizar todos los cursos echos en los últimos 365 dias."
    )

    ANSWER_9 = (
        ">Debes registrarte primero en la plataforma antes de intentar iniciar sesión. "
        "Link de registro: https://portal.securecodewarrior.com/#/register/526126899721"
    )

    ANSWER_10 = (
        ">Después de finalizar el curso, espere al menos 1 día hábil para "
        "que se actualice el tablero."
    )

    ANSWER_11 = (
        ">No será necesario, basta con consultar en Tableau el curso "
        "que queda por completar y finalizarlo."
    )
