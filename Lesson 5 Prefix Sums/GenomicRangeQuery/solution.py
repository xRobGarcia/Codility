"""
GenomicRangeQuery - Versión Codility (Sucinta)
Para copiar directamente a Codility.
"""

def solution(S, P, Q):
    """Find minimal impact factor in DNA ranges. O(N+M) time, O(N) space."""
    n = len(S)
    m = len(P)
    
    # Map nucleotides to impact factors
    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Build prefix sum arrays for each nucleotide
    # prefix[i][j] = count of nucleotide i from position 0 to j
    prefix = {
        'A': [0] * (n + 1),
        'C': [0] * (n + 1),
        'G': [0] * (n + 1),
        'T': [0] * (n + 1)
    }
    
    for i in range(n):
        for nucleotide in 'ACGT':
            prefix[nucleotide][i + 1] = prefix[nucleotide][i]
        prefix[S[i]][i + 1] += 1
    
    # Answer queries
    result = []
    for k in range(m):
        start, end = P[k], Q[k]
        
        # Check each nucleotide in order of impact factor (A, C, G, T)
        for nucleotide in 'ACGT':
            count = prefix[nucleotide][end + 1] - prefix[nucleotide][start]
            if count > 0:
                result.append(impact[nucleotide])
                break
    
    return result


if __name__ == "__main__":
    # Test case
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    
    print(f"S = '{S}'")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"Result: {solution(S, P, Q)}")
    print(f"Expected: [2, 4, 1]")
