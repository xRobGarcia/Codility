"""
GenomicRangeQuery - Prueba de Escritorio
Visualización paso a paso del algoritmo.
"""

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


if __name__ == "__main__":
    # Test case 1
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    solution_desk_check(S, P, Q)
    
    # Test case 2
    print("\nPRUEBA ADICIONAL:")
    S2 = "AAAA"
    P2 = [0, 1]
    Q2 = [3, 2]
    solution_desk_check(S2, P2, Q2)
