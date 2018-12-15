from operator import mul
from functools import reduce


def product(items):
    '''The multiplicative equivalent of the built-in "sum" function.
    '''
    return reduce(mul, items, 1)


if __name__ == "__main__":
    print('Product of empty list is {}.'.format(product(1)))
    print(
        'Product of list of 1-5 inclusive is {}.'.
        format(product(range(1, 4+1))))
