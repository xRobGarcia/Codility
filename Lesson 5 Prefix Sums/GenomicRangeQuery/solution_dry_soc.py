"""
GenomicRangeQuery - Versión DRY & SoC
Aplicando principios de diseño: Don't Repeat Yourself y Separation of Concerns.
"""

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


if __name__ == "__main__":
    # Test case
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    
    print("VERSIÓN DRY & SoC (Clase)")
    print("=" * 70)
    print(f"S = '{S}'")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"Result: {solution_dry_soc(S, P, Q)}")
    print(f"Expected: [2, 4, 1]")
    
    # Demo: Reusability
    print("\n" + "=" * 70)
    print("DEMO: REUTILIZACIÓN (DRY/SoC)")
    print("=" * 70)
    analyzer = DNAAnalyzer("CAGCCTA")
    print("Crear analyzer una vez, reutilizar para múltiples queries:")
    print(f"  Query 1: {analyzer.analyze_queries([0], [2])}")
    print(f"  Query 2: {analyzer.analyze_queries([1, 3], [4, 6])}")
    print(f"  Query 3: {analyzer.analyze_queries([5], [5])}")
