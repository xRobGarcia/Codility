"""
Práctica de Slicing en Python
Sintaxis: array[start:stop:step]
- start: índice inicial (incluido)
- stop: índice final (excluido)
- step: salto entre elementos
"""

# ============ EJEMPLOS BÁSICOS ============
print("=== EJEMPLOS BÁSICOS ===\n")

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array original: {arr}")
print(f"arr[2:5]   = {arr[2:5]}")    # [2, 3, 4]
print(f"arr[:5]    = {arr[:5]}")     # [0, 1, 2, 3, 4] (desde inicio)
print(f"arr[5:]    = {arr[5:]}")     # [5, 6, 7, 8, 9] (hasta final)
print(f"arr[:]     = {arr[:]}")      # [0...9] (copia completa)

# ============ ÍNDICES NEGATIVOS ============
print("\n=== ÍNDICES NEGATIVOS ===\n")
print(f"arr[-3:]   = {arr[-3:]}")    # [7, 8, 9] (últimos 3)
print(f"arr[:-3]   = {arr[:-3]}")    # [0...6] (todos menos últimos 3)
print(f"arr[-5:-2] = {arr[-5:-2]}")  # [5, 6, 7] (desde -5 hasta -2)

# ============ STEP (SALTOS) ============
print("\n=== STEP (SALTOS) ===\n")
print(f"arr[::2]   = {arr[::2]}")    # [0, 2, 4, 6, 8] (cada 2)
print(f"arr[1::2]  = {arr[1::2]}")   # [1, 3, 5, 7, 9] (impares)
print(f"arr[::3]   = {arr[::3]}")    # [0, 3, 6, 9] (cada 3)
print(f"arr[::-1]  = {arr[::-1]}")   # [9, 8...0] (invertir)
print(f"arr[::-2]  = {arr[::-2]}")   # [9, 7, 5, 3, 1] (reverso, cada 2)

# ============ EJERCICIOS PRÁCTICOS ============
print("\n=== EJERCICIOS ===\n")

# Ejercicio 1: Obtener los primeros 3 elementos
resultado1 = arr[:3]
print(f"1. Primeros 3: {resultado1}")  # [0, 1, 2]

# Ejercicio 2: Obtener del índice 3 al 7
resultado2 = arr[3:8]
print(f"2. Del 3 al 7: {resultado2}")  # [3, 4, 5, 6, 7]

# Ejercicio 3: Últimos 4 elementos
resultado3 = arr[-4:]
print(f"3. Últimos 4: {resultado3}")   # [6, 7, 8, 9]

# Ejercicio 4: Todos excepto el primero y último
resultado4 = arr[1:-1]
print(f"4. Sin extremos: {resultado4}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# Ejercicio 5: Elementos pares (índices pares)
resultado5 = arr[::2]
print(f"5. Índices pares: {resultado5}")  # [0, 2, 4, 6, 8]

# ============ SLICING CON STRINGS ============
print("\n=== SLICING CON STRINGS ===\n")

text = "Python Programming"
print(f"Texto: '{text}'")
print(f"text[0:6]  = '{text[0:6]}'")   # 'Python'
print(f"text[7:]   = '{text[7:]}'")    # 'Programming'
print(f"text[::-1] = '{text[::-1]}'")  # 'gnimmargorP nohtyP' (reverso)
print(f"text[::2]  = '{text[::2]}'")   # 'Pto rgamn' (cada 2 chars)

# ============ CASOS ESPECIALES ============
print("\n=== CASOS ESPECIALES ===\n")

print(f"arr[100:]  = {arr[100:]}")     # [] (fuera de rango = vacío)
print(f"arr[-100:] = {arr[-100:]}")    # [0...9] (desde inicio si negativo muy grande)
print(f"arr[5:2]   = {arr[5:2]}")      # [] (start > stop = vacío)
print(f"arr[5:2:-1]= {arr[5:2:-1]}")   # [5, 4, 3] (reverso con límites)

# ============ TU TURNO: PRACTICA AQUÍ ============
print("\n=== PRACTICA AQUÍ ===\n")

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Array para practicar: {numeros}")

# TODO: Intenta estos ejercicios
# 1. Obtén [30, 40, 50]
# 2. Obtén los últimos 3 elementos
# 3. Invierte el array
# 4. Obtén los elementos en posiciones impares
# 5. Obtén del índice 2 al 6 saltando de 2 en 2

print("\nTus soluciones:")
# Descomenta y completa:
# print(f"1. {numeros[???]}")
# print(f"2. {numeros[???]}")
# print(f"3. {numeros[???]}")
# print(f"4. {numeros[???]}")
# print(f"5. {numeros[???]}")
