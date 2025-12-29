"""
GenomicRangeQuery - Versión Detallada
Con comentarios completos, análisis de complejidad y ejemplos.
"""

def solution_detailed(S, P, Q):
    """
    Find minimal impact factor of nucleotides in DNA sequence ranges.
    
    PROBLEM:
    - DNA sequence S with N nucleotides (A, C, G, T)
    - Impact factors: A=1, C=2, G=3, T=4
    - M queries: for each query (P[k], Q[k]), find minimal impact in range [P[k]..Q[k]]
    
    NAIVE APPROACH (TOO SLOW):
    For each query, iterate through substring S[P[k]..Q[k]] and find minimum
    Time: O(N * M) - up to 100,000 * 50,000 = 5 billion operations
    
    OPTIMAL APPROACH - PREFIX SUMS:
    Build prefix sum arrays for each nucleotide type to answer queries in O(1)
    
    ALGORITHM:
    1. Create 4 prefix sum arrays (one per nucleotide: A, C, G, T)
    2. prefix[nuc][i] = count of nucleotide 'nuc' from position 0 to i-1
    3. For query [P, Q]: count = prefix[nuc][Q+1] - prefix[nuc][P]
    4. Check nucleotides in order A→C→G→T (smallest to largest impact)
    5. Return impact factor of first nucleotide found in range
    
    COMPLEXITY ANALYSIS:
    - Time: O(N + M)
      * Build prefix arrays: O(4*N) = O(N)
      * Answer M queries: O(4*M) = O(M)
      * Total: O(N + M)
    
    - Space: O(N)
      * 4 prefix arrays of size N+1: O(4*N) = O(N)
      * Result array: O(M)
      * Total: O(N + M), dominated by N if N > M
    
    EXAMPLE:
    S = "CAGCCTA"
    Query: P=2, Q=4 (substring "GCC")
    
    Prefix sums at positions:
              0  1  2  3  4  5  6  7
    prefix_A [0, 0, 1, 1, 1, 1, 1, 1]
    prefix_C [0, 1, 1, 1, 2, 3, 3, 3]
    prefix_G [0, 0, 0, 1, 1, 1, 1, 1]
    prefix_T [0, 0, 0, 0, 0, 0, 1, 2]
    
    For range [2, 4]:
    - Count A: prefix_A[5] - prefix_A[2] = 1 - 1 = 0 (no A)
    - Count C: prefix_C[5] - prefix_C[2] = 3 - 1 = 2 (has C!)
    - Return 2 (impact of C)
    """
    n = len(S)
    m = len(P)
    
    # Map nucleotides to impact factors
    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Build prefix sum arrays for each nucleotide type
    # prefix[nucleotide][i] = count of that nucleotide from index 0 to i-1
    prefix = {
        'A': [0] * (n + 1),  # +1 for easier range queries
        'C': [0] * (n + 1),
        'G': [0] * (n + 1),
        'T': [0] * (n + 1)
    }
    
    # Fill prefix sum arrays - O(N)
    for i in range(n):
        # Copy previous counts
        for nucleotide in 'ACGT':
            prefix[nucleotide][i + 1] = prefix[nucleotide][i]
        
        # Increment count for current nucleotide
        prefix[S[i]][i + 1] += 1
    
    # Answer all queries - O(M)
    result = []
    for k in range(m):
        start, end = P[k], Q[k]
        
        # Check nucleotides in order of impact factor (A=1, C=2, G=3, T=4)
        # Return as soon as we find one present in the range
        for nucleotide in 'ACGT':
            # Count occurrences in range [start, end]
            count = prefix[nucleotide][end + 1] - prefix[nucleotide][start]
            
            if count > 0:
                # Found this nucleotide in range, return its impact
                result.append(impact[nucleotide])
                break
    
    return result


if __name__ == "__main__":
    # Test case
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    
    print("VERSIÓN DETALLADA CON COMENTARIOS")
    print("=" * 70)
    print(f"S = '{S}'")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"Result: {solution_detailed(S, P, Q)}")
    print(f"Expected: [2, 4, 1]")
