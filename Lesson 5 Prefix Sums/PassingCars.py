def solution(A):
    """Count passing car pairs.
    
    COMPLEXITY ANALYSIS:
    - Time: O(N) where N = len(A)
      * Single pass through array: N iterations
      * Each iteration: O(1) operations (increment, add, compare)
      * Total: O(N)
    
    - Space: O(1)
      * Only 2 integer variables used (east_count, passing_pairs)
      * No additional data structures created
      * Memory usage independent of input size
    """
    east_count = 0
    passing_pairs = 0
    
    for car in A:  # O(N) - iterate through all elements
        if car == 0:
            east_count += 1  # O(1)
        else:
            passing_pairs += east_count  # O(1)
            if passing_pairs > 1_000_000_000:  # O(1)
                return -1
    
    return passing_pairs

def solution_with_comments(A):
	"""Count the number of passing cars on the road.
	
	IMPORTANT CONCEPT:
	- Cars going EAST (0) travel right →
	- Cars going WEST (1) travel left ←
	- They "pass" when they CROSS PATHS (opposite directions)
	
	RULE: A pair (P, Q) passes when:
	  1. P < Q (P comes before Q in the array)
	  2. A[P] = 0 (P travels east →)
	  3. A[Q] = 1 (Q travels west ←)
	  → They will meet and pass each other!
	
	Example: [0, 1, 0, 1, 1]
	         [→, ←, →, ←, ←]
	  - Position 0 (→) will cross positions 1, 3, 4 (←) = 3 pairs
	  - Position 2 (→) will cross positions 3, 4 (←) = 2 pairs
	  - Total = 5 pairs
	
	ALGORITHM:
	- Track count of east-bound cars seen so far
	- Each west-bound car crosses ALL previous east-bound cars
	- Add east_count to total for each west-bound car
	
	Time: O(N) - single pass
	Space: O(1) - only counters
	"""
	east_count = 0  # How many cars traveling east (→) we've seen
	passing_pairs = 0
	
	for car in A:
		if car == 0:
			# Found a car going east (→)
			# It will eventually pass all future west-bound cars
			east_count += 1
		else:
			# Found a car going west (←)
			# It crosses ALL east-bound cars we've seen so far
			passing_pairs += east_count
			
			# Check limit: return -1 if exceeded 1 billion
			if passing_pairs > 1_000_000_000:
				return -1
	
	return passing_pairs

def solution_readable(A):
	"""Alternative solution - more explicit and easier to read.
	
	Same algorithm but with clearer variable names and explicit checks.
	
	COMPLEXITY:
	- Time: O(N) - single loop through N elements
	- Space: O(1) - constant number of variables
	"""
	EAST = 0
	WEST = 1
	MAX_PAIRS = 1_000_000_000
	
	cars_going_east = 0
	total_passing_pairs = 0
	
	for position in range(len(A)):
		current_car = A[position]
		
		if current_car == EAST:
			# This car goes east, will pass future west-bound cars
			cars_going_east += 1
		
		elif current_car == WEST:
			# This car goes west, passes all previous east-bound cars
			total_passing_pairs += cars_going_east
			
			# Check if we exceeded the limit
			if total_passing_pairs > MAX_PAIRS:
				return -1
	
	return total_passing_pairs




if __name__ == "__main__":
	print(solution([0, 1, 0, 1, 1]))  # 5
	print(solution([0]))  # 0
	print(solution([1]))  # 0
	print(solution([1, 0]))  # 0
	print(solution([0, 1]))  # 1
	print(solution([0, 0, 0, 1, 1, 1]))  # 9 (3 east * 3 west)
	
	print("\nAlternative (more readable):")
	print(solution_readable([0, 1, 0, 1, 1]))  # 5
	print(solution_readable([0]))  # 0
	print(solution_readable([1]))  # 0
	print(solution_readable([1, 0]))  # 0
	print(solution_readable([0, 1]))  # 1
	print(solution_readable([0, 0, 0, 1, 1, 1]))  # 9



# PassingCars

# Count the number of passing cars on the road.
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

# Array A contains only 0s and/or 1s:

# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

# For example, consider array A such that:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

# The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

# For example, given:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.