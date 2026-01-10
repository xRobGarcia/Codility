
from math import isqrt


def solution(N, P, Q):
	"""CountSemiprimes (Codility)

	For each query (P[k], Q[k]) return how many semiprimes are in [P[k], Q[k]].

	Approach:
	- Build smallest-prime-factor (SPF) array up to N using a sieve.
	- Mark semiprimes using SPF (x is semiprime if x = p*q where p and q are prime).
	- Prefix-sum the semiprime markers for O(1) query answers.

	Time:  O(N log log N + M)
	Space: O(N)
	"""
	if len(P) != len(Q):
		raise ValueError("P and Q must have the same length")
	if N < 4 or not P:
		return [0] * len(P)

	# Smallest prime factor sieve (single pass).
	# After this, spf[x] == x iff x is prime (for x >= 2).
	spf = [0] * (N + 1)
	root = isqrt(N)
	for i in range(2, N + 1):
		if spf[i] == 0:
			spf[i] = i
			if i <= root:
				start = i * i
				step = i
				for j in range(start, N + 1, step):
					if spf[j] == 0:
						spf[j] = i

	# Mark semiprimes.
	semiprime = [0] * (N + 1)
	for x in range(4, N + 1):
		p = spf[x]
		q = x // p
		# x is semiprime iff q is prime (p is prime by construction).
		if q > 1 and spf[q] == q:
			semiprime[x] = 1

	# Prefix sums.
	prefix = [0] * (N + 1)
	running = 0
	for i in range(1, N + 1):
		running += semiprime[i]
		prefix[i] = running

	# Answer queries.
	out = [0] * len(P)
	for k, (pk, qk) in enumerate(zip(P, Q)):
		out[k] = prefix[qk] - prefix[pk - 1]

	return out


if __name__ == "__main__":
	# Example from the problem statement
	N = 26
	P = [1, 4, 16]
	Q = [26, 10, 20]
	print(solution(N, P, Q))  # Expected: [10, 4, 0]

	# A few extra sanity checks
	assert solution(1, [1], [1]) == [0]
	assert solution(2, [1], [2]) == [0]
	assert solution(4, [1], [4]) == [1]  # {4}
	assert solution(5, [4], [5]) == [1]  # {4}
	assert solution(10, [1, 4, 7], [10, 10, 10]) == [4, 4, 2]  # {4,6,9,10}


# CountSemiprimes

# Count the semiprime numbers in the given range [a..b]
# Programming language:

# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

# Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

# For example, consider an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# The number of semiprimes within each of these ranges is as follows:

#         (1, 26) is 10,
#         (4, 10) is 4,
#         (16, 20) is 0.

# Write a function:

#     def solution(N, P, Q)

# that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

# For example, given an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# the function should return the values [10, 4, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..50,000];
#         M is an integer within the range [1..30,000];
#         each element of arrays P and Q is an integer within the range [1..N];
#         P[i] ≤ Q[i].

# Copyright 2009–2026 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
