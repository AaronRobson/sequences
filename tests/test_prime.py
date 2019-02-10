#!/usr/bin/python

import unittest
import prime

oddNum = 3
evenNum = 12


class TestSupport(unittest.TestCase):

    def setUp(self):
        self.support = prime

    def testIsEvenAndOdd(self):
        self.assertTrue(self.support.IsEven(evenNum), '')
        self.assertFalse(self.support.IsEven(oddNum), '')

        self.assertFalse(self.support.IsOdd(evenNum), '')
        self.assertTrue(self.support.IsOdd(oddNum), '')

    def testNextEvenAndOdd(self):
        self.assertEqual(self.support.NextEven(evenNum), evenNum+2, '')
        self.assertEqual(self.support.NextEven(oddNum), oddNum+1, '')

        self.assertEqual(self.support.NextOdd(evenNum), evenNum+1, '')
        self.assertEqual(self.support.NextOdd(oddNum), oddNum+2, '')

    def testIsDivisable(self):
        self.assertTrue(self.support.IsDivisable(4, 2), '')
        self.assertFalse(self.support.IsDivisable(3, 2), '')
        self.assertFalse(
            self.support.IsDivisable(2, 0),
            'Division by zero should be treated as not divisable.')


class TestPrime(unittest.TestCase):

    def setUp(self):
        self.support = prime
        self.firstPrimes = (
            2, 3, 5, 7, 11,
            13, 17, 19, 23, 29,
            31, 37, 41, 43, 47,
            53, 59, 61, 67, 71)

    def testPrimeCollection(self):
        def FirstPrimesTest():
            for expected, actual in zip(
                    self.firstPrimes, prime.PrimeCollection()):
                self.assertEqual(expected, actual)

            self.assertTrue(
                len(self.firstPrimes) <= len(prime.PrimeCollection()),
                'Number of stored primes not enough to account for the ' +
                'number that should be correct (zip terminates on shortest' +
                'collection (the other is infinite though)).')

            self.assertEqual(
                prime.PrimeCollection().cache[:len(self.firstPrimes)],
                self.firstPrimes,
                'White box testing of the cache inconsistant.')

        FirstPrimesTest()
        FirstPrimesTest()

    def testPrimesFirstN(self):
        self.assertEqual(
            tuple(self.support.PrimesFirstN(len(self.firstPrimes))),
            self.firstPrimes)

    def testNthPrime(self):
        self.assertEqual(prime.NthPrime(1), 2)
        self.assertEqual(prime.NthPrime(2), 3)
        self.assertEqual(prime.NthPrime(3), 5)
        self.assertEqual(prime.NthPrime(4), 7)
        self.assertEqual(prime.NthPrime(5), 11)
        self.assertEqual(prime.NthPrime(6), 13)
        self.assertEqual(prime.NthPrime(7), 17)

    def testIsPrime(self):
        self.assertTrue(self.support.IsPrime(2))
        self.assertTrue(self.support.IsPrime(13))

        self.assertFalse(self.support.IsPrime(4))
        self.assertFalse(self.support.IsPrime(42))

        self.assertTrue(self.support.IsPrime(1453))

    def testPrimeFactors(self):
        self.assertEqual(tuple(self.support.PrimeFactors(2)), (2,))
        self.assertEqual(
            tuple(self.support.PrimeFactors(6)),
            (2, 3), 'Factorial factors (of 3!) not found.')
        self.assertEqual(
            tuple(self.support.PrimeFactors(81)),
            (3,)*4,
            'Repeated factors incorrect.')

        self.assertEqual(
            tuple(self.support.PrimeFactors(1453)),
            (1453,),
            'Prime factors of prime number as here:' +
            'http://xkcd.com/247/ incorrect.')

        self.assertTrue(1453 in prime.PrimeCollection().cache)

        self.assertRaises(
            ValueError,
            lambda _: tuple(self.support.PrimeFactors(1)),
            'Too low a number allowed.')

    def testPrimeFactorsWithoutDuplicates(self):
        self.assertEqual(
            tuple(self.support.PrimeFactorsWithoutDuplicates(6)),
            (2, 3),
            'Factorial factors (of 3!) not found.')
        self.assertEqual(
            tuple(self.support.PrimeFactorsWithoutDuplicates(81)),
            (3,),
            'Single factor not correctly found.')

    def testCountOfDistinctPrimeFactors(self):
        self.assertEqual(
            self.support.CountOfDistinctPrimeFactors(24),
            2,
            'CountOfDistinctPrimeFactors Fail: 24.')

    def testPrimeFactorsDict(self):
        self.assertEqual(
            self.support.PrimeFactorsDict(24),
            {2: 3, 3: 1})
        self.assertEqual(
            self.support.PrimeFactorsDict(2**2, 3**3),
            {2: 2, 3: 3},
            'PrimeFactorsDict Fail: multiple numbers.')

    def testFactors(self):
        self.assertEqual(
            list(self.support.Factors(60)),
            [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60])

    def testHighestFactors(self):
        self.assertEqual(
            self.support.HighestFactors([3, 5, 6, 12, 25]),
            {2: 2, 3: 1, 5: 2})

    def testFactorDictToNumber(self):
        self.assertEqual(self.support.FactorDictToNumber({2: 3, 3: 1}), 24)

    def testLeastCommonMultiple(self):
        self.assertEqual(
            self.support.LeastCommonMultiple(range(1, 10+1)),
            2520,
            'LeastCommonMultiple Fail: 1 to 10.')
        self.assertEqual(
            self.support.LeastCommonMultiple(range(1, 20+1)),
            232792560,
            'LeastCommonMultiple Fail: 1 to 20.')
