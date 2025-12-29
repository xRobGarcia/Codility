"""
GenomicRangeQuery - Ejecutar todas las versiones
Importa y ejecuta todas las soluciones para comparar.
"""

from solution import solution
from solution_detailed import solution_detailed
from solution_desk_check import solution_desk_check
from solution_dry_soc import solution_dry_soc, DNAAnalyzer
from solution_functional import solution_functional


def main():
    """Ejecutar todas las versiones."""
    # Test data
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    expected = [2, 4, 1]
    
    print("=" * 80)
    print("GENOMIC RANGE QUERY - TODAS LAS VERSIONES")
    print("=" * 80)
    print(f"Input: S = '{S}', P = {P}, Q = {Q}")
    print(f"Expected: {expected}\n")
    
    # Version 1: Codility
    print("1. VERSIÓN CODILITY (Sucinta)")
    print("-" * 80)
    result1 = solution(S, P, Q)
    print(f"Result: {result1}")
    print(f"Status: {'✓ PASS' if result1 == expected else '✗ FAIL'}\n")
    
    # Version 2: Detailed
    print("2. VERSIÓN DETALLADA (Con comentarios)")
    print("-" * 80)
    result2 = solution_detailed(S, P, Q)
    print(f"Result: {result2}")
    print(f"Status: {'✓ PASS' if result2 == expected else '✗ FAIL'}\n")
    
    # Version 3: DRY & SoC
    print("3. VERSIÓN DRY & SoC (Clase)")
    print("-" * 80)
    result3 = solution_dry_soc(S, P, Q)
    print(f"Result: {result3}")
    print(f"Status: {'✓ PASS' if result3 == expected else '✗ FAIL'}\n")
    
    # Version 4: Functional
    print("4. VERSIÓN FUNCIONAL (Pure Functions)")
    print("-" * 80)
    result4 = solution_functional(S, P, Q)
    print(f"Result: {result4}")
    print(f"Status: {'✓ PASS' if result4 == expected else '✗ FAIL'}\n")
    
    # Version 5: Desk Check (verbose)
    print("5. PRUEBA DE ESCRITORIO (Visualización)")
    print("-" * 80)
    result5 = solution_desk_check(S, P, Q)
    
    # Summary
    print("\n" + "=" * 80)
    print("RESUMEN")
    print("=" * 80)
    all_pass = all([
        result1 == expected,
        result2 == expected,
        result3 == expected,
        result4 == expected,
        result5 == expected
    ])
    
    if all_pass:
        print("✓ TODAS LAS VERSIONES PASARON LOS TESTS")
    else:
        print("✗ ALGUNAS VERSIONES FALLARON")
    
    print("\nArchivos creados:")
    print("  - solution.py              (Para Codility)")
    print("  - solution_detailed.py     (Con análisis completo)")
    print("  - solution_desk_check.py   (Prueba de escritorio)")
    print("  - solution_dry_soc.py      (DRY & SoC - Clase)")
    print("  - solution_functional.py   (Programación funcional)")
    print("  - run_all.py               (Este archivo)")


if __name__ == "__main__":
    main()
