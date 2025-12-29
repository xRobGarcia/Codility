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


def solution_desk_check(S, P, Q):
    """
    Versión con PRUEBA DE ESCRITORIO completa.
    """
    print(f"\n{'='*70}")
    print(f"PRUEBA DE ESCRITORIO: GenomicRangeQuery")
    print(f"{'='*70}")
    print(f"DNA Sequence: S = '{S}'")
    print(f"Queries: {len(P)} queries")
    for i in range(len(P)):
        print(f"  Query {i}: P={P[i]}, Q={Q[i]} → substring S[{P[i]}..{Q[i]}]")
    
    n = len(S)
    m = len(P)
    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Build prefix arrays
    print(f"\n--- PASO 1: Construir arrays de prefix sums ---")
    prefix = {nuc: [0] * (n + 1) for nuc in 'ACGT'}
    
    for i in range(n):
        for nucleotide in 'ACGT':
            prefix[nucleotide][i + 1] = prefix[nucleotide][i]
        prefix[S[i]][i + 1] += 1
    
    # Display prefix arrays
    print(f"\nSecuencia con índices:")
    print(f"  Index: ", end="")
    for i in range(n):
        print(f"{i:3}", end=" ")
    print()
    print(f"  DNA:   ", end="")
    for char in S:
        print(f"{char:>3}", end=" ")
    print("\n")
    
    print(f"Prefix Sum Arrays (prefix[nuc][i] = count from 0 to i-1):")
    for nuc in 'ACGT':
        print(f"  {nuc}: {prefix[nuc]}")
    
    # Answer queries
    print(f"\n--- PASO 2: Responder Queries ---")
    result = []
    
    for k in range(m):
        start, end = P[k], Q[k]
        substring = S[start:end+1]
        
        print(f"\n  Query {k}: Range [{start}..{end}]")
        print(f"    Substring: '{substring}'")
        print(f"    Checking nucleotides in order (A→C→G→T):")
        
        for nucleotide in 'ACGT':
            count = prefix[nucleotide][end + 1] - prefix[nucleotide][start]
            print(f"      {nucleotide} (impact={impact[nucleotide]}): ", end="")
            print(f"prefix[{end+1}] - prefix[{start}] = ", end="")
            print(f"{prefix[nucleotide][end+1]} - {prefix[nucleotide][start]} = {count}", end="")
            
            if count > 0:
                print(f" ✓ FOUND!")
                result.append(impact[nucleotide])
                print(f"    → Answer: {impact[nucleotide]}")
                break
            else:
                print(f" (not present)")
    
    # Verification
    print(f"\n--- VERIFICACIÓN ---")
    print(f"Resultados: {result}")
    
    # Manual check
    print(f"\nVerificación manual:")
    for k in range(m):
        start, end = P[k], Q[k]
        substring = S[start:end+1]
        min_impact = min(impact[c] for c in substring)
        match = "✓" if result[k] == min_impact else "✗"
        print(f"  Query {k}: '{substring}' → min={min_impact}, got={result[k]} {match}")
    
    print(f"{'='*70}\n")
    return result


class DNAAnalyzer:
    """
    Encapsulates DNA sequence analysis following DRY and SoC principles.
    
    SEPARATION OF CONCERNS:
    - Nucleotide data (constants) → separate attributes
    - Prefix sum construction → _build_prefix_sums()
    - Range query logic → _query_range()
    - Result processing → analyze_queries()
    
    DRY PRINCIPLES:
    - No repeated constants (NUCLEOTIDES, IMPACT_FACTORS)
    - Reusable prefix sum builder
    - Single source of truth for nucleotide ordering
    """
    
    # Constants - Single source of truth (DRY)
    NUCLEOTIDES = ('A', 'C', 'G', 'T')
    IMPACT_FACTORS = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    def __init__(self, sequence):
        """Initialize with DNA sequence and build prefix sums."""
        self.sequence = sequence
        self.n = len(sequence)
        self.prefix_sums = self._build_prefix_sums()
    
    def _build_prefix_sums(self):
        """
        Build prefix sum arrays for all nucleotides.
        
        RESPONSIBILITY: Data preprocessing
        Returns: dict of prefix sum arrays
        """
        prefix = {nuc: [0] * (self.n + 1) for nuc in self.NUCLEOTIDES}
        
        for i, nucleotide in enumerate(self.sequence):
            # Copy previous counts
            for nuc in self.NUCLEOTIDES:
                prefix[nuc][i + 1] = prefix[nuc][i]
            # Increment current nucleotide
            prefix[nucleotide][i + 1] += 1
        
        return prefix
    
    def _query_range(self, start, end):
        """
        Find minimal impact factor in range [start, end].
        
        RESPONSIBILITY: Single query logic
        Args:
            start: Starting position (inclusive)
            end: Ending position (inclusive)
        Returns:
            Minimal impact factor in range
        """
        for nucleotide in self.NUCLEOTIDES:  # Already ordered by impact
            count = self.prefix_sums[nucleotide][end + 1] - self.prefix_sums[nucleotide][start]
            if count > 0:
                return self.IMPACT_FACTORS[nucleotide]
        
        return None  # Should never happen with valid input
    
    def analyze_queries(self, P, Q):
        """
        Answer multiple range queries.
        
        RESPONSIBILITY: Batch processing
        Args:
            P: List of start positions
            Q: List of end positions
        Returns:
            List of minimal impact factors
        """
        return [self._query_range(P[k], Q[k]) for k in range(len(P))]
    
    def get_prefix_sums(self):
        """Accessor for prefix sums (encapsulation)."""
        return self.prefix_sums


def solution_dry_soc(S, P, Q):
    """
    DRY & SoC version using DNAAnalyzer class.
    
    BENEFITS:
    - Clear separation of concerns (data, preprocessing, queries)
    - No repeated code or magic numbers
    - Easy to test individual components
    - Reusable for different query sets on same sequence
    
    COMPLEXITY: O(N + M) time, O(N) space
    """
    analyzer = DNAAnalyzer(S)
    return analyzer.analyze_queries(P, Q)


# Functional approach (alternative DRY/SoC)
def build_nucleotide_prefix_sums(sequence, nucleotides=('A', 'C', 'G', 'T')):
    """Pure function: Build prefix sums. No side effects."""
    n = len(sequence)
    prefix = {nuc: [0] * (n + 1) for nuc in nucleotides}
    
    for i, nuc in enumerate(sequence):
        for n in nucleotides:
            prefix[n][i + 1] = prefix[n][i]
        prefix[nuc][i + 1] += 1
    
    return prefix


def find_minimal_impact(prefix_sums, start, end, nucleotides=('A', 'C', 'G', 'T'), impacts=None):
    """Pure function: Query minimal impact in range."""
    if impacts is None:
        impacts = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    for nuc in nucleotides:
        if prefix_sums[nuc][end + 1] - prefix_sums[nuc][start] > 0:
            return impacts[nuc]
    
    return None


def solution_functional(S, P, Q):
    """
    Functional programming approach - Pure functions, no state.
    
    DRY: Functions are reusable
    SoC: Each function has one responsibility
    """
    prefix = build_nucleotide_prefix_sums(S)
    return [find_minimal_impact(prefix, P[k], Q[k]) for k in range(len(P))]


if __name__ == "__main__":
    # Test cases
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    
    print("="*70)
    print("VERSIÓN CODILITY (Sucinta)")
    print("="*70)
    print(f"S = '{S}'")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"Result: {solution(S, P, Q)}")
    print(f"Expected: [2, 4, 1]")
    
    print("\n" + "="*70)
    print("VERSIÓN DETALLADA")
    print("="*70)
    print(f"Result: {solution_detailed(S, P, Q)}")
    
    print("\n" + "="*70)
    print("VERSIÓN DRY & SoC (Clase)")
    print("="*70)
    print(f"Result: {solution_dry_soc(S, P, Q)}")
    
    print("\n" + "="*70)
    print("VERSIÓN FUNCIONAL (Pure Functions)")
    print("="*70)
    print(f"Result: {solution_functional(S, P, Q)}")
    
    # Desk check
    solution_desk_check(S, P, Q)
    
    # Additional test
    print("\n" + "="*70)
    print("PRUEBA ADICIONAL")
    print("="*70)
    S2 = "AAAA"
    P2 = [0, 1]
    Q2 = [3, 2]
    solution_desk_check(S2, P2, Q2)
    
    # Demo: Reusability with DRY/SoC approach
    print("\n" + "="*70)
    print("DEMO: REUTILIZACIÓN (DRY/SoC)")
    print("="*70)
    analyzer = DNAAnalyzer("CAGCCTA")
    print("Crear analyzer una vez, reutilizar para múltiples queries:")
    print(f"  Query 1: {analyzer.analyze_queries([0], [2])}")
    print(f"  Query 2: {analyzer.analyze_queries([1, 3], [4, 6])}")
    print(f"  Query 3: {analyzer.analyze_queries([5], [5])}")


# GenomicRangeQuery

# Find the minimal nucleotide from a range of sequence DNA.
# Programming language: 
# Python
# A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

# For example, consider string S = CAGCCTA and arrays P, Q such that:

#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
# The answers to these M = 3 queries are as follows:

# The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
# The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
# The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
# Write a function:

# def solution(S, P, Q)

# that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

# Result array should be returned as an array of integers.

# For example, given the string S = CAGCCTA and arrays P, Q such that:

#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
# the function should return the values [2, 4, 1], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# M is an integer within the range [1..50,000];
# each element of arrays P and Q is an integer within the range [0..N - 1];
# P[K] ≤ Q[K], where 0 ≤ K < M;
# string S consists only of upper-case English letters A, C, G, T.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.