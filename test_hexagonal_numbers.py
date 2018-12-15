#!/usr/bin/python

import unittest

import hexagonal_numbers as hn
from itertoolsrecipes import take


class TestHexagonalNumber(unittest.TestCase):

    def test(self):
        self.assertEqual(hn.HexagonalNumber(5), 45)


class TestHexagonalNumbers(unittest.TestCase):

    def test(self):
        self.assertEqual(
            list(take(10, hn.HexagonalNumbers())),
            [1, 6, 15, 28, 45, 66, 91, 120, 153, 190])


class TestIsHexagonalNumber(unittest.TestCase):

    def testPositive(self):
        self.assertTrue(hn.IsHexagonalNumber(45))

    def testNegative(self):
        self.assertFalse(hn.IsHexagonalNumber(46))


if __name__ == "__main__":
    unittest.main()
