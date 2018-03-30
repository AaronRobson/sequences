#!/usr/bin/python

from itertools import islice
import unittest

import badger

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

class TestBadger(unittest.TestCase):

    def testCycling(self):
        gen = badger.BadgerMushroomSnakeGenerator()
        firstLoop = take(len(badger.full), gen)
        secondLoop = take(len(badger.full), gen)
        self.assertEqual(firstLoop, secondLoop)


if __name__ == "__main__":
    unittest.main()
