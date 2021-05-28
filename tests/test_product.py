#!/usr/bin/python

import unittest

from product import product


class TestProduct(unittest.TestCase):

    def test_null_case(self):
        self.assertEqual(product([]), 1, 'Null case has not been considered.')

    def test_one_to_five(self):
        self.assertEqual(product(range(1, 4+1)), 24)
