#!/usr/bin/python

import unittest

import triangle_numbers as tn
from itertoolsrecipes import take


class TestTriangleNumber(unittest.TestCase):

    def testPositive(self):
        self.assertEqual(tn.TriangleNumber(5), 15)


class TestTriangularNumbers(unittest.TestCase):

    def test(self):
        self.assertEqual(
            list(take(10, tn.TriangleNumbers())),
            [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])


class TestIsTriangleNumber(unittest.TestCase):

    def testPositive(self):
        self.assertTrue(tn.IsTriangleNumber(15))

    def testNegative(self):
        self.assertFalse(tn.IsTriangleNumber(16))
