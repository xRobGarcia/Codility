def solution(N: int) -> int:
    """Devuelve el tamaño del *binary gap* más largo de N.

    Un *binary gap* es una secuencia máxima de ceros consecutivos que está
    *rodeada por unos* en la representación binaria de N.

    Ejemplos:
    - 9   -> 1001        -> gap = 2
    - 20  -> 10100       -> gap = 1 (los ceros finales NO cuentan)
    - 32  -> 100000      -> gap = 0 (solo ceros finales)

    Enfoque (sin convertir a string):
    - Recorremos los bits de N de derecha a izquierda (dividiendo entre 2 o
      usando operaciones bit a bit).
    - Ignoramos ceros iniciales (en realidad: ceros *al final* de la forma binaria)
      hasta ver el primer '1'.
    - A partir de ese primer '1', contamos ceros consecutivos.
      Cada vez que encontramos un '1', cerramos un gap y actualizamos el máximo.

    Complejidad:
    - Tiempo:  O(log N) (se procesa un bit por iteración)
    - Espacio: O(1)
    """

    # 1) Saltar ceros finales (en binario): mientras el bit menos significativo sea 0
    #    Ej: 20 (10100) -> eliminamos los dos 0 del final antes de empezar a contar gaps.
    while N > 0 and (N & 1) == 0:
        N >>= 1

    max_gap = 0
    current_gap = 0

    # 2) Recorrer bits restantes
    #    Invariante: ya hemos visto al menos un '1' antes de empezar el bucle,
    #    por lo que ahora los ceros que contemos sí pueden formar un gap.
    while N > 0:
        if (N & 1) == 0:
            # Estamos dentro de un posible gap
            current_gap += 1
        else:
            # Encontramos un '1': cerramos el gap actual
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0

        N >>= 1

    return max_gap


if __name__ == "__main__":
    tests = [
        (9, 2),
        (529, 4),
        (20, 1),
        (15, 0),
        (32, 0),
        (1041, 5),
        (1, 0),
        (6, 0),   # 110
        (10, 1),  # 1010
    ]

    for n, expected in tests:
        got = solution(n)
        print(f"N={n:<5} bin={bin(n)[2:]:<12} gap={got} (expected {expected})")
        assert got == expected
