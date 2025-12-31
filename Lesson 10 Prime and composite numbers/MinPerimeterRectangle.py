# MinPerimeterRectangle - Codility Solution
# Time:  O(√N)
# Space: O(1)

import math

def solution(N):
    """
    Minimal perimeter: find largest divisor ≤ √N.
    Time: O(√N), Space: O(1)
    """
    root = math.isqrt(N)
    for a in range(root, 0, -1):
        if N % a == 0:
            return 2 * (a + N // a)


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        (1, 4),       # 1×1
        (30, 22),     # 5×6
        (36, 24),     # 6×6 (perfect square)
        (100, 40),    # 10×10
        (101, 204),   # 1×101 (prime)
        (1000000000, 126500),
    ]
    
    print("Testing MinPerimeterRectangle solution:\n")
    all_passed = True
    
    for n, expected in test_cases:
        result = solution(n)
        is_correct = result == expected
        all_passed &= is_correct
        
        # Show factorization
        root = math.isqrt(n)
        for a in range(root, 0, -1):
            if n % a == 0:
                A, B = a, n // a
                break
        
        status = "✓" if is_correct else "✗"
        print(f"{status} N={n}: {A}×{B}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# MinPerimeterRectangle

# Find the minimal perimeter of any rectangle whose area equals N.
# Programming language: 
# Python
# An integer N is given, representing the area of some rectangle.

# The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

# The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

# For example, given integer N = 30, rectangles of area 30 are:

# (1, 30), with a perimeter of 62,
# (2, 15), with a perimeter of 34,
# (3, 10), with a perimeter of 26,
# (5, 6), with a perimeter of 22.
# Write a function:

# def solution(N)

# that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

# For example, given an integer N = 30, the function should return 22, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..1,000,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.