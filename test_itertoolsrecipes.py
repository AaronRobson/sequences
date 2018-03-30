#!/usr/bin/python

import unittest

import itertoolsrecipes
itertoolsextras = itertoolsrecipes


class TestTake(unittest.TestCase):

    def testSimple(self):
        self.assertEqual(list(itertoolsrecipes.take(3, range(5))), [0, 1, 2])


#######


class TestFirstNClass(unittest.TestCase):
    def setUp(self):
        self.support = itertoolsextras
        self.ex = self.support.DifferentLengthsError

    def testFirstN(self):
        FirstNFixed = lambda *a: tuple(self.support.FirstN(*a))

        self.assertEqual(FirstNFixed(range(5), 3), tuple(range(3)), 'FirstN Fail: within range.')

        self.assertEqual(FirstNFixed(range(5), 5), tuple(range(5)), 'FirstN Fail: just within range.')

        self.assertRaises(self.ex, lambda _: FirstNFixed(range(5), 6), 'FirstN Fail: just outside range.')

    def testSkipFirstN(self):
        SkipFirstNFixed = lambda *a: tuple(self.support.SkipFirstN(*a))

        self.assertEqual(SkipFirstNFixed(range(5)), tuple(range(5)), 'SkipFirstN Fail: default.')

        self.assertEqual(SkipFirstNFixed(range(5), 2), (2,3,4), 'SkipFirstN Fail: within range.')

        self.assertEqual(SkipFirstNFixed(range(5), 5), tuple(), 'SkipFirstN Fail: just within range.')

        self.assertEqual(SkipFirstNFixed(range(5), 6), tuple(), 'SkipFirstN Fail: just outside range.')

    def testNthTerm(self):
        self.assertEqual(self.support.NthTerm(range(10), 10), 9, 'NthTerm Fail: just within range.')

        self.assertRaises(self.ex, lambda _: self.support.NthTerm(range(10), 11), 'NthTerm Fail: just out of range.')

    def testZipErrorIfDifferentLengths(self):
        ZipErrorIfDifferentLengthsFixed = lambda *a: tuple(self.support.ZipErrorIfDifferentLengths(*a))

        self.assertEqual(ZipErrorIfDifferentLengthsFixed(range(2), range(2)), ((0,0),(1,1)), 'ZipErrorIfDifferentLengths Fail: same length.')

        self.assertRaises(self.ex, lambda _: ZipErrorIfDifferentLengthsFixed(range(4), range(5)), 'ZipErrorIfDifferentLengths Fail: different length.')

    def testItemsEqual(self):
        self.assertTrue(self.support.ItemsEqual(), 'ItemsEqual Fail: Empty.')
        self.assertTrue(self.support.ItemsEqual(1,1,1), 'ItemsEqual Fail: Same.')
        self.assertFalse(self.support.ItemsEqual(1,2,2), 'ItemsEqual Fail: Different.')

    def testCollectionsEqual(self):
        self.assertTrue(self.support.CollectionsEqual(), 'CollectionsEqual Fail: Empty.')
        self.assertTrue(self.support.CollectionsEqual(range(5), range(5), range(5)), 'CollectionsEqual Fail: Same.')
        self.assertFalse(self.support.CollectionsEqual(range(4), range(4), range(5)), 'CollectionsEqual Fail: Different.')

    def testCombo(self):
        self.assertTrue(self.support.CollectionsEqual(self.support.FirstN(range(10), 5), range(5)))

    def testLenOfGenerator(self):
        for i in range(1, 10+1):
            self.assertEqual(self.support.LenOfGenerator(range(i)), i, 'LenOfGenerator Fail: on length of %d.' % (i))

    def testRollingCollection(self):
        self.assertEqual(tuple(self.support.RollingCollection([], 5)), tuple(), 'RollingCollection Fail: null case.')
        self.assertEqual(tuple(self.support.RollingCollection(range(4), 5)), tuple(), 'RollingCollection Fail: squeezed out case.')
        self.assertEqual(tuple(self.support.RollingCollection(range(5), 5)), (tuple(range(5)),), 'RollingCollection Fail: single roll.')
        self.assertEqual(tuple(self.support.RollingCollection(range(6), 5)), (tuple(range(5)), tuple(range(1, 6))), 'RollingCollection Fail: two rolls.')
        self.assertEqual(tuple(self.support.RollingCollection(range(6), 5, pad=1)), ((None,0,1,2,3), tuple(range(5)), tuple(range(1, 6)), (2,3,4,5,None)), 'RollingCollection Fail with padding.')

    def testAreConsecutive(self):
        self.assertTrue(self.support.AreConsecutive([]), 'Null case.')
        self.assertTrue(self.support.AreConsecutive([1]), 'Single element.')
        self.assertTrue(self.support.AreConsecutive([1,2]), 'Ordered pair.')
        self.assertFalse(self.support.AreConsecutive([2,1]), 'Unordered pair.')

    def testLenOfGeneratorIsNotLessThan(self):
        self.assertTrue(self.support.LenOfGeneratorIsNotLessThan([], 0), 'Null case allowable.')
        self.assertFalse(self.support.LenOfGeneratorIsNotLessThan([], 1), 'Null case disallowable.')
        self.assertTrue(self.support.LenOfGeneratorIsNotLessThan(range(5), 4), 'More than.')
        self.assertTrue(self.support.LenOfGeneratorIsNotLessThan(range(5), 5), 'Same as.')
        self.assertFalse(self.support.LenOfGeneratorIsNotLessThan(range(5), 6), 'Less than')


if __name__ == "__main__":
    unittest.main()
