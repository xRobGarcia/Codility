"""
PRÁCTICA: LIST, TUPLE, SET Y OTRAS COLECCIONES EN PYTHON
========================================================

Este script muestra las diferencias principales entre:
- list
- tuple
- set
- dict
- range
- frozenset

Idea clave:
- list: ordenada, mutable, permite duplicados
- tuple: ordenada, inmutable, permite duplicados
- set: sin orden garantizado, mutable, no permite duplicados
- dict: pares clave-valor, mutable, claves únicas
- range: secuencia inmutable de enteros generada bajo demanda
- frozenset: set inmutable
"""

print("=" * 70)
print("PARTE 1: CREACIÓN BÁSICA")
print("=" * 70)

my_list = [10, 20, 20, 30]
my_tuple = (10, 20, 20, 30)
my_set = {10, 20, 20, 30}
my_dict = {"name": "Ana", "age": 30, "city": "CDMX"}
my_range = range(1, 6)
my_frozenset = frozenset([10, 20, 20, 30])

print(f"list      = {my_list}")
print(f"tuple     = {my_tuple}")
print(f"set       = {my_set}")
print(f"dict      = {my_dict}")
print(f"range     = {my_range}")
print(f"frozenset = {my_frozenset}")


print("\n" + "=" * 70)
print("PARTE 2: DUPLICADOS")
print("=" * 70)

print("\nlist guarda duplicados:")
print(my_list)

print("\ntuple también guarda duplicados:")
print(my_tuple)

print("\nset elimina duplicados automáticamente:")
print(my_set)

print("\nfrozenset también elimina duplicados:")
print(my_frozenset)


print("\n" + "=" * 70)
print("PARTE 3: MUTABILIDAD")
print("=" * 70)

print("\nlist es mutable:")
nums = [1, 2, 3]
print(f"Antes: {nums}")
nums.append(4)
nums[0] = 99
print(f"Después: {nums}")

print("\ntuple es inmutable:")
coords = (5, 8)
print(f"Tuple original: {coords}")
print("No puedes hacer coords[0] = 99 porque lanza TypeError")

print("\nset es mutable:")
tags = {"python", "sql"}
print(f"Antes: {tags}")
tags.add("bash")
print(f"Después: {tags}")

print("\nfrozenset es inmutable:")
frozen_tags = frozenset(["python", "sql"])
print(f"frozenset: {frozen_tags}")
print("No puedes hacer add() ni remove() sobre frozenset")

print("\ndict es mutable:")
user = {"name": "Luis", "age": 25}
print(f"Antes: {user}")
user["age"] = 26
user["role"] = "admin"
print(f"Después: {user}")


print("\n" + "=" * 70)
print("PARTE 4: ACCESO POR ÍNDICE")
print("=" * 70)

letters_list = ["a", "b", "c"]
letters_tuple = ("a", "b", "c")
letters_set = {"a", "b", "c"}

print(f"letters_list[1]  = {letters_list[1]}")
print(f"letters_tuple[1] = {letters_tuple[1]}")
print("set no tiene acceso por índice: letters_set[1] da error")


print("\n" + "=" * 70)
print("PARTE 5: ORDEN")
print("=" * 70)

ordered_list = [3, 1, 2]
ordered_tuple = (3, 1, 2)
unordered_set = {3, 1, 2}

print(f"list mantiene orden de inserción:  {ordered_list}")
print(f"tuple mantiene orden de inserción: {ordered_tuple}")
print(f"set no garantiza orden lógico:     {unordered_set}")


print("\n" + "=" * 70)
print("PARTE 6: USOS TÍPICOS")
print("=" * 70)

print("\nCuándo usar list:")
print("- Cuando necesitas modificar elementos")
print("- Cuando importa el orden")
print("- Cuando pueden existir repetidos")

print("\nCuándo usar tuple:")
print("- Cuando los datos no deben cambiar")
print("- Para coordenadas, fechas, registros fijos")

print("\nCuándo usar set:")
print("- Para eliminar duplicados")
print("- Para membership rápido: x in my_set")
print("- Para operaciones de conjuntos")

print("\nCuándo usar dict:")
print("- Para guardar datos con nombre")
print("- Para búsquedas por clave")
print("- Para representar objetos simples")

print("\nCuándo usar range:")
print("- Para iterar secuencias numéricas")
print("- Para no crear listas grandes innecesarias")

print("\nCuándo usar frozenset:")
print("- Cuando quieres un set que no cambie")
print("- Cuando necesitas usar un conjunto como clave o valor seguro")


print("\n" + "=" * 70)
print("PARTE 7: MEMBERSHIP - OPERADOR in")
print("=" * 70)

print(f"20 in my_list      -> {20 in my_list}")
print(f"20 in my_tuple     -> {20 in my_tuple}")
print(f"20 in my_set       -> {20 in my_set}")
print(f"'name' in my_dict  -> {'name' in my_dict}")
print(f"3 in my_range      -> {3 in my_range}")
print(f"20 in my_frozenset -> {20 in my_frozenset}")

print("\nEn dict, 'in' busca claves, no valores:")
print(f"'Ana' in my_dict -> {'Ana' in my_dict}")


print("\n" + "=" * 70)
print("PARTE 8: CONVERSIONES ÚTILES")
print("=" * 70)

data = [1, 2, 2, 3, 3, 3]
print(f"\nLista original: {data}")
print(f"tuple(data)     -> {tuple(data)}")
print(f"set(data)       -> {set(data)}")
print(f"list(set(data)) -> {list(set(data))}")
print(f"frozenset(data) -> {frozenset(data)}")


print("\n" + "=" * 70)
print("PARTE 9: OPERACIONES EXCLUSIVAS DE set")
print("=" * 70)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"a = {a}")
print(f"b = {b}")
print(f"a | b  (unión)         = {a | b}")
print(f"a & b  (intersección)  = {a & b}")
print(f"a - b  (diferencia)    = {a - b}")
print(f"a ^ b  (simétrica)     = {a ^ b}")


print("\n" + "=" * 70)
print("PARTE 10: COLECCIONES ANIDADAS")
print("=" * 70)

nested_data = [
  {
    "name": "Ana",
    "skills": ["python", "sql"],
    "scores": (95, 88, 91),
    "tags": {"backend", "api"},
  },
  {
    "name": "Luis",
    "skills": ["bash", "git"],
    "prefs": {"theme": "light", "alerts": True},
  },
]

print("\nSí se pueden anidar distintos tipos de colecciones:")
print(nested_data)

print("\nAcceso a datos anidados:")
print(f"Primer nombre:           {nested_data[0]['name']}")
print(f"Segunda skill de Ana:    {nested_data[0]['skills'][1]}")
print(f"Primer score de Ana:     {nested_data[0]['scores'][0]}")
print(f"Preferencia de tema:     {nested_data[1]['prefs']['theme']}")

good_dict = {(1, 2): "punto"}
good_set = {("python", "sql"), ("bash", "git")}

print("\nTambién puedes usar tuplas dentro de dict y set:")
print(f"good_dict = {good_dict}")
print(f"good_set  = {good_set}")

print("\nRestricción importante:")
print("set y las claves de dict solo aceptan elementos hashables")

try:
  {[1, 2]: "valor"}
except TypeError as exc:
  print(f"list como clave de dict falla: {exc}")

try:
  {[1, 2], [3, 4]}
except TypeError as exc:
  print(f"list dentro de set falla:      {exc}")


print("\n" + "=" * 70)
print("PARTE 11: RESUMEN RÁPIDO")
print("=" * 70)

print("""
list:
  - Mutable
  - Ordenada
  - Permite duplicados

tuple:
  - Inmutable
  - Ordenada
  - Permite duplicados

set:
  - Mutable
  - Sin duplicados
  - Sin índice

dict:
  - Mutable
  - Clave -> valor
  - Claves únicas

range:
  - Inmutable
  - Secuencia numérica eficiente

frozenset:
  - Inmutable
  - Sin duplicados
""")


print("=" * 70)
print("PARTE 12: TU TURNO")
print("=" * 70)

print("1. Crea una list con números repetidos y conviértela a set")
print("2. Crea una tuple con una coordenada (x, y)")
print("3. Crea un dict con tus datos: nombre, edad, ciudad")
print("4. Recorre un range(5, 11)")
print("5. Intenta modificar una tuple y observa el error")
print("6. Crea una list de dict con una tuple y un set dentro")