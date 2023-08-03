"""
Slack Events Blueprint

This module provides routes for handling incoming Slack events and interactive actions.
"""

import json
from flask import Blueprint, request, Response
from slack_sdk.signature import SignatureVerifier

from src.environment import env
from src.services.events_service.events_service import handle_events
from src.services.interactive_service.interactive_service import handle_actions

slack_events_blueprint = Blueprint('slack_events', __name__)
signature_verifier = SignatureVerifier(env.get_signing_secret())


@slack_events_blueprint.route("/slack/events", methods=["POST"])
def handle_slack_events() -> tuple[Response, int]:
    """
    Handle incoming Slack events received at the "/slack/events" endpoint.

    This function verifies the incoming request, processes the event payload,
    and delegates handling to appropriate event and action handlers.

    Returns:
        tuple[Response, int]: A tuple containing a response object and an HTTP status code.
    """
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return Response(), 403

    data = request.get_json()

    if data.get("event") is not None:
        response = handle_events(data["event"])
        if response is not None:
            return Response(), 200

    return Response(), 200


@slack_events_blueprint.route("/interactive-endpoint", methods=["POST"])
def interactive_endpoint() -> tuple[Response, int]:
    """
    Handle incoming interactive actions received at the "/interactive-endpoint" endpoint.

    This function processes interactive action payloads, and
    delegates handling to appropriate action.

    Returns:
        tuple[Response, int]: A tuple containing a response object and an HTTP status code.
    """
    payload = json.loads(request.form['payload'])
    if not payload["user"]:
        return Response(), 200

    # Actions flow
    if payload.get("actions") is not None:
        result = handle_actions(payload)
        if result is not None:
            return Response(), 200

    return Response(), 200
