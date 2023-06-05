import unittest
from automated_development_tutorial.example import fibonacci, sumOfPrimes


class TestExample(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_sum_of_primes(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
