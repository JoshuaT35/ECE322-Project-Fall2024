import unittest

def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x

class TestGCD(unittest.TestCase):
    def test_both_zero(self):
        # GCD-TC-1: Both inputs are zero
        self.assertEqual(gcd(0, 0), 0, "GCD of (0, 0) should be 0")

    def test_one_zero(self):
        # GCD-TC-2: One input is zero, the other positive
        self.assertEqual(gcd(0, 5), 5, "GCD of (0, 5) should be 5")
        # GCD-TC-3: One input is zero, the other positive
        self.assertEqual(gcd(7, 0), 7, "GCD of (7, 0) should be 7")

    def test_negative_and_positive(self):
        # GCD-TC-4: Negative and positive inputs
        self.assertEqual(gcd(-10, 5), 5, "GCD of (-10, 5) should be 5")

    def test_both_negative(self):
        # GCD-TC-5: Both inputs are negative
        self.assertEqual(gcd(-10, -5), -5, "GCD of (-10, -5) should be 5")

    def test_prime_numbers(self):
        # GCD-TC-6: Prime numbers with no common divisor
        self.assertEqual(gcd(13, 7), 1, "GCD of (13, 7) should be 1")

    def test_large_numbers(self):
        # GCD-TC-7: Large inputs with a common divisor
        self.assertEqual(gcd(100000000, 50000000), 50000000, "GCD of (100000000, 50000000) should be 50000000")

    def test_common_divisors(self):
        # GCD-TC-8: Positive inputs with a common divisor
        self.assertEqual(gcd(24, 36), 12, "GCD of (24, 36) should be 12")
        # GCD-TC-9: Negative and positive inputs with a divisor
        self.assertEqual(gcd(-24, 36), 12, "GCD of (-24, 36) should be 12")

if __name__ == "__main__":
    unittest.main()
