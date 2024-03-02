# tests/test_activity1.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity1 import calculate_operations

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("1: Calculate Operations")

    # Test adding positive numbers
    test("Adding positive numbers", calculate_operations, "Sum: 8, Product: 15, Difference: 2", 5, 3)
    # Test adding a positive and a negative number
    test("Adding a positive and a negative number", calculate_operations, "Sum: 2, Product: -15, Difference: 8", 5, -3)
    # Test adding negative numbers
    test("Adding negative numbers", calculate_operations, "Sum: -8, Product: 15, Difference: -2", -5, -3)
    # Test working with zero
    test("Working with zero as the first number", calculate_operations, "Sum: 0, Product: 0, Difference: 0", 0, 0)
    test("Working with zero as the second number", calculate_operations, "Sum: 5, Product: 0, Difference: 5", 5, 0)
    # Test with large numbers
    test("Handling large numbers", calculate_operations, "Sum: 100000, Product: 499975, Difference: 99990", 99995, 5)
    # Test with one operand being 1, edge case for multiplication
    test("Multiplying by one", calculate_operations, "Sum: 6, Product: 5, Difference: 4", 5, 1)
    # Test subtraction resulting in negative
    test("Subtraction resulting in negative", calculate_operations, "Sum: 10, Product: 21, Difference: -4", 3, 7)
    # Test with both operands negative, close to zero
    test("Both operands negative, close to zero", calculate_operations, "Sum: -2, Product: 1, Difference: 0", -1, -1)
    # Test with decimal numbers
    test("Adding decimal numbers", calculate_operations, "Sum: 5.5, Product: 7.26, Difference: 1.0999999999999996", 3.3, 2.2)
    # Test with very small numbers
    test("Working with small decimal numbers", calculate_operations, "Sum: 0.2, Product: 0.0075, Difference: 0.09999999999999999", 0.15, 0.05)
    # Test with one very large and one small number
    test("One large and one small number", calculate_operations, "Sum: 100000.05, Product: 5000.0, Difference: 99999.95", 100000, 0.05)
    # Test where difference is zero
    test("Difference resulting in zero", calculate_operations, "Sum: 10, Product: 25, Difference: 0", 5, 5)
    # Test addition leading to a round number
    test("Addition leading to a round number", calculate_operations, "Sum: 100, Product: 2275, Difference: 30", 65, 35)
    # Test with negative decimal numbers
    test("Adding negative decimal numbers", calculate_operations, "Sum: -5.5, Product: 7.26, Difference: -1.0999999999999996", -3.3, -2.2)
