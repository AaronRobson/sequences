#!/usr/bin/python

import unittest

import triangle_numbers as tn
from itertoolsrecipes import take


class TestTriangleNumber(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(tn.triangle_number(5), 15)


class TestTriangularNumbers(unittest.TestCase):

    def test(self):
        self.assertEqual(
            list(take(10, tn.triangle_numbers())),
            [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])


class TestIsTriangleNumber(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(tn.is_triangle_number(15))

    def test_negative(self):
        self.assertFalse(tn.is_triangle_number(16))
