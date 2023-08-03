import json

from flask import Blueprint, request, Response, jsonify
from slack_sdk.signature import SignatureVerifier

from src.environment import env
from src.services.events_service.events_service import handle_events
from src.services.interactive_service.interactive_service import handle_actions, handle_view_flow

slack_events_blueprint = Blueprint('slack_events', __name__)
signature_verifier = SignatureVerifier(env.get_signing_secret())


@slack_events_blueprint.route("/slack/events", methods=["POST"])
def handle_slack_events():
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return jsonify({"error": "Invalid request"}), 403

    data = request.get_json()

    if data.get("event") is not None:
        return handle_events(data["event"])

    return Response(), 200


@slack_events_blueprint.route("/interactive-endpoint", methods=["POST"])
def echo_interactive():
    payload = json.loads(request.form['payload'])
    if not payload["user"]:
        return Response(), 200

    # Actions flow
    if payload.get("actions") is not None:
        result = handle_actions(payload)
        if result is not None:
            return Response(), 200

    # View Flow
    if payload.get("view") is not None:
        result = handle_view_flow(payload)
        if result is not None:
            return Response(), 200

    print(payload)
    return {"opa": "opa"}, 200
