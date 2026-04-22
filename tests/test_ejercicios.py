import pytest
from ejercicios import FibonacciIterador, aplanar, ventana_deslizante


# ── Tests de FibonacciIterador ────────────────────────────────

def test_fibonacci_primeros_seis():
    assert list(FibonacciIterador(6)) == [0, 1, 1, 2, 3, 5]


def test_fibonacci_primero():
    assert list(FibonacciIterador(1)) == [0]


def test_fibonacci_cero():
    assert list(FibonacciIterador(0)) == []


def test_fibonacci_diez():
    assert list(FibonacciIterador(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_es_iterable_dos_veces():
    fib = FibonacciIterador(4)
    primero = list(fib)
    assert primero == [0, 1, 1, 2]


# ── Tests de aplanar ──────────────────────────────────────────

def test_aplanar_simple():
    assert list(aplanar([1, [2, 3], [4, [5, 6]]])) == [1, 2, 3, 4, 5, 6]


def test_aplanar_profundo():
    assert list(aplanar([[1, 2], [3, [4, [5]]]])) == [1, 2, 3, 4, 5]


def test_aplanar_plano():
    assert list(aplanar([1, 2, 3])) == [1, 2, 3]


def test_aplanar_vacio():
    assert list(aplanar([])) == []


def test_aplanar_no_aplana_strings():
    assert list(aplanar(["hola", "mundo"])) == ["hola", "mundo"]


# ── Tests de ventana_deslizante ───────────────────────────────

def test_ventana_numeros():
    assert list(ventana_deslizante([1, 2, 3, 4, 5], 3)) == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]


def test_ventana_strings():
    assert list(ventana_deslizante("abcde", 2)) == [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")]


def test_ventana_muy_grande():
    assert list(ventana_deslizante([1, 2], 3)) == []


def test_ventana_tamaño_uno():
    assert list(ventana_deslizante([1, 2, 3], 1)) == [(1,), (2,), (3,)]
