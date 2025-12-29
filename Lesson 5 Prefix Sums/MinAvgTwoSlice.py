"""
MinAvgTwoSlice - Versión Codility (Sucinta)

INSIGHT MATEMÁTICO CLAVE:
El promedio mínimo SIEMPRE está en un slice de tamaño 2 o 3.

¿Por qué solo buscar en slices de tamaño 2 y 3? 🤔
(Explicado para un niño)

Imagina que tienes una fila de cajas con números:
[4, 2, 2, 5, 1, 5, 8]

Quieres encontrar el grupo de cajas (mínimo 2) con el PROMEDIO más bajo.

🎯 LA REGLA MÁGICA:
Si un grupo grande tiene el promedio más bajo, SIEMPRE puedes encontrar
un grupo más pequeño (de 2 o 3 cajas) que sea igual de bueno o MEJOR.

📦 EJEMPLO CON CAJAS:

Grupo grande de 4 cajas: [2, 2, 5, 1]
Promedio = (2 + 2 + 5 + 1) / 4 = 2.5

Pero mira, dentro de ese grupo hay grupos más pequeños:
- [2, 2] → promedio = 2.0  ← ¡MEJOR!
- [2, 5] → promedio = 3.5
- [5, 1] → promedio = 3.0

¡Encontramos uno más pequeño con promedio MENOR!

🧮 ¿POR QUÉ FUNCIONA?

Piensa en el promedio como "repartir caramelos equitativamente":

Grupo de 4: [10, 2, 2, 2]
Promedio = 16/4 = 4 caramelos por persona

Este grupo de 4 se puede dividir en:
- Grupo A (2): [10, 2] → promedio = 6
- Grupo B (2): [2, 2] → promedio = 2  ← ¡Este tiene menos!

Si el promedio del grupo grande es 4, y lo divides en dos partes,
AL MENOS UNA de esas partes debe tener promedio ≤ 4.

¿Por qué? Porque si ambas partes tuvieran promedio > 4,
el promedio total sería > 4 (¡contradicción!)

🎲 MATEMÁTICA SIMPLE:

Cualquier grupo grande se puede dividir así:
- Grupo de 4 = grupo de 2 + grupo de 2
- Grupo de 5 = grupo de 2 + grupo de 3
- Grupo de 6 = grupo de 3 + grupo de 3
- etc.

Si el grupo grande tiene el mínimo, uno de sus "pedazos" pequeños
también tendrá ese mínimo (o uno más bajo).

📚 EJEMPLO COMPLETO CON 5 ELEMENTOS:

Array: [3, 6, 1, 2, 4]

Supongamos que el slice de 5 elementos [3, 6, 1, 2, 4] tiene el promedio mínimo.
Promedio del grupo completo: (3 + 6 + 1 + 2 + 4) / 5 = 16/5 = 3.2

Ahora dividimos este grupo de 5 en grupos más pequeños:

División 1: grupo de 2 + grupo de 3
  [3, 6] + [1, 2, 4]
  Promedios: 4.5 + 2.33
  
  El slice [1, 2, 4] tiene promedio 2.33 < 3.2 ← ¡Mejor que el grande!

División 2: grupo de 3 + grupo de 2
  [3, 6, 1] + [2, 4]
  Promedios: 3.33 + 3.0
  
  El slice [2, 4] tiene promedio 3.0 < 3.2 ← ¡También mejor!

Dentro de [1, 2, 4], podemos buscar slices de tamaño 2:
  [1, 2] → promedio = 1.5 ← ¡Aún MEJOR!
  [2, 4] → promedio = 3.0

Conclusión: El slice [1, 2] tiene el VERDADERO promedio mínimo (1.5).
¡El slice grande de 5 elementos NO era el mínimo real!

Por lo tanto: solo necesitamos revisar slices de tamaño 2 y 3.
Complejidad: O(N) tiempo, O(1) espacio

✨ RESUMEN PARA NIÑOS:
"No necesitas mirar grupos grandes. El grupo más pequeño
con el promedio más bajo siempre tendrá 2 o 3 elementos."
"""

def solution(A):
    """Find starting position of slice with minimal average. O(N) time, O(1) space."""
    n = len(A)
    min_avg = float('inf')
    min_pos = 0
    
    for i in range(n - 1):
        # Check slice of size 2: [i, i+1]
        avg2 = (A[i] + A[i + 1]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_pos = i
        
        # Check slice of size 3: [i, i+1, i+2]
        if i < n - 2:
            avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            if avg3 < min_avg:
                min_avg = avg3
                min_pos = i
    
    return min_pos


if __name__ == "__main__":
    # Test case from problem
    A = [4, 2, 2, 5, 1, 5, 8]
    print(f"A = {A}")
    print(f"Result: {solution(A)}")
    print(f"Expected: 1")
    print(f"Slice [1, 2] = [2, 2], avg = 2.0")
    
    # Additional test cases
    print("\n--- Test 2 ---")
    A2 = [-3, -5, -8, -4, -10]
    print(f"A = {A2}")
    print(f"Result: {solution(A2)}")
    print(f"Expected: 2 (slice [-8, -4, -10], avg = -7.33)")
    
    print("\n--- Test 3 ---")
    A3 = [1, 1]
    print(f"A = {A3}")
    print(f"Result: {solution(A3)}")
    print(f"Expected: 0")


# MinAvgTwoSlice

# Find the minimal average of any slice containing at least two elements.
# Programming language: 
# Python
# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
# Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
