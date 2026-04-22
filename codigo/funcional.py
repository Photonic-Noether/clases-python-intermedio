"""Ejemplos de programación funcional: map, filter, reduce, partial."""
from functools import reduce, partial


def aplicar_a_todos(funcion, iterable):
    """Equivalente a map, pero devuelve una lista."""
    return list(map(funcion, iterable))


def filtrar(predicado, iterable):
    """Equivalente a filter, pero devuelve una lista."""
    return list(filter(predicado, iterable))


def acumular(funcion, iterable, inicial=None):
    """Reduce el iterable a un único valor."""
    if inicial is None:
        return reduce(funcion, iterable)
    return reduce(funcion, iterable, inicial)


def componer(*funciones):
    """Compone funciones de derecha a izquierda: componer(f, g)(x) == f(g(x))."""
    def aplicar(x):
        for f in reversed(funciones):
            x = f(x)
        return x
    return aplicar


if __name__ == "__main__":
    numeros = range(1, 11)
    print("Cuadrados de pares:", aplicar_a_todos(lambda x: x**2, filtrar(lambda x: x % 2 == 0, numeros)))
    suma_total = acumular(lambda a, b: a + b, numeros)
    print("Suma 1..10:", suma_total)
