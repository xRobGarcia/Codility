def solution(N):
    """
    Binary Gap - Find longest sequence of zeros surrounded by ones.
    
    Time:  O(log N) - N has ~log₂(N) bits; bin(), strip(), split() each traverse the bit string once
    Space: O(log N) - binary string representation stores ~log₂(N) characters
    """
    return max((len(g) for g in bin(N)[2:].strip('0').split('1') if g), default=0)

if __name__ == "__main__":
    print("N=9:", solution(9))  # 2
    print("N=529:", solution(529))  # 4
    print("N=20:", solution(20))  # 1
    print("N=15:", solution(15))  # 0
    print("N=32:", solution(32))  # 0
    print("N=1041:", solution(1041))  # 5

"""

https://app.codility.com/programmers/lessons/1-iterations/binary_gap/start/

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""