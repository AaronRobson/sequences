#!/usr/bin/python

'''From:
https://docs.python.org/3.8/library/itertools.html#itertools-recipes

Using the names as used in Haskell code as these seem to be the cleanest.
'''

from itertools import islice

from operator import eq as equal
from itertools import islice, chain, count

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

####

class DifferentLengthsError(IndexError):
    pass

def FirstN(generator, n=None):
    '''Developed from: http://wiki.python.org/moin/Generators
    http://linuxgazette.net/100/pramode.html
    '''
    if n is not None:
        result = take(n, generator)
        if len(result) < n:
            raise DifferentLengthsError('Requested amount exceeds the number in the iteration.')
        return result
    else:
        return generator

def SkipFirstN(generator, n=None):
    return islice(generator, n, None)

def NthTerm(generator, n=None):
    if (n is not None) and (n < 0):
        raise ValueError('Index must be above zero; %r is invalid.' % (n))

    for item in FirstN(generator, n):
        value = item

    #"value" should have a value otherwise "FirstN" would have raised a "DifferentLengthsError".
    return value

def NthTermZeroBased(generator, n=None):
    if n is not None:
        if n <= 0:
            raise ValueError('Index must be zero or above; %r is invalid.' % (n))
        else:
            return NthTerm(generator, n+1)
    else:
        assert n is None
        return NthTerm(generator, n)

def ZipErrorIfDifferentLengths(*collections):
    iterators = tuple(map(iter, collections))

    while True:
        ended = None
        output = []
        for iterator in iterators:
            try:
                output.append(next(iterator))
            except StopIteration:
                newEnded = True
            else:
                newEnded = False

            if (ended != None) and (ended != newEnded):
                raise DifferentLengthsError('The iterations are of unequal lengths.')

            ended = newEnded

        if ended:
            break

        yield tuple(output)

def ItemsEqual(*items):
    if items:
        first = items[0]
        others = items[1:]
        return all(equal(first, other) for other in others)
    else:
        return True

def CollectionsEqual(*collections):
    if collections:
        try:
            return all(ItemsEqual(*items) for items in ZipErrorIfDifferentLengths(*collections))
        except DifferentLengthsError:
            return False
    else:
        return True

def LenOfGenerator(gen):
    '''Will use up the generator, use itertools.tee to make independently usable copies beforehand if required.

    Found at:
    http://stackoverflow.com/questions/393053/length-of-generator-output
    '''
    return sum(1 for _ in gen)

def LenOfGeneratorIsNotLessThan(gen, minimumLen):
    '''The idea being to save resources by allowing generators to terminate earlier
    when the length is known to be enough for some purpose.
    '''
    MIN_LEN = 0
    if minimumLen < MIN_LEN:
        raise ValueError('Length must be at least %r, %r rejected.' % (MIN_LEN, minimumLen))

    if minimumLen == MIN_LEN:
        return True

    for currentLen, item in enumerate(gen, 1):
        if minimumLen <= currentLen:
            return True
    else:
        return False

#testing an idea for showing the surrounding padding
def RollingCollection(items, sampleSize, pad=0, padValue=None):
    if sampleSize < 1:
        raise ValueError('Sample Size must be at least 1.')

    if pad < 0:
        raise ValueError('Padding should be at least 0.')

    paddingItems = (padValue,) * pad
    items = chain(paddingItems, items, paddingItems)

    items = tuple(items)

    for i in range(len(items)-sampleSize+1):
        yield items[i:i+sampleSize]

def AreConsecutive(items):
    items = iter(items)

    try:
        firstValue = next(items)
    except StopIteration:
        return True
    else:
        return all(item == expected for item, expected in zip(chain([firstValue], items), count(firstValue)))

if __name__ == "__main__":
    print('Itertools Recipes:')
