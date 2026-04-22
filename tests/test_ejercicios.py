import pytest
from ejercicios import Pila, ValidadorContrasena, Conversor


# ── Tests de Pila ─────────────────────────────────────────────

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

def test_pila_push_pop(pila_vacia):
    pila_vacia.push(10)
    pila_vacia.push(20)
    assert pila_vacia.pop() == 20
    assert pila_vacia.pop() == 10

def test_pila_peek(pila_con_elementos):
    assert pila_con_elementos.peek() == 3
    assert len(pila_con_elementos) == 3  # peek no elimina

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

@pytest.fixture
def validador_defecto():
    return ValidadorContrasena()

@pytest.mark.parametrize("contrasena, esperado", [
    ("MiPass123", True),
    ("abc", False),              # muy corta
    ("mipassword1", False),      # sin mayúscula
    ("MIPASSWORD1", True),
    ("MiPass", False),           # sin número
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
    v = ValidadorContrasena(requiere_mayuscula=False)
    assert v.validar("minombre123") is True


# ── Tests de Conversor ────────────────────────────────────────

@pytest.fixture
def conversor():
    return Conversor()

def test_km_a_millas(conversor):
    assert abs(conversor.km_a_millas(1) - 0.621371) < 0.0001

def test_millas_a_km(conversor):
    assert abs(conversor.millas_a_km(1) - 1.60934) < 0.001

def test_kg_a_libras(conversor):
    assert abs(conversor.kg_a_libras(1) - 2.20462) < 0.0001

def test_celsius_a_fahrenheit(conversor):
    assert conversor.celsius_a_fahrenheit(0) == 32.0
    assert conversor.celsius_a_fahrenheit(100) == 212.0

def test_fahrenheit_a_celsius(conversor):
    assert conversor.fahrenheit_a_celsius(32) == 0.0
    assert conversor.fahrenheit_a_celsius(212) == 100.0

def test_km_negativo_lanza_error(conversor):
    with pytest.raises(ValueError):
        conversor.km_a_millas(-1)
