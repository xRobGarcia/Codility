# MaxProfit - Codility Solution

def solution(A):
    """
    MaxProfit (Codility)
    --------------------
    Given daily stock prices A, return the maximum profit from one transaction
    (buy once, sell once) with buy day <= sell day. If no profit is possible,
    return 0.

    Time:  O(N)
    Space: O(1)
    """
    n = len(A)
    if n < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        # If today's price is a new minimum, it's a better buy candidate.
        if price < min_price:
            min_price = price
        else:
            # Otherwise, consider selling today.
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# ------------------ Tests ------------------
if __name__ == "__main__":
    test_cases = [
        ([23171, 21011, 21123, 21366, 21013, 21367], 356),  # Example: buy day 1, sell day 5
        ([5, 4, 3, 2, 1], 0),                               # Strictly decreasing - no profit
        ([1, 2, 3, 4, 5], 4),                               # Strictly increasing - buy first, sell last
        ([3, 1, 4, 1, 5, 9, 2, 6], 8),                      # Buy at 1 (day 1 or 3), sell at 9
        ([10], 0),                                          # Single element
        ([], 0),                                            # Empty array
        ([5, 5, 5, 5], 0),                                  # All same - no profit
        ([10, 7, 5, 8, 11, 9], 6),                          # Buy at 5, sell at 11
    ]
    
    print("Testing MaxProfit solution:\n")
    all_passed = True
    
    for array, expected in test_cases:
        result = solution(array)
        is_correct = result == expected
        all_passed &= is_correct
        status = "✓" if is_correct else "✗"
        print(f"{status} A={array}")
        print(f"   Expected: {expected}, Got: {result}\n")
    
    print(f"{'All tests passed!' if all_passed else 'Some tests failed!'}")


# MaxProfit

# Given a log of stock prices compute the maximum possible earning.
# Programming language: 
# Python
# Spoken language: 
# English
# An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

# For example, consider the following array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

# Write a function,

# def solution(A)

# that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

# For example, given array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# the function should return 356, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..400,000];
# each element of array A is an integer within the range [0..200,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.