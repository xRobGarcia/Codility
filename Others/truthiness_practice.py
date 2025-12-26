"""
TRUTHINESS EN PYTHON - Guía de Práctica
========================================

En Python, todos los objetos tienen un valor de "verdad" (truthiness).
Pueden ser evaluados como True o False en contextos booleanos.

VALORES FALSY (se evalúan como False):
---------------------------------------
- None
- False
- 0 (cero de cualquier tipo numérico: 0, 0.0, 0j)
- '' (string vacío)
- [] (lista vacía)
- {} (diccionario vacío)
- () (tupla vacía)
- set() (conjunto vacío)
- range(0) (rango vacío)

VALORES TRUTHY (se evalúan como True):
---------------------------------------
- True
- Cualquier número diferente de cero (1, -1, 3.14, etc.)
- Cualquier string no vacío ('a', 'hello', ' ')
- Cualquier contenedor con al menos un elemento ([1], {'a': 1}, (1,))
- Objetos personalizados (por defecto, a menos que definan __bool__ o __len__)
"""

# ============================================================================
# PARTE 1: LISTAS Y EL OPERADOR 'not'
# ============================================================================

print("=" * 60)
print("PARTE 1: LISTAS Y EL OPERADOR 'not'")
print("=" * 60)

# Lista vacía es FALSY
empty_list = []
print(f"\nempty_list = {empty_list}")
print(f"bool(empty_list) = {bool(empty_list)}")  # False
print(f"not empty_list = {not empty_list}")      # True

# Lista con elementos es TRUTHY
full_list = [1, 2, 3]
print(f"\nfull_list = {full_list}")
print(f"bool(full_list) = {bool(full_list)}")    # True
print(f"not full_list = {not full_list}")        # False

# Caso práctico: Validación de entrada
def process_array(A):
    if not A:  # Si A está vacía o es None
        print("Array está vacío o es None, retornando []")
        return []
    print(f"Procesando array con {len(A)} elementos")
    return A

print("\nEjemplos de uso:")
process_array([])           # Array vacío
process_array([1, 2, 3])    # Array con datos
process_array(None)         # None también es falsy


# ============================================================================
# PARTE 2: STRINGS
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 2: STRINGS")
print("=" * 60)

empty_string = ""
non_empty_string = "hello"
space_string = " "

print(f"\nempty_string = '{empty_string}'")
print(f"bool(empty_string) = {bool(empty_string)}")      # False
print(f"not empty_string = {not empty_string}")          # True

print(f"\nnon_empty_string = '{non_empty_string}'")
print(f"bool(non_empty_string) = {bool(non_empty_string)}")  # True
print(f"not non_empty_string = {not non_empty_string}")      # False

print(f"\nspace_string = '{space_string}'")
print(f"bool(space_string) = {bool(space_string)}")      # True (tiene un espacio!)
print(f"not space_string = {not space_string}")          # False

# Validación de entrada de usuario
def validate_name(name):
    if not name:
        return "Error: El nombre no puede estar vacío"
    return f"Hola, {name}!"

print("\nEjemplos de validación:")
print(validate_name(""))           # Vacío
print(validate_name("Carlos"))     # Válido
print(validate_name(" "))          # Espacio (cuenta como válido!)


# ============================================================================
# PARTE 3: DICCIONARIOS Y CONJUNTOS
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 3: DICCIONARIOS Y CONJUNTOS")
print("=" * 60)

empty_dict = {}
full_dict = {"name": "Ana", "age": 30}
empty_set = set()
full_set = {1, 2, 3}

print(f"\nempty_dict = {empty_dict}")
print(f"bool(empty_dict) = {bool(empty_dict)}")    # False
print(f"not empty_dict = {not empty_dict}")        # True

print(f"\nfull_dict = {full_dict}")
print(f"bool(full_dict) = {bool(full_dict)}")      # True
print(f"not full_dict = {not full_dict}")          # False

print(f"\nempty_set = {empty_set}")
print(f"bool(empty_set) = {bool(empty_set)}")      # False
print(f"not empty_set = {not empty_set}")          # True

print(f"\nfull_set = {full_set}")
print(f"bool(full_set) = {bool(full_set)}")        # True
print(f"not full_set = {not full_set}")            # False


# ============================================================================
# PARTE 4: NÚMEROS
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 4: NÚMEROS")
print("=" * 60)

zero = 0
positive = 5
negative = -3
float_zero = 0.0
small_float = 0.0001

print(f"\nzero = {zero}")
print(f"bool(zero) = {bool(zero)}")                # False
print(f"not zero = {not zero}")                    # True

print(f"\npositive = {positive}")
print(f"bool(positive) = {bool(positive)}")        # True
print(f"not positive = {not positive}")            # False

print(f"\nnegative = {negative}")
print(f"bool(negative) = {bool(negative)}")        # True (números negativos son truthy!)
print(f"not negative = {not negative}")            # False

print(f"\nfloat_zero = {float_zero}")
print(f"bool(float_zero) = {bool(float_zero)}")    # False
print(f"not float_zero = {not float_zero}")        # True

print(f"\nsmall_float = {small_float}")
print(f"bool(small_float) = {bool(small_float)}")  # True
print(f"not small_float = {not small_float}")      # False


# ============================================================================
# PARTE 5: None
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 5: None")
print("=" * 60)

value = None
print(f"\nvalue = {value}")
print(f"bool(value) = {bool(value)}")              # False
print(f"not value = {not value}")                  # True
print(f"value is None = {value is None}")          # True

# Buena práctica: Usar 'is None' en lugar de 'not value' cuando verificas None específicamente
def check_value(val):
    if val is None:
        print("Valor es None específicamente")
    elif not val:
        print("Valor es falsy pero no None")
    else:
        print("Valor es truthy")

print("\nEjemplos:")
check_value(None)   # None específicamente
check_value([])     # Falsy pero no None
check_value(0)      # Falsy pero no None
check_value([1])    # Truthy


# ============================================================================
# PARTE 6: COMPARACIONES Y CONTEXTOS BOOLEANOS
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 6: COMPARACIONES Y CONTEXTOS BOOLEANOS")
print("=" * 60)

# Los valores truthy/falsy se usan automáticamente en:
# 1. Condiciones if/while
# 2. Operadores lógicos (and, or, not)
# 3. Comprensiones con filtros

# Ejemplo 1: if/while
my_list = [1, 2, 3]
if my_list:  # No necesitas 'if len(my_list) > 0'
    print(f"\nLista tiene {len(my_list)} elementos")

# Ejemplo 2: Operadores lógicos
def get_name_or_default(name):
    return name or "Anónimo"  # Si name es falsy, usa "Anónimo"

print(f"\nget_name_or_default('') = '{get_name_or_default('')}'")
print(f"get_name_or_default('Juan') = '{get_name_or_default('Juan')}'")

# Ejemplo 3: Valores por defecto
def divide(a, b):
    if not b:  # Si b es 0 (falsy)
        print("Error: División por cero")
        return None
    return a / b

print(f"\ndivide(10, 2) = {divide(10, 2)}")
print(f"divide(10, 0) = {divide(10, 0)}")


# ============================================================================
# PARTE 7: DIFERENCIAS IMPORTANTES
# ============================================================================

print("\n" + "=" * 60)
print("PARTE 7: DIFERENCIAS IMPORTANTES")
print("=" * 60)

# ¡CUIDADO! Estos casos pueden ser confusos:

# Caso 1: Lista con False vs lista vacía
list_with_false = [False]
empty_list = []

print(f"\nlist_with_false = {list_with_false}")
print(f"bool(list_with_false) = {bool(list_with_false)}")  # True (tiene un elemento!)
print(f"not list_with_false = {not list_with_false}")      # False

print(f"\nempty_list = {empty_list}")
print(f"bool(empty_list) = {bool(empty_list)}")            # False
print(f"not empty_list = {not empty_list}")                # True

# Caso 2: String "0" vs número 0
string_zero = "0"
number_zero = 0

print(f"\nstring_zero = '{string_zero}'")
print(f"bool(string_zero) = {bool(string_zero)}")          # True (es un string!)
print(f"not string_zero = {not string_zero}")              # False

print(f"\nnumber_zero = {number_zero}")
print(f"bool(number_zero) = {bool(number_zero)}")          # False
print(f"not number_zero = {not number_zero}")              # True

# Caso 3: Lista con None vs None
list_with_none = [None]
none_value = None

print(f"\nlist_with_none = {list_with_none}")
print(f"bool(list_with_none) = {bool(list_with_none)}")    # True (tiene un elemento!)
print(f"not list_with_none = {not list_with_none}")        # False

print(f"\nnone_value = {none_value}")
print(f"bool(none_value) = {bool(none_value)}")            # False
print(f"not none_value = {not none_value}")                # True


# ============================================================================
# EJERCICIOS DE PRÁCTICA
# ============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS DE PRÁCTICA")
print("=" * 60)

def test_exercise(description, result, expected):
    status = "✓" if result == expected else "✗"
    print(f"{status} {description}: {result} (esperado: {expected})")

print("\n--- Ejercicio 1: Predice el resultado ---")
# ¿Cuál será el resultado de estas expresiones?
test_exercise("not []", not [], True)
test_exercise("not [0]", not [0], False)
test_exercise("not ''", not '', True)
test_exercise("not '0'", not '0', False)
test_exercise("not 0", not 0, True)
test_exercise("not None", not None, True)
test_exercise("not {}", not {}, True)
test_exercise("not {'a': 0}", not {'a': 0}, False)

print("\n--- Ejercicio 2: Operadores lógicos ---")
# and retorna el primer falsy o el último valor
# or retorna el primer truthy o el último valor
test_exercise("[] or [1]", [] or [1], [1])
test_exercise("[1] or []", [1] or [], [1])
test_exercise("[] and [1]", [] and [1], [])
test_exercise("[1] and []", [1] and [], [])
test_exercise("'' or 'hello'", '' or 'hello', 'hello')
test_exercise("'hello' or ''", 'hello' or '', 'hello')
test_exercise("0 or 5", 0 or 5, 5)
test_exercise("5 or 0", 5 or 0, 5)

print("\n--- Ejercicio 3: Funciones de validación ---")

def validate_input(data):
    """Valida que data sea una lista no vacía de números positivos"""
    if not data:
        return False
    if not all(isinstance(x, (int, float)) for x in data):
        return False
    if not all(x > 0 for x in data):
        return False
    return True

test_exercise("validate_input([])", validate_input([]), False)
test_exercise("validate_input([1, 2, 3])", validate_input([1, 2, 3]), True)
test_exercise("validate_input([1, -2, 3])", validate_input([1, -2, 3]), False)
test_exercise("validate_input(['a'])", validate_input(['a']), False)
test_exercise("validate_input(None)", validate_input(None), False)


# ============================================================================
# RESUMEN Y MEJORES PRÁCTICAS
# ============================================================================

print("\n" + "=" * 60)
print("RESUMEN Y MEJORES PRÁCTICAS")
print("=" * 60)

print("""
1. USA 'not container' para verificar si está vacío:
   ✓ if not my_list:
   ✗ if len(my_list) == 0:

2. USA 'is None' para verificar None específicamente:
   ✓ if value is None:
   ✗ if not value:  (esto también es True para [], 0, '', etc.)

3. USA 'or' para valores por defecto:
   ✓ name = input_name or "Anónimo"
   ✗ name = input_name if input_name else "Anónimo"

4. CUIDADO con [False], [0], [None]:
   - Estas listas NO están vacías, son truthy!
   - bool([False]) == True
   - bool([0]) == True
   - bool([None]) == True

5. RECUERDA que solo estos son falsy:
   None, False, 0, 0.0, '', [], {}, (), set(), range(0)
   ¡TODO LO DEMÁS es truthy!

6. CONTEXTOS donde se usa truthiness automáticamente:
   - if/while/for condiciones
   - not, and, or operadores
   - Comprensiones con if
   - Funciones como all(), any(), filter()
""")

print("\n¡Fin de la práctica de Truthiness!")
