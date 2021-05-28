#!/usr/bin/python

import unittest

import itertoolsrecipes
itertoolsextras = itertoolsrecipes


class TestTake(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(list(itertoolsrecipes.take(3, range(5))), [0, 1, 2])


class TestFirstNClass(unittest.TestCase):
    def setUp(self):
        self.support = itertoolsextras
        self.ex = self.support.DifferentLengthsError

    def test_first_n(self):
        def first_n_fixed(*a):
            return tuple(self.support.first_n(*a))

        self.assertEqual(
            first_n_fixed(range(5), 3),
            tuple(range(3)),
            'Within range.')

        self.assertEqual(
            first_n_fixed(range(5), 5),
            tuple(range(5)),
            'Just within range.')

        self.assertRaises(
            self.ex,
            lambda _: first_n_fixed(range(5), 6),
            'Just outside range.')

    def test_skip_first_n(self):
        def skip_first_n_fixed(*a):
            return tuple(self.support.skip_first_n(*a))

        self.assertEqual(
            skip_first_n_fixed(range(5)),
            tuple(range(5)),
            'Default.')

        self.assertEqual(
            skip_first_n_fixed(range(5), 2),
            (2, 3, 4),
            'Within range.')

        self.assertEqual(
            skip_first_n_fixed(range(5), 5),
            tuple(),
            'Just within range.')

        self.assertEqual(
            skip_first_n_fixed(range(5), 6),
            tuple(),
            'Just outside range.')

    def test_nth_term(self):
        self.assertEqual(
            self.support.nth_term(range(10), 10),
            9,
            'Just within range.')

        self.assertRaises(
            self.ex,
            lambda _: self.support.nth_term(range(10), 11),
            'Just out of range.')

    def test_zip_error_if_different_lengths(self):
        def zip_error_if_different_lengths(*a):
            return tuple(self.support.zip_error_if_different_lengths(*a))

        self.assertEqual(
            zip_error_if_different_lengths(range(2), range(2)),
            ((0, 0), (1, 1)),
            'Same length.')

        self.assertRaises(
            self.ex,
            lambda _: zip_error_if_different_lengths(range(4), range(5)),
            'Different length.')

    def test_items_equal(self):
        self.assertTrue(
            self.support.items_equal(), 'Empty.')
        self.assertTrue(
            self.support.items_equal(1, 1, 1), 'Same.')
        self.assertFalse(
            self.support.items_equal(1, 2, 2), 'Different.')

    def test_collections_equal(self):
        self.assertTrue(
            self.support.collections_equal(), 'Empty.')
        self.assertTrue(
            self.support.collections_equal(range(5), range(5), range(5)),
            'Same.')
        self.assertFalse(
            self.support.collections_equal(range(4), range(4), range(5)),
            'Different.')

    def test_combo(self):
        self.assertTrue(
            self.support.collections_equal(
                self.support.first_n(range(10), 5), range(5)))

    def test_len_of_generator(self):
        for i in range(1, 10+1):
            self.assertEqual(
                self.support.len_of_generator(range(i)),
                i,
                'On length of %d.' % (i))

    def test_rolling_collection(self):
        self.assertEqual(
            tuple(self.support.rolling_collection([], 5)),
            tuple(),
            'Null case.')
        self.assertEqual(
            tuple(self.support.rolling_collection(range(4), 5)),
            tuple(),
            'Squeezed out case.')
        self.assertEqual(
            tuple(self.support.rolling_collection(range(5), 5)),
            (tuple(range(5)),),
            'Single roll.')
        self.assertEqual(
            tuple(self.support.rolling_collection(range(6), 5)),
            (tuple(range(5)), tuple(range(1, 6))),
            'Two rolls.')
        self.assertEqual(
            tuple(self.support.rolling_collection(range(6), 5, pad=1)),
            (
                (None, 0, 1, 2, 3),
                tuple(range(5)),
                tuple(range(1, 6)), (2, 3, 4, 5, None)
            ),
            'With padding.')

    def test_are_consecutive(self):
        self.assertTrue(self.support.are_consecutive([]), 'Null case.')
        self.assertTrue(self.support.are_consecutive([1]), 'Single element.')
        self.assertTrue(self.support.are_consecutive([1, 2]), 'Ordered pair.')
        self.assertFalse(
            self.support.are_consecutive([2, 1]), 'Unordered pair.')

    def test_len_of_generator_is_not_less_than(self):
        self.assertTrue(
            self.support.len_of_generator_is_not_less_than([], 0),
            'Null case allowable.')
        self.assertFalse(
            self.support.len_of_generator_is_not_less_than([], 1),
            'Null case disallowable.')
        self.assertTrue(
            self.support.len_of_generator_is_not_less_than(range(5), 4),
            'More than.')
        self.assertTrue(
            self.support.len_of_generator_is_not_less_than(range(5), 5),
            'Same as.')
        self.assertFalse(
            self.support.len_of_generator_is_not_less_than(range(5), 6),
            'Less than')
