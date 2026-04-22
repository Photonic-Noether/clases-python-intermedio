# ============================================================
# EJERCICIOS — CLASE 3
# Iteradores, generadores y corrutinas
# ============================================================


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa la clase `FibonacciIterador`.
#
# Un iterador que genera los primeros `n` números de Fibonacci.
# La sucesión empieza: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Debe funcionar en un for loop y con next():
#   fib = FibonacciIterador(6)
#   list(fib) → [0, 1, 1, 2, 3, 5]
#
# Implementa __iter__ y __next__.


class FibonacciIterador:
    def __init__(self, n: int):
        pass  # escribe tu implementación aquí

    def __iter__(self):
        pass

    def __next__(self):
        pass


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa el generador `aplanar(iterable_anidado)`.
#
# Dado un iterable que puede contener otros iterables anidados
# a cualquier profundidad, yield cada elemento hoja en orden.
#
# Ejemplos:
#   list(aplanar([1, [2, 3], [4, [5, 6]]])) → [1, 2, 3, 4, 5, 6]
#   list(aplanar([[1, 2], [3, [4, [5]]]])) → [1, 2, 3, 4, 5]
#   list(aplanar([1, 2, 3])) → [1, 2, 3]
#
# Pista: los strings también son iterables, pero no debes aplanarlos.
# Usa isinstance(elemento, str) para tratarlos como hojas.
# Usa yield from para la recursión.


def aplanar(iterable_anidado):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa `ventana_deslizante(iterable, n)`.
#
# Genera tuplas de n elementos consecutivos del iterable.
# Si el iterable tiene menos de n elementos, no genera nada.
#
# Ejemplos:
#   list(ventana_deslizante([1,2,3,4,5], 3)) → [(1,2,3), (2,3,4), (3,4,5)]
#   list(ventana_deslizante("abcde", 2))     → [('a','b'),('b','c'),('c','d'),('d','e')]
#   list(ventana_deslizante([1,2], 3))        → []
#
# Implementa esto como un generador usando collections.deque.


def ventana_deslizante(iterable, n: int):
    pass  # escribe tu implementación aquí
