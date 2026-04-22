# ============================================================
# EJERCICIOS — CLASE 6
# Librería estándar 1 + Type hinting y genéricos
# ============================================================

from typing import TypeVar, Generic

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa la clase genérica `Cola[T]` (queue — estructura FIFO).
#
# Una cola es FIFO: el primero en entrar es el primero en salir.
# Usa `typing.Generic[T]` para que sea type-safe.
#
# Métodos:
#   - encolar(elemento: T): añade al final
#   - desencolar() -> T: elimina y devuelve el primero. IndexError si vacía.
#   - primero() -> T: devuelve el primero sin eliminar. IndexError si vacía.
#   - __len__() -> int
#   - __bool__() -> bool  (False si vacía)
#
# Usa collections.deque internamente para tener O(1) en ambos extremos.


class Cola(Generic[T]):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa `frecuencia_palabras(texto)` usando Counter.
#
# Dado un texto (string), devuelve un dict con la frecuencia de
# cada palabra, ignorando mayúsculas/minúsculas y signos de puntuación
# (.,;:!?'"-()).
#
# Ejemplos:
#   frecuencia_palabras("Hola mundo, hola Python.")
#   → {"hola": 2, "mundo": 1, "python": 1}
#
# Usa Counter internamente.


def frecuencia_palabras(texto: str) -> dict[str, int]:
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa la clase genérica `Repositorio[T]`.
#
# Un repositorio almacena objetos y permite buscarlos.
# Los objetos deben tener un atributo `id` (usa Protocol o asúmelo).
#
# Métodos:
#   - guardar(elemento: T): almacena el elemento por su id
#   - obtener(id) -> T | None: devuelve el elemento con ese id, o None
#   - todos() -> list[T]: devuelve todos los elementos
#   - eliminar(id) -> bool: elimina el elemento, devuelve True si existía
#   - __len__() -> int: número de elementos almacenados


class Repositorio(Generic[T]):
    pass  # escribe tu implementación aquí
