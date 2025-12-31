"""
================================================================================
PROBLEMA: Flags (Banderas en Montañas)
================================================================================

ENUNCIADO:
-----------
Tienes una montaña representada por un array A. Quieres colocar banderas en los
picos de la montaña. Las reglas son:

1. Un PICO es un índice P donde: A[P-1] < A[P] > A[P+1]
   (es mayor que sus vecinos)

2. Si decides llevar K banderas, entonces entre CUALQUIER par de banderas que
   coloques, la distancia debe ser AL MENOS K posiciones.
   
   Ejemplos para entenderlo:
   
   Si llevas K=2 banderas:
   - Entre bandera 1 y bandera 2: distancia ≥ 2
   - Ejemplo válido: banderas en posiciones 5 y 7 (distancia = 7-5 = 2 ✓)
   - Ejemplo válido: banderas en posiciones 1 y 10 (distancia = 10-1 = 9 ✓)
   - Ejemplo inválido: banderas en posiciones 3 y 4 (distancia = 1 < 2 ✗)
   
   Si llevas K=3 banderas:
   - Entre bandera 1 y bandera 2: distancia ≥ 3
   - Entre bandera 2 y bandera 3: distancia ≥ 3
   - Entre bandera 1 y bandera 3: distancia ≥ 3
   - Ejemplo válido: banderas en posiciones 1, 5, 10
     * 1→5: distancia = 4 ≥ 3 ✓
     * 5→10: distancia = 5 ≥ 3 ✓
     * 1→10: distancia = 9 ≥ 3 ✓
   
   Si llevas K=4 banderas:
   - TODAS las parejas deben tener distancia ≥ 4
   
   ⚠️ IMPORTANTE: El número K que decides llevar ES el mismo que la distancia
   mínima requerida. Si llevas 5 banderas, necesitas distancia ≥ 5 entre ellas.

3. Encuentra el MÁXIMO número de banderas que puedes colocar.

EJEMPLO:
--------
A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
     0  1  2  3  4  5  6  7  8  9 10 11

Picos están en índices: 1, 3, 5, 10
(porque A[1]=5 > A[0]=1 y A[1]=5 > A[2]=3, etc.)

Si intentamos K=4 banderas:
- Necesitamos distancia ≥ 4 entre banderas
- Pico 1, luego pico 5 (distancia=4), luego... no hay más picos a distancia ≥4
- Solo podemos colocar 3 banderas

Si intentamos K=3 banderas:
- Pico 1, luego pico 5 (distancia=4≥3), luego pico 10 (distancia=5≥3)
- ¡Funciona! Podemos colocar 3 banderas

Respuesta: 3


================================================================================
¿POR QUÉ FUNCIONA ESTA SOLUCIÓN?
================================================================================

IDEA CLAVE 1: Tabla de Saltos (next_peak)
------------------------------------------
Esta es la OPTIMIZACIÓN CLAVE que hace el algoritmo rápido.

PROBLEMA SIN next_peak:
Imagina que quieres colocar una bandera y necesitas saber: "¿cuál es el 
siguiente pico a partir de la posición 7?"

Solución lenta:
  for i in range(7, n):
      if is_peak[i]:
          return i
  
  Esto toma O(N) tiempo en el peor caso (si no hay picos adelante).
  
  Si lo haces para cada bandera, el algoritmo se vuelve MUY lento.

SOLUCIÓN CON next_peak:
Precalculamos una tabla donde:
  next_peak[i] = "índice del primer pico a partir de i (inclusive)"
  
  Si no hay picos: next_peak[i] = -1

Ahora buscar el siguiente pico es INSTANTÁNEO: O(1)
  siguiente_pico = next_peak[7]  # ¡Listo! Sin bucles


EJEMPLO DETALLADO:
------------------
Array: A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
Índices:    0  1  2  3  4  5  6  7  8  9 10 11

Picos en: 1, 3, 5, 10

Tabla next_peak que construimos:
  next_peak[0] = 1    ← primer pico desde 0 es en índice 1
  next_peak[1] = 1    ← ya estamos en un pico
  next_peak[2] = 3    ← siguiente pico desde 2 es en índice 3
  next_peak[3] = 3    ← ya estamos en un pico
  next_peak[4] = 5    ← siguiente pico desde 4 es en índice 5
  next_peak[5] = 5    ← ya estamos en un pico
  next_peak[6] = 10   ← siguiente pico desde 6 es en índice 10
  next_peak[7] = 10   ← siguiente pico desde 7 es en índice 10
  next_peak[8] = 10   ← siguiente pico desde 8 es en índice 10
  next_peak[9] = 10   ← siguiente pico desde 9 es en índice 10
  next_peak[10] = 10  ← ya estamos en un pico
  next_peak[11] = -1  ← no hay más picos después de 11


USO PRÁCTICO en el algoritmo:
------------------------------
Cuando queremos colocar banderas con distancia K:

  1. Colocamos primera bandera en: pos = next_peak[0]
     → pos = 1 (primer pico del array)
  
  2. Para la siguiente bandera, saltamos K posiciones:
     salto = pos + K = 1 + 3 = 4
     pos = next_peak[4]  ← ¡Búsqueda instantánea O(1)!
     → pos = 5 (siguiente pico después de saltar)
  
  3. Siguiente bandera:
     salto = pos + K = 5 + 3 = 8
     pos = next_peak[8]  ← ¡Otra vez O(1)!
     → pos = 10
  
  4. Siguiente:
     salto = pos + K = 10 + 3 = 13
     pos = next_peak[13] → pero 13 > 11, entonces pos = -1
     ¡Se acabaron los picos!

SIN next_peak: cada búsqueda sería O(N)
CON next_peak: cada búsqueda es O(1)

Para colocar K banderas:
  - Sin tabla: O(K × N) en el peor caso
  - Con tabla: O(K) 
  
¡Muchísimo más rápido!


CONSTRUCCIÓN de next_peak:
---------------------------
Se construye de ATRÁS hacia ADELANTE (muy importante):

  next_peak[n] = -1  # No hay nada después del final
  
  for i in range(n-1, -1, -1):  # De atrás hacia adelante
      if is_peak[i]:
          next_peak[i] = i  # Sí es pico, apuntamos a nosotros mismos
      else:
          next_peak[i] = next_peak[i+1]  # No es pico, heredamos del siguiente

¿Por qué de atrás hacia adelante?
Porque next_peak[i] depende de next_peak[i+1], entonces necesitamos
calcular primero los índices mayores.

Ejemplo paso a paso con [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]:
  
  i=12 (fuera): next_peak[12] = -1
  i=11: no es pico → next_peak[11] = next_peak[12] = -1
  i=10: SÍ es pico → next_peak[10] = 10
  i=9:  no es pico → next_peak[9] = next_peak[10] = 10
  i=8:  no es pico → next_peak[8] = next_peak[9] = 10
  ...
  i=5:  SÍ es pico → next_peak[5] = 5
  i=4:  no es pico → next_peak[4] = next_peak[5] = 5
  ...

Costo: O(N) tiempo, O(N) espacio

RESUMEN:
--------
next_peak es una tabla de "atajos" que nos permite:
✓ Saltar al siguiente pico en O(1) en lugar de O(N)
✓ Hace el algoritmo MUCHO más rápido
✓ Es la diferencia entre una solución aceptada y una que da timeout en Codility

Con esta tabla, saltar al siguiente pico es O(1) (instantáneo).


IDEA CLAVE 2: ¿Por qué el límite es √N?
----------------------------------------
Esta es la IDEA GENIAL del problema. Vamos a entenderla paso a paso:

INTUICIÓN VISUAL:
Imagina que tienes K banderas y DEBES poner distancia K entre ellas.
¿Cuánto espacio necesitas en total?

Si pones K banderas separadas por K posiciones cada una:

  Bandera 1:  posición 0
  Bandera 2:  posición 0 + K
  Bandera 3:  posición 0 + K + K = 0 + 2K
  Bandera 4:  posición 0 + K + K + K = 0 + 3K
  ...
  Bandera K:  posición 0 + (K-1) × K

DISTANCIA TOTAL OCUPADA = (K-1) × K

Ejemplo concreto:
- Si quieres 4 banderas (K=4) con distancia ≥4 entre ellas:
  * Banderas en: 0, 4, 8, 12
  * Espacio total: 12 = (4-1) × 4 = 3 × 4
  
- Si quieres 5 banderas (K=5) con distancia ≥5 entre ellas:
  * Banderas en: 0, 5, 10, 15, 20
  * Espacio total: 20 = (5-1) × 5 = 4 × 5

Ahora, si tu array solo tiene N posiciones, entonces:

    (K-1) × K ≤ N
    
Aproximadamente: K × K ≤ N  (porque K-1 ≈ K cuando K es grande)
                 K² ≤ N
                 K ≤ √N

¡ESO ES TODO! Por eso √N es el límite superior.

MATEMÁTICA DETALLADA:
Si colocamos K banderas con distancia K entre ellas:
- Primera bandera en posición p₁
- Segunda bandera en posición p₂ ≥ p₁ + K
- Tercera bandera en posición p₃ ≥ p₂ + K ≥ p₁ + 2K
- ...
- K-ésima bandera en posición pₖ ≥ p₁ + (K-1)×K

Entonces: pₖ - p₁ ≥ K(K-1)

Si N es el tamaño del array, entonces: K(K-1) ≤ N
Resolviendo: K² - K ≤ N
             K² ≤ N + K
             K ≤ √(N + K) ≈ √N (cuando N es grande)

EJEMPLOS NUMÉRICOS:
- N=100 → máximo K ≈ √100 = 10 banderas
  (necesitarías 9×10=90 posiciones, cabe en 100 ✓)
  
- N=100, intentar K=11 → necesitas 10×11=110 posiciones ✗ (no cabe)

- N=400,000 → máximo K ≈ √400000 ≈ 632 banderas
  (necesitarías 631×632=398,792 posiciones, cabe ✓)

¡Esto significa que NUNCA podremos colocar más de √N+1 banderas!


IDEA CLAVE 3: Búsqueda Binaria
-------------------------------
No probamos K=1, 2, 3, 4, ... hasta √N linealmente.
Usamos búsqueda binaria:
- Si podemos colocar K banderas, también podríamos colocar K-1, K-2, etc.
- Si NO podemos colocar K banderas, tampoco podemos colocar K+1, K+2, etc.

Esta propiedad (monotonía) permite búsqueda binaria.

Ejemplo con límite √100 = 10:
- Probar K=5 (mitad entre 1 y 10)
  - Si funciona → buscar en [6, 10]
  - Si no funciona → buscar en [1, 4]

Esto reduce de 10 intentos a log(10) ≈ 3-4 intentos.


IDEA CLAVE 4: Colocación Codiciosa (Greedy)
--------------------------------------------
Para verificar si podemos colocar K banderas:
1. Colocar la primera bandera en el primer pico
2. Colocar la siguiente bandera en el primer pico disponible a distancia ≥ K
3. Repetir hasta colocar K banderas o quedarse sin picos

¿Por qué funciona colocar banderas "lo antes posible"?
Porque mientras más temprano coloquemos banderas, más espacio nos queda
para las siguientes. Es la estrategia óptima (demostrable matemáticamente).


================================================================================
COMPLEJIDAD
================================================================================

Tiempo: O(N + √N log N)

Vamos a calcularlo paso a paso:

PASO 1: Encontrar picos
------------------------
  for i in range(1, n - 1):
      if A[i - 1] < A[i] > A[i + 1]:
          is_peak[i] = True

  Recorremos todo el array una vez → O(N)


PASO 2: Construir tabla next_peak
----------------------------------
  for i in range(n - 1, -1, -1):
      next_peak[i] = i if is_peak[i] else next_peak[i + 1]

  Recorremos todo el array una vez de atrás hacia adelante → O(N)


PASO 3: Búsqueda binaria del máximo K
--------------------------------------
  ¿Cuántas iteraciones tiene la búsqueda binaria?
  
  Buscamos en el rango [1, √N+1]
  Búsqueda binaria en un rango de tamaño √N:
  
    Iteraciones = log₂(√N) = log₂(N^(1/2)) = (1/2) × log₂(N)
    
  Simplificado: O(log N) iteraciones


PASO 4: Verificar si podemos colocar K banderas (dentro de cada iteración)
---------------------------------------------------------------------------
  while pos != -1 and used < mid:
      used += 1
      jump = pos + mid
      pos = next_peak[jump]

  ¿Cuántas veces se ejecuta este while?
  - Colocamos MÁXIMO mid banderas
  - En cada iteración colocamos 1 bandera
  - Por lo tanto: O(mid) operaciones
  
  Como mid ≤ √N (porque buscamos hasta √N+1):
    Costo por verificación = O(√N)


PASO 5: Costo total de la búsqueda binaria
-------------------------------------------
  Iteraciones: O(log N)
  Costo por iteración: O(√N)
  
  Total búsqueda = O(log N) × O(√N) = O(√N × log N)


RESUMEN FINAL
-------------
  Paso 1 (encontrar picos):        O(N)
  Paso 2 (construir next_peak):    O(N)
  Paso 3-5 (búsqueda binaria):     O(√N × log N)
  
  TOTAL = O(N) + O(N) + O(√N × log N)
        = O(N) + O(√N × log N)
        = O(N + √N log N)


¿POR QUÉ O(N + √N log N) y no solo O(N)?
-----------------------------------------
Porque necesitamos considerar ambos términos:

- Para N pequeño: el término O(N) domina
  Ejemplo: N=100 → O(100 + √100 × log 100) = O(100 + 10×7) = O(170) ≈ O(N)

- Para N muy grande: el término O(N) sigue dominando
  Ejemplo: N=400,000 → O(400,000 + √400000 × log 400000)
                     = O(400,000 + 632×19)
                     = O(400,000 + 12,008)
                     = O(412,008) ≈ O(N)

En general, O(N) es el término dominante, pero mantenemos O(N + √N log N)
para ser precisos sobre TODAS las operaciones del algoritmo.


COMPARACIÓN CON SOLUCIÓN INGENUA
---------------------------------
Solución ingenua (probar cada K linealmente):
  - Probar K = 1, 2, 3, ..., √N
  - Para cada K, verificar todos los picos: O(P) donde P = número de picos
  - Total: O(√N × P) → en el peor caso P = N/2, entonces O(√N × N) = O(N^(3/2))

Nuestra solución con búsqueda binaria:
  - O(N + √N log N) 
  - Mucho más rápido para N grandes!

Ejemplo con N=400,000:
  - Ingenua: O(400,000^(3/2)) ≈ O(252,982,212) operaciones
  - Nuestra: O(400,000 + 12,008) ≈ O(412,008) operaciones
  - ¡Nuestra solución es ~600 veces más rápida!


Espacio: O(N) para las tablas is_peak y next_peak


================================================================================
EJEMPLOS PASO A PASO
================================================================================
"""

import math

def solution(A):
    """Max flags on peaks using a next-peak jump table + binary search.
    Time: O(n + √n log n). Space: O(n).
    """
    n = len(A)
    if n < 3:
        return 0

    # 1) Identify peaks
    is_peak = [False] * n
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            is_peak[i] = True

    # 2) Build next_peak[i] = index of first peak at or after i, else -1
    next_peak = [-1] * (n + 1)
    for i in range(n - 1, -1, -1):
        next_peak[i] = i if is_peak[i] else next_peak[i + 1]

    # VERIFICACIÓN CRÍTICA: ¿Hay al menos UN pico en el array?
    # next_peak[0] nos dice: "¿cuál es el primer pico desde el inicio del array?"
    # Si next_peak[0] == -1, significa que NO HAY NINGÚN pico en todo el array
    # Sin picos, no podemos colocar ninguna bandera → retornar 0
    if next_peak[0] == -1:
        return 0
    
    # Si llegamos aquí, sabemos que HAY al menos un pico
    # (porque next_peak[0] != -1, es un índice válido)

    # Binary search for max K
    peak_count = sum(is_peak)
    
    # ¿Por qué √N+1?
    # Si colocamos K banderas con distancia K, ocupamos (K-1)×K posiciones
    # Como el array tiene N posiciones: (K-1)×K ≤ N → K² ≤ N → K ≤ √N
    # Entonces NUNCA podremos colocar más de √N+1 banderas (límite matemático)
    #
    # ¿Por qué el +1?
    # Porque isqrt(N) redondea HACIA ABAJO. Ejemplos:
    #   N=12: isqrt(12)=3, pero K=4 funciona: (4-1)×4=12 ≤ 12 ✓
    #   N=13: isqrt(13)=3, pero K=4 funciona: (4-1)×4=12 ≤ 13 ✓
    #   N=25: isqrt(25)=5, y K=5 funciona: (5-1)×5=20 ≤ 25 ✓
    # El +1 es un margen de seguridad para no quedarnos cortos
    #
    # ¿Por qué min(√N+1, peak_count)?
    # Obvio: no podemos colocar más banderas que picos disponibles
    # Ejemplo: Si N=1000 (√N≈31) pero solo hay 5 picos → límite real es 5
    lo, hi = 1, min(math.isqrt(n) + 1, peak_count)
    ans = 1

    while lo <= hi:
        num_flags = (lo + hi) // 2
        
        # Check if we can place num_flags flags
        pos = next_peak[0]
        used = 0
        while pos != -1 and used < num_flags:
            used += 1
            jump = pos + num_flags
            pos = next_peak[jump] if jump <= n else -1
        
        if used == num_flags:
            ans = num_flags
            lo = num_flags + 1
        else:
            hi = num_flags - 1

    return ans


def solution_explicada(A):
    """
    Versión con prints para entender paso a paso qué hace el algoritmo.
    """
    n = len(A)
    print(f"\n{'='*70}")
    print(f"ARRAY A = {A}")
    print(f"Tamaño N = {n}")
    print(f"{'='*70}\n")
    
    if n < 3:
        print("⚠️  Array muy pequeño (N < 3), no puede haber picos.")
        return 0

    # 1) Encontrar picos
    print("PASO 1: Encontrar todos los picos")
    print("-" * 70)
    is_peak = [False] * n
    peaks_list = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            is_peak[i] = True
            peaks_list.append(i)
            print(f"  ✓ Pico en índice {i}: A[{i-1}]={A[i-1]} < A[{i}]={A[i]} > A[{i+1}]={A[i+1]}")
    
    if not peaks_list:
        print("  ⚠️  No se encontraron picos.")
        return 0
    
    print(f"\n  Total de picos encontrados: {len(peaks_list)}")
    print(f"  Posiciones: {peaks_list}\n")

    # 2) Construir tabla de saltos
    print("PASO 2: Construir tabla next_peak[] para saltos O(1)")
    print("-" * 70)
    next_peak = [-1] * (n + 1)
    for i in range(n - 1, -1, -1):
        next_peak[i] = i if is_peak[i] else next_peak[i + 1]
    
    print("  next_peak[i] = primer pico desde índice i (o -1 si no hay)")
    print(f"  Ejemplos:")
    for i in [0, n//4, n//2, 3*n//4, n-1]:
        if i < n:
            print(f"    next_peak[{i}] = {next_peak[i]}")
    print()

    # 3) Calcular límite superior
    peak_count = len(peaks_list)
    upper_bound_sqrt = math.isqrt(n) + 1  # isqrt = raíz cuadrada ENTERA
    hi = min(upper_bound_sqrt, peak_count)
    
    print("PASO 3: Determinar límite superior para K")
    print("-" * 70)
    print(f"  √N = √{n} ≈ {math.sqrt(n):.2f}")
    print(f"  Límite teórico: √N + 1 = {upper_bound_sqrt}")
    print()
    print("  ¿POR QUÉ √N?")
    print("  " + "─" * 66)
    print("  Si colocamos K banderas con distancia K entre ellas:")
    print("    • Bandera 1 en posición p₁")
    print("    • Bandera 2 en posición p₁ + K")
    print("    • Bandera 3 en posición p₁ + 2K")
    print("    • ...")
    print("    • Bandera K en posición p₁ + (K-1)K")
    print()
    print("  El espacio mínimo necesario es: (K-1) × K")
    print(f"  Como el array tiene {n} posiciones: (K-1) × K ≤ {n}")
    print()
    print("  Resolviendo: K² - K ≤ N")
    print("             K² ≤ N + K")
    print("             K ≤ √N (aproximadamente)")
    print()
    print(f"  Ejemplo con N={n}:")
    print(f"    Si K={upper_bound_sqrt}: necesitamos ({upper_bound_sqrt}-1)×{upper_bound_sqrt} = {(upper_bound_sqrt-1)*upper_bound_sqrt} posiciones")
    if (upper_bound_sqrt-1)*upper_bound_sqrt <= n:
        print(f"    {(upper_bound_sqrt-1)*upper_bound_sqrt} ≤ {n} ✓ (cabe en el array)")
    else:
        print(f"    {(upper_bound_sqrt-1)*upper_bound_sqrt} > {n} ✗ (no cabe)")
    print()
    print(f"  Número de picos: {peak_count}")
    print(f"  Límite real: min({upper_bound_sqrt}, {peak_count}) = {hi}")
    print(f"  → Buscaremos K en el rango [1, {hi}]\n")

    # 4) Búsqueda binaria
    print("PASO 4: Búsqueda binaria para encontrar el máximo K")
    print("-" * 70)
    lo = 1
    ans = 1
    iteration = 0

    while lo <= hi:
        iteration += 1
        num_flags = (lo + hi) // 2
        
        print(f"\n  Iteración {iteration}: lo={lo}, hi={hi}, probando K={num_flags}")
        
        # Verificar si podemos colocar num_flags banderas
        pos = next_peak[0]
        used = 0
        positions = []
        
        print(f"    Colocación codiciosa con K={num_flags}:")
        while pos != -1 and used < num_flags:
            used += 1
            positions.append(pos)
            print(f"      Bandera {used}: colocar en pico índice {pos}")
            
            jump = pos + num_flags
            if jump <= n:
                new_pos = next_peak[jump]
                if new_pos != -1 and new_pos != pos:
                    print(f"        → saltar a índice {jump}, siguiente pico: {new_pos}")
                elif new_pos == -1:
                    print(f"        → saltar a índice {jump}, no hay más picos")
                pos = new_pos
            else:
                print(f"        → saltar a índice {jump} (fuera del array)")
                pos = -1
        
        print(f"    Resultado: colocamos {used} banderas en posiciones {positions}")
        
        if used == num_flags:
            ans = num_flags
            print(f"    ✓ Éxito! Podemos colocar {num_flags} banderas")
            print(f"      → Intentar más: buscar en [{num_flags+1}, {hi}]")
            lo = num_flags + 1
        else:
            print(f"    ✗ Fallo. Solo colocamos {used} < {num_flags}")
            print(f"      → Intentar menos: buscar en [{lo}, {num_flags-1}]")
            hi = num_flags - 1
    
    print(f"\n{'='*70}")
    print(f"RESPUESTA FINAL: {ans} banderas")
    print(f"{'='*70}\n")
    
    return ans


# ------------------ Tests ------------------
if __name__ == "__main__":
    print("\n" + "="*80)
    print(" "*25 + "TESTS DEL ALGORITMO")
    print("="*80)
    
    test_cases = [
        ([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3, "Ejemplo principal"),
        ([1, 3, 2], 1, "Un solo pico"),
        ([1, 2, 1], 1, "Un pico simple"),
        ([0, 0, 0], 0, "Sin picos (plano)"),
        ([1, 2, 3, 4, 5], 0, "Sin picos (creciente)"),
        ([1], 0, "Array tamaño 1"),
        ([1, 2], 0, "Array tamaño 2"),
    ]
    
    for i, (A, expected, description) in enumerate(test_cases, 1):
        print(f"\n{'#'*80}")
        print(f"# TEST {i}: {description}")
        print(f"{'#'*80}")
        
        result_simple = solution(A)
        is_correct = result_simple == expected
        
        status = "✓ PASS" if is_correct else "✗ FAIL"
        print(f"\n{status}: Esperado={expected}, Obtenido={result_simple}")
        
        # Mostrar explicación detallada solo para casos interesantes
        if len(A) <= 20 and i == 1:  # Solo el primer caso
            print("\n" + "~"*80)
            print("VEAMOS PASO A PASO:")
            print("~"*80)
            solution_explicada(A)
    
    print("\n" + "="*80)
    print(" "*30 + "FIN DE TESTS")
    print("="*80 + "\n")


    # Ejemplo adicional con visualización
    print("\n" + "="*80)
    print(" "*20 + "EJEMPLO ADICIONAL CON VISUALIZACIÓN")
    print("="*80)
    
    A_visual = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    print(f"\nArray: {A_visual}")
    print("Índices: " + "  ".join(f"{i:2d}" for i in range(len(A_visual))))
    print()
    
    # Visualización ASCII
    max_val = max(A_visual)
    for level in range(max_val, 0, -1):
        line = ""
        for val in A_visual:
            if val >= level:
                line += " ██"
            else:
                line += "   "
        print(f"{level:2d} |{line}")
    print("   +" + "---" * len(A_visual))
    print("     " + "  ".join(f"{i:2d}" for i in range(len(A_visual))))
    
    # Marcar picos
    peaks = [i for i in range(1, len(A_visual)-1) 
             if A_visual[i-1] < A_visual[i] > A_visual[i+1]]
    print("\nPicos: " + "   " * min(peaks) + "  ↑" + 
          "".join("   " if i+1 not in peaks else "  ↑" for i in peaks[:-1]))
    print("Índices: " + ", ".join(str(p) for p in peaks))
    
    result = solution(A_visual)
    print(f"\nRESPUESTA: Podemos colocar máximo {result} banderas\n")
