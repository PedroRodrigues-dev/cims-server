import datetime
import threading
from time import sleep


def tila(line):
    tokens = line.replace("#![", "").replace("]!#", "").split(" ")
    timeDelta = ""

    if len(tokens) != 3:
        return f"invalid tila code -> {line}"

    if tokens[0].lower() == "aways":
        try:
            tokens[1] = int(tokens[1])
        except:
            return f"invalid tila code -> {line}"

        if tokens[2].lower() == "seconds":
            timeDelta = datetime.timedelta(seconds=tokens[1])

        elif tokens[2].lower() == "minutes":
            timeDelta = datetime.timedelta(minutes=tokens[1])

        elif tokens[2].lower() == "hours":
            timeDelta = datetime.timedelta(hours=tokens[1])

        elif tokens[2].lower() == "days":
            timeDelta = datetime.timedelta(hours=tokens[1] * 24)

        elif tokens[2].lower() == "weeks":
            timeDelta = datetime.timedelta(weeks=tokens[1])

        else:
            return f"invalid tila code -> {line}"
    else:
        return f"invalid tila code -> {line}"

    return timeDelta


def interpreter(code):
    lines = code.split("\n")

    if lines[0].startswith("#![") and lines[0].endswith("]!#"):
        timeDelta = tila(lines[0])
    else:
        return "tila code not found"

    lines.pop(0)

    if type(timeDelta) == str:
        return timeDelta

    for line in lines:
        if line.startswith("#![") and line.endswith("]!#"):
            return f"tila code in wrong position -> {line}"
        if line.find("input") != -1 or line.find("print") != -1:
            return f"invalid tila code -> {line}"

    pythonCode = "\n".join(lines)

    threading.Thread(target=routine, args=[pythonCode, timeDelta]).start()


def routine(pythonCode, timeDelta):
    dateTimeNow = datetime.datetime.now()
    routineTime = dateTimeNow

    while 1:
        dateTimeNow = datetime.datetime.now()

        if (routineTime - dateTimeNow).total_seconds() <= 0:
            exec(pythonCode)
            routineTime = dateTimeNow + timeDelta

        sleep(0.2)
