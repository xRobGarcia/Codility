


# NumberOfDiscIntersections - Codility
# Time:  O(N log N)
# Space: O(N)

def solution(A):
    LIMIT = 10_000_000
    n = len(A)
    if n < 2:
        return 0

    # Event encoding:
    # (position, kind) where kind is 0 for START and 1 for END.
    # Sorting puts START before END at the same position (0 < 1),
    # which is required so "touching" discs count as intersections.
    START, END = 0, 1

    events = []
    for center, r in enumerate(A):
        events.append((center - r, START))
        events.append((center + r, END))

    events.sort()

    active = 0
    intersections = 0

    for _, kind in events:
        if kind == START:
            # This disc intersects with all currently active discs.
            intersections += active
            if intersections > LIMIT:
                return -1
            active += 1
        else:
            active -= 1

    return intersections


if __name__ == "__main__":
    print("=" * 80)
    print("NUMBER OF DISC INTERSECTIONS - Test Cases")
    print("=" * 80)
    
    # Test 1: Example from problem
    print("\n✓ Test 1: Example from problem")
    A1 = [1, 5, 2, 1, 4, 0]
    result1 = solution(A1)
    print(f"  Input: {A1}")
    print(f"  Expected: 11")
    print(f"  Result: {result1}")
    print(f"  Status: {'PASS ✓' if result1 == 11 else 'FAIL ✗'}")
    
    # Test 2: No intersections
    print("\n✓ Test 2: No intersections")
    A2 = [0, 0, 0]
    result2 = solution(A2)
    print(f"  Input: {A2}")
    print(f"  Expected: 0 (point discs at different positions)")
    print(f"  Result: {result2}")
    print(f"  Status: {'PASS ✓' if result2 == 0 else 'FAIL ✗'}")
    
    # Test 3: All discs intersect
    print("\n✓ Test 3: All discs intersect")
    A3 = [1, 1, 1]
    result3 = solution(A3)
    print(f"  Input: {A3}")
    print(f"  Expected: 3 (all pairs intersect: (0,1), (0,2), (1,2))")
    print(f"  Result: {result3}")
    print(f"  Status: {'PASS ✓' if result3 == 3 else 'FAIL ✗'}")
    
    # Test 4: Large disc covering all
    print("\n✓ Test 4: Large disc covering all others")
    A4 = [10, 0, 0, 0, 0]
    result4 = solution(A4)
    print(f"  Input: {A4}")
    print(f"  Expected: 4 (disc 0 intersects all others)")
    print(f"  Result: {result4}")
    print(f"  Status: {'PASS ✓' if result4 == 4 else 'FAIL ✗'}")
    
    # Test 5: Empty and edge cases
    print("\n✓ Test 5: Edge cases")
    A5_empty = []
    A5_single = [5]
    result5_empty = solution(A5_empty)
    result5_single = solution(A5_single)
    print(f"  Input: {A5_empty}")
    print(f"  Result: {result5_empty} (Expected: 0)")
    print(f"  Status: {'PASS ✓' if result5_empty == 0 else 'FAIL ✗'}")
    print(f"  Input: {A5_single}")
    print(f"  Result: {result5_single} (Expected: 0)")
    print(f"  Status: {'PASS ✓' if result5_single == 0 else 'FAIL ✗'}")
    
    # Test 6: Touching discs (boundary case)
    print("\n✓ Test 6: Touching discs")
    A6 = [1, 0, 1]  # Disc 0: [-1,1], Disc 1: [1,1], Disc 2: [1,3]
    result6 = solution(A6)
    print(f"  Input: {A6}")
    print(f"  Intervals: [-1,1], [1,1], [1,3]")
    print(f"  Expected: 3 (all touch/overlap at point 1)")
    print(f"  Result: {result6}")
    print(f"  Status: {'PASS ✓' if result6 == 3 else 'FAIL ✗'}")
    
    print("\n" + "=" * 80)


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================
# NumberOfDiscIntersections

# Compute the number of intersections in a sequence of discs.
# Programming language: 
# Python
# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


# ============================================================================
# TESTING
# ============================================================================

