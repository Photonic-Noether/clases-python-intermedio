import pytest
from ejercicios.clase_5.ejercicios import Pila, ValidadorContrasena, Conversor


@pytest.fixture
def pila_vacia():
    return Pila()


@pytest.fixture
def pila_con_elementos():
    p = Pila()
    p.push(1)
    p.push(2)
    p.push(3)
    return p


@pytest.fixture
def validador_defecto():
    return ValidadorContrasena()


@pytest.fixture
def conversor():
    return Conversor()
