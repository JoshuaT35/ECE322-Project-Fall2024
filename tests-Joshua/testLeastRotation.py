'''
Testcases for least_rotation() in pyrival/strings/min_rotation.py

The function in question to be tested:
------
def least_rotation(s):
    a, n = 0, len(s)
    s = s + s

    b = 1
    while b < n:
        for i in range(b - a):
            if s[a + i] > s[b + i]:
                a = b
                b += 1
                break
            if s[a + i] < s[b + i]:
                b += i + 1
                break
        else:
            b += b - a
    return s[a:a + n]
------
    
PyRival is credited as the source of the function.

NOTE: since no unreliable dependencies can be seen in the function,
we do not require unittest.
'''

# import libraries
from pyrival.strings import min_rotation
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
        "empty string",
        "1 item in string - letter",
        "1 item in string - non-letter",
        "1 item in string - space",
        "2+ items in string - all letters (same letter)",
        "2+ items in string - all letters (different letters), ordered",
        "2+ items in string - all letters (different letters), not ordered",
        "non-letter in sequence",
        "space at end",
        "space in the middle",
        "multiple spaces"
        "all uppercase",
        "mixed case",
        "long sequence"
    ]

    # create input
    test_case_input = [
        "",
        "a",
        "+",
        " ",
        "aaaa",
        "abbc",
        "bbbaaaccc",
        "cc+aab",
        "ccab ",
        "cc ab",
        "CCABB",
        "ABBbCcaa",
        "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    ]

    # create expected result
    test_case_expected = [
        "",
        "a",
        "Invalid",
        " ",
        "aaaa",
        "abbc",
        "aaacccbbb",
        "+aabcc",
        " ccab",
        " abcc",
        "ABBCC",
        "aaABBbCc",
        "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
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
            results.loc[rowIdx, actual_str] = min_rotation.least_rotation(test_case_input[rowIdx])
        except:
            results.loc[rowIdx, actual_str] = "ERROR THROWN BY PROGRAM"
    
    # write result to excel file
    results.to_excel("least_rotation.xlsx")


if __name__ == "__main__":
    main()
