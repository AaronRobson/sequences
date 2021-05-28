#!/usr/bin/python

import unittest

from fibonacci_numbers import fibonacci_number, fibonacci_numbers


class TestFibonacciNumbers(unittest.TestCase):

    def test_fibonacci_number(self):
        with self.assertRaises(ValueError):
            fibonacci_number(-1)

        self.assertEqual(fibonacci_number(0), 0)
        self.assertEqual(fibonacci_number(1), 1)
        self.assertEqual(fibonacci_number(2), 1)
        self.assertEqual(fibonacci_number(3), 2)
        self.assertEqual(fibonacci_number(4), 3)
        # ...
        self.assertEqual(fibonacci_number(12), 144)

    def test_first_10_fibonacci_numbers(self):
        self.assertEqual(
            tuple(fibonacci_numbers(10)),
            (0, 1, 1, 2, 3, 5, 8, 13, 21, 34))
