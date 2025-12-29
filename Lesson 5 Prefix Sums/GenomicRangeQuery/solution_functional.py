"""
GenomicRangeQuery - Versión Funcional
Programación funcional: Pure functions, sin estado compartido.
"""

def build_nucleotide_prefix_sums(sequence, nucleotides=('A', 'C', 'G', 'T')):
    """
    Pure function: Build prefix sums. No side effects.
    
    Args:
        sequence: DNA sequence string
        nucleotides: Tuple of nucleotides to track
    
    Returns:
        Dictionary of prefix sum arrays
    """
    n = len(sequence)
    prefix = {nuc: [0] * (n + 1) for nuc in nucleotides}
    
    for i, nuc in enumerate(sequence):
        for n in nucleotides:
            prefix[n][i + 1] = prefix[n][i]
        prefix[nuc][i + 1] += 1
    
    return prefix


def find_minimal_impact(prefix_sums, start, end, nucleotides=('A', 'C', 'G', 'T'), impacts=None):
    """
    Pure function: Query minimal impact in range.
    
    Args:
        prefix_sums: Dictionary of prefix sum arrays
        start: Start position (inclusive)
        end: End position (inclusive)
        nucleotides: Tuple of nucleotides in order
        impacts: Dictionary mapping nucleotides to impact factors
    
    Returns:
        Minimal impact factor in range
    """
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
    
    COMPLEXITY: O(N + M) time, O(N) space
    """
    prefix = build_nucleotide_prefix_sums(S)
    return [find_minimal_impact(prefix, P[k], Q[k]) for k in range(len(P))]


if __name__ == "__main__":
    # Test case
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    
    print("VERSIÓN FUNCIONAL (Pure Functions)")
    print("=" * 70)
    print(f"S = '{S}'")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"Result: {solution_functional(S, P, Q)}")
    print(f"Expected: [2, 4, 1]")
    
    # Demo: Functions are composable and reusable
    print("\n" + "=" * 70)
    print("DEMO: COMPOSABILIDAD")
    print("=" * 70)
    prefix = build_nucleotide_prefix_sums("CAGCCTA")
    print("Prefix sums construidos una vez, usar múltiples veces:")
    print(f"  Query [0, 2]: {find_minimal_impact(prefix, 0, 2)}")
    print(f"  Query [1, 4]: {find_minimal_impact(prefix, 1, 4)}")
    print(f"  Query [5, 6]: {find_minimal_impact(prefix, 5, 6)}")
