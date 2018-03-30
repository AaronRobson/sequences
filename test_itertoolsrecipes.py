#!/usr/bin/python

import unittest

from itertoolsrecipes import take


class TestTake(unittest.TestCase):

    def testSimple(self):
        self.assertEqual(list(take(3, range(5))), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
