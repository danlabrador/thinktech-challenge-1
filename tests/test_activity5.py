# tests/test_activity5.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity5 import format_data

# Descriptive testing for Activity 5
if __name__ == "__main__":
    test = describe("5: Format Data")

    # Test with typical data
    test("Formatting with typical data", format_data, 
         "John Doe is 30 years old and loves the color blue.", 
         ("John", "Doe", 30), {"favorite_color": "blue"})

    # Test with empty first name
    test("Formatting with empty first name", format_data, 
         " Doe is 25 years old and loves the color green.", 
         ("", "Doe", 25), {"favorite_color": "green"})

    # Test with empty last name
    test("Formatting with empty last name", format_data, 
         "Alice  is 22 years old and loves the color red.", 
         ("Alice", "", 22), {"favorite_color": "red"})

    # Test with empty favorite color
    test("Formatting with empty favorite color", format_data, 
         "Charlie Brown is 28 years old and loves the color .", 
         ("Charlie", "Brown", 28), {"favorite_color": ""})

    # Test with all parameters empty
    test("Formatting with all parameters empty", format_data, 
         "  is 0 years old and loves the color .", 
         ("", "", 0), {"favorite_color": ""})

    # Test with non-traditional names and colors
    test("Formatting with non-traditional names and colors", format_data, 
         "X Æ A-12 Musk is 1 year old and loves the color infrared.", 
         ("X Æ A-12", "Musk", 1), {"favorite_color": "infrared"})

    # Test with long strings
    test("Formatting with long strings", format_data, 
         "Maximiliana Constantine the Third is 89 years old and loves the color ultraviolet.", 
         ("Maximiliana", "Constantine the Third", 89), {"favorite_color": "ultraviolet"})

    # Test with non-integer age
    test("Formatting with non-integer age", format_data, 
      "John Doe is 30.5 years old and loves the color blue.", 
      ("John", "Doe", 30.5), {"favorite_color": "blue"})

    # Test with missing age
    test("Formatting with missing age", format_data, 
      "John Doe is years old and loves the color blue.", 
      ("John", "Doe"), {"favorite_color": "blue"})

    # Test with missing favorite color
    test("Formatting with missing favorite color", format_data, 
      "John Doe is 30 years old and loves the color .", 
      ("John", "Doe", 30), {})

    # Test with additional information
    test("Formatting with additional information", format_data, 
      "John Doe is 30 years old and loves the color blue. Occupation: Engineer", 
      ("John", "Doe", 30), {"favorite_color": "blue", "occupation": "Engineer"})
