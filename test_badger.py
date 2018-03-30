#!/usr/bin/python

import unittest

import badger
from itertoolsrecipes import take

class TestBadger(unittest.TestCase):

    def testCycling(self):
        gen = badger.BadgerMushroomSnakeGenerator()
        firstLoop = take(len(badger.full), gen)
        secondLoop = take(len(badger.full), gen)
        self.assertEqual(firstLoop, secondLoop)


if __name__ == "__main__":
    unittest.main()
