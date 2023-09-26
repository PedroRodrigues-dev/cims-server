import subprocess


commandDict = {"help": "Show the list of all commands"}


def help():
    return "\n".join([f"{k}: {v}" for k, v in commandDict.items()])


commandCall = {"help": help}
