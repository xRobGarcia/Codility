def solution(A):
	"""Find the smallest positive integer that does not occur in A.
	
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


if __name__ == "__main__":
	print(solution([1, 3, 6, 4, 1, 2]))  # 5
	print(solution([1, 2, 3]))  # 4
	print(solution([-1, -3]))  # 1
	print(solution([1]))  # 2
	print(solution([2]))  # 1
	print(solution([5]))  # 1


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