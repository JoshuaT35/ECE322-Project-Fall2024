'''
Testcases for least_rotation()
'''

# import libraries
import unittest
from least_rotation import least_rotation

class TestLeastRotation(unittest.TestCase):
    
    def testEmptyString(self):
        input = ""
        expected_value = ""
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testOneItemLetter(self):
        input = "a"
        expected_value = "a"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testOneItemSpace(self):
        input = " "
        expected_value = " "
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testTwoOrMoreItemsSameLetter(self):
        input = "aaaa"
        expected_value = "aaaa"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testTwoOrMoreItemsDifferentLettersOrdered(self):
        input = "abbc"
        expected_value = "abbc"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testTwoOrMoreItemsDifferentLettersNotOrdered(self):
        input = "bbbaaaccc"
        expected_value = "aaacccbbb"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testNonLetterInSequence(self):
        input = "cc+aab"
        with self.assertRaises(Exception):
            least_rotation(input)

    def testSpaceAtEnd(self):
        input = "ccab "
        expected_value = " ccab"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testSpaceInTheMiddle(self):
        input = "cc ab"
        expected_value = " abcc"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testMultipleSpaces(self):
        input = "cc ab"
        expected_value = " abcc"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testAllUppercase(self):
        input = "CCABB"
        expected_value = "ABBCC"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testMixedCase(self):
        input = "aaABBbC"
        expected_value = "ABBbCaa"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)

    def testLongSequence(self):
        input = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        expected_value = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        actual_value = least_rotation(input)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()
