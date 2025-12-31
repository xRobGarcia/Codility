def solution(A):
    """
    CountNonDivisible (Codility) - Versión Detallada en Español
    -------------------------------------------------------------
    Para cada A[i], devuelve cuántos elementos en A NO son divisores de A[i].

    Complejidad:
    - Tiempo:  O(maxA log maxA)  donde maxA <= 2N
    - Espacio: O(maxA)
    
    Estrategia: Criba de Eratóstenes inversa
    -----------------------------------------
    En lugar de verificar para cada elemento todos los demás (O(N²)),
    usamos una criba que recorre cada valor presente y marca todos sus múltiplos.
    """
    
    # ========================================
    # 1. CONFIGURACIÓN INICIAL
    # ========================================
    n = len(A)           # Total de elementos en el array
    maxA = max(A)        # Valor máximo del array (límite superior para la criba)
    
    print(f"\n=== ENTRADA ===")
    print(f"Array A: {A}")
    print(f"Longitud N: {n}")
    print(f"Valor máximo: {maxA}")
    
    
    # ========================================
    # 2. TABLA DE FRECUENCIAS
    # ========================================
    # freq[x] = cuántas veces aparece el valor x en A
    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1
    
    print(f"\n=== FRECUENCIAS ===")
    print(f"Valores que aparecen en A:")
    for i in range(len(freq)):
        if freq[i] > 0:
            print(f"  {i}: aparece {freq[i]} {'vez' if freq[i] == 1 else 'veces'}")
    
    
    # ========================================
    # 3. LISTA DE VALORES PRESENTES
    # ========================================
    # Solo iteramos sobre valores que realmente existen en A
    # Esto optimiza cuando el array tiene pocos valores únicos
    present = [i for i, c in enumerate(freq) if c]
    
    print(f"\n=== VALORES ÚNICOS ===")
    print(f"Valores presentes: {present}")
    print(f"Total valores únicos: {len(present)}")
    
    
    # ========================================
    # 4. CRIBA: CONTAR DIVISORES
    # ========================================
    # div_cnt[v] = cuántos elementos en A dividen al valor v
    div_cnt = [0] * (maxA + 1)
    
    print(f"\n=== CRIBA (Marcando múltiplos) ===")
    
    limit = maxA + 1
    for d in present:
        c = freq[d]  # Cantidad de veces que aparece d
        
        print(f"\nProcesando divisor d = {d} (aparece {c} {'vez' if c == 1 else 'veces'}):")
        print(f"  Múltiplos de {d} en rango [1..{maxA}]:", end=" ")
        
        multiples_list = []
        m = d
        while m < limit:
            div_cnt[m] += c
            multiples_list.append(m)
            m += d
        
        print(multiples_list)
    
    print(f"\n=== CONTEO DE DIVISORES ===")
    print(f"div_cnt (cuántos elementos de A dividen cada valor):")
    for i in range(len(div_cnt)):
        if div_cnt[i] > 0:
            print(f"  {i}: {div_cnt[i]} divisores")
    
    
    # ========================================
    # 5. CALCULAR NO-DIVISORES
    # ========================================
    # Para cada elemento x en A:
    # no_divisores = total_elementos - divisores_de_x
    print(f"\n=== CÁLCULO FINAL ===")
    result = []
    for i, x in enumerate(A):
        non_div_count = n - div_cnt[x]
        result.append(non_div_count)
        print(f"A[{i}] = {x}: divisores = {div_cnt[x]}, no-divisores = {non_div_count}")
    
    print(f"\n=== RESULTADO ===")
    print(f"Output: {result}")
    
    return result


# ============================================
# EXPLICACIÓN DEL ALGORITMO
# ============================================
"""
IDEA PRINCIPAL:
---------------
En vez de preguntarnos "¿cuántos NO dividen a X?", nos preguntamos
"¿cuántos SÍ dividen a X?" y luego restamos del total.

PASOS:
------
1. Contamos frecuencias: ¿cuántas veces aparece cada valor?

2. Construimos lista de "present": valores únicos que existen en A

3. CRIBA: Para cada valor d que existe en A:
   - Recorremos todos sus múltiplos: d, 2d, 3d, 4d, ...
   - A cada múltiplo m, le sumamos freq[d]
   - Esto significa: "d divide a m, y d aparece freq[d] veces"

4. Para cada A[i], calculamos:
   no_divisores = N - div_cnt[A[i]]

EJEMPLO: A = [3, 1, 2, 3, 6]
---------
freq = [0, 1, 1, 2, 0, 0, 1]
       indices: 0  1  2  3  4  5  6
       
present = [1, 2, 3, 6]

Criba:
  d=1: marca múltiplos 1,2,3,4,5,6 → cada uno recibe +1
  d=2: marca múltiplos 2,4,6      → cada uno recibe +1
  d=3: marca múltiplos 3,6        → cada uno recibe +2 (freq[3]=2)
  d=6: marca múltiplo 6           → recibe +1

div_cnt después de la criba:
  div_cnt[1] = 1  (solo 1 divide a 1)
  div_cnt[2] = 2  (1 y 2 dividen a 2)
  div_cnt[3] = 3  (1 y 3×2=dos treses dividen a 3)
  div_cnt[6] = 5  (1, 2, 3×2, 6 dividen a 6)

Resultado final:
  A[0]=3 → 5-3=2 no-divisores
  A[1]=1 → 5-1=4 no-divisores
  A[2]=2 → 5-2=3 no-divisores
  A[3]=3 → 5-3=2 no-divisores
  A[4]=6 → 5-5=0 no-divisores

COMPLEJIDAD:
------------
Tiempo:  O(maxA log maxA)
  - Construcción freq: O(N)
  - Lista present: O(maxA)
  - Criba: Σ(maxA/d) para d en present ≈ maxA × log(maxA)
  - Resultado: O(N)
  
Espacio: O(maxA)
  - Arrays freq y div_cnt de tamaño maxA+1
"""


# Test con el ejemplo
if __name__ == "__main__":
    A = [3, 1, 2, 3, 6]
    result = solution(A)
    
    print(f"\n{'='*60}")
    print(f"VERIFICACIÓN")
    print(f"{'='*60}")
    print(f"Resultado obtenido: {result}")
    print(f"Resultado esperado: [2, 4, 3, 2, 0]")
    print(f"¿Correcto? {'✅ SÍ' if result == [2, 4, 3, 2, 0] else '❌ NO'}")
