#!/usr/bin/python

import unittest

import triangle_numbers as tn


class TestTriangleNumber(unittest.TestCase):

    def testPositive(self):
        self.assertEqual(tn.TriangleNumber(5), 15)


class TestIsTriangleNumber(unittest.TestCase):

    def testPositive(self):
        self.assertTrue(tn.IsTriangleNumber(15))

    def testPositive(self):
        self.assertFalse(tn.IsTriangleNumber(16))


if __name__ == "__main__":
    unittest.main()
