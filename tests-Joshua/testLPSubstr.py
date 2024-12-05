'''
Testcases for LPSubstr()
'''

# import libraries
import unittest
from LPSubstr import LPSubstr

class TestLpSubstr(unittest.TestCase):

    def testSingleCharacter(self):
        input_str = "a"
        expected_value = ('', 'a')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testNoPalindromeLongerThanOne(self):
        input_str = "abc"
        expected_value = ('', 'a')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testEntireStringIsPalindrome(self):
        input_str = "racecar"
        expected_value = ('', 'racecar')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testPalindromeWithEvenLength(self):
        input_str = "abba"
        expected_value = ('abba', 'a')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testPalindromeWithOddLength(self):
        input_str = "madam"
        expected_value = ('', 'madam')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMixedCasePalindrome(self):
        input_str = "AbcCba"
        expected_value = ('', 'AbcCba')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testLongStringWithPalindromes(self):
        input_str = "abcdcbac"
        expected_value = ('', 'abcdcba')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesEvenOdd(self):
        input_str = "abbamadam"
        expected_value = ('abba', 'madam')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesEvenEvenSameLength(self):
        input_str = "abbaqwwq"
        expected_value = ('abba', 'a')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesEvenEvenDifferentLength(self):
        input_str = "abbaqwffwq"
        expected_value = ('qwffwq', 'a')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesOddOddSameLength(self):
        input_str = "madamxyzyx"
        expected_value = ('', 'madam')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesOddOddDifferentLength(self):
        input_str = "madamwxyzyxw"
        expected_value = ('', 'wxyzyxw')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesPart1SameLengthFirstPalindromeUsed(self):
        input_str = "abazyz"
        expected_value = ('', 'aba')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testMultiplePalindromesPart2SameLengthFirstPalindromeUsed(self):
        input_str = "zyzaba"
        expected_value = ('', 'zyz')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

    def testEmptyString(self):
        input_str = ""
        expected_value = ('', '')
        actual_value = LPSubstr(input_str)
        self.assertEqual(expected_value, actual_value)

if __name__ == '__main__':
    unittest.main()
    