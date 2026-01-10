def solution(X, Y, D):
    """
    Calculate minimum jumps from X to reach Y with jump size D.
    Time: O(1), Space: O(1)
    
    Why ceil() instead of floor():
    - Distance to cover: Y - X
    - Each jump covers D units
    - If (Y-X) is divisible by D: exactly (Y-X)//D jumps needed
    - If NOT divisible: need ONE MORE jump to cover the remainder
    
    Example: X=10, Y=85, D=30
    - Distance = 75
    - 75 / 30 = 2.5
    - With 2 jumps: 10 + 60 = 70 (doesn't reach 85)
    - With 3 jumps: 10 + 90 = 100 (reaches 85 ✓)
    - ceil(2.5) = 3 jumps
    
    Implementation: ((Y - X) + D - 1) // D
    
    Why the "- 1"?
    - Formula: ceil(a/b) = (a + b - 1) // b
    - Without -1: (a + b) // b would give WRONG result when a is divisible by b
    
    Case 1: NOT divisible (has remainder)
      a=75, b=30 → 75/30 = 2.5 → need ceil = 3
      (75 + 30 - 1) // 30 = 104 // 30 = 3 ✓
    
    Case 2: Divisible exactly (no remainder)
      a=60, b=30 → 60/30 = 2 → need ceil = 2
      (60 + 30 - 1) // 30 = 89 // 30 = 2 ✓
      WITHOUT -1: (60 + 30) // 30 = 90 // 30 = 3 ✗ (1 extra jump!)
    
    The "-1" prevents adding an extra jump when division is exact.
    """
    return ((Y - X) + D - 1) // D

# Test
if __name__ == "__main__":
    print(solution(10, 85, 30))  # 3
    print(solution(10, 10, 30))  # 0
    print(solution(1, 1000000000, 1))  # 999999999

# FrogJmp
# START
# Count minimal number of jumps from position X to Y.

# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

# Write a function:

# def solution(X, Y, D)

# that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
# Write an efficient algorithm for the following assumptions:

# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.