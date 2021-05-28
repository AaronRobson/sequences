#!/usr/bin/python

import itertools
from math import sqrt
from collections import Counter
from functools import reduce
from operator import or_
from typing import List

from product import product
from itertoolsrecipes import first_n, len_of_generator
from exceed import until_exceeded


def is_even(num):
    return is_divisable(int(num), 2)


def is_odd(num):
    return not is_even(num)


def _make_next(func):
    def _next(num):
        if func(num):
            return num + 2
        else:
            return num + 1

    return _next


next_even = _make_next(is_even)
next_odd = _make_next(is_odd)


def is_divisable(numerator, denominator):
    '''Encapsulate division by zero error in this one place.
    '''
    try:
        return numerator % denominator == 0
    except ZeroDivisionError:
        return False


FIRST_PRIME = 2


class PrimeCollection():
    _cache: List[int] = []

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
            number = next_odd(self.last)
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

    def _add_to_cache(self, number):
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
        def new_primes():
            while True:
                yield self.__next__()

        return itertools.chain(self.cache, new_primes())

    def __next__(self):
        '''If working from cache the next tried number will always be the next
        odd number after the last in the cache.

        Works on the principle of http://en.wikipedia.org/wiki/Trial_division
        '''

        def possibly_find_factor(num):
            '''Should not be run until squareRoot variable is initialised
            from outside this method.
            '''
            return num <= square_root

        for n in self._potentialPrimes:
            square_root = int(sqrt(n))
            for prime in itertools.takewhile(possibly_find_factor, self._cache):
                if is_divisable(n, prime):
                    break
            else:
                self._add_to_cache(n)
                return n

    def __getitem__(self, key):
        if type(key) != int:
            raise TypeError('Only integer indexes may be used.')

        if key <= 0:
            raise ValueError('Primes are indexed starting at 1.')

        for prime in primes_first_n(key):
            last_prime = prime

        return last_prime


def primes_first_n(number_of_primes):
    return first_n(PrimeCollection(), number_of_primes)


def nth_prime(nth_prime):
    return PrimeCollection()[nth_prime]


def is_prime(number):
    '''Doesn't require PrimeFactors.
    Should be simpler.

    Same as:
    return len(tuple(PrimeFactors(number))) == 1
    '''
    number = int(number)

    for prime in until_exceeded(number, PrimeCollection()):
        if prime == number:
            return True
    else:
        return False


def prime_factors(number):
    '''Return is in sorted order.
    If the length of the return is 1 it indicates the number is prime.
    '''
    number = int(number)
    if number < FIRST_PRIME:
        raise ValueError(
            'Lowest allowed number is %d, %r rejected.' % (
                FIRST_PRIME, number))

    for prime in PrimeCollection():
        while is_divisable(number, prime):
            yield prime
            number //= prime

        if number == 1:
            break


def prime_factors_without_duplicates(number):
    '''Takes advantage of the fact that the "PrimeFactors" generator
    returns duplicate numbers consecutively
    (as they are in ascending order).
    '''
    last_number = None
    for number in prime_factors(number):
        if number != last_number:
            yield number
            last_number = number


def count_of_distinct_prime_factors(number):
    return len_of_generator(prime_factors_without_duplicates(number))


def prime_factors_dict(*numbers):
    output = Counter()

    for number in numbers:
        number = int(number)
        assert(0 < number)

        if 1 < number:
            for prime_factor in prime_factors(number):
                output[prime_factor] += 1

    return output


def factors(number):
    '''Sorted order with no duplicates.
    Not necessarily primes.
    '''
    assert(0 < number)

    def combinations_with_duplicates(items):
        items = tuple(items)

        for lengths in range(1, len(items)+1):
            for item in itertools.combinations(items, lengths):
                yield item

    yield 1
    if number != 1:
        for item in sorted(set(map(
                product,
                combinations_with_duplicates(prime_factors(number))))):
            yield item


def highest_factors(numbers):
    '''Similar to an intersection of the sets of the prime factors of each of
    the numbers in a sequence.
    Returns a dictionary containing as it's keys all the applicable
    prime factors and the values indicate the largest amount of them contained
    as factors within a single number from the sequence.
    '''
    # "or_" means the the union operator in this context.
    return reduce(or_, map(prime_factors_dict, numbers), Counter())


def factor_dict_to_number(factor_dict):
    return product(key ** value for key, value in factor_dict.items())


def least_common_multiple(numbers):
    return factor_dict_to_number(highest_factors(numbers))


if __name__ == "__main__":
    print('Prime Generator')

    from time import sleep

    def print_primes():
        for prime in PrimeCollection():
            print(prime)
            # seems to be the same tempo as:
            # The Beatles - The White Album - Honey Pie and
            # Nightwish - Angels Fall First - Elvenpath
            sleep(0.42)

    import threading

    t = threading.Thread(target=print_primes)
    t.setDaemon(True)

    print('\nPress Enter to Exit:')
    t.start()
    input()
