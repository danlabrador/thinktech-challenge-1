# tests/test_activity7.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity7 import run_quiz

# Sample questions for the quiz
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct": "4"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "H2"], "correct": "H2O"}
]

# Descriptive testing for Activity 7
if __name__ == "__main__":
    test = describe("Activity 7: Quiz Game Functionality")

    # Test with all correct answers
    test("All answers correct", run_quiz, 3, questions, ["Paris", "4", "H2O"])

    # Test with some incorrect answers
    test("Some answers incorrect", run_quiz, 1, questions, ["London", "4", "CO2"])

    # Test with all incorrect answers
    test("All answers incorrect", run_quiz, 0, questions, ["Madrid", "5", "O2"])

    # Test with no answers (simulating no input/skipped questions)
    test("No answers provided", run_quiz, 0, questions, ["", "", ""])

    # Additional custom test cases...
