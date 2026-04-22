import pytest
from ejercicios.clase_5.ejercicios import Pila, ValidadorContrasena


# ── Tests de Pila ─────────────────────────────────────────────

def test_pila_push_pop(pila_vacia):
    pila_vacia.push(10)
    pila_vacia.push(20)
    assert pila_vacia.pop() == 20
    assert pila_vacia.pop() == 10


def test_pila_peek(pila_con_elementos):
    assert pila_con_elementos.peek() == 3
    assert len(pila_con_elementos) == 3


def test_pila_is_empty(pila_vacia):
    assert pila_vacia.is_empty() is True
    pila_vacia.push(1)
    assert pila_vacia.is_empty() is False


def test_pila_pop_vacia(pila_vacia):
    with pytest.raises(IndexError):
        pila_vacia.pop()


def test_pila_peek_vacia(pila_vacia):
    with pytest.raises(IndexError):
        pila_vacia.peek()


def test_pila_len(pila_con_elementos):
    assert len(pila_con_elementos) == 3


# ── Tests de ValidadorContrasena ──────────────────────────────

@pytest.mark.parametrize("contrasena, esperado", [
    ("MiPass123", True),
    ("abc", False),
    ("mipassword1", False),
    ("MIPASSWORD1", True),
    ("MiPass", False),
])
def test_validar_parametrizado(validador_defecto, contrasena, esperado):
    assert validador_defecto.validar(contrasena) == esperado


def test_errores_vacio_si_valida(validador_defecto):
    assert validador_defecto.errores("MiPass123") == []


def test_errores_lista_no_vacia(validador_defecto):
    errores = validador_defecto.errores("abc")
    assert len(errores) > 0
    assert all(isinstance(e, str) for e in errores)


def test_validador_sin_mayuscula_requerida():
    from ejercicios.clase_5.ejercicios import ValidadorContrasena
    v = ValidadorContrasena(requiere_mayuscula=False)
    assert v.validar("minombre123") is True
