from operator import mul
from functools import reduce


def product(items):
    '''The multiplicative equivalent of the built-in "sum" function.
    '''
    return reduce(mul, items, 1)
