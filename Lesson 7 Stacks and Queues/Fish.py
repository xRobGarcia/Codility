# Fish - Codility Solution
# Time:  O(N) - single pass, each fish pushed/popped at most once
# Space: O(N) - stack stores downstream fish

def solution(A, B) -> int:
    UPSTREAM = 0
    DOWNSTREAM = 1
    
    downstream = []
    alive = 0

    for size, direction in zip(A, B):
        if direction == DOWNSTREAM:
            downstream.append(size)
        else:  # UPSTREAM
            # Current upstream fish fights all smaller downstream fish
            while downstream:
                downstream_fish = downstream[-1]
                upstream_wins = size > downstream_fish
                
                if upstream_wins:
                    downstream.pop()  # Upstream fish eats downstream fish
                else:
                    break  # Downstream fish eats upstream fish
            
            # If no downstream fish left, upstream fish survives
            if not downstream:
                alive += 1

    return alive + len(downstream)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]), 2),  # Example from problem
        (([4, 3, 2, 1], [0, 0, 0, 0]), 4),         # All upstream, no fights
        (([1, 2, 3, 4], [1, 1, 1, 1]), 4),         # All downstream, no fights
        (([5], [0]), 1),                            # Single fish
        (([3, 5], [1, 0]), 1),                      # 5 eats 3
        (([5, 3], [1, 0]), 1),                      # 5 survives
        (([1, 2], [1, 1]), 2),                      # Same direction
        (([2, 1], [0, 0]), 2),                      # Both upstream
    ]
    
    print("Testing Fish solution:\n")
    all_passed = True
    
    for (A, B), expected in test_cases:
        result = solution(A, B)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status} A={A}, B={B} → {result} (expected {expected})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# Fish

# N voracious fish are moving along a river. Calculate how many fish are alive.
# Programming language: 
# Python
# You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

# The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

# Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

# 0 represents a fish flowing upstream,
# 1 represents a fish flowing downstream.
# If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

# If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
# If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
# We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

# For example, consider arrays A and B such that:

#   A[0] = 4    B[0] = 0
#   A[1] = 3    B[1] = 1
#   A[2] = 2    B[2] = 0
#   A[3] = 1    B[3] = 0
#   A[4] = 5    B[4] = 0
# Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

# Write a function:

# def solution(A, B)

# that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

# For example, given the arrays shown above, the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000];
# each element of array B is an integer that can have one of the following values: 0, 1;
# the elements of A are all distinct.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.