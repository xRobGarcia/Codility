# Dominator - Codility Solution (VERSIÓN DETALLADA CON EXPLICACIÓN)
# Time:  O(N)  (Boyer–Moore + one verification pass)
# Space: O(1)

"""
================================================================================
EXPLICACIÓN DEL ALGORITMO BOYER-MOORE PARA ENCONTRAR EL ELEMENTO MAYORITARIO
================================================================================

El algoritmo Boyer-Moore (también conocido como Boyer-Moore Majority Vote Algorithm)
es un algoritmo elegante y eficiente para encontrar el elemento mayoritario en un
array, es decir, el elemento que aparece más de N/2 veces.

CONCEPTOS CLAVE:
----------------
1. **Elemento Mayoritario (Dominator)**: Un valor que aparece en más de la mitad
   de las posiciones del array. Por ejemplo, en [3,3,4,3,3], el 3 aparece 4 veces
   de 5 elementos (4 > 5/2), por lo tanto 3 es el dominator.

2. **Propiedad fundamental**: Si un elemento es mayoritario, entonces después de
   cancelar pares de elementos diferentes, el elemento mayoritario sobrevivirá.

CÓMO FUNCIONA EL ALGORITMO:
---------------------------

FASE 1: ENCONTRAR UN CANDIDATO (Boyer-Moore)
--------------------------------------------
El algoritmo mantiene dos variables:
- `candidate_index`: índice del candidato actual
- `vote_count`: contador de "votos" (balance)

Reglas:
1. Si vote_count == 0: Selecciona el elemento actual como nuevo candidato
2. Si el elemento actual == candidato: Incrementa vote_count (voto a favor)
3. Si el elemento actual != candidato: Decrementa vote_count (voto en contra)

Ejemplo paso a paso con A = [3, 4, 3, 2, 3, -1, 3, 3, 5, 5]:
-------------------------------------------------------
i=0, val=3:  vote_count=0 → Nuevo candidato=3, vote_count=1
i=1, val=4:  val≠3 → vote_count=0 (cancelación)
i=2, val=3:  vote_count=0 → Nuevo candidato=3, vote_count=1
i=3, val=2:  val≠3 → vote_count=0 (cancelación)
i=4, val=3:  vote_count=0 → Nuevo candidato=3, vote_count=1
i=5, val=-1: val≠3 → vote_count=0 (cancelación)
i=6, val=3:  vote_count=0 → Nuevo candidato=3, vote_count=1
i=7, val=3:  val=3 → vote_count=2
i=8, val=5:  val≠3 → vote_count=1 (cancelación)
i=9, val=5:  val≠3 → vote_count=0 (cancelación)

Resultado: vote_count=0 → NO hay candidato, no existe dominator
El 3 aparece 5 veces, pero necesita > 10/2 (es decir, ≥6 veces)

FASE 2: VERIFICAR EL CANDIDATO
-------------------------------
¿Por qué necesitamos verificar?
El algoritmo garantiza encontrar el elemento mayoritario SI EXISTE, pero si no
existe ningún elemento mayoritario, puede devolver un candidato falso.

Ejemplo sin dominator: [1, 2, 3]
- Después de Fase 1: candidato podría ser 3 (último elemento)
- Verificación: 3 aparece solo 1 vez, y 1 ≤ 3/2, entonces NO es dominator

Por eso contamos cuántas veces aparece el candidato y verificamos que sea > N/2.

COMPLEJIDAD:
------------
- Tiempo: O(N) - dos pasadas por el array
- Espacio: O(1) - solo usamos variables escalares

VENTAJAS SOBRE OTRAS SOLUCIONES:
---------------------------------
- Counter/HashMap: O(N) tiempo pero O(N) espacio
- Ordenar: O(N log N) tiempo
- Boyer-Moore: O(N) tiempo y O(1) espacio ← ÓPTIMO
================================================================================
"""

def solution(A):
    """
    Returns an index of the dominator (value occurring in > N/2 positions),
    or -1 if no dominator exists.
    
    Args:
        A: Array de enteros
        
    Returns:
        int: Índice de cualquier ocurrencia del dominator, o -1 si no existe
    """
    array_length = len(A)
    
    # Caso base: array vacío no tiene dominator
    if array_length == 0:
        return -1

    # ========================================================================
    # FASE 1: ALGORITMO BOYER-MOORE - ENCONTRAR CANDIDATO
    # ========================================================================
    # La idea es "votar" por elementos. Cuando vemos el candidato actual,
    # incrementamos su voto. Cuando vemos un elemento diferente, decrementamos.
    # Si el voto llega a 0, significa que hemos cancelado todos los elementos
    # hasta ahora, y elegimos un nuevo candidato.
    
    candidate_index = 0  # Índice del candidato actual
    vote_count = 0       # Contador de votos (balance)

    print(f"\n=== FASE 1: Búsqueda de candidato ===")
    print(f"Array: {A}\n")
    
    for index, value in enumerate(A):
        if vote_count == 0:
            # No hay candidato activo, seleccionar este elemento como candidato
            candidate_index = index
            vote_count = 1
            print(f"i={index}, val={value}: vote_count=0 → Nuevo candidato={value} (idx={index}), vote_count=1")
        elif value == A[candidate_index]:
            # El elemento actual coincide con el candidato, incrementar votos
            vote_count += 1
            print(f"i={index}, val={value}: Coincide con candidato {A[candidate_index]} → vote_count={vote_count}")
        else:
            # Elemento diferente, decrementar votos (cancelación)
            vote_count -= 1
            print(f"i={index}, val={value}: Diferente de candidato {A[candidate_index]} → vote_count={vote_count}")

    # Si vote_count == 0, todos los elementos se cancelaron entre sí
    # Esto significa que ningún elemento puede ser mayoritario
    if vote_count == 0:
        print(f"\n⚠️  vote_count=0 → No hay candidato, no existe dominator")
        return -1

    print(f"\n✓ Candidato encontrado: {A[candidate_index]} (índice {candidate_index})")
    print(f"  vote_count final: {vote_count}")

    # ========================================================================
    # FASE 2: VERIFICACIÓN - CONFIRMAR QUE EL CANDIDATO ES REALMENTE DOMINATOR
    # ========================================================================
    # El algoritmo Boyer-Moore garantiza que si existe un elemento mayoritario,
    # será el candidato. Pero si NO existe, puede haber un candidato falso.
    # Por eso debemos verificar contando sus ocurrencias.
    
    candidate_value = A[candidate_index]
    required_count = array_length // 2 + 1  # Debe aparecer > N/2 veces
    occurrences = 0

    print(f"\n=== FASE 2: Verificación ===")
    print(f"Candidato: {candidate_value}")
    print(f"Ocurrencias necesarias: > {array_length // 2} (es decir, ≥ {required_count})")
    print(f"\nContando ocurrencias...")
    
    for value in A:
        if value == candidate_value:
            occurrences += 1
            print(f"  Encontrado en posición → occurrences={occurrences}", end="")
            
            # Optimización: salida temprana cuando alcanzamos el umbral
            if occurrences == required_count:
                print(f" ✓ ¡Umbral alcanzado!")
                print(f"\n✅ DOMINATOR CONFIRMADO: {candidate_value} aparece {occurrences} veces")
                print(f"   Retornando índice: {candidate_index}")
                return candidate_index
            print()

    # Si llegamos aquí, el candidato no tiene suficientes ocurrencias
    print(f"\n❌ El candidato {candidate_value} solo aparece {occurrences} veces")
    print(f"   No es suficiente para ser dominator (necesita ≥ {required_count})")
    return -1


# ============================================================================
# VERSIÓN SIN DEBUG PRINTS (para usar en producción/Codility)
# ============================================================================

def solution_clean(A):
    """Versión sin prints de debug, óptima para Codility"""
    array_length = len(A)
    if array_length == 0:
        return -1

    # Fase 1: Boyer–Moore
    candidate_index = 0
    vote_count = 0

    for index, value in enumerate(A):
        if vote_count == 0:
            candidate_index = index
            vote_count = 1
        elif value == A[candidate_index]:
            vote_count += 1
        else:
            vote_count -= 1

    if vote_count == 0:
        return -1

    # Fase 2: Verificación
    candidate_value = A[candidate_index]
    required_count = array_length // 2 + 1
    occurrences = 0

    for value in A:
        if value == candidate_value:
            occurrences += 1
            if occurrences == required_count:
                return candidate_index

    return -1


# ============================================================================
# TESTS CON EXPLICACIONES
# ============================================================================

from collections import Counter

def _is_valid_answer(A, index):
    """Verifica si la respuesta es correcta"""
    array_length = len(A)
    
    if index == -1:
        # Valid only if no dominator exists
        if array_length == 0:
            return True
        counts = Counter(A)
        return max(counts.values()) <= array_length // 2
    
    if not (0 <= index < array_length):
        return False
    
    value = A[index]
    return A.count(value) > array_length // 2


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 3, 2, 3, -1, 3, 3, 5, 5], "Vamos a retar el algoritmo"),
        ([3, 4, 3, 2, 3, -1, 3, 3], "Caso con dominator: 3 aparece 5/8 veces"),
        ([1, 2, 3], "Sin dominator: todos aparecen 1 vez"),
        ([1], "Array de un elemento: siempre es dominator"),
        ([], "Array vacío: sin dominator"),
        ([1, 1, 1, 2, 2], "1 aparece 3/5 veces > 2.5"),
        ([2, 2, 2, 2, 1], "2 aparece 4/5 veces > 2.5"),
        ([1, 2, 1, 2, 1], "1 aparece 3/5 veces > 2.5"),
        ([5, 5, 5, 5], "Todos iguales: 5 aparece 4/4 veces"),
    ]

    print("="*80)
    print("TESTING DOMINATOR - ALGORITMO BOYER-MOORE")
    print("="*80)
    
    # Prueba detallada del primer caso
    print("\n" + "="*80)
    print("EJEMPLO DETALLADO - Primer test case")
    print("="*80)
    result = solution(test_cases[0][0])
    is_valid = _is_valid_answer(test_cases[0][0], result)
    print(f"\nResultado final: {result}")
    print(f"Validación: {'✓ CORRECTO' if is_valid else '✗ INCORRECTO'}")
    
    # Resto de tests sin debug
    print("\n" + "="*80)
    print("RESTO DE TEST CASES (sin debug)")
    print("="*80 + "\n")
    
    all_passed = True
    for array, description in test_cases[1:]:
        result = solution_clean(array)
        is_valid = _is_valid_answer(array, result)
        all_passed &= is_valid
        status = "✓" if is_valid else "✗"
        
        # Mostrar información del dominator si existe
        if result != -1:
            dom_value = array[result]
            count = array.count(dom_value)
            detail = f"dominator={dom_value} ({count}/{len(array)} veces)"
        else:
            detail = "sin dominator"
        
        print(f"{status} {description}")
        print(f"   Array: {array}")
        print(f"   Resultado: índice={result} ({detail})\n")

    print("="*80)
    print(f"RESULTADO FINAL: {'✅ Todos los tests pasaron' if all_passed else '❌ Algunos tests fallaron'}")
    print("="*80)
