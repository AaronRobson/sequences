#!/usr/bin/python

import unittest

import badger
from itertoolsrecipes import take


class TestBadger(unittest.TestCase):

    def test_cycling(self):
        gen = badger.badger_mushroom_snake_generator()
        first_loop = take(len(badger.full), gen)
        second_loop = take(len(badger.full), gen)
        self.assertEqual(first_loop, second_loop)
