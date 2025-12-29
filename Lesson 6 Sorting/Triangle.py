# Triangle - Codility Solution Template
# O(N log N) time, O(1) space

"""
WHY SORTING WORKS - LOGICAL ANALYSIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Triangle requires THREE conditions (all must be true):
1. A[P] + A[Q] > A[R]
2. A[Q] + A[R] > A[P]
3. A[R] + A[P] > A[Q]

AFTER SORTING: A[i] ≤ A[i+1] ≤ A[i+2]

┌─────────────────────────┬──────────────────────┬─────────────────────┐
│ Condition               │ After Sorting        │ Status              │
├─────────────────────────┼──────────────────────┼─────────────────────┤
│ A[i] + A[i+1] > A[i+2]  │ SMALLEST + MEDIUM    │ ❓ MUST CHECK       │
│                         │ vs LARGEST           │                     │
├─────────────────────────┼──────────────────────┼─────────────────────┤
│ A[i+1] + A[i+2] > A[i]  │ MEDIUM + LARGEST     │ ✓ ALWAYS TRUE       │
│                         │ vs SMALLEST          │ (Sum > Smallest)    │
├─────────────────────────┼──────────────────────┼─────────────────────┤
│ A[i] + A[i+2] > A[i+1]  │ SMALLEST + LARGEST   │ ✓ ALWAYS TRUE       │
│                         │ vs MEDIUM            │ (A[i+2] ≥ A[i+1])   │
└─────────────────────────┴──────────────────────┴─────────────────────┘

PROOF that conditions 2 & 3 are automatic:

Condition 2: A[i+1] + A[i+2] > A[i]
  Since A[i+1] ≥ A[i] (from sorting):
  → A[i+1] + A[i+2] ≥ A[i] + A[i+2]
  → Since A[i+2] > 0 (positive edge):
  → A[i] + A[i+2] > A[i]
  → Therefore: A[i+1] + A[i+2] > A[i] ✓

Condition 3: A[i] + A[i+2] > A[i+1]
  Since A[i+2] ≥ A[i+1] (from sorting):
  → A[i] + A[i+2] ≥ A[i] + A[i+1]
  → Since A[i] ≥ 0 (non-negative edge):
  → A[i] + A[i+1] > A[i+1]
  → Therefore: A[i] + A[i+2] > A[i+1] ✓

CONCLUSION: Only check A[i] + A[i+1] > A[i+2]

EXAMPLE WITH NUMBERS:
  Sorted: [3, 4, 5]
  ┌─────────────────────────────────────────────────────────┐
  │ Condition 1: 3 + 4 > 5? → 7 > 5 ✓ → MUST CHECK          │
  │ Condition 2: 4 + 5 > 3? → 9 > 3 ✓ → AUTOMATIC (always)  │
  │ Condition 3: 3 + 5 > 4? → 8 > 4 ✓ → AUTOMATIC (always)  │
  └─────────────────────────────────────────────────────────┘

WHY CONSECUTIVE ONLY?
  If [A, B, C] fails (A+B ≤ C), then [A, B, D] also fails where D > C
  If [A, B, C] passes, return 1 immediately!


PROBLEM-SOLVING METHODOLOGY (How to reach this logic):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: START WITH CONCRETE EXAMPLES (Simplification)
  Example 1: [3, 4, 5] - classic triangle
    Check: 3+4>5? ✓ (7>5), 4+5>3? ✓ (9>3), 3+5>4? ✓ (8>4)
    Notice: Already sorted! 
  
  Example 2: [10, 2, 5] - unsorted
    Original: Check all combinations? (10,2,5), (10,5,2), (2,5,10)...
    Sorted: [2, 5, 10]
    Check: 2+5>10? ✗ (7>10) → No triangle
    Insight: Sorting helps organize the check!

STEP 2: RECOGNIZE PATTERNS (Pattern Recognition)
  Try more sorted examples:
    [5, 5, 5]: 5+5>5? ✓ → Triangle
    [1, 2, 4]: 1+2>4? ✗ → No triangle
    [3, 4, 6]: 3+4>6? ✓ → Triangle
  
  Pattern emerging: "First condition (smallest sum) seems critical!"

STEP 3: ANALYZE CONSTRAINTS (Mathematical Reasoning)
  Given sorted: a ≤ b ≤ c
  
  Question: Which conditions are ALWAYS true?
  
  Test: b + c > a?
    Since b ≥ a and c > 0 → b + c ≥ a + positive → ALWAYS TRUE ✓
  
  Test: a + c > b?
    Since c ≥ b → a + c ≥ a + b > b → ALWAYS TRUE ✓
  
  Test: a + b > c?
    Smallest sum vs largest value → MUST CHECK ❓
  
  Conclusion: Only need ONE check after sorting!

STEP 4: TEST EDGE CASES (Extreme Value Analysis)
  All same: [5, 5, 5] → 5+5>5 ✓ Works!
  Barely triangle: [3, 4, 6] → 3+4>6 ✓ Works!
  Barely not: [3, 4, 7] → 3+4>7 ✗ Works!
  Large gap: [1, 2, 1000] → 1+2>1000 ✗ Works!

STEP 5: OPTIMIZE WITH GREEDY INSIGHT (Why consecutive?)
  Question: Can I skip elements?
  
  Proof by logic:
    If a+b ≤ c (fails), and d > c (larger element)
    Then a+b ≤ c < d → a+b ≤ d (also fails!)
  
  Conclusion: If consecutive fails, all larger elements fail too!
  
  Greedy strategy: Check consecutive pairs, stop at first success

STEP 6: COMPLEXITY ANALYSIS (Reduction)
  Brute force (no sorting):
    Check all triplets: C(N,3) = O(N³)
    Each needs 3 checks
    Total: O(N³) - TOO SLOW for N=100,000
  
  With sorting:
    Sort: O(N log N)
    Check consecutive: O(N) triplets × 1 check
    Total: O(N log N) - EFFICIENT ✓

STEP 7: VERIFY & PROVE (Look Back)
  Mathematical proof: ✓ (conditions 2 & 3 always true)
  Test cases: ✓ (all pass)
  Complexity: ✓ (meets Codility requirements)
  Edge cases: ✓ (empty, small, negatives)

COGNITIVE TECHNIQUES USED:
  1. Simplification: Start with [3,4,5]
  2. Pattern recognition: Notice sorted structure
  3. Constraint analysis: Which inequalities are redundant?
  4. Reduction: 3 checks → 1 check
  5. Greedy insight: Consecutive only
  6. Proof by contradiction: Why not skip elements?
  7. Complexity comparison: O(N³) → O(N log N)

POLYA'S PROBLEM-SOLVING STEPS:
  1. Understand: Need all 3 triangle conditions
  2. Plan: Try sorting to organize data
  3. Execute: Test examples, find pattern
  4. Review: Prove why sorting works mathematically
"""

def solution(A):
    """
    Triangle inequality: A[P] + A[Q] > A[R]
    After sorting, only need to check consecutive triplets.
    
    Time Complexity: O(N log N) - dominated by sorting
    Space Complexity: O(1) - in-place sorting
    """
    # Step 1: Handle edge cases - O(1)
    if len(A) < 3:
        return 0
    
    # Step 2: Sort array - O(N log N)
    A.sort()
    
    # Step 3: Check consecutive triplets - O(N)
    for i in range(len(A) - 2):
        # After sorting: A[i] <= A[i+1] <= A[i+2]
        # Only need to check: A[i] + A[i+1] > A[i+2] - O(1)
        if A[i] + A[i+1] > A[i+2]:
            return 1
    
    return 0


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        ([10, 2, 5, 1, 8, 20], 1, "Example 1: triangle exists (5+8>10)"),
        ([10, 50, 5, 1], 0, "Example 2: no triangle possible"),
        ([5, 3, 3], 1, "Minimal triangle (3+3>5)"),
        ([1, 2, 4], 0, "Not a triangle (1+2<4)"),
        ([], 0, "Empty array"),
        ([1], 0, "Single element"),
        ([1, 2], 0, "Two elements"),
        ([3, 3, 3], 1, "Equilateral triangle"),
        ([5, 4, 3], 1, "Valid triangle (3+4>5)"),
        ([1, 1, 1000000], 0, "Two small + one huge"),
        ([10, 10, 10, 10], 1, "Multiple same values"),
        ([2147483647, 2147483647, 2147483647], 1, "Max integer values (overflow safe)"),
        ([-1, -2, -3], 0, "Negative values (no triangle)"),
    ]
    
    print("=" * 80)
    print("TRIANGLE - Test Results")
    print("=" * 80)
    
    all_passed = True
    for i, (input_arr, expected, description) in enumerate(test_cases, 1):
        result = solution(input_arr.copy())  # copy to avoid modifying test data
        passed = result == expected
        status = "✓ PASS" if passed else "✗ FAIL"
        
        if not passed:
            all_passed = False
        
        print(f"{status} Test {i}: {description}")
        if len(input_arr) <= 10:
            print(f"     Input: {input_arr}")
        else:
            print(f"     Input: length={len(input_arr)}")
        print(f"     Expected: {expected}, Got: {result}")
        print()
    
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# Triangle

# Determine whether a triangle can be built from a given set of edges.
# Programming language: 
# Python
# Spoken language: 
# English
# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# Triplet (0, 2, 4) is triangular.

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

# For example, given array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# the function should return 1, as explained above. Given array A such that:

#   A[0] = 10    A[1] = 50    A[2] = 5
#   A[3] = 1
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.