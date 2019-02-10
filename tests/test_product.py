#!/usr/bin/python

import unittest

from product import product


class TestProduct(unittest.TestCase):

    def testNullCase(self):
        self.assertEqual(product([]), 1, 'Null case has not been considered.')

    def testOneToFive(self):
        self.assertEqual(product(range(1, 4+1)), 24)
