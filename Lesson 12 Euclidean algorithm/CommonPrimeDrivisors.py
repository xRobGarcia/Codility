
"""CommonPrimeDivisors helpers and solution."""

from math import gcd


def _strip_common(x: int, common: int) -> int:
    while x != 1:
        d = gcd(x, common)
        if d == 1:
            return x
        x //= d
    return 1


def _same_primes(a: int, b: int) -> bool:
    common = gcd(a, b)

    if _strip_common(a, common) != 1:
        return False

    return _strip_common(b, common) == 1


def solution(A, B):
    """
    CommonPrimeDivisors (Codility)
    -------------------------------
    Count pairs whose prime-divisor sets are exactly the same.

    Time: O(Z * log(maxV)^2) in practice from repeated gcd reductions
    Space: O(1)

    Trick:
    Let common = gcd(a, b). If a and b have the same prime divisors, then every
    prime factor in a and b must also be inside common.

    Example 1:
      a = 15, b = 75, common = 15
      15 -> divide by gcd(15, 15) = 15 -> 1
      75 -> divide by gcd(75, 15) = 15 -> 5
         -> divide by gcd(5, 15) = 5 -> 1
      Both end at 1, so both use only primes {3, 5}.

    Example 2:
      a = 10, b = 30, common = 10
      10 -> divide by gcd(10, 10) = 10 -> 1
      30 -> divide by gcd(30, 10) = 10 -> 3
         -> gcd(3, 10) = 1, so 3 remains
      That leftover 3 exists only in b, so the prime-divisor sets differ.
    """
    count = 0

    for a, b in zip(A, B):
        if _same_primes(a, b):
            count += 1

    return count


if __name__ == "__main__":
    tests = [
        ([15, 10, 3], [75, 30, 5], 1),
        ([2, 1, 12], [4, 1, 18], 3),
        ([9, 10, 14], [5, 30, 28], 1),
    ]

    for A, B, expected in tests:
        result = solution(A, B)
        print(f"A:        {A}")
        print(f"B:        {B}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"OK:       {result == expected}\n")