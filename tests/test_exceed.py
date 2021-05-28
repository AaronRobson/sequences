#!/usr/bin/python

from itertools import chain
import unittest

from exceed import until_exceeded, filter_exceeded


small_num, big_num = sorted((8, 10))
values = tuple(chain(range(big_num), range(big_num)))
one_expected = tuple(range(small_num+1))
two_expected = tuple(chain(one_expected, one_expected))


class TestUntilExceeded(unittest.TestCase):

    def test(self):
        self.assertEqual(tuple(until_exceeded(small_num, values)), one_expected)
        self.assertEqual(tuple(until_exceeded(5, [1, 5, 3, 7])), (1, 5, 3))


class TestFilterExceeded(unittest.TestCase):

    def test(self):
        self.assertEqual(tuple(filter_exceeded(small_num, values)), two_expected)
