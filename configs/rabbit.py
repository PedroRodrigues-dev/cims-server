import json
import logging
import time
import pika

from configs.environment import (
    rabbitHost,
    rabbitPassword,
    rabbitUsername,
    systemTimeout,
)
from tools.interpreter import interpreter


def connect():
    credentials = pika.PlainCredentials(rabbitUsername(), rabbitPassword())
    parameters = pika.ConnectionParameters(rabbitHost(), 5672, "/", credentials)
    connection = None

    try:
        connection = pika.BlockingConnection(parameters)
    except pika.exceptions.AMQPConnectionError:
        connection = None

    while connection is None:
        print("Trying to reconnect with rabbitMQ")
        time.sleep(systemTimeout())
        connect()

    return connection


def clearQueues(queueName):
    connection = connect()

    channel = connection.channel()

    channel.queue_delete(queue=f"{queueName}-bot")
    channel.queue_delete(queue=f"{queueName}-server")

    connection.close()


def sendMessage(queueName, queueMessage):
    connection = connect()

    queueName = f"{queueName}-server"

    channel = connection.channel()

    channel.queue_declare(queue=queueName, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=queueName,
        body=json.dumps(queueMessage),
        properties=pika.BasicProperties(delivery_mode=2),
    )

    channel.close()

    connection.close()


def reciveMessages(queueName):
    originalQueueName = queueName

    if queueName:
        connection = connect()

        queueName = f"{queueName}-bot"

        channel = connection.channel()

        channel.queue_declare(queue=queueName, durable=True)

        def callback(ch, method, properties, body):
            message = interpreter(json.loads(body))

            sendMessage(originalQueueName, message)

        channel.basic_consume(
            queue=queueName, on_message_callback=callback, auto_ack=True
        )

        channel.start_consuming()

        connection.close()
