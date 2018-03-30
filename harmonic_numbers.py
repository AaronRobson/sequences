from fractions import Fraction
from itertools import count, accumulate

#http://en.wikipedia.org/wiki/Harmonic_number

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
