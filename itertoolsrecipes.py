#!/usr/bin/python

'''From:
https://docs.python.org/3.8/library/itertools.html#itertools-recipes

Using the names as used in Haskell code as these seem to be the cleanest.
'''

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
