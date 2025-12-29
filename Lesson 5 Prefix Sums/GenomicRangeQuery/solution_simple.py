"""
GenomicRangeQuery - Versión Didáctica (con conceptos + debug)

CONCEPTOS IMPORTANTES (en español):

1) Nucleótidos (explicado para niños):
   
   ¿Qué es un nucleótido? 🧬
   
   Imagina que el ADN es como un COLLAR DE CUENTAS. Cada cuenta es diferente
   y tiene un color:
   
   🔴 A (Adenina)   = cuenta roja
   🔵 C (Citosina)  = cuenta azul
   🟢 G (Guanina)   = cuenta verde
   🟡 T (Timina)    = cuenta amarilla
   
   Cada "cuenta" se llama NUCLEÓTIDO. Son las piezas que forman el ADN.
   
   Por ejemplo:
   ADN = "CAGCCTA" es como un collar: 🔵🔴🟢🔵🔵🟡🔴
   
   En este problema, cada letra (A, C, G, T) es un nucleótido.
   Simplemente son las "letras" que forman la cadena de ADN.

2) Impact factor (factor de impacto):
   
   ⚠️ IMPORTANTE: "Impacto" NO es algo real de biología.
   Es solo un NÚMERO INVENTADO para este ejercicio de Codility.
   
   Cada nucleótido tiene un número asignado:
   A = 1
   C = 2
   G = 3
   T = 4

   Piensa en el "impacto" como un PUNTAJE o PESO arbitrario.
   Es como si dijeran: "A vale 1 punto, C vale 2 puntos", etc.
   
   Entre más pequeño el número, "mejor" (menor impacto/puntaje).
   Por eso A (impacto=1) es el mínimo posible.
   
   En biología real, los 4 nucleótidos son IGUAL de importantes.
   El "impacto" solo existe en este problema matemático. 📊

3) ¿Qué son P y Q?
   
   P y Q son DOS LISTAS que definen los rangos de las consultas:
   
   • P = lista de posiciones de INICIO (start)
   • Q = lista de posiciones de FIN (end)
   
   Cada par (P[i], Q[i]) representa UNA consulta:
   
   Ejemplo:
   S = "CAGCCTA"  (índices: 0,1,2,3,4,5,6)
   P = [2, 5, 0]
   Q = [4, 5, 6]
   
   Tenemos 3 consultas:
   - Consulta 0: P[0]=2, Q[0]=4 → rango S[2..4] = "GCC"
   - Consulta 1: P[1]=5, Q[1]=5 → rango S[5..5] = "T"
   - Consulta 2: P[2]=0, Q[2]=6 → rango S[0..6] = "CAGCCTA" (todo)
   
   🎯 Los rangos son INCLUSIVOS: ambos extremos están incluidos.

4) Query / Consulta:
   Una consulta es una pregunta del tipo:
   "En el rango S[inicio..fin] (inclusive), ¿cuál es el impacto mínimo?"

4) Impacto mínimo:
   Es el número más pequeño entre los nucleótidos que aparecen en el rango.
   Ejemplo: si el substring tiene 'C' y 'T' -> impactos 2 y 4 -> mínimo = 2

5) ¿Cómo resolvemos rápido?
   Si revisáramos cada substring letra por letra, sería lento.
   Usamos prefix sums (conteos acumulados) para contar A/C/G/T en cualquier rango
   en tiempo constante O(1).

6) Prefix sums (conteo acumulado) - EL TRUCO MATEMÁTICO 🧮:
   
   a) ¿QUÉ ES?
   conteo_A[i] = cuántas 'A' hay en S[0..i-1]
   (nota: i es "hasta antes de", por eso usamos tamaño n+1)
   
   Es como un ODÓMETRO que va sumando kilómetros recorridos.
   
   b) LA MAGIA: RESTA DE ACUMULADOS
   
   Para contar elementos en un rango [inicio, fin]:
     cantidad = conteo[fin+1] - conteo[inicio]
   
   EJEMPLO VISUAL:
   S = "CAGCCTA"
   
   Conteo acumulado de 'C':
   Posición:  0  1  2  3  4  5  6  7
   Letra:     -  C  A  G  C  C  T  A
   conteo_C: [0, 1, 1, 1, 2, 3, 3, 3]
            ↑  ↑           ↑
            |  |           |
         inicio|         después
                         de 'C'
   
   ¿Cuántas 'C' hay en S[2..4] = "GCC"?
   conteo_C[5] - conteo_C[2] = 3 - 1 = 2 ✓ (correcto!)
                 ↑           ↑
                 |           |
             después de    antes de
             posición 4    posición 2
   
   c) ¿POR QUÉ FUNCIONA? (Teoría Matemática)
   
   Es como medir distancia entre dos puntos en un mapa:
   
   Kilómetros totales hasta el FIN - Kilómetros totales hasta el INICIO
   = Kilómetros SOLO en ese tramo
   
   Formalmente:
   ∑(i=inicio hasta fin) S[i] = ∑(i=0 hasta fin) S[i] - ∑(i=0 hasta inicio-1) S[i]
   
   O sea: "Total hasta el fin" MENOS "Total hasta antes del inicio"
   
   d) VENTAJA: "CACHE GENÉRICO" 🚀
   
   PREPROCESAMIENTO (una sola vez):
   - Recorremos S una vez: O(N)
   - Guardamos todos los conteos acumulados
   
   CONSULTAS (múltiples veces):
   - Cada consulta es solo 1 resta: O(1)
   - Sin importar el tamaño del rango!
   
   Es como construir un ÍNDICE en una biblioteca:
   - Tardas tiempo inicial en crear el índice (preprocesamiento)
   - Después encuentras cualquier libro instantáneamente (consultas)
   
   e) MEJOR PRÁCTICA DE PROGRAMACIÓN: 💡
   
   Esta técnica se llama: "TRADE-OFF TIEMPO-ESPACIO"
   (Space-Time Tradeoff o Time-Memory Tradeoff)
   
   Principio:
   "Sacrifica más MEMORIA para ganar VELOCIDAD"
   
   En este caso:
   - Usamos O(N) memoria extra (los arrays de prefix)
   - Ganamos O(N×M) → O(N+M) en tiempo
   - ¡33,333x más rápido!
   
   Otras técnicas similares:
   
   - MEMOIZATION (guardar resultados calculados):
     
     📖 DEFINICIÓN:
     Memoization es una técnica de OPTIMIZACIÓN en programación donde guardamos
     el resultado de funciones costosas en un "caché" (diccionario/memoria) para
     no tener que recalcularlas.
     
     ⚠️ CUIDADO: NO confundir con "memorización"
     
     • MEMOIZATION (computación) 💻
       - Técnica de programación
       - La computadora guarda resultados automáticamente
       - Viene de "memo" (nota, apunte)
       - Escrito así en inglés: "memoization" (con una 'r')
     
     • MEMORIZACIÓN (aprendizaje) 🧠
       - Proceso mental humano
       - Aprender algo de memoria
       - En inglés: "memorization" (con dos 'r')
     
     Relación: Ambos guardan información para uso futuro, pero:
     - Memoization → automático, para computadoras
     - Memorización → manual, para humanos
     
     Ejemplo: calcular Fibonacci
     
     ¿Qué es Fibonacci? 🔢
     Es una secuencia famosa en matemáticas donde cada número es la SUMA
     de los dos anteriores:
     
     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
     ↑  ↑  ↑
     |  |  |
     |  |  └─ 0 + 1 = 1
     |  └──── primer número = 1
     └─────── empieza en 0
     
     Fórmula: fib(n) = fib(n-1) + fib(n-2)
     Ejemplo: fib(5) = fib(4) + fib(3) = 3 + 2 = 5
     
     Aparece en: naturaleza (espirales de caracoles, flores), arte, música
     
     Sin memoization (lento, recalcula todo):
     fib(5) llama a fib(4) y fib(3)
     fib(4) llama a fib(3) y fib(2)  ← fib(3) se calcula 2 veces!
     
     Con memoization (rápido, guarda en diccionario):
     cache = {}
     Si fib(3) ya fue calculado → usa el valor guardado
     Si no → calcula y guarda en cache
     
     Es como apuntar las respuestas de un examen:
     - Primera vez: resuelves el problema
     - Próximas veces: solo copias la respuesta guardada
   
   - CACHING (guardar datos frecuentes):
     Navegadores web guardan imágenes/CSS para no descargar siempre
   
   - LOOKUP TABLES (tablas precalculadas):
     Videojuegos precalculan senos/cosenos en una tabla
   
   f) PATRÓN DE DISEÑO: "PRECOMPUTE & QUERY" 📋
   
   Este patrón se usa cuando:
   1. Tienes datos que NO cambian (inmutables)
   2. Harás MUCHAS consultas sobre los mismos datos
   3. Calcular cada vez es costoso
   
   Solución:
   1. PRECOMPUTE: Calcula todo una vez al inicio
   2. QUERY: Responde consultas en O(1)
   
   Ejemplos en el mundo real:
   - Google: indexa páginas una vez, búsquedas instantáneas
   - Bases de datos: índices precalculados
   - GPS: mapas precalculados
   - Videojuegos: texturas/shaders precompilados
   
   g) TEORÍA MATEMÁTICA: SUMAS PARCIALES (Partial Sums) 🔢
   
   Viene de matemáticas:
   
   Definición:
   prefix[i] = a₀ + a₁ + a₂ + ... + aᵢ₋₁
   
   Propiedad de resta:
   sum(aᵢ, aᵢ₊₁, ..., aⱼ) = prefix[j+1] - prefix[i]
   
   Esto es parte de:
   - Cálculo de Diferencias Finitas
   - Análisis de Series
   - Programación Dinámica (subcampo)
   
   Usado en:
   - Procesamiento de señales
   - Análisis financiero (ganancias acumuladas)
   - Física (trabajo acumulado, desplazamiento)
   - Bioinformática (análisis de secuencias genéticas)

7) Resumen Simple - ¿Por qué es tan rápido?:
   
   ✅ PREPROCESAMOS una vez: guardamos conteos acumulados
   ✅ Cada consulta es SOLO UNA RESTA: O(1)
   ✅ Sin importar si el rango tiene 10 o 100,000 elementos!
   
   Es como tener un "diccionario mágico" que ya sabe todas las respuestas.

8) ¿Por qué probamos en orden A -> C -> G -> T?
   Porque sus impactos son 1,2,3,4.
   El primer nucleótido que exista en el rango es el mínimo impacto.
"""

def solution(S, P, Q, debug=False):
    # -----------------------------
    # PASO 0: Impactos
    # -----------------------------
    # No es estrictamente necesario guardar el diccionario, porque ya sabemos
    # A=1, C=2, G=3, T=4, pero lo dejamos claro.
    IMPACT = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    n = len(S)

    # -----------------------------
    # PASO 1: Construir prefix sums
    # -----------------------------
    # Cada arreglo tiene tamaño n+1.
    # El índice 0 representa: "antes de leer cualquier letra", o sea 0 conteos.
    conteo_A = [0] * (n + 1)
    conteo_C = [0] * (n + 1)
    conteo_G = [0] * (n + 1)
    conteo_T = [0] * (n + 1)

    for i in range(n):
        # Copiamos el acumulado anterior (lo que ya llevábamos contando)
        conteo_A[i + 1] = conteo_A[i]
        conteo_C[i + 1] = conteo_C[i]
        conteo_G[i + 1] = conteo_G[i]
        conteo_T[i + 1] = conteo_T[i]

        # Sumamos 1 al nucleótido que aparece en S[i]
        if S[i] == 'A':
            conteo_A[i + 1] += 1
        elif S[i] == 'C':
            conteo_C[i + 1] += 1
        elif S[i] == 'G':
            conteo_G[i + 1] += 1
        else:  # 'T'
            conteo_T[i + 1] += 1

    if debug:
        print("\n==============================")
        print("DEBUG: PREFIJOS (PREFIX SUMS)")
        print("==============================")
        print("S =", S)
        print("Index:   ", " ".join(f"{i:2}" for i in range(n)))
        print("DNA:      ", " ".join(f"{c:2}" for c in S))
        print("conteo_A:", conteo_A)
        print("conteo_C:", conteo_C)
        print("conteo_G:", conteo_G)
        print("conteo_T:", conteo_T)
        print("\nInterpretación:")
        print("  conteo_A[i] = # de 'A' en S[0..i-1]")
        print("  Por eso para un rango [inicio..fin], usamos fin+1.\n")

    # -----------------------------
    # PASO 2: Responder queries
    # -----------------------------
    resultados = []

    for k in range(len(P)):
        inicio = P[k]
        fin = Q[k]
        sub = S[inicio:fin+1]  # solo para debug/entender

        # Cantidad de cada letra en el rango [inicio..fin]
        cuantos_A = conteo_A[fin + 1] - conteo_A[inicio]
        cuantos_C = conteo_C[fin + 1] - conteo_C[inicio]
        cuantos_G = conteo_G[fin + 1] - conteo_G[inicio]
        cuantos_T = conteo_T[fin + 1] - conteo_T[inicio]

        if debug:
            print("----------------------------------------")
            print(f"Query {k}: inicio={inicio}, fin={fin}")
            print(f"Substring = '{sub}'")
            print("Cálculos con prefijos (fin+1 - inicio):")
            print(f"  A: {conteo_A[fin+1]} - {conteo_A[inicio]} = {cuantos_A}")
            print(f"  C: {conteo_C[fin+1]} - {conteo_C[inicio]} = {cuantos_C}")
            print(f"  G: {conteo_G[fin+1]} - {conteo_G[inicio]} = {cuantos_G}")
            print(f"  T: {conteo_T[fin+1]} - {conteo_T[inicio]} = {cuantos_T}")

        # Impacto mínimo:
        # - Si hay al menos una A, el mínimo impacto ES 1 (no existe más bajo)
        # - Si no hay A pero sí C, mínimo es 2
        # - etc.
        if cuantos_A > 0:
            resultados.append(IMPACT['A'])
            if debug: print("→ Impacto mínimo: 1 (A) porque existe A en el rango.\n")
        elif cuantos_C > 0:
            resultados.append(IMPACT['C'])
            if debug: print("→ Impacto mínimo: 2 (C) porque NO hay A, pero sí C.\n")
        elif cuantos_G > 0:
            resultados.append(IMPACT['G'])
            if debug: print("→ Impacto mínimo: 3 (G) porque NO hay A ni C, pero sí G.\n")
        else:
            resultados.append(IMPACT['T'])
            if debug: print("→ Impacto mínimo: 4 (T) porque solo queda T como opción.\n")

    return resultados


if __name__ == "__main__":
    # Caso de ejemplo
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]

    print("Resultado:", solution(S, P, Q, debug=True))
    print("Esperado: [2, 4, 1]")

    # Caso simple
    print("\n--- CASO SIMPLE ---")
    S2 = "AAAA"
    P2 = [0, 1]
    Q2 = [3, 2]
    print("Resultado:", solution(S2, P2, Q2, debug=True))
    print("Esperado: [1, 1]")
