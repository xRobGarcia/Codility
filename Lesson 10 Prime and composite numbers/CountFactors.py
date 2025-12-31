# CountFactors - Codility Solution

import math

def solution(N):
    """
    Count factors of N.
    Factors come in pairs (i, N//i), only iterate up to √N.
    Time: O(√N), Space: O(1)
    """
    count = 0
    limit = math.isqrt(N)
    
    for i in range(1, limit + 1):
        if N % i == 0:
            # Each factor i has a "pair" N//i
            # Example: if N=24 and i=3, then N//i=8
            # Both are factors: 24 = 3×8
            count += 2  # Count both: i and N//i
    
    if limit * limit == N:  # Perfect square adjustment
        count -= 1
    
    return count


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        (1, 1),      # Only factor: 1
        (24, 8),     # Factors: 1,2,3,4,6,8,12,24
        (16, 5),     # Factors: 1,2,4,8,16 (4 is sqrt, counted once)
        (36, 9),     # Factors: 1,2,3,4,6,9,12,18,36 (6 is sqrt)
        (10, 4),     # Factors: 1,2,5,10
        (2147483647, 2),  # Prime number (max value)
    ]
    
    print("Testing CountFactors solution:\n")
    all_passed = True
    
    for n, expected in test_cases:
        result = solution(n)
        is_correct = result == expected
        all_passed &= is_correct
        status = "✓" if is_correct else "✗"
        print(f"{status} N={n}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# CountFactors

# Count factors of given number n.
# Programming language: 
# Python
# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the number of its factors.

# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.