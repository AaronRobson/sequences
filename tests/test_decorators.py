#!/usr/bin/python

import unittest

import decorators


class TestMemoise(unittest.TestCase):

    def test(self):
        @decorators.memoised
        def f(x):
            return x + 1
        self.assertEqual(f(1), 2)
        self.assertEqual(f(1), 2)
