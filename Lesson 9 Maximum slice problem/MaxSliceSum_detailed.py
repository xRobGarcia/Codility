# MaxSliceSum - Solución Codility (VERSIÓN DETALLADA CON EXPLICACIÓN)
# Algoritmo de Kadane

"""
================================================================================
EXPLICACIÓN DEL ALGORITMO DE KADANE - MÁXIMA SUMA DE SUBARREGLO
================================================================================

¿QUÉ ES UN SLICE (SUBARREGLO)?
-------------------------------
Un slice es una secuencia CONTINUA de elementos del array.

Ejemplo: A = [3, 2, -6, 4, 0]
- [3, 2] es un slice → suma = 5
- [3, 2, -6] es un slice → suma = -1
- [4] es un slice → suma = 4
- [2, -6, 4, 0] es un slice → suma = 0

¿QUÉ BUSCAMOS?
--------------
El slice con la SUMA MÁXIMA posible.

Ejemplo: A = [3, 2, -6, 4, 0]
Todos los slices posibles:
  [3]           → suma = 3
  [3, 2]        → suma = 5  ← ¡MÁXIMO!
  [3, 2, -6]    → suma = -1
  [3, 2, -6, 4] → suma = 1
  [3, 2, -6, 4, 0] → suma = 1
  [2]           → suma = 2
  [2, -6]       → suma = -4
  [2, -6, 4]    → suma = 0
  [2, -6, 4, 0] → suma = 0
  [-6]          → suma = -6
  [-6, 4]       → suma = -2
  [-6, 4, 0]    → suma = -2
  [4]           → suma = 4
  [4, 0]        → suma = 4
  [0]           → suma = 0

Respuesta: 5 (el slice [3, 2])

EL ALGORITMO DE KADANE (SIMPLE Y GENIAL)
-----------------------------------------
En lugar de probar TODOS los slices posibles (O(N²)), usamos una técnica GREEDY
que recorre el array UNA SOLA VEZ (O(N)).

IDEA CLAVE:
En cada posición, tomamos una DECISIÓN GREEDY:
  1. ¿Continúo con el slice anterior (sumo el valor actual)?
  2. ¿O empiezo un slice NUEVO desde aquí?

Elegimos la opción que da MAYOR suma.

VARIABLES:
- max_slice_ending: Mejor suma terminando EXACTAMENTE en la posición actual
- max_slice_global: Mejor suma encontrada EN TODO el recorrido

EJEMPLO PASO A PASO:
--------------------
Array: [3, 2, -6, 4, 0]

Posición 0 (valor = 3):
  max_slice_ending = 3 (es el primer elemento)
  max_slice_global = 3
  Interpretación: El mejor slice que termina aquí es [3]

Posición 1 (valor = 2):
  Decisión: ¿(3) + 2 = 5  o  empezar nuevo con 2?
  max_slice_ending = max(2, 3 + 2) = max(2, 5) = 5 ✓
  max_slice_global = max(3, 5) = 5
  Interpretación: Mejor slice que termina aquí es [3, 2] con suma 5

Posición 2 (valor = -6):
  Decisión: ¿(5) + (-6) = -1  o  empezar nuevo con -6?
  max_slice_ending = max(-6, 5 + (-6)) = max(-6, -1) = -1
  max_slice_global = max(5, -1) = 5 (no mejora)
  Interpretación: Mejor slice que termina aquí es [3, 2, -6] con suma -1

Posición 3 (valor = 4):
  Decisión: ¿(-1) + 4 = 3  o  empezar nuevo con 4?
  max_slice_ending = max(4, -1 + 4) = max(4, 3) = 4 ✓
  max_slice_global = max(5, 4) = 5 (no mejora)
  Interpretación: ¡Mejor empezar slice nuevo [4] que continuar!

Posición 4 (valor = 0):
  Decisión: ¿(4) + 0 = 4  o  empezar nuevo con 0?
  max_slice_ending = max(0, 4 + 0) = max(0, 4) = 4
  max_slice_global = max(5, 4) = 5 (no mejora)
  Interpretación: Mejor slice que termina aquí es [4, 0] con suma 4

RESPUESTA FINAL: 5

¿POR QUÉ FUNCIONA?
------------------
La clave es que max_slice_ending siempre contiene la MEJOR suma que TERMINA
en la posición actual. Si esa suma es negativa o menor que empezar de cero,
entonces es mejor "resetear" y empezar un nuevo slice.

¿POR QUÉ NECESITAMOS LA DECISIÓN GREEDY? (EXPLICACIÓN DETALLADA)
----------------------------------------------------------------

PREGUNTA FUNDAMENTAL:
En cada posición i, ¿por qué tenemos que decidir entre:
  A) Continuar el slice anterior: max_slice_ending + A[i]
  B) Empezar un slice nuevo: A[i]

RESPUESTA:
Porque necesitamos saber cuál es la MEJOR SUMA que TERMINA en la posición i.

PRINCIPIO CLAVE - SUBESTRUCTURA ÓPTIMA:
Para encontrar el mejor slice que termina en posición i, solo hay DOS opciones:

1. El mejor slice INCLUYE elementos anteriores
   → Entonces extendemos max_slice_ending (que ya es óptimo para i-1)
   
2. El mejor slice es SOLO el elemento actual
   → Porque agregar elementos anteriores EMPEORA la suma

EJEMPLO ILUSTRATIVO:
Array: [5, -7, 3, 5]

Posición 2 (valor = 3):
  Opción A (continuar): [-2] + 3 = 1
    Esto significa: slice [5, -7, 3] con suma 1
  
  Opción B (empezar nuevo): 3
    Esto significa: slice [3] con suma 3
  
  ¿Cuál elegimos? ¡Opción B! Porque 3 > 1
  
  ¿POR QUÉ? Porque llevar "arrastrando" el -2 nos PERJUDICA.
  Si continuamos con -2, cualquier suma futura será 2 puntos PEOR.
  Es mejor "cortar" y empezar fresco.

RAZONAMIENTO MATEMÁTICO:
Si max_slice_ending (suma acumulada hasta i-1) es NEGATIVA:
  → max_slice_ending + A[i] < A[i]
  → Es mejor empezar de nuevo en i

Si max_slice_ending es POSITIVA:
  → max_slice_ending + A[i] > A[i]
  → Nos conviene continuar (aprovechamos la suma acumulada)

LA DECISION GREEDY ES:
max_slice_ending = max(A[i], max_slice_ending + A[i])
                   ↑              ↑
              empezar nuevo    continuar

ESTO ES GREEDY PORQUE:
- En cada paso elegimos lo que es ÓPTIMO LOCALMENTE (mejor suma en posición i)
- NO miramos hacia adelante (¿qué vendrá después?)
- Solo comparamos: ¿me ayuda el pasado o me perjudica?

¿POR QUÉ ESTA DECISIÓN GREEDY FUNCIONA?
-----------------------------------------

TEOREMA: La decisión greedy en cada posición garantiza el óptimo global.

DEMOSTRACIÓN (por contradicción):
Supongamos que existe un slice óptimo S* que NO sigue nuestra estrategia.

Caso 1: S* incluye un prefijo con suma negativa
  Ejemplo: S* = [-3, 5, 8] con suma 10
  
  Si quitamos el prefijo negativo:
  S' = [5, 8] tiene suma 13 > 10
  
  ¡Contradicción! S* no era óptimo.

Caso 2: S* NO extiende un slice que tenía suma positiva
  Ejemplo: Tenemos suma acumulada +5, y S* empieza nuevo en el siguiente elemento
  
  Si S* es [7, 2] con suma 9, y la suma anterior era +5:
  S' = [...elementos con suma 5..., 7, 2] tiene suma 14 > 9
  
  ¡Contradicción! S* no era óptimo.

CONCLUSIÓN:
La estrategia greedy de "continuar si suma acumulada > 0, empezar nuevo si < 0"
es la ÚNICA forma de encontrar el slice óptimo.

INTUICIÓN ECONÓMICA:
Imagina que cada número es una ganancia/pérdida de dinero.
- Si llevas ganancia acumulada (+), ¡CONVIENE seguir!
- Si llevas pérdida acumulada (-), ¡es hora de RESETEAR!

Es como un juego donde puedes "cash out" (empezar de nuevo) en cualquier momento.
La estrategia greedy te dice cuándo es óptimo hacer cash out.

EJEMPLO COMPLETO DE LA DECISIÓN:
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Posición 0: [-2]
  max_slice_ending = -2 (no hay decisión)

Posición 1: valor = 1
  ¿Continuar? -2 + 1 = -1
  ¿Empezar nuevo? 1
  Decisión: 1 > -1 → ¡Empezar nuevo! ✓
  Razón: Arrastrar -2 es PEOR que empezar fresco

Posición 2: valor = -3
  ¿Continuar? 1 + (-3) = -2
  ¿Empezar nuevo? -3
  Decisión: -2 > -3 → Continuar (es "menos malo")
  Razón: Aunque ambos son negativos, -2 es mejor que -3

Posición 3: valor = 4
  ¿Continuar? -2 + 4 = 2
  ¿Empezar nuevo? 4
  Decisión: 4 > 2 → ¡Empezar nuevo! ✓
  Razón: Arrastrar -2 reduce la ganancia de 4 a 2

Posición 4: valor = -1
  ¿Continuar? 4 + (-1) = 3
  ¿Empezar nuevo? -1
  Decisión: 3 > -1 → Continuar
  Razón: Tenemos +4 acumulado, perder 1 no es tan malo

Posición 5: valor = 2
  ¿Continuar? 3 + 2 = 5
  ¿Empezar nuevo? 2
  Decisión: 5 > 2 → Continuar
  Razón: La suma acumulada +3 nos ayuda

Posición 6: valor = 1
  ¿Continuar? 5 + 1 = 6
  ¿Empezar nuevo? 1
  Decisión: 6 > 1 → Continuar
  Razón: La suma acumulada +5 nos ayuda

Máximo global: 6 (slice [4, -1, 2, 1])

LECCIÓN FINAL:
La decisión greedy NO es arbitraria. Es la ÚNICA forma correcta de construir
la solución óptima, porque:
1. Cualquier slice con prefijo negativo se puede mejorar quitando ese prefijo
2. Cualquier slice que no aprovecha una suma positiva anterior es subóptimo
3. Por lo tanto, en cada paso DEBEMOS elegir entre continuar o resetear

CASO ESPECIAL: TODOS LOS NÚMEROS NEGATIVOS
-------------------------------------------
Array: [-5, -2, -8, -1]

max_slice_ending va eligiendo el "menos malo":
  Posición 0: max_slice_ending = -5
  Posición 1: max(-2, -5 + -2) = max(-2, -7) = -2
  Posición 2: max(-8, -2 + -8) = max(-8, -10) = -8
  Posición 3: max(-1, -8 + -1) = max(-1, -9) = -1

Respuesta: -1 (el número menos negativo)

COMPLEJIDAD:
------------
Tiempo:  O(N) - un solo recorrido
Espacio: O(1) - solo dos variables

COMPARACIÓN CON FUERZA BRUTA:
------------------------------
Fuerza bruta: probar todos los slices posibles → O(N²)
Kadane: decisión greedy en cada paso → O(N) ¡1000x más rápido para N=1000!

================================================================================
"""

def solution(A):
    """
    Encuentra la suma máxima de cualquier subarreglo contiguo usando Kadane.
    """
    n = len(A)
    
    print(f"\n{'='*70}")
    print("ALGORITMO DE KADANE - MÁXIMA SUMA DE SUBARREGLO")
    print(f"{'='*70}")
    print(f"Array: {A}\n")
    
    # Inicialización
    max_slice_ending = A[0]
    max_slice_global = A[0]
    
    print(f"Inicialización:")
    print(f"  Posición 0, valor = {A[0]}")
    print(f"  max_slice_ending = {max_slice_ending}")
    print(f"  max_slice_global = {max_slice_global}")
    print()
    
    # Recorrer desde el segundo elemento
    for i in range(1, n):
        value = A[i]
        old_ending = max_slice_ending
        
        # DECISIÓN GREEDY: ¿Continuar o empezar nuevo?
        continuar = old_ending + value
        empezar_nuevo = value
        
        print(f"Posición {i}, valor = {value}:")
        print(f"  Opción 1 (continuar):     {old_ending} + {value} = {continuar}")
        print(f"  Opción 2 (empezar nuevo): {value}")
        
        max_slice_ending = max(empezar_nuevo, continuar)
        
        if max_slice_ending == empezar_nuevo:
            print(f"  ⚡ ¡MEJOR empezar NUEVO! max_slice_ending = {max_slice_ending}")
        else:
            print(f"  ✓ Continuar es mejor. max_slice_ending = {max_slice_ending}")
        
        # Actualizar máximo global si mejora
        old_global = max_slice_global
        max_slice_global = max(max_slice_global, max_slice_ending)
        
        if max_slice_global > old_global:
            print(f"  🎯 ¡NUEVO MÁXIMO GLOBAL! {old_global} → {max_slice_global}")
        else:
            print(f"  max_slice_global sigue siendo {max_slice_global}")
        print()
    
    print(f"{'='*70}")
    print(f"RESPUESTA FINAL: {max_slice_global}")
    print(f"{'='*70}\n")
    
    return max_slice_global


# ============================================================================
# VERSIÓN LIMPIA (sin prints de debug, para Codility)
# ============================================================================

def solution_clean(A):
    """Versión limpia sin prints, óptima para envío a Codility"""
    max_slice_ending = A[0]
    max_slice_global = A[0]

    for value in A[1:]:
        max_slice_ending = max(value, max_slice_ending + value)
        max_slice_global = max(max_slice_global, max_slice_ending)

    return max_slice_global


# ============================================================================
# TESTS CON EXPLICACIONES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        ([3, 2, -6, 4, 0], 5, "Ejemplo de Codility"),
        ([-2, -3, -1, -5], -1, "Todos negativos - devuelve el menos negativo"),
        ([5, -7, 3, 5, -2, 1], 8, "Slice [3, 5, -2, 1] = 8"),
        ([1], 1, "Un solo elemento"),
        ([1, 2, 3, 4, 5], 15, "Todos positivos - suma todo"),
        ([5, -3, 5], 7, "Slice completo [5, -3, 5] = 7"),
        ([-10, 2, -1, 3, -1, 5], 8, "Slice [2, -1, 3, -1, 5] = 8"),
    ]

    print("\n" + "="*70)
    print("PRUEBAS DEL ALGORITMO DE KADANE")
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
