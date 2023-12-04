import threading
from tools import keepAlive, interpreter, threadMonitor


def main():
    threading.Thread(target=keepAlive.init).start()
    threading.Thread(target=interpreter.messageSystem).start()
    threading.Thread(target=threadMonitor.threadsMonitor).start()
    print("CIMS-SERVER Started")


if __name__ == "__main__":
    main()
