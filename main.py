import threading
from tools import keepAlive, interpreter


def main():
    threading.Thread(target=keepAlive.init).start()
    threading.Thread(target=interpreter.messageSystem).start()
    print("CIMS-SERVER Started")


if __name__ == "__main__":
    main()
