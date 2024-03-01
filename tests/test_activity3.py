# tests/test_activity3.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity3 import categorize_age

# Descriptive testing for Activity 3
if __name__ == "__main__":
    test = describe("Activity 3: Categorize Age Functionality")

    # Test with ages for a minor
    test("Age below 18 should categorize as Minor", categorize_age, "Minor", 17)
    test("Age at the boundary of Minor (exclusive)", categorize_age, "Minor", 0)

    # Test with ages for a young adult
    test("Age at the lower boundary of Young Adult (inclusive)", categorize_age, "Young Adult", 18)
    test("Age in the middle of Young Adult range", categorize_age, "Young Adult", 30)
    test("Age at the upper boundary of Young Adult (inclusive)", categorize_age, "Young Adult", 40)

    # Test with ages for an adult
    test("Age just above Young Adult range", categorize_age, "Adult", 41)
    test("Age well above Young Adult range", categorize_age, "Adult", 60)

    # Edge cases and unusual values
    test("Negative age (unrealistic but test-worthy)", categorize_age, "Minor", -1)
    test("Very high age", categorize_age, "Adult", 120)
    test("Age as a floating point (should still work)", categorize_age, "Young Adult", 18.5)
