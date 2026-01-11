def solution(N, P, Q):
    # Time:  O(N log log N + M)
    # Space: O(N)

    # Build smallest prime factor (SPF) array
    spf = [0] * (N + 1)

    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == 0:              # i is prime
            for j in range(i * i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i

    # Mark remaining primes
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i

    # Identify semiprimes
    semiprime = [0] * (N + 1)
    for i in range(4, N + 1):
        p = spf[i]
        q = i // p
        if spf[q] == q:              # q is prime
            semiprime[i] = 1

    # Prefix sums of semiprimes
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + semiprime[i]

    # Answer queries
    result = []
    for i in range(len(P)):
        result.append(prefix[Q[i]] - prefix[P[i] - 1])

    return result



if __name__ == "__main__":
    N = 26
    P = [1, 4, 16]
    Q = [26, 10, 20]
    print(solution(N, P, Q))  # Expected: [10, 4, 0]

    assert solution(1, [1], [1]) == [0]
    assert solution(2, [1], [2]) == [0]
    assert solution(4, [1], [4]) == [1]   # {4}
    assert solution(5, [4], [5]) == [1]   # {4}
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
