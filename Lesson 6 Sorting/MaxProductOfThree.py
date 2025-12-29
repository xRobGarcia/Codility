# MaxProductOfThree - Codility Solution
# O(N log N) time, O(1) space

"""
ALGORITHM EXPLANATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE PROBLEM: Find maximum product of any three numbers in array

KEY INSIGHT: After sorting, maximum product comes from ONLY two cases:

Case 1: Three largest numbers
   Example: [1, 2, 3, 4, 5, 6]
   Answer: 6 × 5 × 4 = 120

Case 2: Two smallest (most negative) × largest positive
   Example: [-10, -5, 1, 2, 3]
   Answer: (-10) × (-5) × 3 = 150
   Why? negative × negative = POSITIVE!
          (-10) × (-5) = 50
          50 × 3 = 150

WHY ONLY THESE TWO CASES?

1. Three positives → obvious (bigger numbers = bigger product)
2. Two negatives + one positive → negatives multiply to POSITIVE, and large 
   negative numbers (like -1000) become large positive (1000) when paired
3. One negative + two positives → ALWAYS worse (negative result or smaller)
4. Three negatives → ALWAYS negative (never maximum)

EXAMPLES:

Example 1: Mix of positive and negative
   A = [-3, 1, 2, -2, 5, 6]
   Sorted: [-3, -2, 1, 2, 5, 6]
   
   Option 1: 6 × 5 × 2 = 60
   Option 2: (-3) × (-2) × 6 = 36
   Maximum: 60 ✓

Example 2: Large negative numbers
   A = [-10, -10, 1, 3, 2]
   Sorted: [-10, -10, 1, 2, 3]
   
   Option 1: 3 × 2 × 1 = 6
   Option 2: (-10) × (-10) × 3 = 300
   Maximum: 300 ✓  (Two negatives make huge positive!)

Example 3: All positive
   A = [4, 7, 3, 2, 5, 1]
   Sorted: [1, 2, 3, 4, 5, 7]
   
   Option 1: 7 × 5 × 4 = 140
   Option 2: 1 × 2 × 7 = 14
   Maximum: 140 ✓

Example 4: All negative
   A = [-5, -2, -7, -3]
   Sorted: [-7, -5, -3, -2]
   
   Option 1: (-2) × (-3) × (-5) = -30
   Option 2: (-7) × (-5) × (-2) = -70
   Maximum: -30 ✓  (Least negative)

COMPLEXITY:
- Time: O(N log N) - sorting dominates
- Space: O(1) - sorting in place (Python's sort modifies original array)
"""

def solution(A):
    # O(N log N) time, O(1) space
    # Max: three largest OR two smallest * largest (negative×negative=positive)
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================
# MaxProductOfThree

# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

# For example, array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:

# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.

# Write a function:

# def solution(A)

# that, given a non-empty array A, returns the value of the maximal product of any triplet.

# For example, given array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.