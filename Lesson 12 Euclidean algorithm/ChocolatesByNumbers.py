def _gcd(a: int, b: int) -> int:
  while b:
    a, b = b, a % b
  return a


def solution(N: int, M: int) -> int:
    """ChocolatesByNumbers (Codility)
    ---------------------------------
    Count how many distinct chocolates you eat when jumping by M (mod N).

    Time: O(log(min(N, M))) - Euclidean gcd
    Space: O(1)

    Key trick:
    You visit positions: 0, M, 2M, 3M, ... (mod N).
    You stop when you repeat a position, i.e. when k*M ≡ 0 (mod N).

    This is equivalent to: N divides (k*M).
    The smallest such k is:
      k = N / gcd(N, M)

    Example: N=10, M=4
      gcd(10,4)=2 → k = 10//2 = 5
      visited: 0,4,8,2,6 (then back to 0)
    """

    result = N // _gcd(N, M)
    return result


if __name__ == "__main__":
    tests = [
        (10, 4, 5),
        (1, 1, 1),
        (10, 5, 2),
        (10, 6, 5),
        (1000000000, 1, 1000000000),
    ]

    for N, M, exp in tests:
        got = solution(N, M)
        print(f"N={N}, M={M} → {got} (expected {exp})")


# ChocolatesByNumbers


# There are N chocolates in a circle. Count the number of chocolates you will eat.
# Programming language: 
# Python
# Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

# You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

# You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

# More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

# You stop eating when you encounter an empty wrapper.

# For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

# The goal is to count the number of chocolates that you will eat, following the above rules.

# Write a function:

# def solution(N, M)

# that, given two positive integers N and M, returns the number of chocolates that you will eat.

# For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..1,000,000,000].
# Copyright 2009–2026 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


