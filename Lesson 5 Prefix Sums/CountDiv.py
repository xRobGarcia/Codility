def solution(A, B, K):
    """Count integers divisible by K in range [A..B].
    
    KEY INSIGHT:
    Instead of iterating through all numbers from A to B (too slow),
    use mathematical formula:
    - Count of multiples of K from 0 to B: B // K
    - Count of multiples of K from 0 to A-1: (A-1) // K
    - Difference gives multiples in range [A..B]
    
    Special case: If A is divisible by K, we need to include it,
    so we use (A-1) // K to count multiples before A.
    
    COMPLEXITY:
    - Time: O(1) - only arithmetic operations
    - Space: O(1) - no extra memory
    
    Examples:
    - A=6, B=11, K=2: divisible numbers are [6, 8, 10] → 3
    - A=11, B=345, K=17: (345//17) - (10//17) = 20 - 0 = 20
    """
    # Count multiples of K from 0 to B
    count_up_to_B = B // K
    
    # Count multiples of K from 0 to A-1 (before A)
    count_before_A = (A - 1) // K
    
    # Difference gives count in range [A, B]
    return count_up_to_B - count_before_A


def solution_codility(A, B, K):
    """Count integers divisible by K in range [A..B]. O(1) time, O(1) space."""
    return B // K - (A - 1) // K


def solution_desk_check(A, B, K):
    """
    Versión con PRUEBA DE ESCRITORIO (Desk Check)
    Muestra paso a paso cómo funciona el algoritmo.
    """
    print(f"\n{'='*60}")
    print(f"PRUEBA DE ESCRITORIO: CountDiv(A={A}, B={B}, K={K})")
    print(f"{'='*60}")
    print(f"Objetivo: Contar números divisibles por {K} en rango [{A}..{B}]")
    
    # Paso 1: Calcular múltiplos de K desde 0 hasta B
    print(f"\n--- PASO 1: Contar múltiplos desde 0 hasta {B} ---")
    count_up_to_B = B // K
    print(f"  B // K = {B} // {K} = {count_up_to_B}")
    
    # Mostrar los múltiplos
    multiples_B = [i * K for i in range(count_up_to_B + 1)]
    print(f"  Múltiplos de {K} desde 0 hasta {B}: {multiples_B}")
    print(f"  Total de múltiplos: {count_up_to_B + 1} (incluyendo 0)")
    
    # Paso 2: Calcular múltiplos de K desde 0 hasta A-1
    print(f"\n--- PASO 2: Contar múltiplos desde 0 hasta {A-1} ---")
    count_before_A = (A - 1) // K
    print(f"  (A-1) // K = ({A}-1) // {K} = {A-1} // {K} = {count_before_A}")
    
    # Mostrar los múltiplos antes de A
    multiples_before = [i * K for i in range(count_before_A + 1)]
    print(f"  Múltiplos de {K} antes de {A}: {multiples_before}")
    print(f"  Total de múltiplos: {count_before_A + 1}")
    
    # Paso 3: Restar para obtener múltiplos en el rango [A, B]
    print(f"\n--- PASO 3: Calcular diferencia ---")
    result = count_up_to_B - count_before_A
    print(f"  Resultado = count_up_to_B - count_before_A")
    print(f"  Resultado = {count_up_to_B} - {count_before_A} = {result}")
    
    # Verificación: mostrar los múltiplos reales en el rango
    print(f"\n--- VERIFICACIÓN ---")
    actual_multiples = [i for i in range(A, B + 1) if i % K == 0]
    print(f"  Múltiplos de {K} en rango [{A}..{B}]: {actual_multiples}")
    print(f"  Cantidad: {len(actual_multiples)}")
    
    # Validar resultado
    if result == len(actual_multiples):
        print(f"  ✓ CORRECTO: {result} == {len(actual_multiples)}")
    else:
        print(f"  ✗ ERROR: {result} != {len(actual_multiples)}")
    
    print(f"{'='*60}\n")
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("EJECUCIONES RÁPIDAS")
    print("=" * 60)
    
    print("\nVerbose version:")
    print(solution(6, 11, 2))    # 3: [6, 8, 10]
    print(solution(11, 345, 17)) # 20
    print(solution(0, 0, 1))     # 1: [0]
    print(solution(1, 1, 1))     # 1: [1]
    print(solution(10, 10, 5))   # 1: [10]
    print(solution(10, 10, 7))   # 0: no multiples
    print(solution(0, 10, 3))    # 4: [0, 3, 6, 9]
    
    print("\nCodility version:")
    print(solution_codility(6, 11, 2))    # 3
    print(solution_codility(11, 345, 17)) # 20
    print(solution_codility(0, 0, 1))     # 1
    
    print("\n" + "=" * 60)
    print("PRUEBAS DE ESCRITORIO (DESK CHECK)")
    print("=" * 60)
    
    # Ejemplo 1: Caso del problema
    solution_desk_check(6, 11, 2)
    
    # Ejemplo 2: Caso con rango más pequeño
    solution_desk_check(0, 10, 3)
    
    # Ejemplo 3: Caso con un solo número
    solution_desk_check(10, 10, 5)


# CountDiv

# Compute number of integers divisible by k in range [a..b].
# Programming language: 
# Python
# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.