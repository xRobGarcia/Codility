# EquiLeader - Solución Codility (VERSIÓN DETALLADA CON EXPLICACIÓN)
# Tiempo:  O(N)
# Espacio: O(1) extra

"""
================================================================================
EXPLICACIÓN DEL ALGORITMO EQUI-LEADER (SIMPLE PARA PRINCIPIANTES)
================================================================================

¿QUÉ ES UN LÍDER?
-----------------
Un líder es un número que aparece MÁS de la mitad de las veces en un array.

Ejemplo 1: [4, 3, 4, 4, 4, 2]
- El array tiene 6 elementos
- El número 4 aparece 4 veces
- ¿Es 4 > 6/2? → ¿Es 4 > 3? → ¡SÍ! ✓
- Entonces 4 es el LÍDER

Ejemplo 2: [1, 2, 3]
- El array tiene 3 elementos
- Cada número aparece solo 1 vez
- ¿Es 1 > 3/2? → ¿Es 1 > 1.5? → NO ✗
- NO hay LÍDER

¿QUÉ ES UN EQUI-LÍDER?
----------------------
Un equi-líder es una posición S donde podemos dividir el array en dos partes,
y AMBAS partes tienen el MISMO líder.

Ejemplo: [4, 3, 4, 4, 4, 2]
         
División en posición 0:
  Izquierda: [4]           → 4 aparece 1/1 veces → 4 es líder ✓
  Derecha:   [3, 4, 4, 4, 2] → 4 aparece 3/5 veces → 4 es líder ✓
  Ambos tienen líder 4 → ¡Posición 0 es EQUI-LÍDER! ✓

División en posición 1:
  Izquierda: [4, 3]        → 4 aparece 1/2 veces → NO es líder ✗
  Derecha:   [4, 4, 4, 2]  → 4 aparece 3/4 veces → 4 es líder ✓
  Solo derecha tiene líder → NO es equi-líder ✗

División en posición 2:
  Izquierda: [4, 3, 4]     → 4 aparece 2/3 veces → 4 es líder ✓
  Derecha:   [4, 4, 2]     → 4 aparece 2/3 veces → 4 es líder ✓
  Ambos tienen líder 4 → ¡Posición 2 es EQUI-LÍDER! ✓

División en posición 3:
  Izquierda: [4, 3, 4, 4]  → 4 aparece 3/4 veces → 4 es líder ✓
  Derecha:   [4, 2]        → 4 aparece 1/2 veces → NO es líder ✗ (exactamente 50%)
  Solo izquierda tiene líder → NO es equi-líder ✗

División en posición 4:
  Izquierda: [4, 3, 4, 4, 4] → 4 aparece 4/5 veces → 4 es líder ✓
  Derecha:   [2]           → 4 aparece 0/1 veces → NO es líder ✗
  Solo izquierda tiene líder → NO es equi-líder ✗

EL ALGORITMO (3 PASOS):
-----------------------

PASO 1: Encontrar el líder del array COMPLETO
  - Usar algoritmo Boyer-Moore (¡el juego de votación!)
  - Esto es súper rápido: O(N) tiempo, O(1) espacio

PASO 2: Verificar que el líder existe
  - Contar cuántas veces aparece
  - Verificar si realmente es más de la mitad

PASO 3: Contar equi-líderes
  - Probar dividir en cada posición
  - Verificar si ambas partes tienen el mismo líder
  - Contar cuántas posiciones funcionan

OBSERVACIÓN CLAVE:
------------------
Si hay un equi-líder en la posición S, entonces AMBAS partes izquierda y 
derecha deben tener el MISMO líder que el array completo!

¿Por qué? Porque si un número diferente fuera líder en una parte, necesitaría
aparecer > 50% en esa parte. Pero entonces el líder original no podría aparecer
> 50% en el array completo. ¡Es imposible!

Entonces solo necesitamos:
1. Encontrar el líder del array completo UNA VEZ
2. Para cada división, verificar si ese MISMO líder domina ambas partes

EJEMPLO PASO A PASO:
--------------------
Array: [4, 3, 4, 4, 4, 2]

Paso 1: Encontrar líder
  - Votación Boyer-Moore: 4 gana
  
Paso 2: Verificar
  - Conteo: 4 aparece 4 veces
  - Total: 6 elementos
  - ¿Es 4 > 3? ¡SÍ! → 4 es el líder ✓

Paso 3: Contar equi-líderes
  Posición 0: [4] | [3,4,4,4,2]
    Izq:  1 cuatro de 1 → 1 > 0.5? SÍ ✓
    Der:  3 cuatros de 5 → 3 > 2.5? SÍ ✓
    → ¡EQUI-LÍDER! Cuenta = 1
    
  Posición 1: [4,3] | [4,4,4,2]
    Izq:  1 cuatro de 2 → 1 > 1? NO ✗
    → NO es equi-líder
    
  Posición 2: [4,3,4] | [4,4,2]
    Izq:  2 cuatros de 3 → 2 > 1.5? SÍ ✓
    Der:  2 cuatros de 3 → 2 > 1.5? SÍ ✓
    → ¡EQUI-LÍDER! Cuenta = 2
    
  Posición 3: [4,3,4,4] | [4,2]
    Izq:  3 cuatros de 4 → 3 > 2? SÍ ✓
    Der:  1 cuatro de 2 → 1 > 1? NO ✗
    → NO es equi-líder
    
  Posición 4: [4,3,4,4,4] | [2]
    Izq:  4 cuatros de 5 → 4 > 2.5? SÍ ✓
    Der:  0 cuatros de 1 → 0 > 0.5? NO ✗
    → NO es equi-líder

Respuesta final: 2 equi-líderes (en posiciones 0 y 2)

¿POR QUÉ ES TAN RÁPIDO?
------------------------
Tiempo: O(N) - recorremos el array solo 2-3 veces
Espacio: O(1) - solo usamos unas pocas variables

Compara con la forma LENTA:
  Para cada posición de división (N posiciones):
    Contar líder en parte izquierda (N operaciones)
    Contar líder en parte derecha (N operaciones)
  Total: O(N²) - ¡MUY LENTO!

Nuestra forma:
  Encontrar líder una vez: O(N)
  Para cada división: solo sumar/restar conteos O(1)
  Total: O(N) - ¡SÚPER RÁPIDO! ✓

================================================================================
"""

def solution(A):
    """
    Retorna el número de equi-líderes en el array.
    
    Un equi-líder es un índice S donde tanto la parte izquierda [0..S] como
    la derecha [S+1..N-1] tienen el mismo valor líder.
    """
    n = len(A)
    if n < 2:
        return 0  # Se necesitan al menos 2 elementos para dividir

    # ========================================================================
    # PASO 1: ENCONTRAR EL LÍDER USANDO EL ALGORITMO BOYER-MOORE
    # ========================================================================
    # Piénsalo como un juego de votación:
    # - Cada número es un candidato
    # - Cuando ves tu candidato, vota por él (+1)
    # - Cuando ves un número diferente, cancela un voto (-1)
    # - El ganador es el que sobrevive con votos > 0
    
    candidato = None  # Candidato ganador actual
    votos = 0         # Número de votos para el candidato

    print(f"\n{'='*70}")
    print("PASO 1: Encontrando el líder (votación Boyer-Moore)")
    print(f"{'='*70}")
    print(f"Array: {A}\n")
    
    for i, valor in enumerate(A):
        if votos == 0:
            # Ningún candidato tiene votos, elegir este
            candidato = valor
            votos = 1
            print(f"Posición {i}, valor {valor}: ¡Nuevo candidato! candidato={candidato}, votos={votos}")
        elif valor == candidato:
            # Igual a nuestro candidato, agregar un voto
            votos += 1
            print(f"Posición {i}, valor {valor}: ¡Voto a favor de {candidato}! votos={votos}")
        else:
            # Número diferente, cancelar un voto
            votos -= 1
            print(f"Posición {i}, valor {valor}: ¡Voto en contra de {candidato}! votos={votos}")
    
    print(f"\nDespués de votar: candidato={candidato}, votos restantes={votos}")

    # ========================================================================
    # PASO 2: VERIFICAR QUE EL CANDIDATO ES REALMENTE EL LÍDER
    # ========================================================================
    # Boyer-Moore garantiza: SI existe un líder, será el candidato
    # Pero aún necesitamos verificar si el candidato aparece > N/2 veces
    
    print(f"\n{'='*70}")
    print("PASO 2: Verificando el candidato")
    print(f"{'='*70}")
    
    conteo_total_lider = sum(1 for valor in A if valor == candidato)
    
    print(f"Candidato {candidato} aparece {conteo_total_lider} veces")
    print(f"Longitud del array: {n}")
    print(f"Necesita más de {n/2} para ser líder")
    print(f"Verificar: {conteo_total_lider} * 2 = {conteo_total_lider * 2} > {n}? ", end="")
    
    if conteo_total_lider * 2 <= n:
        print("NO ✗")
        print(f"\n{candidato} NO es líder → NO hay equi-líderes posibles")
        return 0
    
    print("SÍ ✓")
    print(f"\n¡{candidato} es el LÍDER! ✓")

    # ========================================================================
    # PASO 3: CONTAR EQUI-LÍDERES
    # ========================================================================
    # Para cada posición de división S:
    #   Parte izquierda: A[0] a A[S]
    #   Parte derecha: A[S+1] a A[N-1]
    # Ambas deben tener el líder (mismo valor) dominándolas
    
    print(f"\n{'='*70}")
    print("PASO 3: Contando equi-líderes")
    print(f"{'='*70}\n")
    
    conteo_equi_lideres = 0
    conteo_lider_izq = 0  # Cuántas veces aparece el líder en la parte izquierda

    for i in range(n - 1):  # No se puede dividir después del último elemento
        # Agregar elemento actual a la parte izquierda
        if A[i] == candidato:
            conteo_lider_izq += 1

        # Calcular tamaños y conteos
        longitud_izq = i + 1
        longitud_der = n - longitud_izq
        conteo_lider_der = conteo_total_lider - conteo_lider_izq

        # Verificar si el líder domina AMBAS partes
        domina_izq = conteo_lider_izq * 2 > longitud_izq
        domina_der = conteo_lider_der * 2 > longitud_der
        
        print(f"División en posición {i}:")
        print(f"  Izq:   {A[:longitud_izq]}")
        print(f"         {candidato} aparece {conteo_lider_izq}/{longitud_izq} veces", end="")
        print(f" → {conteo_lider_izq}*2={conteo_lider_izq*2} > {longitud_izq}? {domina_izq}")
        print(f"  Der:   {A[longitud_izq:]}")
        print(f"         {candidato} aparece {conteo_lider_der}/{longitud_der} veces", end="")
        print(f" → {conteo_lider_der}*2={conteo_lider_der*2} > {longitud_der}? {domina_der}")
        
        if domina_izq and domina_der:
            conteo_equi_lideres += 1
            print(f"  → ✓ ¡EQUI-LÍDER #{conteo_equi_lideres}!")
        else:
            print(f"  → ✗ No es equi-líder")
        print()

    print(f"{'='*70}")
    print(f"RESPUESTA FINAL: {conteo_equi_lideres} equi-líder(es)")
    print(f"{'='*70}\n")
    
    return conteo_equi_lideres


# ============================================================================
# VERSIÓN LIMPIA (sin prints de debug, para Codility)
# ============================================================================

def solution_clean(A):
    """Versión limpia sin prints, óptima para envío a Codility"""
    n = len(A)
    if n < 2:
        return 0

    # Paso 1: Encontrar candidato a líder
    candidato = None
    votos = 0
    for valor in A:
        if votos == 0:
            candidato = valor
            votos = 1
        elif valor == candidato:
            votos += 1
        else:
            votos -= 1

    # Paso 2: Verificar que el candidato es líder
    conteo_total_lider = sum(1 for valor in A if valor == candidato)
    if conteo_total_lider * 2 <= n:
        return 0

    # Paso 3: Contar equi-líderes
    conteo_equi_lideres = 0
    conteo_lider_izq = 0

    for i in range(n - 1):
        if A[i] == candidato:
            conteo_lider_izq += 1

        longitud_izq = i + 1
        longitud_der = n - longitud_izq
        conteo_lider_der = conteo_total_lider - conteo_lider_izq

        if (conteo_lider_izq * 2 > longitud_izq and 
            conteo_lider_der * 2 > longitud_der):
            conteo_equi_lideres += 1

    return conteo_equi_lideres


# ============================================================================
# TESTS CON EXPLICACIONES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        ([4, 3, 4, 4, 4, 2], 2, "Ejemplo de Codility"),
        ([4, 4, 2, 5, 3, 4, 4, 4], 3, "Múltiples equi-líderes en 0, 2, 6"),
        ([1, 2, 3], 0, "Sin líder"),
        ([1, 1, 1, 1], 3, "Todos iguales - todas las divisiones funcionan"),
        ([1], 0, "Solo un elemento - no se puede dividir"),
        ([1, 2, 1], 0, "Tiene líder (1) pero no equi-líderes"),
        ([2, 1, 1, 1, 2], 0, "Tiene líder (1) pero no equi-líderes"),
        ([1, 1, 1], 2, "Todos 1s - posiciones 0 y 1 son equi-líderes"),
    ]

    print("\n" + "="*70)
    print("PRUEBAS DEL ALGORITMO EQUI-LÍDER")
    print("="*70)
    
    # Mostrar ejecución detallada para el primer caso de prueba
    print("\n" + "="*70)
    print("EJEMPLO DETALLADO - Caso de Prueba #1")
    print("="*70)
    array, esperado, descripcion = test_cases[0]
    resultado = solution(array)
    es_correcto = resultado == esperado
    print(f"Esperado: {esperado}, Obtenido: {resultado}")
    print(f"Estado: {'✓ ¡CORRECTO!' if es_correcto else '✗ ¡INCORRECTO!'}\n")
    
    # Ejecutar pruebas restantes con versión limpia
    print("="*70)
    print("CASOS DE PRUEBA RESTANTES (usando versión limpia)")
    print("="*70 + "\n")
    
    todos_pasaron = True
    for i, (array, esperado, descripcion) in enumerate(test_cases[1:], start=2):
        resultado = solution_clean(array)
        es_correcto = resultado == esperado
        todos_pasaron &= es_correcto
        estado = "✓" if es_correcto else "✗"
        
        print(f"{estado} Prueba #{i}: {descripcion}")
        print(f"   Array: {array}")
        print(f"   Esperado: {esperado}, Obtenido: {resultado}\n")
    
    # Incluir primera prueba en resultado general
    todos_pasaron &= (test_cases[0][1] == solution_clean(test_cases[0][0]))
    
    print("="*70)
    print(f"RESULTADO: {'✅ ¡Todas las pruebas pasaron!' if todos_pasaron else '❌ ¡Algunas pruebas fallaron!'}")
    print("="*70)
