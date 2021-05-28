#!/usr/bin/python

import unittest

import hexagonal_numbers as hn
from itertoolsrecipes import take


class TestHexagonalNumber(unittest.TestCase):

    def test(self):
        self.assertEqual(hn.hexagonal_number(5), 45)


class TestHexagonalNumbers(unittest.TestCase):

    def test(self):
        self.assertEqual(
            list(take(10, hn.hexagonal_numbers())),
            [1, 6, 15, 28, 45, 66, 91, 120, 153, 190])


class TestIsHexagonalNumber(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(hn.is_hexagonal_number(45))

    def test_negative(self):
        self.assertFalse(hn.is_hexagonal_number(46))
