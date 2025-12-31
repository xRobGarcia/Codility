import math

def solution(A):
    """Max flags on peaks using a next-peak jump table + binary search.
    Time: O(n + √n log n). Space: O(n).
    """
    n = len(A)
    if n < 3:
        return 0

    # 1) Identify peaks
    is_peak = [False] * n
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            is_peak[i] = True

    # 2) Build next_peak[i] = index of first peak at or after i, else -1
    next_peak = [-1] * (n + 1)
    for i in range(n - 1, -1, -1):
        next_peak[i] = i if is_peak[i] else next_peak[i + 1]

    if next_peak[0] == -1:
        return 0

    # Binary search for max K
    peak_count = sum(is_peak)
    lo, hi = 1, min(int(math.isqrt(n)) + 1, peak_count)
    ans = 1

    while lo <= hi:
        mid = (lo + hi) // 2
        
        # Check if we can place mid flags
        pos = next_peak[0]
        used = 0
        while pos != -1 and used < mid:
            used += 1
            jump = pos + mid
            pos = next_peak[jump] if jump <= n else -1
        
        if used == mid:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3),
        ([1, 3, 2], 1),
        ([1, 2, 1], 1),
        ([0, 0, 0], 0),
        ([1, 2, 3, 4, 5], 0),  # No peaks
        ([1], 0),
        ([1, 2], 0),
    ]
    
    print("Testing Flags solution:\n")
    all_passed = True
    
    for A, expected in test_cases:
        result = solution(A)
        is_correct = result == expected
        all_passed &= is_correct
        
        status = "✓" if is_correct else "✗"
        print(f"{status} A={A}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

# For example, given the mountain range represented by array A, above, with N = 12, if you take:

# two flags, you can set them on peaks 1 and 5;
# three flags, you can set them on peaks 1, 5 and 10;
# four flags, you can set only three flags, on peaks 1, 5 and 10.
# You can therefore set a maximum of three flags in this case.

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# the function should return 3, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..400,000];
# each element of array A is an integer within the range [0..1,000,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.