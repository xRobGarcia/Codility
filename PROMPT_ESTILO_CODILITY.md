# 🎯 Prompt: Resuelve Challenges de Codility con Mi Estilo

## Contexto
Soy un desarrollador Python resolviendo challenges de Codility. Necesito que me ayudes a resolver problemas siguiendo **exactamente** mi estilo de código.

---

## 📋 Mi Estilo de Código

### 1. **Estructura de la Solución Principal**

```python
def solution(params):
    """
    [Nombre del Problema] (Codility)
    ---------------------------------
    [Descripción breve en 1-2 líneas]
    
    Time: O(X), Space: O(Y)
    
    [Explicación opcional de la estrategia si no es obvia]
    """
    # Código conciso y eficiente
    # Variables con nombres claros pero cortos (maxA, freq, result)
    # Evitar verbosidad innecesaria
    return result
```

**Características clave:**
- Docstring con nombre del problema, complejidad y descripción breve
- Variables claras pero concisas: `maxA`, `freq`, `div_cnt`, `left_sum`
- NO usar nombres largos tipo `maximum_value_in_array` o `frequency_counter`
- Comentarios inline solo para fórmulas/trucos no obvios
- Código directo al grano, sin over-engineering

---

### 2. **Múltiples Soluciones (cuando sea relevante)**

Si hay diferentes enfoques, incluir versiones alternativas:

```python
def solution(A):
    """Approach 1: [descripción]. Time: O(X), Space: O(Y)"""
    # implementación

def solution_optimized(A):
    """Approach 2: [descripción]. Time: O(X), Space: O(Y)"""
    # implementación con optimización matemática

def solution_xor(A):
    """Approach 3: Using XOR. Time: O(X), Space: O(Y)"""
    # implementación con operador ^=

def solution_enumerate(A):
    """More Pythonic with enumerate. Time: O(X), Space: O(Y)"""
    # versión usando enumerate() cuando sea más limpio
```

**Cuándo crear múltiples versiones:**
- Cuando hay trade-offs interesantes (tiempo vs espacio)
- Para comparar enfoques (matemático vs iterativo, XOR vs suma, etc.)
- Versión con `enumerate()` si hace el código más Pythonic
- NO crear versiones solo por crearlas

---

### 3. **Explicaciones de Fórmulas Complejas**

Cuando uses trucos matemáticos, SIEMPRE explica:

```python
def solution(Y, X, D):
    """
    [...]
    
    Formula: ceil(a/b) = (a + b - 1) // b
    
    Why the "- 1"?
    Case 1: NOT divisible (has remainder)
      a=75, b=30 → 75/30 = 2.5 → need ceil = 3
      (75 + 30 - 1) // 30 = 104 // 30 = 3 ✓
    
    Case 2: Divisible exactly (no remainder)
      a=60, b=30 → 60/30 = 2 → need ceil = 2
      (60 + 30 - 1) // 30 = 89 // 30 = 2 ✓
      WITHOUT -1: (60 + 30) // 30 = 90 // 30 = 3 ✗
    
    The "-1" prevents adding an extra when division is exact.
    """
    return ((Y - X) + D - 1) // D
```

**Incluir:**
- Fórmula matemática claramente identificada
- Casos de ejemplo con números concretos
- Explicación de por qué funciona el truco
- Qué pasaría si NO usáramos el truco

---

### 4. **Testing**

```python
if __name__ == "__main__":
    # Test con casos representativos
    A = [3, 1, 2, 3, 6]
    result = solution(A)
    print(f"Input: {A}")
    print(f"Output: {result}")
    print(f"Expected: [2, 4, 3, 2, 0]")
    
    # Si hay múltiples soluciones, comparar todas
    print("\nComparing approaches:")
    print(f"Original:   {solution(A)}")
    print(f"Optimized:  {solution_optimized(A)}")
    print(f"XOR:        {solution_xor(A)}")
```

---

### 5. **Versión Detallada (solo para problemas complejos)**

Para problemas difíciles (Lesson 9+, o que requieren técnicas avanzadas), crear archivo separado `[problema]_detallado.py`:

```python
def solution(A):
    """
    [Nombre] - Versión Detallada en Español
    ----------------------------------------
    [Descripción extendida]
    
    Complejidad:
    - Tiempo:  O(X) - [explicación detallada]
    - Espacio: O(Y) - [explicación detallada]
    
    Estrategia: [Nombre de la técnica]
    -----------------------------------
    [Explicación de la estrategia en 2-3 párrafos]
    """
    
    # ========================================
    # PASO 1: [Nombre del paso]
    # ========================================
    print(f"\n=== [PASO] ===")
    # Código con prints para debugging
    
    # ========================================
    # PASO 2: [Siguiente paso]
    # ========================================
    # etc...
    
    return result


# ============================================
# EXPLICACIÓN DEL ALGORITMO
# ============================================
"""
IDEA PRINCIPAL:
---------------
[Explicación conceptual]

PASOS:
------
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

EJEMPLO: A = [...]
---------
[Ejemplo trabajado paso a paso con ASCII art si ayuda]

COMPLEJIDAD:
------------
Tiempo:  O(X)
  - [Desglose detallado de cada operación]
  
Espacio: O(Y)
  - [Desglose de uso de memoria]

COMPARACIÓN CON BRUTE FORCE:
-----------------------------
[Si es relevante, mostrar cuánto mejoramos]
"""
```

---

### 6. **Operadores y Estilos Preferidos**

✅ **USA:**
- `enumerate(A)` en lugar de `range(len(A))` cuando necesites índice y valor
- `enumerate(A[:-1])` para iterar sin el último elemento
- Operador `^=` para XOR acumulativo
- List comprehensions para transformaciones simples
- `A[:-1]`, `A[-K:]` para slicing limpio
- `float('inf')` para valores máximos iniciales
- Variables locales para acceso repetido (`c = freq[d]`)

❌ **EVITA:**
- Loops con `range(len(A))` si puedes usar `enumerate()` o iterar directamente
- Nombres de variables excesivamente largos
- Comentarios obvios ("increment counter by 1")
- Over-engineering con clases cuando una función basta

---

### 7. **Complejidad Algorítmica**

**Formato estándar:**
```python
"""
Time: O(N log N) - [explicación: ej. "sieve over multiples up to maxA"]
Space: O(N) - [explicación: ej. "prefix sum arrays"]
"""
```

**Siempre incluir:**
- Big-O con variables relevantes (N, M, X, Y, maxA, etc.)
- Breve explicación de dónde viene la complejidad
- Relaciones entre variables cuando sea relevante (ej: "maxA ≤ 2N")

**Explicaciones detalladas cuando:**
- Complejidad no obvia (ej: harmonic series → O(N log N))
- Hay optimización matemática (ej: evitar recálculos)
- Trade-off espacio-tiempo relevante

---

## 🎯 Instrucciones de Uso

Cuando me presentes un problema de Codility, sígueme este flujo:

### Paso 1: Análisis Inicial
1. Identifica el patrón/técnica principal (prefix sums, XOR, stack, DP, etc.)
2. Determina la complejidad objetivo basándote en las restricciones

### Paso 2: Implementación
1. Crea la solución principal optimizada
2. Si hay enfoques alternativos interesantes, agrégalos
3. Si usas trucos matemáticos, explícalos con ejemplos
4. Agrega tests básicos

### Paso 3: Versión Detallada (solo si es complejo)
- Si el problema es Lesson 9+ O usa técnicas avanzadas:
  - Crea versión `_detallado.py` con prints y explicación completa
  - Incluye sección de "EXPLICACIÓN DEL ALGORITMO"
  - Trabaja un ejemplo paso a paso

---

## 📝 Ejemplo de Petición

**Yo digo:**
> Resuelve el problema "[NombreProblema]" de Codility Lesson X

**Tú haces:**
1. Analizas el problema
2. Creas solución optimizada siguiendo mi estilo
3. Agregas alternativas si son relevantes
4. Incluyes tests
5. Si es complejo (Lesson 9+), preguntas: "¿Quieres versión detallada?"

---

## ✅ Checklist de Calidad

Antes de entregar código, verifica:

- [ ] Docstring con complejidad Time/Space
- [ ] Variables con nombres concisos pero claros
- [ ] Comentarios solo donde agreguen valor (fórmulas, trucos)
- [ ] Uso de `enumerate()` donde sea más Pythonic
- [ ] Tests con resultados esperados
- [ ] Explicación de trucos matemáticos con ejemplos
- [ ] Si es complejo: ofrecimiento de versión detallada
- [ ] Código listo para copiar/pegar en Codility

---

## 🚀 Ejemplo Completo de Mi Estilo

```python
def solution(A):
    """
    Find missing element using arithmetic.
    Time: O(N), Space: O(1)
    
    Sum formula: 1+2+...+N = N(N+1)/2
    Missing = expected_sum - actual_sum
    """
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum

def solution_xor_compact(A):
    """
    Using XOR: a^a=0, paired numbers cancel.
    Time: O(N), Space: O(1)
    """
    result = len(A) + 1  # Start with last expected number
    for i, num in enumerate(A, 1):
        result ^= i ^ num
    return result

if __name__ == "__main__":
    A = [2, 3, 1, 5]
    print(f"Arithmetic: {solution(A)}")  # 4
    print(f"XOR:        {solution_xor_compact(A)}")  # 4
```

---

## 💡 Notas Finales

- **Prefiero claridad sobre cleverness**, pero no a costa de verbosidad
- **Valoro las optimizaciones matemáticas** cuando mejoran complejidad
- **Me gusta ver alternativas** para aprender diferentes enfoques
- **Aprecio las explicaciones detalladas** de algoritmos complejos
- **Código debe ser production-ready** para Codility

---

**¡Listo! Con este prompt puedes ayudarme a resolver cualquier challenge de Codility siguiendo exactamente mi estilo.** 🎯
