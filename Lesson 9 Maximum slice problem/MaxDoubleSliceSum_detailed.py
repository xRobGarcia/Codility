# MaxDoubleSliceSum - Solución Codility (VERSIÓN DETALLADA CON EXPLICACIÓN)
# Programación Dinámica + Kadane
# Tiempo:  O(N)
# Espacio: O(N)

"""
================================================================================
EXPLICACIÓN DEL ALGORITMO MAX DOUBLE SLICE SUM
================================================================================

¿QUÉ ES UN DOUBLE SLICE?
-------------------------
Un double slice es un triplete (X, Y, Z) donde:
  - 0 ≤ X < Y < Z < N
  - La suma incluye elementos:
        izquierda: A[X+1] + ... + A[Y-1]
        derecha:   A[Y+1] + ... + A[Z-1]
  - PERO excluye: A[X], A[Y], A[Z]

IMPORTANTE: A[Y] NO se incluye (es el "hueco" en el medio)

FÓRMULA:
Double slice (X, Y, Z) =
    A[X+1] + A[X+2] + ... + A[Y-1]   +   A[Y+1] + ... + A[Z-1]
     └────────── izquierda ──────────┘     └────── derecha ──────┘
                        (A[Y] es el hueco)

EJEMPLO:
Array:   [3, 2, 6, -1, 4, 5, -1, 2]
Índices:  0  1  2   3  4  5   6  7

Double slice (0, 3, 6):
  Izquierda: A[1] + A[2] = 2 + 6 = 8
  Derecha:   A[4] + A[5] = 4 + 5 = 9
  A[3] = -1 NO se incluye (es el hueco Y)
  Total = 8 + 9 = 17 ✓
  
  Nota: A[0], A[6] y A[7] NO se usan porque:
    - A[0]: excluido (es X)
    - A[6]: excluido (es Z)
    - A[7]: fuera del triplete (está más allá de Z=6)

¿QUÉ HACE DIFÍCIL ESTE PROBLEMA?
--------------------------------
- Hay O(N³) tripletes (X,Y,Z).
- No es un slice continuo: hay un hueco en Y.
- Debemos probar todos los Y posibles.

LA SOLUCIÓN: DP + KADANE
------------------------
Si fijamos Y, la mejor suma es:

  (mejor slice interno que termina en Y-1) + (mejor slice interno que empieza en Y+1)

Precomputamos dos arreglos:

1) max_ending[i] = máxima suma de un slice contiguo DENTRO de los índices
   internos (1..n-2) que TERMINA en i
   (se calcula de izquierda a derecha)

   max_ending[i] = max(0, max_ending[i-1] + A[i])

2) max_starting[i] = máxima suma de un slice contiguo DENTRO de los índices
   internos (1..n-2) que EMPIEZA en i
   (se calcula de derecha a izquierda)

   max_starting[i] = max(0, max_starting[i+1] + A[i])

Luego para cada Y (que recorre 1..n-2):

  total(Y) = max_ending[Y-1] + max_starting[Y+1]
             └─ termina ANTES del hueco ─┘  └─ empieza DESPUÉS del hueco ─┘
             (ambos tramos son independientes, por eso se suman)

NOTA CRÍTICA SOBRE BORDES (PUNTO CLAVE):
-------------------------------------------
- max_ending[0] = 0 y max_ending[n-1] = 0 porque los extremos NO pueden ser parte del slice interno.
- max_starting[0] = 0 y max_starting[n-1] = 0 por la misma razón.
- Si Y = n-2, entonces Y+1 = n-1 y max_starting[n-1] = 0 ⇒ "derecha vacía" (válido).
- Si Y = 1, entonces Y-1 = 0 y max_ending[0] = 0 ⇒ "izquierda vacía" (válido).

Aquí, permitir 0 es intencional: significa "prefiero un slice vacío a sumar negativos".

Recuerda: Y debe tener al menos un elemento a cada lado para formar un triplete válido,
por eso Y recorre 1..n-2 (no puede ser 0 ni n-1).

EJEMPLO COMPLETO PASO A PASO:
------------------------------
Array: [3, 2, 6, -1, 4, 5, -1, 2]

PASO 1: Calcular max_ending (izquierda → derecha)
  max_ending[0] = 0 (no podemos usar posición 0 como parte del slice interno)
  
  max_ending[1] = max(0, 0 + 2) = max(0, 2) = 2
    Interpretación: slice [2] con suma 2
  
  max_ending[2] = max(0, 2 + 6) = max(0, 8) = 8
    Interpretación: slice [2, 6] con suma 8
  
  max_ending[3] = max(0, 8 + (-1)) = max(0, 7) = 7
    Interpretación: slice [2, 6, -1] con suma 7
  
  max_ending[4] = max(0, 7 + 4) = max(0, 11) = 11
    Interpretación: slice [2, 6, -1, 4] con suma 11
  
  max_ending[5] = max(0, 11 + 5) = max(0, 16) = 16
    Interpretación: slice [2, 6, -1, 4, 5] con suma 16
  
  max_ending[6] = max(0, 16 + (-1)) = max(0, 15) = 15
    Interpretación: slice [2, 6, -1, 4, 5, -1] con suma 15
  
  max_ending[7] = 0 (no podemos usar posición 7 como parte del slice interno)

PASO 2: Calcular max_starting (derecha → izquierda)
  max_starting[7] = 0 (no podemos usar última posición)
  
  max_starting[6] = max(0, 0 + (-1)) = max(0, -1) = 0
    Interpretación: slice vacío es mejor que [-1]
  
  max_starting[5] = max(0, 0 + 5) = max(0, 5) = 5
    Interpretación: slice [5] con suma 5
  
  max_starting[4] = max(0, 5 + 4) = max(0, 9) = 9
    Interpretación: slice [4, 5] con suma 9
  
  max_starting[3] = max(0, 9 + (-1)) = max(0, 8) = 8
    Interpretación: slice [-1, 4, 5] con suma 8
  
  max_starting[2] = max(0, 8 + 6) = max(0, 14) = 14
    Interpretación: slice [6, -1, 4, 5] con suma 14
  
  max_starting[1] = max(0, 14 + 2) = max(0, 16) = 16
    Interpretación: slice [2, 6, -1, 4, 5] con suma 16
  
  max_starting[0] = 0 (no podemos usar primera posición)

PASO 3: Para cada Y, combinar izquierda + derecha
  Y=1: max_ending[0] + max_starting[2] = 0 + 14 = 14
  Y=2: max_ending[1] + max_starting[3] = 2 + 8 = 10
  Y=3: max_ending[2] + max_starting[4] = 8 + 9 = 17 ✓ MÁXIMO
  Y=4: max_ending[3] + max_starting[5] = 7 + 5 = 12
  Y=5: max_ending[4] + max_starting[6] = 11 + 0 = 11
  Y=6: max_ending[5] + max_starting[7] = 16 + 0 = 16

RESPUESTA: 17

¿POR QUÉ FUNCIONA?
------------------

TEOREMA: Para cualquier double slice (X, Y, Z), la suma es:
  (suma de mejor slice de X+1 a Y-1) + (suma de mejor slice de Y+1 a Z-1)

Y ambas partes son independientes (no se solapan porque Y las separa).

Por lo tanto:
- max_ending[Y-1] contiene la mejor suma posible para la parte izquierda
  (ya probó todos los X posibles al calcular hacia la derecha)
- max_starting[Y+1] contiene la mejor suma posible para la parte derecha
  (ya probó todos los Z posibles al calcular hacia la izquierda)
- Probar todos los Y posibles garantiza encontrar el óptimo global

Esto es PROGRAMACIÓN DINÁMICA: reutilizamos los cálculos previos
en lugar de probar cada triplete (X,Y,Z) por separado.

CASO ESPECIAL: TODOS NEGATIVOS
-------------------------------
Array: [-5, -3, -1, -2]

max_ending: [0, 0, 0, 0] (todos los slices tienen suma negativa → usar vacío)
max_starting: [0, 0, 0, 0]

Para cada Y:
  Y=1: 0 + 0 = 0
  Y=2: 0 + 0 = 0

Respuesta: 0 (double slice vacío es mejor que incluir números negativos)

COMPLEJIDAD:
------------
Tiempo:  O(N) - tres recorridos lineales del array:
         1. Llenar max_ending (N operaciones)
         2. Llenar max_starting (N operaciones)
         3. Probar cada Y (N operaciones)
Espacio: O(N) - dos arrays de tamaño N

COMPARACIÓN CON FUERZA BRUTA:
------------------------------
Fuerza bruta: probar todos los (X,Y,Z) y calcular suma → O(N³)
              Para N=100: ~1,000,000 de operaciones
Nuestra solución: DP + Kadane → O(N)
                  Para N=100: ~300 operaciones
¡Un millón de veces más rápido para N=100!

================================================================================
"""

def solution(A):
    """
    Versión educativa: imprime explicación paso a paso.
    """
    n = len(A)

    print(f"\n{'='*70}")
    print("ALGORITMO MAX DOUBLE SLICE SUM")
    print(f"{'='*70}")
    print(f"Array:   {A}")
    print(f"Índices: {list(range(n))}\n")

    if n < 4:
        print("Array muy pequeño (N < 4) → Respuesta: 0")
        return 0

    # ========================================================================
    # PASO 1: Calcular max_ending (izquierda → derecha)
    # ========================================================================
    print(f"{'='*70}")
    print("PASO 1: Calculando max_ending (izquierda → derecha)")
    print(f"{'='*70}\n")

    max_ending = [0] * n
    print("Regla: max_ending[i] = max(0, max_ending[i-1] + A[i])")
    print("Bordes: max_ending[0]=0 y max_ending[n-1]=0 (no pueden ser internos)\n")

    # Solo calculamos parte interna: i=1..n-2
    # (i=0 e i=n-1 no pueden ser parte de slice interno por definición)
    for i in range(1, n - 1):
        opcion_vacio = 0  # Empezar slice vacío desde aquí
        opcion_continuar = max_ending[i - 1] + A[i]  # Continuar desde el anterior
        max_ending[i] = max(opcion_vacio, opcion_continuar)  # Decisión greedy

        # Determinar qué subarray representa max_ending[i]
        if max_ending[i] == 0:
            subarray_repr = "[]"  # Slice vacío
        else:
            # Retroceder desde i hasta encontrar el inicio del slice
            start = i
            suma_temp = 0
            while start >= 1 and suma_temp < max_ending[i]:
                suma_temp += A[start]
                if suma_temp == max_ending[i]:
                    break
                start -= 1
            subarray_repr = str(A[start:i+1])

        print(f"max_ending[{i}] = max(0, {max_ending[i-1]} + {A[i]})"
              f" = max({opcion_vacio}, {opcion_continuar}) = {max_ending[i]}")
        print(f"  Subarray: {subarray_repr}\n")

    print(f"\nResultado max_ending: {max_ending}\n")

    # ========================================================================
    # PASO 2: Calcular max_starting (derecha → izquierda)
    # ========================================================================
    print(f"{'='*70}")
    print("PASO 2: Calculando max_starting (derecha → izquierda)")
    print(f"{'='*70}\n")

    max_starting = [0] * n
    print("Regla: max_starting[i] = max(0, max_starting[i+1] + A[i])")
    print("Bordes: max_starting[0]=0 y max_starting[n-1]=0 (no pueden ser internos)\n")

    # Solo calculamos parte interna: i=n-2..1 (recorriendo hacia atrás)
    # (i=0 e i=n-1 no pueden ser parte de slice interno por definición)
    for i in range(n - 2, 0, -1):
        opcion_vacio = 0  # Empezar slice vacío desde aquí
        opcion_continuar = max_starting[i + 1] + A[i]  # Continuar desde el siguiente
        max_starting[i] = max(opcion_vacio, opcion_continuar)  # Decisión greedy

        # Determinar qué subarray representa max_starting[i]
        if max_starting[i] == 0:
            subarray_repr = "[]"  # Slice vacío
        else:
            # Avanzar desde i hasta encontrar el final del slice
            end = i
            suma_temp = 0
            while end < n - 1 and suma_temp < max_starting[i]:
                suma_temp += A[end]
                if suma_temp == max_starting[i]:
                    break
                end += 1
            subarray_repr = str(A[i:end+1])

        print(f"max_starting[{i}] = max(0, {max_starting[i+1]} + {A[i]})"
              f" = max({opcion_vacio}, {opcion_continuar}) = {max_starting[i]}")
        print(f"  Subarray: {subarray_repr}\n")

    print(f"\nResultado max_starting: {max_starting}\n")

    # ========================================================================
    # PASO 3: Para cada Y, combinar izquierda + derecha
    # ========================================================================
    print(f"{'='*70}")
    print("PASO 3: Probando cada Y (elemento del medio a excluir)")
    print(f"{'='*70}\n")
    print("Nota: max_ending[y-1] representa el mejor tramo que TERMINA ANTES del hueco")
    print("      max_starting[y+1] representa el mejor tramo que EMPIEZA DESPUÉS del hueco")
    print("      Ambos son independientes → se suman directamente\n")

    max_sum = 0
    mejor_y = None

    # y recorre 1..n-2 (range(1, n-1)) porque 0 y n-1 no pueden ser Y
    for y in range(1, n - 1):
        suma_izquierda = max_ending[y - 1]  # termina ANTES del hueco
        suma_derecha = max_starting[y + 1]  # empieza DESPUÉS del hueco
        suma_total = suma_izquierda + suma_derecha

        # Construir representación de subarrays izquierda/derecha
        if suma_izquierda == 0:
            izq_repr = "[]"
        else:
            # Buscar el inicio del slice que termina en y-1
            start = y - 1
            suma_temp = 0
            while start >= 1:
                suma_temp += A[start]
                if suma_temp == suma_izquierda:
                    break
                start -= 1
            izq_repr = str(A[start:y])

        if suma_derecha == 0:
            der_repr = "[]"
        else:
            # Buscar el final del slice que empieza en y+1
            end = y + 1
            suma_temp = 0
            while end < n - 1:
                suma_temp += A[end]
                if suma_temp == suma_derecha:
                    break
                end += 1
            der_repr = str(A[y+1:end+1])

        print(f"Y={y} (A[{y}]={A[y]} es el HUECO):")
        print(f"  Izquierda: max_ending[{y-1}]   = {suma_izquierda}  ← subarray: {izq_repr}")
        print(f"  Derecha:   max_starting[{y+1}] = {suma_derecha}  ← subarray: {der_repr}")
        print(f"  ─────────────────────────────────────────────────")
        
        # Mostrar la combinación visual
        if suma_izquierda == 0 and suma_derecha == 0:
            print(f"  Combinación: [] (hueco en Y={y}) []")
        elif suma_izquierda == 0:
            print(f"  Combinación: [] (hueco en Y={y}) {der_repr}")
        elif suma_derecha == 0:
            print(f"  Combinación: {izq_repr} (hueco en Y={y}) []")
        else:
            print(f"  Combinación: {izq_repr} (hueco en Y={y}) {der_repr}")
        
        print(f"  Total: {suma_izquierda} + {suma_derecha} = {suma_total}")

        if suma_total > max_sum:
            max_sum = suma_total
            mejor_y = y
            print(f"  🎯 ¡NUEVO MÁXIMO! {suma_total}")
        print()

    print(f"{'='*70}")
    print(f"RESPUESTA FINAL: {max_sum}")
    if mejor_y is not None:
        print(f"Mejor Y: {mejor_y} (excluimos A[{mejor_y}]={A[mejor_y]})")
    print(f"{'='*70}\n")

    return max_sum


# ============================================================================
# VERSIÓN LIMPIA (sin prints, para Codility)
# ============================================================================
def solution_clean(A):
    """
    Versión limpia sin prints, óptima para envío a Codility.
    """
    n = len(A)
    if n < 4:
        return 0

    max_ending = [0] * n
    for i in range(1, n - 1):
        max_ending[i] = max(0, max_ending[i - 1] + A[i])

    max_starting = [0] * n
    for i in range(n - 2, 0, -1):
        max_starting[i] = max(0, max_starting[i + 1] + A[i])

    # Para fines didácticos: guardamos todos los valores en un arreglo
    sums = []
    for y in range(1, n - 1):
        suma_actual = max_ending[y - 1] + max_starting[y + 1]
        sums.append(suma_actual)
        # max_sum = max(max_sum, max_ending[y - 1] + max_starting[y + 1])  # Versión optimizada
    
    # Calcular el máximo de todas las sumas evaluadas
    max_sum = max(sums) if sums else 0

    return max_sum


# ============================================================================
# TESTS CON EXPLICACIONES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        ([3, 2, 6, -1, 4, 5, -1, 2], 17, "Ejemplo Codility: (0,3,6) = 2+6+4+5 = 17"),
        ([0, 10, -5, -2, 0], 10, "Solo un tramo positivo a un lado del hueco"),
        ([5, 17, 0, 3], 17, "Double slice (0,2,3): izquierda=17, derecha vacía"),
        ([-2, -3, -1, -5], 0, "Todos negativos → conviene slice vacío"),
        ([1, 1, 1, 1], 1, "Mejor double slice suma 1"),
        ([10, -1, -1, 10], 0, "El hueco no salva negativos internos suficientes"),
        ([1, 2, 3, 4, 5, 6], 12, "CORREGIDO: mejor derecha 3+4+5=12 (Y=1)"),
    ]

    print("\n" + "=" * 70)
    print("PRUEBAS DEL ALGORITMO MAX DOUBLE SLICE SUM")
    print("=" * 70)

    # Ejecución detallada del primer caso
    array, esperado, descripcion = test_cases[0]
    print("\n" + "=" * 70)
    print("EJEMPLO DETALLADO - Caso de Prueba #1")
    print("=" * 70)
    resultado = solution(array)
    print(f"Esperado: {esperado}, Obtenido: {resultado}")
    print(f"Estado: {'✓ ¡CORRECTO!' if resultado == esperado else '✗ ¡INCORRECTO!'}\n")

    # Resto con versión limpia
    print("=" * 70)
    print("CASOS DE PRUEBA RESTANTES (usando versión limpia)")
    print("=" * 70 + "\n")

    todos_pasaron = True
    for i, (array, esperado, descripcion) in enumerate(test_cases[1:], start=2):
        resultado = solution_clean(array)
        ok = (resultado == esperado)
        todos_pasaron &= ok
        print(f"{'✓' if ok else '✗'} Prueba #{i}: {descripcion}")
        print(f"   Array: {array}")
        print(f"   Esperado: {esperado}, Obtenido: {resultado}\n")

    # Incluir primera prueba en resultado general
    todos_pasaron &= (test_cases[0][1] == solution_clean(test_cases[0][0]))

    print("=" * 70)
    print(f"RESULTADO: {'✅ ¡Todas las pruebas pasaron!' if todos_pasaron else '❌ ¡Algunas pruebas fallaron!'}")
    print("=" * 70)
    print("="*70)
