#!/usr/bin/python

import unittest

import badger
from itertoolsrecipes import take


class TestIterToolsRecipes(unittest.TestCase):

    def testTake(self):
        self.assertEqual(list(take(3, range(5))), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
