import json
from tools.commands import commandDict, commandCall


def interpreter(message):
    if message["command"] in commandDict:
        body = commandCall[message["command"]]()

        return json.dumps({"author_id": message["author_id"], "body": body})
    else:
        return json.dumps(
            {"author_id": message["author_id"], "body": "command not found"}
        )
