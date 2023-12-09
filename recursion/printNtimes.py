from typing import *


def printNtimes(n: int) -> None:

    printString = " ".join(recursiveFunc(n, []))
    print(printString)


def recursiveFunc(n, arrayN):

    if n == 0:
        return arrayN

    arrayN.append("Coding Ninjas")
    # cooked
    return recursiveFunc(n - 1, arrayN)


printNtimes(5)
