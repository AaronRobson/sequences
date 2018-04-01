from itertools import count

try:
    from itertools import accumulate
except ImportError:
    import operator
    # https://docs.python.org/3.8/library/itertools.html#itertools.accumulate
    def accumulate(iterable, func=operator.add):
        'Return running totals'
        # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
        # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
        it = iter(iterable)
        try:
            total = next(it)
        except StopIteration:
            return
        yield total
        for element in it:
            total = func(total, element)
            yield total

try:
    from itertools import imap as map
except ImportError:
    pass

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
