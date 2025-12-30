# StoneWall - Codility Solution
# Time:  O(N) - single pass, each height pushed/popped at most once
# Space: O(N) - stack stores active heights

def solution(H):
    stack = []
    blocks = 0
    
    for height in H:
        # Remove blocks taller than current height
        while stack and stack[-1] > height:
            stack.pop()
        
        # If stack empty or current height not in stack, need new block
        if not stack or stack[-1] < height:
            stack.append(height)
            blocks += 1
        # If stack[-1] == height, reuse existing block (do nothing)
    
    return blocks


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([8, 8, 5, 7, 9, 8, 7, 4, 8], 7),  # Example from problem
        ([1], 1),                            # Single block
        ([1, 1, 1], 1),                      # Same height
        ([1, 2, 3], 3),                      # Increasing
        ([3, 2, 1], 3),                      # Decreasing
        ([1, 2, 1], 2),                      # Up and down
        ([5, 5, 5, 5], 1),                   # Flat
        ([1, 3, 2, 1], 2),                   # Peak
        ([2, 5, 1, 4, 6, 7, 9, 10, 1], 6),   # Complex
    ]
    
    print("Testing StoneWall solution:\n")
    all_passed = True
    
    for H, expected in test_cases:
        result = solution(H)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status} H={H} → {result} (expected {expected})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")


# ============================================================================
# ORIGINAL PROBLEM STATEMENT
# ============================================================================


# StoneWall

# Cover "Manhattan skyline" using the minimum number of rectangles.
# Programming language: 
# Python
# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

# Write a function:

# def solution(H)

# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

# For example, given array H containing N = 9 integers:

#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.



# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..1,000,000,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.