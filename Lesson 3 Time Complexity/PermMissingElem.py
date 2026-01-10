def solution(A):
    """
    Find missing element using arithmetic formula.
    Time: O(N), Space: O(1)
    
    Sum of 1..N = N(N+1)/2
    Missing = expected_sum - actual_sum
    """
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum

# Alternative: XOR-based solution using reduce
def solution_xor(A):
    """
    Find missing element using XOR with reduce.
    Time: O(N), Space: O(N) - creates combined list
    
    XOR all numbers 1..(N+1) with all numbers in A.
    Paired numbers cancel (a^a=0), leaving only missing element.
    """
    from functools import reduce
    from operator import xor

    N = len(A)
    all_numbers = list(range(1, N + 2)) + A
    return reduce(xor, all_numbers)

# Alternative: XOR-based solution using ^= (more efficient)
def solution_xor_compact(A):
    """
    Find missing element using XOR with ^= operator.
    Time: O(N), Space: O(1)
    
    Start with N+1, then XOR each index with its value.
    Paired numbers cancel, leaving only missing element.
    """
    result = len(A) + 1  # Last number in range [1..N+1]
    for i, num in enumerate(A, 1):  # i goes from 1 to N
        result ^= i ^ num
    return result

# Test
if __name__ == "__main__":
    A = [2, 3, 1, 5]
    print("Sum solution:", solution(A))  # 4
    print("XOR solution:", solution_xor(A))  # 4
    print("XOR ^= solution:", solution_xor_compact(A))  # 4

# PermMissingElem
# START
# Find the missing element in a given permutation.
# Programming language: 
# Python
# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.