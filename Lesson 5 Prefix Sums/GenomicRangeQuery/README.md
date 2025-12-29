# GenomicRangeQuery - Multiple Solutions

Solución al problema GenomicRangeQuery de Codility con múltiples enfoques.

## Archivos

### 1. `solution.py` ⭐ Para Codility
Versión sucinta y limpia lista para copiar directamente a Codility.
- Código compacto
- Comentarios mínimos
- Complejidad: O(N+M) tiempo, O(N) espacio

```bash
python solution.py
```

### 2. `solution_detailed.py` 📚 Educativa
Versión con explicación completa del algoritmo.
- Explicación detallada del problema
- Comparación naive vs optimal
- Análisis completo de complejidad
- Ejemplo paso a paso

```bash
python solution_detailed.py
```

### 3. `solution_desk_check.py` 🔍 Debugging
Prueba de escritorio con visualización paso a paso.
- Muestra construcción de prefix sums
- Visualiza cada query
- Verificación manual de resultados

```bash
python solution_desk_check.py
```

### 4. `solution_dry_soc.py` 🏗️ DRY & SoC
Versión orientada a objetos aplicando principios de diseño.
- Don't Repeat Yourself (DRY)
- Separation of Concerns (SoC)
- Reutilizable y mantenible
- Fácil de testear

```bash
python solution_dry_soc.py
```

### 5. `solution_functional.py` λ Funcional
Versión con programación funcional pura.
- Pure functions sin efectos secundarios
- Composable y reutilizable
- Sin estado compartido

```bash
python solution_functional.py
```

### 6. `run_all.py` 🚀 Test Suite
Ejecuta todas las versiones y compara resultados.

```bash
python run_all.py
```

## Problema

Dada una secuencia de DNA con nucleótidos (A, C, G, T) donde cada uno tiene un factor de impacto (1, 2, 3, 4), responder múltiples queries para encontrar el mínimo factor de impacto en un rango dado.

## Algoritmo: Prefix Sums

1. Construir 4 arrays de prefix sums (uno por nucleótido)
2. Para cada query, revisar nucleótidos en orden A→C→G→T
3. Retornar el primer nucleótido encontrado en el rango

**Complejidad**: O(N + M) en lugar de O(N × M) naive

## Uso

### Para Codility
Copia el contenido de `solution.py` directamente.

### Para aprender
Lee `solution_detailed.py` primero, luego ejecuta `solution_desk_check.py` para ver el algoritmo en acción.

### Para proyectos reales
Usa `solution_dry_soc.py` o `solution_functional.py` según tu estilo de programación.

## Tests

Todos los archivos incluyen casos de prueba. Para ejecutar todo:

```bash
python run_all.py
```

## Autor

Solución educativa para práctica de algoritmos Codility.
