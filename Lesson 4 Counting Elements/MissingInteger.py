def solution(A):
	"""Find the smallest positive integer that does not occur in A.
	
	Approach 1: Boolean array - predictable performance
	Time: O(N)
	Space: O(N)
	"""
	n = len(A)
	seen = [False] * (n + 1)
	
	for value in A:
		if 1 <= value <= n:
			seen[value] = True
	
	for i in range(1, n + 1):
		if not seen[i]:
			return i
	
	return n + 1


def solution_set(A):
	"""Find the smallest positive integer that does not occur in A.
	
	Approach 2: Set-based - potentially faster for sparse data
	Time: O(N)
	Space: O(N) worst case, O(K) where K = count of positive numbers
	"""
	positive_set = set(x for x in A if x > 0)
	
	i = 1
	while i in positive_set:
		i += 1
	return i


if __name__ == "__main__":
	print("Approach 1: Boolean array")
	print(solution([1, 3, 6, 4, 1, 2]))  # 5
	print(solution([1, 2, 3]))  # 4
	print(solution([-1, -3]))  # 1
	print(solution([1]))  # 2
	print(solution([2]))  # 1
	print(solution([5]))  # 1
	
	print("\nApproach 2: Set-based")
	print(solution_set([1, 3, 6, 4, 1, 2]))  # 5
	print(solution_set([1, 2, 3]))  # 4
	print(solution_set([-1, -3]))  # 1
	print(solution_set([1]))  # 2
	print(solution_set([2]))  # 1
	print(solution_set([5]))  # 1


# MissingInteger
# START
# Find the smallest positive integer that does not occur in a given sequence.
# Programming language: 
# Python
# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.