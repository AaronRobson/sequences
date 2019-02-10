#!/usr/bin/python

import unittest

import fibonacci_numbers


class TestFibonacciNumbers(unittest.TestCase):

    def testFibonacciNumber(self):
        with self.assertRaises(ValueError):
            fibonacci_numbers.FibonacciNumber(-1)

        self.assertEqual(fibonacci_numbers.FibonacciNumber(0), 0)
        self.assertEqual(fibonacci_numbers.FibonacciNumber(1), 1)
        self.assertEqual(fibonacci_numbers.FibonacciNumber(2), 1)
        self.assertEqual(fibonacci_numbers.FibonacciNumber(3), 2)
        self.assertEqual(fibonacci_numbers.FibonacciNumber(4), 3)
        # ...
        self.assertEqual(fibonacci_numbers.FibonacciNumber(12), 144)

    def testFirst10FibonacciNumbers(self):
        self.assertEqual(
            tuple(fibonacci_numbers.FibonacciNumbers(10)),
            (0, 1, 1, 2, 3, 5, 8, 13, 21, 34))
