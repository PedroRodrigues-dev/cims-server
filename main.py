import threading
from configs.environment import serverName
from configs.rabbit import reciveMessages, clearQueues
from tools import keepAlive


def main():
    clearQueues(serverName())
    threading.Thread(target=keepAlive.init).start()
    threading.Thread(target=reciveMessages, args=[serverName()]).start()


if __name__ == "__main__":
    main()
