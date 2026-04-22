# ============================================================
# EJERCICIOS — CLASE 2
# Programación funcional y OOP avanzada
# ============================================================


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa la clase `Vector` con los siguientes dunders:
#   - __init__(self, x, y)
#   - __repr__: devuelve "Vector(x, y)"
#   - __add__: suma de vectores
#   - __mul__: multiplicación por escalar (Vector * número)
#   - __abs__: módulo del vector (raíz de x²+y²)
#   - __eq__: dos vectores son iguales si tienen las mismas componentes
#
# La clase debe estar completa: no uses herencia ni módulos externos.


class Vector:
    pass  # escribe tu implementación aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa la función `pipeline(*funciones)`.
#
# Dado un número de funciones, devuelve una nueva función que
# aplica todas esas funciones en secuencia al argumento dado.
#
# Ejemplo:
#   duplicar = lambda x: x * 2
#   sumar_uno = lambda x: x + 1
#   op = pipeline(duplicar, sumar_uno)  # primero duplica, luego suma 1
#   op(5)  → 11   (5 * 2 = 10, 10 + 1 = 11)
#   op(0)  → 1
#
# Implementa `pipeline` usando functools.reduce.
# Si no se pasan funciones, devuelve una función identidad (lambda x: x).


def pipeline(*funciones):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa la clase `Pila` (stack) usando property y dunders.
#
# Una pila es una estructura LIFO (last-in, first-out).
# La clase debe tener:
#   - __init__: inicializa la pila vacía
#   - push(elemento): añade un elemento a la cima
#   - pop(): elimina y devuelve el elemento de la cima.
#             Lanza IndexError si la pila está vacía.
#   - @property cima: devuelve el elemento de la cima sin eliminarlo.
#                     Lanza IndexError si la pila está vacía.
#   - __len__: número de elementos en la pila
#   - __bool__: True si la pila tiene elementos, False si está vacía
#   - __repr__: representación legible


class Pila:
    pass  # escribe tu implementación aquí
