# tests/test_activity6.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity6 import get_valid_number

# Descriptive testing for Activity 6
if __name__ == "__main__":
    test = describe("6: Get Valid Number")

    # Test with immediate valid number
    test("First input is a valid number", get_valid_number, 42, ["42"])

    # Test with invalid followed by valid number
    test("Invalid input followed by valid number", get_valid_number, 3.14, ["not a number", "3.14"])

    # Test with multiple invalid inputs before a valid one
    test("Multiple invalid inputs before a valid number", get_valid_number, -1, ["nope", "nah", "-1"])

    # Test with only invalid inputs
    test("Only invalid inputs", get_valid_number, None, ["invalid", "also invalid"])

    # Test with valid number among non-string inputs (to simulate user error)
    test("Valid number among non-string inputs", get_valid_number, 100, [None, True, 100, "100"])

    # Test with all inputs valid, returns first
    test("All inputs valid, return first", get_valid_number, 1, ["1", "2", "3"])

    # Test with a mix of integer and float strings
    test("Mix of integer and float strings", get_valid_number, 0.56, ["0.56", "7"])

    # Test with leading and trailing spaces in input
    test("Leading and trailing spaces in input", get_valid_number, 123, ["  123  "])

    # Test input with a plus sign
    test("Input with a plus sign", get_valid_number, 42, ["+42"])

    # Test input with a minus sign
    test("Input with a minus sign", get_valid_number, -15, ["-15"])

    test("Empty input list", get_valid_number, None, [])  # Test with an empty input list

    test("Input list with non-numeric values", get_valid_number, None, ["abc", "def", "ghi"])  # Test with input list containing non-numeric values only

    test("Input list with mix of numeric and non-numeric values", get_valid_number, 42, ["abc", "123", "def"])  # Test with input list containing a mix of numeric and non-numeric values

    test("Input list with valid number as first element", get_valid_number, 3.14, ["3.14", "abc", "def"])  # Test with input list containing a valid number as the first element

    test("Input list with valid number as last element", get_valid_number, 7, ["abc", "def", "7"])  # Test with input list containing a valid number as the last element

    test("Input list with valid number in the middle", get_valid_number, 0.5, ["abc", "0.5", "def"])  # Test with input list containing a valid number in the middle

    test("Input list with multiple valid numbers", get_valid_number, 1, ["abc", "1", "2", "3", "def"])  # Test with input list containing multiple valid numbers

    test("Input list with leading and trailing spaces in valid number", get_valid_number, 42, [" abc ", "42", " def "])  # Test with input list containing valid numbers with leading and trailing spaces

    test("Input list with valid number as a string with plus sign", get_valid_number, 100, ["+100", "abc", "def"])  # Test with input list containing a valid number as a string with a plus sign

    test("Input list with valid number as a string with minus sign", get_valid_number, -15, ["-15", "abc", "def"])  # Test with input list containing a valid number as a string with a minus sign
