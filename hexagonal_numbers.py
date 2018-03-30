from itertools import count, accumulate

from exceed import UntilExceeded

def HexagonalNumber(n):
    n = int(n)
    return n*(2*n-1)

def HexagonalNumbers():
    return map(HexagonalNumber, count(1))

def IsHexagonalNumber(number):
    last = None

    for num in UntilExceeded(number, HexagonalNumbers()):
        last = num

    return number == last

if __name__ == "__main__":
    from time import sleep

    print('Hexagonal Numbers (Ctrl-C to Exit):')

    for tNum in HexagonalNumbers():
        print(tNum)
        sleep(0.42)
