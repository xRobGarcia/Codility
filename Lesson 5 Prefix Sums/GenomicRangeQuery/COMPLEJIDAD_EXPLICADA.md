# Complejidad Algorítmica Explicada 📊

## ¿Qué es la Complejidad?

La **complejidad** mide qué tan eficiente es un algoritmo cuando la cantidad de datos crece.

Hay DOS tipos:
1. **Complejidad en Tiempo** → ¿Qué tan RÁPIDO?
2. **Complejidad en Espacio** → ¿Cuánta MEMORIA usa?

---

## 1. COMPLEJIDAD EN TIEMPO ⏱️

**Pregunta:** ¿Cuántas operaciones hace el algoritmo?

### Notación Big O

Usamos la notación **O(...)** para expresar el tiempo:

| Notación | Nombre | ¿Qué significa? | Ejemplo |
|----------|--------|-----------------|---------|
| **O(1)** | Constante | Siempre toma el mismo tiempo | Acceder a un elemento: `lista[5]` |
| **O(log N)** | Logarítmico | Crece muy lento | Búsqueda binaria |
| **O(N)** | Lineal | Crece proporcionalmente | Recorrer una lista completa |
| **O(N log N)** | Lineal-logarítmico | Un poco más lento | Ordenar eficientemente (merge sort) |
| **O(N²)** | Cuadrático | Crece muy rápido | Dos loops anidados |
| **O(2^N)** | Exponencial | ¡EXPLOTA! | Recursión mal hecha |

### Ejemplos Visuales

```python
# O(1) - Constante
# No importa el tamaño, siempre 1 operación
def obtener_primero(lista):
    return lista[0]  # ← 1 operación

# O(N) - Lineal
# Si la lista tiene N elementos, hace N operaciones
def contar_pares(lista):
    contador = 0
    for numero in lista:  # ← N iteraciones
        if numero % 2 == 0:
            contador += 1
    return contador

# O(N²) - Cuadrático
# Loop dentro de loop: N × N = N²
def encontrar_duplicados(lista):
    for i in range(len(lista)):      # ← N veces
        for j in range(len(lista)):  # ← N veces cada vez
            if i != j and lista[i] == lista[j]:
                return True
    return False
```

### Comparación de Tiempos

Si N = 1,000,000 elementos:

| Complejidad | Operaciones | Tiempo aproximado |
|-------------|-------------|-------------------|
| O(1) | 1 | 0.00001 seg |
| O(log N) | 20 | 0.0002 seg |
| O(N) | 1,000,000 | 0.01 seg |
| O(N log N) | 20,000,000 | 0.2 seg |
| O(N²) | 1,000,000,000,000 | 🔥 ¡3 HORAS! |

**¡Por eso la complejidad importa!** 🚀

---

## 2. COMPLEJIDAD EN ESPACIO 💾

**Pregunta:** ¿Cuánta memoria RAM necesita el algoritmo?

### ¿Qué cuenta como espacio?

- ✅ Listas, arrays, diccionarios que creas
- ✅ Variables extra (strings grandes, etc.)
- ❌ Variables simples (números, booleanos)
- ❌ El input original (no lo cuentas, ya existe)

### Ejemplos

```python
# O(1) - Espacio Constante
# Solo usa unas pocas variables
def suma_lista(lista):
    total = 0      # ← 1 variable
    for num in lista:
        total += num
    return total
# Memoria: O(1) → solo 'total', no importa el tamaño de 'lista'

# O(N) - Espacio Lineal
# Crea una lista nueva del mismo tamaño
def duplicar_elementos(lista):
    nueva = []     # ← nueva lista
    for num in lista:
        nueva.append(num * 2)  # ← N elementos
    return nueva
# Memoria: O(N) → 'nueva' tiene N elementos

# O(N²) - Espacio Cuadrático
# Crea una matriz NxN
def crear_tabla_multiplicacion(n):
    tabla = []
    for i in range(n):         # ← N filas
        fila = []
        for j in range(n):     # ← N columnas
            fila.append(i * j)
        tabla.append(fila)
    return tabla
# Memoria: O(N²) → tabla de N×N = N² elementos
```

---

## GenomicRangeQuery - Análisis Detallado 🧬

### Problema
- Input: Cadena S de longitud N, listas P y Q de longitud M
- Output: Lista de M respuestas

### SOLUCIÓN NAIVE (mala) 😰

```python
def solution_naive(S, P, Q):
    result = []
    for k in range(len(P)):
        substring = S[P[k]:Q[k]+1]  # Extraer substring
        min_impact = 4
        for char in substring:       # Recorrer substring
            if char == 'A':
                min_impact = min(min_impact, 1)
            elif char == 'C':
                min_impact = min(min_impact, 2)
            # etc...
        result.append(min_impact)
    return result
```

**Análisis:**
- **Tiempo:** O(N × M)
  - M queries
  - Cada query recorre hasta N caracteres
  - Total: M × N operaciones
  - Si N=100,000 y M=50,000: ¡5 mil millones de operaciones! 💥

- **Espacio:** O(M)
  - Solo la lista de resultados (M elementos)

**Veredicto:** ❌ Demasiado lento para Codility

---

### SOLUCIÓN OPTIMAL (prefix sums) ✅

```python
def solution(S, P, Q):
    n = len(S)
    
    # PASO 1: Construir prefix sums
    prefix = {
        'A': [0] * (n + 1),
        'C': [0] * (n + 1),
        'G': [0] * (n + 1),
        'T': [0] * (n + 1)
    }
    
    for i in range(n):                    # ← O(N)
        for nucleotide in 'ACGT':         # ← O(4) = O(1)
            prefix[nucleotide][i+1] = prefix[nucleotide][i]
        prefix[S[i]][i+1] += 1
    
    # PASO 2: Responder queries
    result = []
    for k in range(len(P)):               # ← O(M)
        start, end = P[k], Q[k]
        for nucleotide in 'ACGT':         # ← O(4) = O(1)
            count = prefix[nucleotide][end+1] - prefix[nucleotide][start]
            if count > 0:
                result.append(impact[nucleotide])
                break
    
    return result
```

**Análisis:**
- **Tiempo:** O(N + M)
  - Construcción de prefix: O(N × 4) = O(N)
  - M queries, cada una O(4) = O(1)
  - Total: O(N) + O(M) = **O(N + M)**
  - Si N=100,000 y M=50,000: solo ¡150,000 operaciones! 🚀
  - **33,333 veces más rápido** que la solución naive

- **Espacio:** O(N)
  - 4 arrays de tamaño N+1: O(4N) = O(N)
  - Lista de resultados: O(M)
  - Total: O(N + M), pero se simplifica a **O(N)** si N > M

**Veredicto:** ✅ Perfecto para Codility

---

## Comparación Visual

### Tiempo: O(N × M) vs O(N + M)

```
Datos: N = 100,000   M = 50,000

Naive O(N × M):
████████████████████████████████████████  5,000,000,000 ops
[█ = 125 millones de operaciones]

Optimal O(N + M):
█  150,000 ops

¡Diferencia de 33,333 veces!
```

### Espacio: O(M) vs O(N)

```
Datos: N = 100,000   M = 50,000

Naive O(M):
█████  50,000 bytes

Optimal O(N):
██████████  400,000 bytes (4 arrays × 100K)

Usa 8x más memoria, pero sigue siendo pequeño (<1MB)
```

---

## Reglas Prácticas 📝

### Complejidad en Tiempo

1. **Un loop:** O(N)
2. **Loop dentro de loop:** O(N²)
3. **Dividir a la mitad repetidamente:** O(log N)
4. **Loop + dividir:** O(N log N)
5. **Acceso directo a índice/diccionario:** O(1)

### Complejidad en Espacio

1. **Solo variables simples:** O(1)
2. **Una lista/array de tamaño N:** O(N)
3. **Matriz NxN:** O(N²)
4. **Diccionario con N elementos:** O(N)

### Lo Importante para Codility

- **O(N) o O(N log N):** ✅ Generalmente aceptable
- **O(N²):** ⚠️ Solo si N < 10,000
- **O(2^N) o O(N³):** ❌ Casi nunca pasa

---

## Ejercicio: Calcula la Complejidad

```python
# Ejercicio 1
def ejemplo1(lista):
    return lista[0] + lista[-1]

# Ejercicio 2
def ejemplo2(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

# Ejercicio 3
def ejemplo3(lista):
    resultado = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            resultado.append(lista[i] + lista[j])
    return resultado
```

<details>
<summary>Respuestas (haz click)</summary>

**Ejercicio 1:**
- Tiempo: O(1) - solo 2 accesos
- Espacio: O(1) - solo variable 'resultado'

**Ejercicio 2:**
- Tiempo: O(N) - un loop de N iteraciones
- Espacio: O(1) - solo variable 'suma'

**Ejercicio 3:**
- Tiempo: O(N²) - loop doble
- Espacio: O(N²) - resultado tiene N×N elementos

</details>

---

## Resumen Final 🎯

| Concepto | Pregunta | Lo Ideal |
|----------|----------|----------|
| **Tiempo** | ¿Qué tan rápido? | O(N) o O(N log N) |
| **Espacio** | ¿Cuánta memoria? | O(1) o O(N) |

**Clave:** Siempre busca reducir el tiempo primero. La memoria es barata, pero el tiempo del usuario es valioso.

**En GenomicRangeQuery:** Cambiamos de O(N×M) a O(N+M) usando más memoria (O(N)). ¡Vale totalmente la pena! 🚀
