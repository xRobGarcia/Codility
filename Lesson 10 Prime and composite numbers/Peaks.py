import math

def solution(A):
    """
    Return max number of equal-sized blocks, each with ≥1 peak.
    
    Peak: A[i-1] < A[i] > A[i+1]
    Strategy: Prefix sums + try divisors (small→large) for early max.
    
    Time: O(N·d(N)), Space: O(N)
    """
    # Step 1: Need at least 3 elements for a peak
    array_length = len(A)
    if array_length < 3:
        return 0

    # Step 2: Build prefix sum: peak_prefix[i] = #peaks in A[0:i]
    peak_prefix = [0] * (array_length + 1)
    total_peaks = 0
    for index in range(1, array_length - 1):
        if A[index - 1] < A[index] > A[index + 1]:
            total_peaks += 1
        peak_prefix[index + 1] = total_peaks
    peak_prefix[array_length] = total_peaks

    # Step 3: Early exit if no peaks
    if total_peaks == 0:
        return 0

    # Step 4: Find all divisors of N (possible block sizes in increasing order)
    sqrt_length = math.isqrt(array_length)
    block_sizes = []
    large_divisors = []
    for divisor in range(1, sqrt_length + 1):
        if array_length % divisor == 0:
            block_sizes.append(divisor)
            complement = array_length // divisor
            if complement != divisor:
                large_divisors.append(complement)
    block_sizes.extend(reversed(large_divisors))

    # Step 5: Try each block size (smallest first = max blocks first)
    for block_size in block_sizes:
        num_blocks = array_length // block_size
        
        # Prune: can't have more blocks than peaks
        if num_blocks > total_peaks:
            continue

        # Step 6: Check if every block has at least one peak
        for block_start in range(0, array_length, block_size):
            if peak_prefix[block_start + block_size] == peak_prefix[block_start]:
                break
        else:
            return num_blocks

    return 0


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3, "Example from problem"),
        ([1, 3, 2], 1, "Single peak - one block"),
        ([1, 2, 1], 1, "One peak"),
        ([1, 2, 3], 0, "No peaks"),
        ([1, 2, 3, 4, 5], 0, "No peaks (increasing)"),
        ([5, 4, 3, 2, 1], 0, "No peaks (decreasing)"),
        ([0, 0, 0], 0, "No peaks (flat)"),
        ([1], 0, "Too small"),
        ([1, 2], 0, "Too small"),
        ([1, 2, 1, 2, 1], 1, "Two peaks, can only make 1 block (N=5 is prime)"),
    ]
    
    print("Testing Peaks solution:\n")
    all_passed = True
    
    for A, expected, description in test_cases:
        result = solution(A)
        is_correct = result == expected
        all_passed &= is_correct
        
        status = "✓" if is_correct else "✗"
        print(f"{status} {description}")
        print(f"   A={A}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# Peaks

# Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 2
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
# has exactly three peaks: 3, 5, 10.

# We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

# A[0], A[1], ..., A[K − 1],
# A[K], A[K + 1], ..., A[2K − 1],
# ...
# A[N − K], A[N − K + 1], ..., A[N − 1].
# What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

# The goal is to find the maximum number of blocks into which the array A can be divided.

# Array A can be divided into blocks as follows:

# one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
# two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
# three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
# However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

# The maximum number of blocks that array A can be divided into is three.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

# If A cannot be divided into some number of blocks, the function should return 0.

# For example, given:

#     A[0] = 1
#     A[1] = 2
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

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.