# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque
import sys
import ast

def solution(A, K):
    """
    Cyclic rotation using deque.
    Time:  O(N) - deque construction O(N), rotate is O(K % N), list conversion O(N)
    Space: O(N) - deque and result list
    """
    d = deque(A)
    d.rotate(K)  # Rotates right by K positions
    return list(d)

# Alternative solution without libraries (using list slicing)
def solution_no_lib(A, K):
    """
    Cyclic rotation using list slicing.
    Time:  O(N) - slicing A[-K:] and A[:-K] each create new lists, concatenation is O(N)
    Space: O(N) - new list created by slicing and concatenation
    """
    if not A:
        return []
    
    # K %= len(A) es equivalente a: K = K % len(A)
    # El operador % (módulo) calcula el residuo de la división K / len(A)
    # Esto reduce K al rango [0, len(A)-1]
    # 
    # Ejemplos:
    # - Si K=20 y len(A)=5: K = 20 % 5 = 0 (20 dividido entre 5 = 4 con residuo 0)
    # - Si K=23 y len(A)=5: K = 23 % 5 = 3 (23 dividido entre 5 = 4 con residuo 3)
    # - Si K=3 y len(A)=5:  K = 3 % 5 = 3  (3 dividido entre 5 = 0 con residuo 3)
    # - Si K=7 y len(A)=5:  K = 7 % 5 = 2  (7 dividido entre 5 = 1 con residuo 2)
    #
    # Por qué funciona: Rotar len(A) veces regresa al estado original,
    # entonces solo importan las rotaciones "sobrantes" después de ciclos completos.
    K %= len(A)
    
    if K == 0:
        return A
    return A[-K:] + A[:-K]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python arrays.py <array> <K>")
        print("Example: python arrays.py \"[3,8,9,7,6]\" 3")
        sys.exit(1)
    
    try:
        A = ast.literal_eval(sys.argv[1])  # Safely parse the list
        K = int(sys.argv[2])
        result = solution(A, K)
        result_no_lib = solution_no_lib(A, K)
        print("Deque result:", result)
        print("No-lib result:", result_no_lib)
    except (ValueError, SyntaxError) as e:
        print("Error parsing arguments:", e)
        sys.exit(1)


#[0..n]

#rotation
#K times


# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# class Solution { public int[] solution(int[] A, int K); }
# content_copy

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3

# content_copy
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

# content_copy
# For another example, given

#     A = [0, 0, 0]
#     K = 1

# content_copy
# the function should return [0, 0, 0]

# Given

#     A = [1, 2, 3, 4]
#     K = 4

# content_copy
# the function should return [1, 2, 3, 4]

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
