import json
from tools.commands import commandDict, commandCall
from configs import broker, environment
from tools.timeLang import interpreter as tilaInterpreter


def interpreter(message):
    command = message["body"]

    if type(command) == dict:
        body = tilaInterpreter(command["code"])

    else:
        if command in commandDict:
            body = commandCall[command]()
        else:
            body = "command not found"

    return {
        "authorId": message["authorId"],
        "channelId": message["channelId"],
        "body": body,
    }


def messageSystem():
    connection = broker.getConnection()
    channel = connection.channel()

    channel.queue_declare(queue=environment.serverName(), durable=True)

    def __callback(ch, method, properties, body):
        body = json.loads(body.decode())
        broker.sendMessage("responses", interpreter(body))

    channel.basic_consume(
        queue=environment.serverName(), on_message_callback=__callback, auto_ack=True
    )

    channel.start_consuming()

    channel.close()
    connection.close()
