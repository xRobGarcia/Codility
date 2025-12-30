# EquiLeader - Codility Solution
# Time:  O(N)
# Space: O(1) extra (besides input array)

def solution(A):
    """
    Returns the number of equi leaders in the array.
    An equi leader is an index S where both left and right subsequences
    have the same leader value.
    """
    n = len(A)
    if n < 2:
        return 0  # no split possible

    # Step 1: Find candidate leader (Boyer-Moore majority vote)
    candidate = None
    vote_count = 0

    for value in A:
        if vote_count == 0:
            candidate = value
            vote_count = 1
        elif value == candidate:
            vote_count += 1
        else:
            vote_count -= 1

    # Step 2: Verify candidate is a leader
    total_leader_count = sum(1 for value in A if value == candidate)
    if total_leader_count * 2 <= n:
        return 0  # no leader => no equi leaders

    # Step 3: Count equi leaders
    equi_leader_count = 0
    left_leader_count = 0

    for i in range(n - 1):
        if A[i] == candidate:
            left_leader_count += 1

        left_length = i + 1
        right_length = n - left_length
        right_leader_count = total_leader_count - left_leader_count

        if (left_leader_count * 2 > left_length and 
            right_leader_count * 2 > right_length):
            equi_leader_count += 1

    return equi_leader_count


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([4, 3, 4, 4, 4, 2], 2),           # Example from problem
        ([4, 4, 2, 5, 3, 4, 4, 4], 3),     # Multiple equi leaders
        ([1, 2, 3], 0),                    # No leader
        ([1, 1, 1, 1], 3),                 # All same (all positions are equi leaders)
        ([1], 0),                          # Single element (no split possible)
        ([1, 2, 1], 0),                    # Leader is 1 but no equi-leaders
        ([2, 1, 1, 1, 2], 0),              # Leader is 1 but no equi-leaders
        ([1, 1, 1], 2),                    # All 1s: positions 0 and 1 are equi-leaders
    ]
    
    print("Testing EquiLeader solution:\n")
    all_passed = True
    
    for array, expected in test_cases:
        result = solution(array)
        is_correct = result == expected
        all_passed &= is_correct
        status = "✓" if is_correct else "✗"
        print(f"{status} A={array}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# EquiLeader

# Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

# For example, given:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.