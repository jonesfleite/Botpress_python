from flask import Flask
import logging
import sys
from flask import jsonify
from flask import request
import requests
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)

action_handlers = {""}

employees = [
    {
        "id": "mhopkins",
        "first_name": "Mike",
        "last_name": "Hopkins",
        "age": 34,
        "department": "IT",
    },
    {
        "id": "lsimpson",
        "first_name": "Lisa",
        "last_name": "Simpson",
        "age": 31,
        "department": "Sales",
    },
    {
        "id": "fhamilton",
        "first_name": "Frank",
        "last_name": "Hamilton",
        "age": 29,
        "department": "HR",
    },
]


@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"


@app.route("/actions/<bot_id>", methods=["GET"])
def actions(bot_id):
    logging.info(f"Requesting actions for bot {bot_id}")
    # Aqui, bot_it não é usado, mas você pode usá-lo para restringir a lista de ações
    # permitido, com base no ID do bot solicitante

    return jsonify(
        [
            {
                "name": "list_employees",
                "description": "Lista funcionários",
                "category": "HR",
                "params": [],
            },
            {
                "name": "get_employee",
                "description": "Obtenha detalhes de um funcionário",
                "category": "HR",
                "params": [
                    {
                        "name": "employee_id",
                        "type": "string",
                        "required": True,
                        "description": "O identificador único para o funcionário obter",
                    }
                ],
            },
        ]
    )


@app.route("/action/run", methods=["POST"])
def run_action():
    request_body = request.json

    print(f"Received request: {request_body}")

    action_name = request_body["actionName"]
    bot_id = request_body["botId"]
    token = request_body["token"]
    action_args = request_body["actionArgs"]
    incoming_event = request_body["incomingEvent"]

    if action_name == "list_employees":
        botpress_server_url = os.environ["BOTPRESS_SERVER_URL"]
        requests.post(
            f"{botpress_server_url}/api/v1/sdk/events/replyToEvent",
            json={
                "event": incoming_event,
                "payloads": [
                    {"type": "text", "text": "OK, O servidor Python está listando funcionários"}
                ],
            },
            headers={"Authorization": f"bearer {token}"},
        )

        incoming_event["state"]["temp"]["employees"] = [
            f'{e["first_name"]} {e["last_name"]}' for e in employees
        ]
    elif action_name == "get_employee":
        employee_id = action_args["employee_id"]
        incoming_event["state"]["temp"]["employee"] = next(
            e for e in employees if e["id"] == employee_id
        )
    else:
        raise RuntimeError(f"Could not find handler for action: {action_name}")

    return jsonify({"incomingEvent": incoming_event})
