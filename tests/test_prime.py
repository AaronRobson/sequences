#!/usr/bin/python

import unittest
import prime

odd_num = 3
even_num = 12


class TestSupport(unittest.TestCase):

    def setUp(self):
        self.support = prime

    def test_is_even_and_odd(self):
        self.assertTrue(self.support.is_even(even_num), '')
        self.assertFalse(self.support.is_even(odd_num), '')

        self.assertFalse(self.support.is_odd(even_num), '')
        self.assertTrue(self.support.is_odd(odd_num), '')

    def test_next_even_and_odd(self):
        self.assertEqual(self.support.next_even(even_num), even_num+2, '')
        self.assertEqual(self.support.next_even(odd_num), odd_num+1, '')

        self.assertEqual(self.support.next_odd(even_num), even_num+1, '')
        self.assertEqual(self.support.next_odd(odd_num), odd_num+2, '')

    def test_is_divisable(self):
        self.assertTrue(self.support.is_divisable(4, 2), '')
        self.assertFalse(self.support.is_divisable(3, 2), '')
        self.assertFalse(
            self.support.is_divisable(2, 0),
            'Division by zero should be treated as not divisable.')


class TestPrime(unittest.TestCase):

    def setUp(self):
        self.support = prime
        self.first_primes = (
            2, 3, 5, 7, 11,
            13, 17, 19, 23, 29,
            31, 37, 41, 43, 47,
            53, 59, 61, 67, 71)

    def test_prime_collection(self):
        def first_primes_test():
            for expected, actual in zip(
                    self.first_primes, prime.PrimeCollection()):
                self.assertEqual(expected, actual)

            self.assertTrue(
                len(self.first_primes) <= len(prime.PrimeCollection()),
                'Number of stored primes not enough to account for the ' +
                'number that should be correct (zip terminates on shortest' +
                'collection (the other is infinite though)).')

            self.assertEqual(
                prime.PrimeCollection().cache[:len(self.first_primes)],
                self.first_primes,
                'White box testing of the cache inconsistant.')

        first_primes_test()
        first_primes_test()

    def test_primes_first_n(self):
        self.assertEqual(
            tuple(self.support.primes_first_n(len(self.first_primes))),
            self.first_primes)

    def test_nth_prime(self):
        self.assertEqual(prime.nth_prime(1), 2)
        self.assertEqual(prime.nth_prime(2), 3)
        self.assertEqual(prime.nth_prime(3), 5)
        self.assertEqual(prime.nth_prime(4), 7)
        self.assertEqual(prime.nth_prime(5), 11)
        self.assertEqual(prime.nth_prime(6), 13)
        self.assertEqual(prime.nth_prime(7), 17)

    def test_is_prime(self):
        self.assertTrue(self.support.is_prime(2))
        self.assertTrue(self.support.is_prime(13))

        self.assertFalse(self.support.is_prime(4))
        self.assertFalse(self.support.is_prime(42))

        self.assertTrue(self.support.is_prime(1453))

    def test_prime_factors(self):
        self.assertEqual(tuple(self.support.prime_factors(2)), (2,))
        self.assertEqual(
            tuple(self.support.prime_factors(6)),
            (2, 3), 'Factorial factors (of 3!) not found.')
        self.assertEqual(
            tuple(self.support.prime_factors(81)),
            (3,)*4,
            'Repeated factors incorrect.')

        self.assertEqual(
            tuple(self.support.prime_factors(1453)),
            (1453,),
            'Prime factors of prime number as here:' +
            'http://xkcd.com/247/ incorrect.')

        self.assertTrue(1453 in prime.PrimeCollection().cache)

        self.assertRaises(
            ValueError,
            lambda _: tuple(self.support.prime_factors(1)),
            'Too low a number allowed.')

    def test_prime_factors_without_duplicates(self):
        self.assertEqual(
            tuple(self.support.prime_factors_without_duplicates(6)),
            (2, 3),
            'Factorial factors (of 3!) not found.')
        self.assertEqual(
            tuple(self.support.prime_factors_without_duplicates(81)),
            (3,),
            'Single factor not correctly found.')

    def test_count_of_distinct_prime_factors(self):
        self.assertEqual(
            self.support.count_of_distinct_prime_factors(24),
            2)

    def test_prime_factors_dict(self):
        self.assertEqual(
            self.support.prime_factors_dict(24),
            {2: 3, 3: 1})
        self.assertEqual(
            self.support.prime_factors_dict(2**2, 3**3),
            {2: 2, 3: 3},
            'Multiple numbers.')

    def test_factors(self):
        self.assertEqual(
            list(self.support.factors(60)),
            [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60])

    def test_highest_factors(self):
        self.assertEqual(
            self.support.highest_factors([3, 5, 6, 12, 25]),
            {2: 2, 3: 1, 5: 2})

    def test_factor_dict_to_number(self):
        self.assertEqual(self.support.factor_dict_to_number({2: 3, 3: 1}), 24)

    def test_least_common_multiple(self):
        self.assertEqual(
            self.support.least_common_multiple(range(1, 10+1)),
            2520,
            '1 to 10.')
        self.assertEqual(
            self.support.least_common_multiple(range(1, 20+1)),
            232792560,
            '1 to 20.')
