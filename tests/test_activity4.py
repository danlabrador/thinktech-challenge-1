# tests/test_activity4.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity4 import process_list

# Descriptive testing for Activity 4
if __name__ == "__main__":
    test = describe("Activity 4: process_list Functionality")

    # Test with a typical list
    test("Processing a typical list", process_list, (6, [3, 2, 1]), [1, 2, 3])

    # Test with an empty list
    test("Processing an empty list", process_list, (0, []), [])

    # Test with a list of negative numbers
    test("Processing a list of negative numbers", process_list, (-6, [-1, -2, -3]), [-3, -2, -1])

    # Test with a list containing zero
    test("Processing a list containing zero", process_list, (3, [0, 1, 2]), [2, 1, 0])

    # Test with a list of same numbers
    test("Processing a list of same numbers", process_list, (20, [5, 5, 5, 5]), [5, 5, 5, 5])

    # Test with a single-element list
    test("Processing a single-element list", process_list, (5, [5]), [5])

    # Test with a large list
    test("Processing a large list", process_list, (55, list(range(10, -1, -1))), list(range(11)))

    # Test with a list of floating-point numbers
    test("Processing a list of floating-point numbers", process_list, (6.6, [3.3, 2.2, 1.1]), [1.1, 2.2, 3.3])

    # Test with a list containing both positive and negative numbers
    test("Processing a list with both positive and negative numbers", process_list, (0, [-1, 1]), [1, -1])

    # Test with a list of large numbers
    test("Processing a list of large numbers", process_list, (10000000, [5000000, 5000000]), [5000000, 5000000])

    # Additional custom test cases...
