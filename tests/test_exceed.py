#!/usr/bin/python

from itertools import chain
import unittest

from exceed import UntilExceeded, FilterExceeded


smallNum, bigNum = sorted((8, 10))
values = tuple(chain(range(bigNum), range(bigNum)))
oneExpected = tuple(range(smallNum+1))
twoExpected = tuple(chain(oneExpected, oneExpected))


class TestUntilExceeded(unittest.TestCase):

    def test(self):
        self.assertEqual(tuple(UntilExceeded(smallNum, values)), oneExpected)
        self.assertEqual(tuple(UntilExceeded(5, [1, 5, 3, 7])), (1, 5, 3))


class TestFilterExceeded(unittest.TestCase):

    def test(self):
        self.assertEqual(tuple(FilterExceeded(smallNum, values)), twoExpected)
