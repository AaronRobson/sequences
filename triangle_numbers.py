from itertools import count, accumulate
from itertoolsrecipes import FirstN, CollectionsEqual
from exceed import UntilExceeded

def TriangleNumber(n):
    '''Does floor division to convert from float to int.
    Otherwise answers are floats which are exactly the same as integers.
    '''
    n = int(n)
    return n*(n+1) // 2

def TriangleNumberAlt(n):
    return sum(range(1, n+1))

def TriangleNumbers():
    #return map(TriangleNumber, count(1))
    return accumulate(count(1))

assert(CollectionsEqual(FirstN(TriangleNumbers(), 10), (1, 3, 6, 10, 15, 21, 28, 36, 45, 55)))

def IsTriangleNumber(number):
    last = None

    for num in UntilExceeded(number, TriangleNumbers()):
        last = num

    return number == last

if __name__ == "__main__":
    from time import sleep

    print('Triangle Numbers (Ctrl-C to Exit):')

    for tNum in TriangleNumbers():
        print(tNum)
        sleep(0.42)
