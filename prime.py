#!/usr/bin/python

import itertools
from math import sqrt
from collections import Counter
from functools import reduce
from operator import or_

from product import product
from itertoolsrecipes import FirstN, LenOfGenerator
from exceed import UntilExceeded


def IsEven(num):
    return IsDivisable(int(num), 2)


def IsOdd(num):
    return not IsEven(num)


def _MakeNext(func):
    def _Next(num):
        if func(num):
            return num + 2
        else:
            return num + 1

    return _Next


NextEven = _MakeNext(IsEven)
NextOdd = _MakeNext(IsOdd)


def IsDivisable(numerator, denominator):
    '''Encapsulate division by zero error in this one place.
    '''
    try:
        return numerator % denominator == 0
    except ZeroDivisionError:
        return False


FIRST_PRIME = 2


class PrimeCollection():
    _cache = []

    def __init__(self, cache=None):
        '''"cache" if given is trusted to be accurate.
        '''
        if cache is None:
            cache = []

        # a list accepted from somewhere else is mutable and may be changed
        # later affecting this data so tupling it first
        cache = list(tuple(cache))

        # save cache only if it is larger than the current one
        if len(self._cache) < len(cache):
            self._cache = cache

        # setup next
        if self.last:
            number = NextOdd(self.last)
        else:
            number = FIRST_PRIME

        assert(FIRST_PRIME <= number)

        self._potentialPrimes = itertools.count(number)

    @property
    def last(self):
        try:
            return self.cache[-1]
        except IndexError:
            return None

    def __len__(self):
        return len(self.cache)

    @property
    def cache(self):
        return tuple(self._cache)

    def _AddToCache(self, number):
        '''Ensure that multiple threads working at the same time cannot fail.
        May want to consider a set type,
        to totally avoid the possiblity of duplicates.
        '''
        if self.last is None or self.last < number:
            self._cache.append(number)

    def __iter__(self):
        '''All primes 2 and up, iterating through collected ones then
        generating new ones.

        Always yields full list (until stopped), uses cached calculated values
        where available.
        '''
        def NewPrimes():
            while True:
                yield self.__next__()

        return itertools.chain(self.cache, NewPrimes())

    def __next__(self):
        '''If working from cache the next tried number will always be the next
        odd number after the last in the cache.

        Works on the principle of http://en.wikipedia.org/wiki/Trial_division
        '''

        def PossiblyFindFactor(num):
            '''Should not be run until squareRoot variable is initialised
            from outside this method.
            '''
            return num <= squareRoot

        for n in self._potentialPrimes:
            squareRoot = int(sqrt(n))
            for prime in itertools.takewhile(PossiblyFindFactor, self._cache):
                if IsDivisable(n, prime):
                    break
            else:
                self._AddToCache(n)
                return n

    def __getitem__(self, key):
        if type(key) != int:
            raise TypeError('Only integer indexes may be used.')

        if key <= 0:
            raise ValueError('Primes are indexed starting at 1.')

        for prime in PrimesFirstN(key):
            lastPrime = prime

        return lastPrime


def PrimesFirstN(numberOfPrimes):
    return FirstN(PrimeCollection(), numberOfPrimes)


def NthPrime(nthPrime):
    return PrimeCollection()[nthPrime]


def IsPrime(number):
    '''Doesn't require PrimeFactors.
    Should be simpler.

    Same as:
    return len(tuple(PrimeFactors(number))) == 1
    '''
    number = int(number)

    for prime in UntilExceeded(number, PrimeCollection()):
        if prime == number:
            return True
    else:
        return False


def PrimeFactors(number):
    '''Return is in sorted order.
    If the length of the return is 1 it indicates the number is prime.
    '''
    number = int(number)
    if number < FIRST_PRIME:
        raise ValueError(
            'Lowest allowed number is %d, %r rejected.' % (
                FIRST_PRIME, number))

    for prime in PrimeCollection():
        while IsDivisable(number, prime):
            yield prime
            number //= prime

        if number == 1:
            break


def PrimeFactorsWithoutDuplicates(number):
    '''Takes advantage of the fact that the "PrimeFactors" generator
    returns duplicate numbers consecutively
    (as they are in ascending order).
    '''
    lastNumber = None
    for number in PrimeFactors(number):
        if number != lastNumber:
            yield number
            lastNumber = number


def CountOfDistinctPrimeFactors(number):
    return LenOfGenerator(PrimeFactorsWithoutDuplicates(number))


def PrimeFactorsDict(*numbers):
    output = Counter()

    for number in numbers:
        number = int(number)
        assert(0 < number)

        if 1 < number:
            for primeFactor in PrimeFactors(number):
                output[primeFactor] += 1

    return output


def Factors(number):
    '''Sorted order with no duplicates.
    Not necessarily primes.
    '''
    assert(0 < number)

    def CombinationsWithDuplicates(items):
        items = tuple(items)

        for lengths in range(1, len(items)+1):
            for item in itertools.combinations(items, lengths):
                yield item

    yield 1
    if number != 1:
        for item in sorted(set(map(
                product,
                CombinationsWithDuplicates(PrimeFactors(number))))):
            yield item


def HighestFactors(numbers):
    '''Similar to an intersection of the sets of the prime factors of each of
    the numbers in a sequence.
    Returns a dictionary containing as it's keys all the applicable
    prime factors and the values indicate the largest amount of them contained
    as factors within a single number from the sequence.
    '''
    # "or_" means the the union operator in this context.
    return reduce(or_, map(PrimeFactorsDict, numbers), Counter())


def FactorDictToNumber(factorDict):
    return product(key ** value for key, value in factorDict.items())


def LeastCommonMultiple(numbers):
    return FactorDictToNumber(HighestFactors(numbers))


if __name__ == "__main__":
    print('Prime Generator')

    from time import sleep

    def PrintPrimes():
        for prime in PrimeCollection():
            print(prime)
            # seems to be the same tempo as:
            # The Beatles - The White Album - Honey Pie and
            # Nightwish - Angels Fall First - Elvenpath
            sleep(0.42)

    import threading

    t = threading.Thread(target=PrintPrimes)
    t.setDaemon(True)

    print('\nPress Enter to Exit:')
    t.start()

    # keep the window open
    input()
