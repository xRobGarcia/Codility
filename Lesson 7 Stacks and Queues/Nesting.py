# Nesting - Codility Solution
# Time:  O(N) - single pass through string
# Space: O(1) - only counter needed

def solution(S: str) -> int:
    balance = 0
    
    for ch in S:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            balance -= 1
            if balance < 0:
                return 0  # More closing than opening
    
    return 1 if balance == 0 else 0


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("(()(())())", 1),   # Properly nested
        ("())", 0),          # Too many closing
        ("", 1),             # Empty string
        ("(", 0),            # Only opening
        (")", 0),            # Only closing
        ("()()", 1),         # Multiple pairs
        ("(())", 1),         # Nested
        ("((", 0),           # Unmatched opening
        ("))(", 0),          # Wrong order
    ]
    
    print("Testing Nesting solution:\n")
    all_passed = True
    
    for S, expected in test_cases:
        result = solution(S)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status} S = '{S:15s}' → {result} (expected {expected})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# Nesting

# Determine whether a given string of parentheses (single type) is properly nested.
# Programming language: 
# Python
# Spoken language: 
# English
# A string S consisting of N characters is called properly nested if:

# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000,000];
# string S is made only of the characters '(' and/or ')'.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.