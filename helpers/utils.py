def infoMessage(message: str):
    print("{}{}{}\n".format("\033[1;33;40m", message, "\033[0;37;40m"))


def successMessage(message: str):
    print("{}{}{}\n".format("\033[1;32;40m", message, "\033[0;37;40m"))


def errorMessage(message: str):
    print("{}{}{}\n".format("\033[1;31;40m", message, "\033[0;37;40m"))


def coloredInput(message: str):
    print(message, end="")
    print("{}".format("\033[1;36;40m"), end="")
    res = input()
    print("{}".format("\033[0;37;40m"), end="")

    return res

def checkFilePath(path: str):

    if not path.lower().endswith(".csv"):
        return path + ".csv"

    return path