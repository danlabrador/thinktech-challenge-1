def describe(description):
    def it(test_description, test_func, expected, *args, **kwargs):
        full_description = f"{description} - {test_description}:"
        try:
            result = test_func(*args, **kwargs)
            if result == expected:
                print(f"\n\033[92m✔ PASSED: {full_description}\033[0m")
            else:
                print(f"\n\033[91m✘ FAILED: {full_description}\033[0m")
                print(f"   Inputs: {args} {kwargs}")
                print(f"   Expected: '{expected}'")
                print(f"   Actual:   '{result}'")
        except Exception as e:
            print(f"\n\033[91m✘ ERROR in {full_description}\033[0m")
            print(f"   Exception: {e}")
    return it
