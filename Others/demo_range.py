"""
DEMOSTRACIÓN: Cómo funciona range() en Triangle
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo: Entender por qué usamos range(len(A) - 2) para verificar triplets
"""

print("=" * 80)
print("DEMOSTRACIÓN: range() en Triangle")
print("=" * 80)

# Ejemplo 1: Array pequeño
print("\n📋 EJEMPLO 1: Array con 5 elementos")
print("-" * 80)
A = [1, 2, 5, 8, 10]
print(f"Array: {A}")
print(f"Longitud: {len(A)}")
print(f"Índices válidos: 0, 1, 2, 3, 4")

print(f"\n¿Por qué range(len(A) - 2)?")
print(f"  len(A) = {len(A)}")
print(f"  len(A) - 2 = {len(A) - 2}")
print(f"  range({len(A) - 2}) = {list(range(len(A) - 2))}")

print("\n🔍 Verificando triplets consecutivos:")
for i in range(len(A) - 2):
    print(f"  i={i}: A[{i}], A[{i+1}], A[{i+2}] → {A[i]}, {A[i+1]}, {A[i+2]}")
    print(f"       → Verifica: {A[i]} + {A[i+1]} > {A[i+2]}? {A[i] + A[i+1]} > {A[i+2]}? {A[i] + A[i+1] > A[i+2]}")

# Ejemplo 2: ¿Qué pasa con range(len(A))?
print("\n\n❌ EJEMPLO 2: ¿Por qué NO usamos range(len(A))?")
print("-" * 80)
print(f"Array: {A}")
print(f"Si usáramos range(len(A)) = range({len(A)}) = {list(range(len(A)))}")
print("\n⚠️  Problema: Intentaría acceder a índices fuera de rango:")

for i in range(len(A)):
    if i + 2 < len(A):
        print(f"  i={i}: A[{i}], A[{i+1}], A[{i+2}] → {A[i]}, {A[i+1]}, {A[i+2]} ✓ OK")
    else:
        print(f"  i={i}: A[{i}], A[{i+1}], A[{i+2}] → ❌ ERROR! A[{i+2}] no existe (índice fuera de rango)")

# Ejemplo 3: Edge cases
print("\n\n📏 EJEMPLO 3: Edge cases - Arrays pequeños")
print("-" * 80)

test_cases = [
    [],
    [5],
    [3, 4],
    [3, 4, 5],
]

for A in test_cases:
    print(f"\nArray: {A if A else '[]'} (longitud {len(A)})")
    print(f"  range(len(A) - 2) = range({len(A) - 2}) = {list(range(len(A) - 2))}")
    if len(A) < 3:
        print(f"  → Sin triplets posibles (necesitamos mínimo 3 elementos)")
    else:
        print(f"  → Triplets a verificar:")
        for i in range(len(A) - 2):
            print(f"     i={i}: [{A[i]}, {A[i+1]}, {A[i+2]}]")

# Ejemplo 4: Visualización completa
print("\n\n🎨 EJEMPLO 4: Visualización con array grande")
print("-" * 80)
A = [1, 2, 3, 5, 8, 13, 21]
print(f"Array: {A}")
print(f"Longitud: {len(A)}")
print()

print("Índices del array:")
print("  ", end="")
for i in range(len(A)):
    print(f"[{i}]  ", end="")
print()

print("Valores del array:")
print("  ", end="")
for val in A:
    print(f" {val:2}  ", end="")
print("\n")

print("Triplets consecutivos verificados:")
for i in range(len(A) - 2):
    print(f"  i={i}: ", end="")
    # Visualizar con flechas
    for j in range(len(A)):
        if j == i:
            print("▼", end="   ")
        elif j == i + 1:
            print("▼", end="   ")
        elif j == i + 2:
            print("▼", end="   ")
        else:
            print(" ", end="   ")
    print(f" → [{A[i]}, {A[i+1]}, {A[i+2]}]")

# Ejemplo 5: Comparación de diferentes ranges
print("\n\n📊 EJEMPLO 5: Comparación de diferentes enfoques")
print("-" * 80)
A = [10, 20, 30, 40]
print(f"Array: {A} (longitud {len(A)})")
print()

approaches = [
    ("range(len(A))", len(A), "❌ Error: accede a índices no existentes"),
    ("range(len(A) - 1)", len(A) - 1, "❌ Error: accede a A[i+2] no existente"),
    ("range(len(A) - 2)", len(A) - 2, "✓ Correcto: todos los índices válidos"),
]

for desc, limit, status in approaches:
    print(f"{desc} = range({limit}) = {list(range(limit))}")
    print(f"  {status}")
    if limit > 0:
        print(f"  Triplets:")
        for i in range(limit):
            try:
                triplet = [A[i], A[i+1], A[i+2]]
                print(f"    i={i}: [{A[i]}, {A[i+1]}, {A[i+2]}]")
            except IndexError as e:
                print(f"    i={i}: ⚠️  IndexError: índice {i+2} fuera de rango")
    print()

# Resumen
print("\n" + "=" * 80)
print("📝 RESUMEN")
print("=" * 80)
print("""
¿Por qué range(len(A) - 2)?

  Para verificar triplets consecutivos [A[i], A[i+1], A[i+2]], necesitamos:
  
  • i puede ser: 0, 1, 2, ..., len(A) - 3
  • i+1 puede ser: 1, 2, 3, ..., len(A) - 2
  • i+2 puede ser: 2, 3, 4, ..., len(A) - 1
  
  El máximo valor de i es: len(A) - 3
  
  range(len(A) - 2) genera: 0, 1, 2, ..., len(A) - 3 ✓
  
  Ejemplo con len(A) = 5:
    range(5 - 2) = range(3) = [0, 1, 2]
    
    i=0: A[0], A[1], A[2] ✓
    i=1: A[1], A[2], A[3] ✓
    i=2: A[2], A[3], A[4] ✓  (último triplet válido)
    
    Si usáramos i=3: A[3], A[4], A[5] ❌ (A[5] no existe!)

REGLA GENERAL:
  Para acceder a A[i], A[i+1], A[i+2] de forma segura:
  → Usar range(len(A) - 2)
  
  Para acceder a A[i], A[i+1] de forma segura:
  → Usar range(len(A) - 1)
""")

print("=" * 80)
