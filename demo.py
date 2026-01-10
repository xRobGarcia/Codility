

def solution(A):
	"""
	MissingInteger (Codility)
	-------------------------
	Return the smallest positive integer (> 0) that does not occur in A.

	Time:  O(N) - single pass to mark seen values + single pass to find answer
	Space: O(N) - boolean array of size N+2 (answer is in [1..N+1])
	"""
	n = len(A)

	seen = [False] * (n + 2)
	for x in A:
		if 1 <= x <= n + 1:
			seen[x] = True

	for i in range(1, n + 2):
		if not seen[i]:
			return i

	return n + 1


def solution_with_xor(A):
	"""
	MissingInteger (Codility) - XOR attempt with safe fallback
	---------------------------------------------------------
	XOR ONLY works when A is a permutation-like array of size N with values in
	[1..N+1] and exactly one missing (i.e., PermMissingElem conditions).

	This wrapper:
	- If A matches those conditions: uses XOR (Time: O(N), Space: O(1))
	- Otherwise: falls back to the correct MissingInteger solution() (O(N) / O(N))
	"""
	n = len(A)

	seen = [False] * (n + 2)
	for x in A:
		if x <= 0 or x > n + 1 or seen[x]:
			return solution(A)
		seen[x] = True

	result = n + 1
	for i, num in enumerate(A, 1):
		result ^= i ^ num
	return result


if __name__ == "__main__":
	tests = [
		([1, 3, 6, 4, 1, 2], 5),
		([1, 2, 3], 4),
		([-1, -3], 1),
		([2], 1),
		([1], 2),
	]

	for A, expected in tests:
		result = solution(A)
		result_xor = solution_with_xor(A)
		status = "✓" if result == expected else "✗"
		status_xor = "✓" if result_xor == expected else "✗"
		print(f"{status} A={A} → {result} (expected {expected})")
		print(f"{status_xor} XOR wrapper → {result_xor}")


# This is a demo task.

# Write a function:

# def solution(A)
# content_copy

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
