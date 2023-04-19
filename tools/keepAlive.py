import json
from time import sleep
import pika
from configs import rabbit
from configs.environment import serverName


def init():
    while 1:
        connection = rabbit.connect()

        queueName = "keepAlive"

        channel = connection.channel()

        channel.queue_declare(queue=queueName, durable=True)

        channel.basic_publish(
            exchange="",
            routing_key=queueName,
            body=json.dumps({"serverName": serverName(), "status": "online"}),
            properties=pika.BasicProperties(delivery_mode=2),
        )

        channel.close()

        connection.close()

        sleep(2)
