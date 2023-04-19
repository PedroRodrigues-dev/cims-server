commandDict = {
    "help": "Show the list of all commands",
}


def help():
    message = ""

    for item in commandDict:
        if message != "":
            message = f"{message}\n{item}: {commandDict[item]}"
        else:
            message = f"{item}: {commandDict[item]}"

    return message


commandCall = {"help": help}
