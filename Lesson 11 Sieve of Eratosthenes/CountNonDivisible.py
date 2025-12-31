
def solution(A):
    """
    CountNonDivisible (Codility)
    ----------------------------
    For each A[i], return how many elements in A are NOT divisors of A[i].

    Time:  O(maxA log maxA)  (sieve over multiples), with maxA <= 2N
    Space: O(maxA)
    """
    n = len(A)
    maxA = max(A)

    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1

    div_cnt = [0] * (maxA + 1)
    present = [i for i, c in enumerate(freq) if c]

    limit = maxA + 1
    for d in present:
        c = freq[d]
        m = d
        while m < limit:
            div_cnt[m] += c
            m += d

    return [n - div_cnt[x] for x in A]


# Test with the example
if __name__ == "__main__":
    A = [3, 1, 2, 3, 6]
    result = solution(A)
    print(f"Input: {A}")
    print(f"Output: {result}")
    print(f"Expected: [2, 4, 3, 2, 0]")
    
    # Note: O(N²) detailed breakdown removed for production use
    # Only safe for tiny test cases



# CountNonDivisible

# Calculate the number of elements of an array that are not divisors of each element.
# Programming language: 
# Python
# You are given an array A consisting of N integers.

# For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

# For example, consider integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:

# A[0] = 3, the non-divisors are: 2, 6,
# A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# A[2] = 2, the non-divisors are: 3, 3, 6,
# A[3] = 3, the non-divisors are: 2, 6,
# A[4] = 6, there aren't any non-divisors.
# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# the function should return [2, 4, 3, 2, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..2 * N].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
