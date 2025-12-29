

# Brackets - Codility Solution
# Time:  O(N) - single pass through string
# Space: O(N) - stack stores opening brackets

def solution(S: str) -> int:
    stack = []
    opener_for = {')': '(', ']': '[', '}': '{'}

    for ch in S:
        if ch in opener_for:
            if not stack or stack[-1] != opener_for[ch]:
                return 0
            stack.pop()
        else:
            stack.append(ch)

    return 1 if not stack else 0


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("{[()()]}", 1),           # Properly nested
        ("([)()]", 0),             # Cross-nested (improper)
        ("((((", 0),               # Only opening brackets
        ("))))", 0),               # Only closing brackets
        ("", 1),                   # Empty string is properly nested
        ("{[(])}", 0),             # Wrong order: [ closed before (
        ("{{{{", 0),               # Unmatched opening
        ("}}}}", 0),               # Closing without opening
        ("()", 1),                 # Single pair
        ("()()()", 1),             # Multiple pairs in sequence
        ("((()))", 1),             # Nested pairs
        ("({[]})", 1),             # All types nested
        ("({[}])", 0),             # Mismatched types
    ]
    
    print("Testing Brackets solution:\n")
    all_passed = True
    
    for S, expected in test_cases:
        result = solution(S)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status} S = '{S:12s}' → {result} (expected {expected})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# Brackets

# Determine whether a given string of parentheses (multiple types) is properly nested.
# Programming language: 
# Python
# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.