# Peaks - Explicación Detallada del Algoritmo

## Descripción del Problema

Dado un array `A` de `N` enteros, queremos dividirlo en el **máximo número de bloques del mismo tamaño**, donde cada bloque debe contener **al menos un pico**.

Un **pico** es un elemento que es mayor que sus vecinos:
- `A[i]` es un pico si: `A[i-1] < A[i] > A[i+1]`
- Los índices válidos para picos son: `0 < i < N-1`

## Estrategia de Solución

La solución utiliza **prefix sums** (sumas de prefijos) y **divisores** para resolver el problema de manera eficiente.

### Complejidad
- **Tiempo:** O(N · d(N)) donde d(N) es el número de divisores de N (muy pequeño para N ≤ 100,000)
- **Espacio:** O(N) para el array de prefix sums

---

## Paso 1: Validar Tamaño Mínimo

```python
array_length = len(A)
if array_length < 3:
    return 0
```

**¿Por qué?**
- Un pico necesita al menos 3 elementos: un elemento central y dos vecinos
- Si `N < 3`, es imposible tener picos → retornamos 0

**Ejemplo:**
- `A = [1, 2]` → No hay picos posibles → retorna 0

---

## Paso 2: Construir Array de Prefix Sums para Picos

```python
peak_prefix = [0] * (array_length + 1)
total_peaks = 0
for index in range(1, array_length - 1):
    if A[index - 1] < A[index] > A[index + 1]:
        total_peaks += 1
    peak_prefix[index + 1] = total_peaks
peak_prefix[array_length] = total_peaks
```

### ¿Qué hace este código?

**Crea un array de prefix sums** donde:
- `peak_prefix[i]` = número total de picos en el rango `A[0:i]`
- Permite consultar "¿cuántos picos hay en el rango [L, R)?" en **O(1)**

### ¿Cómo funciona?

1. **Inicialización:** Creamos un array de tamaño `N+1` con ceros
2. **Iterar por elementos internos:** Solo índices `1` hasta `N-2` (posibles picos)
3. **Detectar picos:** Si `A[index-1] < A[index] > A[index+1]` → es un pico
4. **Acumular:** `peak_prefix[index+1]` guarda el total acumulado hasta ese punto

### Ejemplo Visual

```
Array A:          [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
Índices:           0  1  2  3  4  5  6  7  8  9 10 11

Picos detectados:
- Índice 3: A[2]=3 < A[3]=4 > A[4]=3 ✓ (pico)
- Índice 5: A[4]=3 < A[5]=4 > A[6]=1 ✓ (pico)
- Índice 10: A[9]=4 < A[10]=6 > A[11]=2 ✓ (pico)

peak_prefix:   [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 3]
Índices:        0  1  2  3  4  5  6  7  8  9 10 11 12
```

### Consultar picos en un rango [start, end)

```python
peaks_in_range = peak_prefix[end] - peak_prefix[start]
```

**Ejemplo:** Picos en el bloque [0, 4):
```
peak_prefix[4] - peak_prefix[0] = 1 - 0 = 1 pico
```

---

## Paso 3: Salida Temprana si No Hay Picos

```python
if total_peaks == 0:
    return 0
```

**¿Por qué?**
- Si no hay picos en todo el array, es imposible dividirlo en bloques que contengan picos
- Retornamos 0 inmediatamente

**Ejemplo:**
- `A = [1, 2, 3, 4, 5]` (creciente) → 0 picos → retorna 0

---

## Paso 4: Encontrar Todos los Divisores de N

```python
sqrt_length = math.isqrt(array_length)
block_sizes = []  # Divisores pequeños (≤ √N)
large_divisors = []  # Divisores grandes (> √N)
for divisor in range(1, sqrt_length + 1):
    if array_length % divisor == 0:
        block_sizes.append(divisor)
        complement = array_length // divisor
        if complement != divisor:
            large_divisors.append(complement)
block_sizes.extend(reversed(large_divisors))
```

### ¿Por qué necesitamos divisores?

Los bloques deben tener **todos el mismo tamaño**, por lo que:
- El tamaño del bloque debe ser un **divisor de N**
- Si `N = 12` y `block_size = 4` → tendremos `12/4 = 3` bloques

### ¿Cómo encontramos divisores eficientemente?

**Propiedad matemática:** Si `d` es divisor de `N`, entonces `N/d` también es divisor.

**Algoritmo:**
1. **Iteramos hasta √N:** Solo necesitamos comprobar hasta la raíz cuadrada
2. **Por cada divisor `d`:** También calculamos su complemento `N/d`
3. **Separamos en dos listas:**
   - `block_sizes`: divisores ≤ √N (en orden creciente)
   - `large_divisors`: divisores > √N
4. **Combinamos:** Agregamos `large_divisors` en orden inverso para mantener orden creciente

### Ejemplo Visual

```
N = 12, √12 ≈ 3.46

Iteración:
d=1: 12%1=0 → block_sizes=[1], large_divisors=[12]
d=2: 12%2=0 → block_sizes=[1,2], large_divisors=[12,6]
d=3: 12%3=0 → block_sizes=[1,2,3], large_divisors=[12,6,4]

Resultado final:
block_sizes = [1, 2, 3] + reversed([12, 6, 4])
            = [1, 2, 3, 4, 6, 12]
```

### ¿Por qué en orden creciente de tamaño?

- Tamaño de bloque pequeño → **Más bloques** (queremos maximizar)
- Ordenamos de menor a mayor tamaño para probar primero las soluciones con más bloques
- **Retornamos en cuanto encontremos** una solución válida → garantiza máximo

---

## Paso 5: Probar Cada Tamaño de Bloque

```python
for block_size in block_sizes:
    num_blocks = array_length // block_size
    
    # Optimización: si necesitamos más bloques que picos totales, imposible
    if num_blocks > total_peaks:
        continue
```

### Optimización: Poda por Pigeonhole Principle

**Principio del Palomar:**
- Si tenemos `num_blocks` bloques y cada uno necesita ≥1 pico
- Necesitamos **al menos `num_blocks` picos** en total
- Si `num_blocks > total_peaks` → **imposible** → saltamos este tamaño

**Ejemplo:**
```
total_peaks = 3
block_size = 2 → num_blocks = 12/2 = 6

¿6 bloques con solo 3 picos? IMPOSIBLE → continue
```

---

## Paso 6: Verificar que Cada Bloque Tenga al Menos Un Pico

```python
for block_start in range(0, array_length, block_size):
    # Si no hay picos en este bloque, salir del for
    if peak_prefix[block_start + block_size] == peak_prefix[block_start]:
        break
else:
    # Si todos los bloques tienen picos, retornar número de bloques
    return num_blocks
```

### ¿Qué hace este for/else?

**For loop:**
- Itera por cada bloque: `[0, block_size), [block_size, 2*block_size), ...`
- **Comprueba picos:** `peak_prefix[end] == peak_prefix[start]` significa **0 picos**
- Si algún bloque no tiene picos → `break` (salir del for)

**Else clause:**
- Solo se ejecuta si el for **terminó normalmente** (sin `break`)
- Significa: **todos los bloques tienen al menos un pico** ✓
- Retornamos `num_blocks` → esta es nuestra respuesta

### Ejemplo Completo

```
A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
N = 12, total_peaks = 3

Probamos block_size = 4:
- num_blocks = 12/4 = 3
- 3 ≤ 3 picos ✓ (pasa la poda)

Bloque 1: [0, 4) → peak_prefix[4] - peak_prefix[0] = 1 - 0 = 1 ✓
Bloque 2: [4, 8) → peak_prefix[8] - peak_prefix[4] = 2 - 1 = 1 ✓
Bloque 3: [8, 12) → peak_prefix[12] - peak_prefix[8] = 3 - 2 = 1 ✓

¡Todos los bloques tienen picos! → return 3
```

---

## Casos Especiales Importantes

### 1. Picos en los Bordes de Bloques

**Pregunta:** ¿Qué pasa si un pico está en el límite entre dos bloques?

**Respuesta:** Los picos se detectan **globalmente en todo el array**, no por bloque. Un elemento en el índice `i` es pico si tiene vecinos en `i-1` y `i+1`, **incluso si están en bloques diferentes**.

**Ejemplo:**
```
A = [1, 2, 3, 4], [3, 4, 1, 2]
Bloques: ↑         ↑
         bloque 1  bloque 2

Índice 3: A[2]=3 < A[3]=4 > A[4]=3
- A[3]=4 está al final del bloque 1
- A[4]=3 está al inicio del bloque 2
- ¡Pero A[3] SIGUE siendo un pico! ✓
```

### 2. Array sin Picos

```python
A = [1, 2, 3, 4, 5]  # Monotónicamente creciente
→ total_peaks = 0 → return 0
```

### 3. N es Primo

```python
A = [1, 2, 1, 2, 1]  # N=5 (primo), 2 picos
→ Divisores de 5: [1, 5]
→ block_size=1: cada bloque es 1 elemento → no puede tener picos
→ block_size=5: num_blocks=1 → 1 bloque con todo el array ✓
→ return 1
```

---

## Resumen del Algoritmo

| Paso | Acción | Complejidad |
|------|--------|-------------|
| 1 | Validar N ≥ 3 | O(1) |
| 2 | Construir prefix sums de picos | O(N) |
| 3 | Verificar si hay picos | O(1) |
| 4 | Encontrar divisores de N | O(√N) |
| 5-6 | Probar cada divisor | O(N · d(N)) |

**Total:** O(N · d(N)) ≈ O(N) en la práctica

---

## ¿Por Qué Esta Solución es Óptima?

1. **Prefix sums:** Consultas de picos en O(1) → eficiente
2. **Solo divisores:** No probamos todos los tamaños, solo divisores válidos
3. **Orden creciente:** Encontramos el máximo inmediatamente
4. **Poda temprana:** Descartamos rápidamente casos imposibles
5. **For/else elegante:** Validación clara y concisa

---

## Casos de Prueba Explicados

### Test 1: Ejemplo del problema
```python
A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
→ 3 picos en índices [3, 5, 10]
→ 3 bloques de tamaño 4 → return 3 ✓
```

### Test 2: Un solo pico
```python
A = [1, 3, 2]
→ 1 pico en índice 1
→ 1 bloque de tamaño 3 → return 1 ✓
```

### Test 3: Sin picos (creciente)
```python
A = [1, 2, 3, 4, 5]
→ 0 picos → return 0 ✓
```

### Test 4: Sin picos (decreciente)
```python
A = [5, 4, 3, 2, 1]
→ 0 picos → return 0 ✓
```

### Test 5: Array pequeño
```python
A = [1, 2]
→ N < 3 → return 0 ✓
```

---

## Conclusión

Este algoritmo es **elegante, eficiente y correcto** para resolver el problema de Peaks en Codility. La combinación de prefix sums para consultas rápidas y la prueba ordenada de divisores garantiza que encontramos la solución óptima de manera eficiente.
