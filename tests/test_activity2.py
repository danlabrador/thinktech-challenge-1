# tests/test_activity2.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity2 import create_message

# Descriptive testing for Activity 2
if __name__ == "__main__":
    test = describe("#2: create_message()")

    # Test with typical inputs
    test("Creating message with typical inputs", create_message, "Hello, my name is Alice, I am 30 years old, and my favorite color is blue.", "Alice", 30, "blue")
    # Test with empty name
    test("Creating message with empty name", create_message, "Hello, my name is , I am 25 years old, and my favorite color is green.", "", 25, "green")
    # Test with zero age
    test("Creating message with zero age", create_message, "Hello, my name is Bob, I am 0 years old, and my favorite color is red.", "Bob", 0, "red")
    # Test with empty favorite color
    test("Creating message with empty favorite color", create_message, "Hello, my name is Charlie, I am 22 years old, and my favorite color is .", "Charlie", 22, "")
    # Test with all parameters empty
    test("Creating message with all parameters empty", create_message, "Hello, my name is , I am 0 years old, and my favorite color is .", "", 0, "")
    # Test with negative age (unusual but possible in input)
    test("Creating message with negative age", create_message, "Hello, my name is Dana, I am -5 years old, and my favorite color is purple.", "Dana", -5, "purple")
    # Test with long strings
    test("Creating message with long name and color", create_message, "Hello, my name is Elizabeth Alexandra Mary, I am 95 years old, and my favorite color is a deep and vibrant shade of cerulean.", "Elizabeth Alexandra Mary", 95, "a deep and vibrant shade of cerulean")
    # Test with numerical values in name and color
    test("Creating message with numbers in name and color", create_message, "Hello, my name is R2D2, I am 40 years old, and my favorite color is #0000FF.", "R2D2", 40, "#0000FF")
    # Additional custom test cases...
