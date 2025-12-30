# MaxSliceSum - Codility Solution (Kadane's Algorithm)

def solution(A):
    """
    MaxSliceSum (Codility)
    ----------------------
    Find the maximum sum of any contiguous subarray (slice).

    Strategy:
    - Use Kadane's algorithm.
    - At each position we decide:
        • continue the previous slice
        • or start a new slice from the current value

    Complexity:
    - Time:  O(N)
    - Space: O(1)
    """

    # Edge case: array with a single element
    max_slice_ending = A[0]   # Best sum ending at current position
    max_slice_global = A[0]   # Best sum found so far

    # Iterate from the second element
    for value in A[1:]:
        # Key decision (GREEDY):
        # Is it better to keep adding or start fresh?
        max_slice_ending = max(value, max_slice_ending + value)

        # Update global maximum if it improves
        max_slice_global = max(max_slice_global, max_slice_ending)

    return max_slice_global


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([3, 2, -6, 4, 0], 5),              # Example: slice [3, 2] = 5
        ([-2, -3, -1, -5], -1),             # All negative: return least negative
        ([5, -7, 3, 5, -2, 1], 8),          # Slice [3, 5, -2, 1] = 8
        ([1], 1),                           # Single element
        ([10, -5, 2, 3], 10),               # Single element gives max
        ([-1, -2, -3], -1),                 # All negative
        ([1, 2, 3, 4, 5], 15),              # All positive: sum all
        ([5, -3, 5], 7),                    # Slice [5, -3, 5] = 7
        ([-10, 2, -1, 3, -1, 5], 8),        # Slice [2, -1, 3, -1, 5] = 8
    ]
    
    print("Testing MaxSliceSum solution:\n")
    all_passed = True
    
    for array, expected in test_cases:
        result = solution(array)
        is_correct = result == expected
        all_passed &= is_correct
        status = "✓" if is_correct else "✗"
        print(f"{status} A={array}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# MaxSliceSum

# Find a maximum sum of a compact subsequence of array elements.
# Programming language: 
# Python
# Spoken language: 
# English
# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

# For example, given array A such that:

# A[0] = 3  A[1] = 2  A[2] = -6
# A[3] = 4  A[4] = 0
# the function should return 5 because:

# (3, 4) is a slice of A that has sum 4,
# (2, 2) is a slice of A that has sum −6,
# (0, 1) is a slice of A that has sum 5,
# no other slice of A has sum greater than (0, 1).
# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..1,000,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000];
# the result will be an integer within the range [−2,147,483,648..2,147,483,647].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.