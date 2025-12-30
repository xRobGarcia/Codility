# MaxDoubleSliceSum - Codility Solution

def solution(A):
    """
    MaxDoubleSliceSum (Codility)
    ----------------------------
    Find the maximum sum of a double slice (X, Y, Z) where:
    - 0 <= X < Y < Z < N
    - Sum = A[X+1] + ... + A[Y-1] + A[Y+1] + ... + A[Z-1]
    - Note: A[X], A[Y], A[Z] are NOT included
    
    Strategy:
    - Use dynamic programming and Kadane's algorithm.
    - Compute two arrays:
        • max_ending[i]: maximum sum of slice ending at index i (computed left→right)
        • max_starting[i]: maximum sum of slice starting at index i (computed right→left)
    - For each Y (the gap), combine: max_ending[Y-1] + max_starting[Y+1]
      (left slice ends before Y, right slice starts after Y)
    
    Complexity:
    - Time:  O(N)
    - Space: O(N)
    """
    n = len(A)
    
    # Edge case: array too small for a double slice
    if n < 4:
        return 0
    
    # Step 1: Compute max_ending: max sum ending at each index from the left
    max_ending = [0] * n
    for i in range(1, n - 1):
        max_ending[i] = max(0, max_ending[i - 1] + A[i])
        # Ensure we don't include negative sums; start fresh if needed
    
    # Step 2: Compute max_starting: max sum starting at each index from the right
    max_starting = [0] * n
    for i in range(n - 2, 0, -1):
        max_starting[i] = max(0, max_starting[i + 1] + A[i])
        # Again, avoid negative sums; reset if necessary
    
    # Step 3: Combine left and right slices for each possible Y
    max_sum = 0
    for y in range(1, n - 1):
        # Combine best left slice ending before Y and best right slice starting after Y
        max_sum = max(max_sum, max_ending[y - 1] + max_starting[y + 1])
    
    return max_sum


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 6, -1, 4, 5, -1, 2], 17),   # Example: (0,3,6) = 2+6+4+5 = 17
        ([0, 10, -5, -2, 0], 10),           # (0,1,4) = 10
        ([5, 17, 0, 3], 17),                # (0,1,3) = 17
        ([6, 1, 5, 6, 4, 2, 9, 4], 26),     # (1,3,7) = 5+6+4+2+9 = 26
        ([-2, -3, -1, -5], 0),              # All negative, best is empty slice
        ([1, 1, 1, 1], 1),                  # (0,1,3) = [] + [1] = 1 or (0,2,3) = [1] + [] = 1
        ([10, -1, -1, 10], 0),              # Best is empty slices both sides
    ]
    
    print("Testing MaxDoubleSliceSum solution:\n")
    all_passed = True
    
    for array, expected in test_cases:
        result = solution(array)
        is_correct = result == expected
        all_passed &= is_correct
        status = "✓" if is_correct else "✗"
        print(f"{status} A={array}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# MaxDoubleSliceSum

# Find the maximal sum of any double slice.
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given.

# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

# For example, array A such that:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:

# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

# For example, given:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# the function should return 17, because no double slice of array A has a sum of greater than 17.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.