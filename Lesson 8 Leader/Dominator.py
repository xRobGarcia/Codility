# Dominator - Codility Solution
# Time:  O(N)  (Boyer–Moore + one verification pass)
# Space: O(1)

def solution(A):
    """
    Returns an index of the dominator (value occurring in > N/2 positions),
    or -1 if no dominator exists.
    """
    array_length = len(A)
    if array_length == 0:
        return -1

    # Phase 1: Boyer–Moore to find a candidate
    candidate_index = 0
    vote_count = 0

    for index, value in enumerate(A):
        if vote_count == 0:
            candidate_index = index
            vote_count = 1
        elif value == A[candidate_index]:
            vote_count += 1
        else:
            vote_count -= 1

    # If vote_count == 0, no candidate survived
    if vote_count == 0:
        return -1

    # Phase 2: verify the candidate
    candidate_value = A[candidate_index]
    required_count = array_length // 2 + 1
    occurrences = sum(1 for value in A if value == candidate_value)

    if occurrences >= required_count:
        return candidate_index

    return -1


# ------------------ simple tests ------------------
from collections import Counter

def _is_valid_answer(A, index):
    array_length = len(A)
    
    if index == -1:
        # Valid only if no dominator exists
        if array_length == 0:
            return True
        counts = Counter(A)
        return max(counts.values()) <= array_length // 2
    
    if not (0 <= index < array_length):
        return False
    
    value = A[index]
    return A.count(value) > array_length // 2


if __name__ == "__main__":
    test_cases = [
        [3, 4, 3, 2, 3, -1, 3, 3],  # dominator = 3
        [1, 2, 3],                  # none
        [1],                        # dominator = 1
        [],                         # none
        [1, 1, 1, 2, 2],            # dominator = 1
        [2, 2, 2, 2, 1],            # dominator = 2
    ]

    print("Testing Dominator solution:\n")
    all_passed = True
    for array in test_cases:
        result = solution(array)
        is_valid = _is_valid_answer(array, result)
        all_passed &= is_valid
        status = "✓" if is_valid else "✗"
        print(f"{status} A={array} -> {result}")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# Dominator

# Find an index of an array such that its value occurs at more than half of indices in the array.
# Programming language: 
# Python
# Spoken language: 
# English
# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

# For example, consider array A such that

#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

# Write a function

# def solution(A)

# that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

# For example, given array A such that

#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.