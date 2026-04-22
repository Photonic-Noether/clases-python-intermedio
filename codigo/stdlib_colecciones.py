"""Ejemplos de uso de collections: Counter, defaultdict, deque, namedtuple."""
from collections import Counter, defaultdict, deque, namedtuple


def top_n(iterable, n: int) -> list[tuple]:
    """Devuelve los n elementos más frecuentes del iterable."""
    return Counter(iterable).most_common(n)


def agrupar_por(iterable, clave) -> dict:
    """Agrupa elementos del iterable por el resultado de la función clave."""
    grupos = defaultdict(list)
    for elemento in iterable:
        grupos[clave(elemento)].append(elemento)
    return dict(grupos)


def ventana_circular(iterable, tamaño: int) -> deque:
    """Mantiene una ventana de los últimos `tamaño` elementos."""
    ventana = deque(maxlen=tamaño)
    for elemento in iterable:
        ventana.append(elemento)
    return ventana


Registro = namedtuple("Registro", ["id", "nombre", "valor"])


if __name__ == "__main__":
    palabras = "el gato y el perro y el gato".split()
    print("Top 2:", top_n(palabras, 2))

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Pares/impares:", agrupar_por(numeros, lambda x: "par" if x % 2 == 0 else "impar"))

    print("Últimos 3:", ventana_circular(range(10), 3))
