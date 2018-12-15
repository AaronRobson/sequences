from fractions import Fraction
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

# http://en.wikipedia.org/wiki/Harmonic_number


def Reciprocal(number):
    return Fraction(1, number)


fractionExample = Fraction(2, 3)
assert Reciprocal(Reciprocal(fractionExample)) == fractionExample


def StrictlyPositiveIntegers():
    return count(1)


def StrictlyPositiveReciprocals():
    return map(Reciprocal, StrictlyPositiveIntegers())


def AccumulatedStrictlyPositiveReciprocals():
    return accumulate(StrictlyPositiveReciprocals())


HarmonicNumbers = AccumulatedStrictlyPositiveReciprocals

if __name__ == '__main__':
    from itertoolsrecipes import take

    numberToShow = 10
    print('Harmonic Numbers; the first {}.'.format(numberToShow))
    for n in take(numberToShow, AccumulatedStrictlyPositiveReciprocals()):
        print(n)
