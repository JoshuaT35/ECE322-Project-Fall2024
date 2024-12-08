import unittest

def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_less_than_2(self):
        # IP-TC-1: Input 0
        self.assertFalse(is_prime(0), "0 is not a prime number")
        # IP-TC-2: Input 1
        self.assertFalse(is_prime(1), "1 is not a prime number")

    def test_small_primes(self):
        # IP-TC-3: Input 2
        self.assertTrue(is_prime(2), "2 is a prime number")
        # IP-TC-4: Input 3
        self.assertTrue(is_prime(3), "3 is a prime number")

    def test_small_composites(self):
        # IP-TC-5: Input 4
        self.assertFalse(is_prime(4), "4 is not a prime number")
        # IP-TC-6: Input 6
        self.assertFalse(is_prime(6), "6 is not a prime number")

    def test_random_primes_and_composites(self):
        # IP-TC-7: Input 29
        self.assertTrue(is_prime(29), "29 is a prime number")
        # IP-TC-8: Input 28
        self.assertFalse(is_prime(28), "28 is not a prime number")

    def test_large_numbers(self):
        # IP-TC-9: Input 104729
        self.assertTrue(is_prime(104729), "104729 is a prime number")
        # IP-TC-10: Input 104730
        self.assertFalse(is_prime(104730), "104730 is not a prime number")

if __name__ == "__main__":
    unittest.main()
