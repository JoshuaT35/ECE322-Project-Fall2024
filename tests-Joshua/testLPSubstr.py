'''
Testcases for LPSubstr() in pyrival/strings/LPSubstr.py

The function in question to be tested:
------
def LPSubstr(s):
    n = len(s)
    p = [[0] * (n + 1), [0] * n]

    for z, p_z in enumerate(p):
        left, right = 0, 0
        for i in range(n):
            t = right - i + 1 - z
            if i < right:
                p_z[i] = min(t, p_z[left + t])
            L, R = i - p_z[i], i + p_z[i] - 1 + z
            while (L >= 1) and (R + 1 < n) and (s[L - 1] == s[R + 1]):
                p_z[i] += 1
                L -= 1
                R += 1
            if R > right:
                left, right = L, R

    i1, x1 = max(enumerate(p[0]), key=lambda x: x[1])
    i2, x2 = max(enumerate(p[1]), key=lambda x: x[1])

    return s[i1 - x1:i1 + x1], s[i2 - x2:i2 + x2 + 1]
------
    
PyRival is credited as the source of the function.

NOTE: since no unreliable dependencies can be seen in the function,
we do not require unittest.
'''

# import libraries
from pyrival.strings import LPSubstr
import pandas as pd

def main():
    # strings
    test_id_str = "Test ID"
    description_str = "Description"
    input_str = "Input"
    expected_str = "Expected Result"
    actual_str = "Actual Result"

    # create table to hold results
    results = pd.DataFrame(
        columns=[
            test_id_str,
            description_str,
            input_str,
            expected_str,
            actual_str
        ]
    )

    # create description
    test_case_description = [
        "Single character",
        "No palindrome longer than 1 character",
        "Entire string is a palindrome",
        "Palindrome with even length",
        "Palindrome with odd length",
        "Mixed case palindrome",
        "Long string with palindromes",
        "Multiple palindromes: even & odd",
        "Multiple palindromes: even & even, same length",
        "Multiple palindromes: even & even, different length",
        "Multiple palindromes: odd & odd, same length",
        "Multiple palindromes: odd & odd, different length",
        "Multiple palindromes part 1: same length, first palindrome used",
        "Multiple palindromes part 2: same length, first palindrome used",
        "Empty string",
        "String with no palindromes"
    ]

    # create input
    test_case_input = [
        "a",
        "abc",
        "racecar",
        "abba",
        "madam",
        "AbcCba",
        "abcdcbac",
        "abbamadam",
        "abbaqwwq",
        "abbaqwffwq",
        "madamxyzyx",
        "madamwxyzyxw",
        "abazyz",
        "zyzaba",
        "",
        "xyz"
    ]

    # create expected result
    test_case_expected = [
        ('', 'a'),
        ('', 'a'),
        ('', 'racecar'),
        ('abba', 'a'),
        ('', 'madam'),
        ('', 'A'),
        ('', 'abcdcba'),
        ('abba', 'madam'),
        ('abba', 'a'),
        ('qwffwq', 'a'),
        ('', 'madam'),
        ('', 'wxyzyxw'),
        ('', 'aba'),
        ('', 'zyz'),
        ('', ''),
        ('x', 'y')
    ]

    # assert that there is message, input, and expectation for each result
    assert len(test_case_description) == len(test_case_input)
    assert len(test_case_description) == len(test_case_expected)
    assert len(test_case_input) == len(test_case_expected)


    # iterate through test cases
    for rowIdx in range(0, len(test_case_description)):

        # add idx
        idx = rowIdx + 1
        results.loc[rowIdx, test_id_str] = idx

        # add description
        results.loc[rowIdx, description_str] = test_case_description[rowIdx]

        # add input
        results.loc[rowIdx, input_str] = test_case_input[rowIdx]

        # add expected
        results.loc[rowIdx, expected_str] = test_case_expected[rowIdx]

        # add actual
        try:
            results.loc[rowIdx, actual_str] = LPSubstr.LPSubstr(test_case_input[rowIdx])
        except:
            results.loc[rowIdx, actual_str] = "ERROR THROWN BY PROGRAM"
    
    # write result to excel file
    results.to_excel("lpsubstr.xlsx")


if __name__ == "__main__":
    main()
    