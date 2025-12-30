# StoneWall - Explicación Detallada en Español
# ====================================================

"""
PROBLEMA:
---------
Construir un muro de piedra con la mínima cantidad de bloques rectangulares.

El muro tiene diferentes alturas en diferentes posiciones, especificadas por el array H.
Cada bloque es un rectángulo que puede extenderse horizontalmente tanto como sea posible.

OBJETIVO: Encontrar el número mínimo de bloques necesarios.


EJEMPLO VISUAL:
---------------
H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

Visualización del muro (cada número es la altura en esa posición):

          9
  8 8 8 8
  8 8 7 7   8
  8 8 7       
  8 8 5 7     
        
  0 1 2 3 4 5 6 7 8  (posiciones)

Los bloques son:
1. Bloque de altura 8 desde posición 0-1 (azul)
2. Bloque de altura 5 en posición 2 (verde)
3. Bloque de altura 7 en posición 3 (amarillo)
4. Bloque de altura 9 en posición 4 (rojo)
5. Bloque de altura 8 en posición 5 (morado)
6. Bloque de altura 7 en posición 6 (naranja)
7. Bloque de altura 4 en posición 7 (gris)
8. Bloque de altura 8 en posición 8 (rosa)

Respuesta: 7 bloques

Nota: El bloque 1 (altura 8) NO puede reutilizarse para la posición 5 y 8
porque hay alturas diferentes en medio (5, 7, 9) que interrumpen la continuidad.


INTUICIÓN CLAVE:
----------------
1. Un bloque puede EXTENDERSE mientras la altura sea la misma
2. Si la altura AUMENTA, necesitamos un NUEVO bloque encima
3. Si la altura DISMINUYE, los bloques más altos deben TERMINAR
4. Usamos un STACK para trackear qué bloques están "activos" (pueden extenderse)


ALGORITMO CON STACK:
--------------------
Stack guarda las alturas de bloques que están activos (aún pueden crecer horizontalmente)

Reglas:
- Si nueva altura > stack top: agregar nuevo bloque (crece hacia arriba)
- Si nueva altura < stack top: remover bloques más altos (terminan)
- Si nueva altura == stack top: reusar ese bloque (se extiende horizontalmente)


WALKTHROUGH PASO A PASO:
-------------------------
H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

Inicio:
  stack = []
  blocks = 0

Posición 0, altura = 8:
  - Stack vacío
  - Agregar altura 8
  - Nuevo bloque necesario
  → stack = [8], blocks = 1

Posición 1, altura = 8:
  - stack[-1] = 8, altura = 8 → IGUALES
  - Reusar bloque existente (se extiende)
  → stack = [8], blocks = 1

Posición 2, altura = 5:
  - stack[-1] = 8 > 5 → bloque de altura 8 termina
  - Pop stack: stack = []
  - Stack vacío, agregar altura 5
  - Nuevo bloque necesario
  → stack = [5], blocks = 2

Posición 3, altura = 7:
  - stack[-1] = 5 < 7 → nueva altura es mayor
  - Agregar altura 7 encima
  - Nuevo bloque necesario
  → stack = [5, 7], blocks = 3
  
  Visualización:
    7
    5 7
    
Posición 4, altura = 9:
  - stack[-1] = 7 < 9 → nueva altura es mayor
  - Agregar altura 9 encima
  - Nuevo bloque necesario
  → stack = [5, 7, 9], blocks = 4
  
  Visualización:
      9
    7 9
    5 7 9

Posición 5, altura = 8:
  - stack[-1] = 9 > 8 → bloque de altura 9 termina
  - Pop: stack = [5, 7]
  - stack[-1] = 7 < 8 → nueva altura es mayor
  - Agregar altura 8
  - Nuevo bloque necesario
  → stack = [5, 7, 8], blocks = 5
  
  Visualización:
      9
    7 9 8
    5 7 9 8

Posición 6, altura = 7:
  - stack[-1] = 8 > 7 → bloque de altura 8 termina
  - Pop: stack = [5, 7]
  - stack[-1] = 7 == 7 → IGUALES
  - Reusar bloque existente (el de posición 3 se extiende)
  → stack = [5, 7], blocks = 5
  
  Visualización:
      9
    7 9 8
    5 7 9 8 7  ← bloque 7 se extiende desde pos 3

Posición 7, altura = 4:
  - stack[-1] = 7 > 4 → bloque de altura 7 termina
  - Pop: stack = [5]
  - stack[-1] = 5 > 4 → bloque de altura 5 termina
  - Pop: stack = []
  - Stack vacío, agregar altura 4
  - Nuevo bloque necesario
  → stack = [4], blocks = 6

Posición 8, altura = 8:
  - stack[-1] = 4 < 8 → nueva altura es mayor
  - Agregar altura 8
  - Nuevo bloque necesario
  → stack = [4, 8], blocks = 7

RESPUESTA FINAL: 7 bloques


POR QUÉ FUNCIONA:
-----------------
1. El stack mantiene las alturas de bloques "abiertos" (que pueden extenderse)
2. Cuando una altura disminuye, los bloques más altos no pueden continuar
3. Cuando una altura aumenta, necesitamos un nuevo bloque
4. Cuando una altura se repite, reusamos el bloque existente
5. Cada bloque se cuenta exactamente una vez cuando se crea


COMPLEJIDAD:
------------
- Tiempo: O(N) - cada altura se agrega y remueve del stack máximo una vez
- Espacio: O(N) - en el peor caso, el stack tiene todas las alturas (alturas crecientes)


CASOS ESPECIALES:
-----------------
1. Alturas todas iguales: [5, 5, 5, 5] → 1 bloque (se extiende todo el camino)
2. Alturas crecientes: [1, 2, 3, 4] → 4 bloques (uno nuevo por cada nivel)
3. Alturas decrecientes: [4, 3, 2, 1] → 4 bloques (cada uno termina inmediatamente)
4. Un solo elemento: [7] → 1 bloque
"""


def solution(H):
    """
    Calcula el número mínimo de bloques rectangulares para construir el muro.
    
    Args:
        H: Array de alturas del muro en cada posición
        
    Returns:
        Número mínimo de bloques necesarios
    """
    stack = []      # Stack de alturas activas (bloques que pueden extenderse)
    blocks = 0      # Contador de bloques utilizados
    
    for height in H:
        # PASO 1: Remover bloques que son más altos que la altura actual
        # Estos bloques terminan porque no pueden continuar a esta altura más baja
        while stack and stack[-1] > height:
            stack.pop()
        
        # PASO 2: Decidir si necesitamos un nuevo bloque
        # Si el stack está vacío O la altura actual es mayor que el top del stack
        if not stack or stack[-1] < height:
            stack.append(height)    # Agregar nueva altura al stack
            blocks += 1              # Incrementar contador (nuevo bloque)
        
        # PASO 3 (implícito): Si stack[-1] == height, no hacemos nada
        # Esto significa que reusamos el bloque existente (se extiende horizontalmente)
    
    return blocks


def solution_verbose(H):
    """
    Versión verbose con print statements para ver el proceso paso a paso.
    """
    stack = []
    blocks = 0
    
    print(f"\nProcesando H = {H}\n")
    print(f"{'Pos':<5} {'Height':<8} {'Stack Before':<20} {'Action':<30} {'Stack After':<20} {'Blocks':<7}")
    print("-" * 100)
    
    for i, height in enumerate(H):
        stack_before = stack.copy()
        action = ""
        
        # Remover bloques más altos
        removed = []
        while stack and stack[-1] > height:
            removed.append(stack.pop())
        
        if removed:
            action = f"Pop {removed} (más altos)"
        
        # Agregar nuevo bloque o reusar existente
        if not stack or stack[-1] < height:
            stack.append(height)
            blocks += 1
            if action:
                action += f", Push {height} (nuevo bloque)"
            else:
                action = f"Push {height} (nuevo bloque)"
        else:  # stack[-1] == height
            if action:
                action += f", Reuse {height}"
            else:
                action = f"Reuse {height} (extiende)"
        
        print(f"{i:<5} {height:<8} {str(stack_before):<20} {action:<30} {str(stack):<20} {blocks:<7}")
    
    print("\n" + "=" * 100)
    print(f"Resultado final: {blocks} bloques\n")
    
    return blocks


if __name__ == "__main__":
    # Ejemplo del problema
    print("=" * 100)
    print("EJEMPLO PRINCIPAL DE CODILITY")
    print("=" * 100)
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    result = solution_verbose(H)
    
    print("\n" + "=" * 100)
    print("CASOS DE PRUEBA ADICIONALES")
    print("=" * 100)
    
    test_cases = [
        ([1, 1, 1], "Alturas todas iguales"),
        ([1, 2, 3], "Alturas crecientes"),
        ([3, 2, 1], "Alturas decrecientes"),
        ([1, 3, 2, 1], "Pico"),
        ([5], "Un solo elemento"),
    ]
    
    for H, description in test_cases:
        print(f"\n{description}: H = {H}")
        result = solution_verbose(H)
