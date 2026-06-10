from math import gcd


def _strip_common(x: int, common: int, trace: bool = False) -> int:
    """
    Quita de x todos los factores primos que ya están dentro de common.

    Si al final queda algo distinto de 1, ese residuo contiene al menos un primo
    que no existe en el otro número.
    """
    while x != 1:
        d = gcd(x, common)

        if trace:
            print(f"  x={x}, gcd(x, common)={d}")

        if d == 1:
            return x

        x //= d

    return 1


def _same_primes(a: int, b: int) -> bool:
    common = gcd(a, b)

    if _strip_common(a, common) != 1:
        return False

    return _strip_common(b, common) == 1


def solution(A, B):
    """
    CommonPrimeDivisors (Codility) - Versión Detallada
    --------------------------------------------------
    Cuenta cuántos pares A[i], B[i] tienen exactamente el mismo conjunto de
    divisores primos.

    Time: O(Z * log(maxV)^2) por reducciones repetidas con gcd
    Space: O(1)

    Estrategia:
    1. Para cada par (a, b), calculamos common = gcd(a, b).
    2. Quitamos de a todos los factores que también estén en common.
    3. Quitamos de b todos los factores que también estén en common.
    4. Si ambos terminan en 1, entonces no sobraron primos exclusivos.

    ¿Por qué funciona?
    Si a y b tienen exactamente los mismos divisores primos, entonces todos esos
    primos deben aparecer dentro de gcd(a, b). Por eso basta con ir dividiendo
    por gcd(x, common) hasta que:

    - lleguemos a 1: todos sus primos estaban en common
    - o nos atasquemos con gcd = 1: quedó un primo extra

    Ejemplo 1:
      a = 15, b = 75
      common = gcd(15, 75) = 15

      Para 15:
        gcd(15, 15) = 15 -> 15 // 15 = 1

      Para 75:
        gcd(75, 15) = 15 -> 75 // 15 = 5
        gcd(5, 15) = 5 -> 5 // 5 = 1

      Ambos terminan en 1, así que sus primos son {3, 5}.

    Ejemplo 2:
      a = 10, b = 30
      common = gcd(10, 30) = 10

      Para 10:
        gcd(10, 10) = 10 -> 1

      Para 30:
        gcd(30, 10) = 10 -> 3
        gcd(3, 10) = 1 -> queda 3 sin eliminar

      Ese 3 solo existe en b, por eso los conjuntos difieren.
    """
    count = 0

    for a, b in zip(A, B):
        if _same_primes(a, b):
            count += 1

    return count


def demo_pair(a: int, b: int) -> None:
    print("\n========================================")
    print(f"Analizando par: a={a}, b={b}")
    print("========================================")

    common = gcd(a, b)
    print(f"gcd({a}, {b}) = {common}")

    print("\nReduciendo a:")
    left_rest = _strip_common(a, common, trace=True)
    print(f"Residuo final de a: {left_rest}")

    print("\nReduciendo b:")
    right_rest = _strip_common(b, common, trace=True)
    print(f"Residuo final de b: {right_rest}")

    same = left_rest == 1 and right_rest == 1
    print(f"\nMismos divisores primos: {same}")


if __name__ == "__main__":
    tests = [
        ([15, 10, 3], [75, 30, 5], 1),
        ([2, 1, 12], [4, 1, 18], 3),
        ([9, 10, 14], [5, 30, 28], 1),
    ]

    print("=== TESTS ===")
    for A, B, expected in tests:
        result = solution(A, B)
        print(f"A:        {A}")
        print(f"B:        {B}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"OK:       {result == expected}\n")

    print("=== DEMO PASO A PASO ===")
    demo_pair(15, 75)
    demo_pair(10, 30)