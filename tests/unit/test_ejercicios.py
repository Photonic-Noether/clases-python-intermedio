import pytest
from ejercicios.clase_2.ejercicios import Vector, pipeline, Pila


# ── Tests de Vector ───────────────────────────────────────────

def test_vector_repr():
    assert repr(Vector(1, 2)) == "Vector(1, 2)"


def test_vector_suma():
    v = Vector(1, 2) + Vector(3, 4)
    assert v == Vector(4, 6)


def test_vector_multiplicacion_escalar():
    v = Vector(2, 3) * 4
    assert v == Vector(8, 12)


def test_vector_abs():
    assert abs(Vector(3, 4)) == 5.0
    assert abs(Vector(0, 0)) == 0.0


def test_vector_igualdad():
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(1, 3)


# ── Tests de pipeline ─────────────────────────────────────────

def test_pipeline_una_funcion():
    doble = pipeline(lambda x: x * 2)
    assert doble(5) == 10


def test_pipeline_dos_funciones():
    op = pipeline(lambda x: x * 2, lambda x: x + 1)
    assert op(5) == 11


def test_pipeline_sin_funciones():
    identidad = pipeline()
    assert identidad(42) == 42
    assert identidad("hola") == "hola"


def test_pipeline_tres_funciones():
    op = pipeline(lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
    assert op(5) == 5


# ── Tests de Pila ─────────────────────────────────────────────

def test_pila_push_pop():
    p = Pila()
    p.push(1)
    p.push(2)
    assert p.pop() == 2
    assert p.pop() == 1


def test_pila_cima():
    p = Pila()
    p.push("hola")
    assert p.cima == "hola"
    p.push("mundo")
    assert p.cima == "mundo"


def test_pila_vacia_error():
    p = Pila()
    with pytest.raises(IndexError):
        p.pop()
    with pytest.raises(IndexError):
        _ = p.cima


def test_pila_len_bool():
    p = Pila()
    assert len(p) == 0
    assert not p
    p.push(10)
    assert len(p) == 1
    assert p
