import time
from configs import broker, environment


def init():
    while True:
        broker.sendMessage(
            "keepAlive", {"serverName": environment.serverName(), "status": "online"}
        )

        time.sleep(1)
