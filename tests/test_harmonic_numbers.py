#!/usr/bin/python

import unittest
from fractions import Fraction

import harmonic_numbers as tn
from itertoolsrecipes import take


class TestHarmonicNumbers(unittest.TestCase):

    def test(self):
        expected = [
            1,
            Fraction('3/2'),
            Fraction('11/6'),
            Fraction('25/12'),
            Fraction('137/60'),
            Fraction('49/20'),
            Fraction('363/140'),
            Fraction('761/280'),
            Fraction('7129/2520'),
            Fraction('7381/2520'),
        ]
        self.assertEqual(list(take(10, tn.HarmonicNumbers())), expected)
