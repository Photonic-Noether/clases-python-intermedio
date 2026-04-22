import pytest
from ejercicios import Cola, frecuencia_palabras, Repositorio


# ── Tests de Cola[T] ─────────────────────────────────────────

def test_cola_encolar_desencolar():
    c: Cola[int] = Cola()
    c.encolar(1)
    c.encolar(2)
    c.encolar(3)
    assert c.desencolar() == 1  # FIFO
    assert c.desencolar() == 2


def test_cola_primero():
    c: Cola[str] = Cola()
    c.encolar("a")
    c.encolar("b")
    assert c.primero() == "a"
    assert len(c) == 2  # primero() no elimina


def test_cola_vacia_lanza_error():
    c: Cola[int] = Cola()
    with pytest.raises(IndexError):
        c.desencolar()
    with pytest.raises(IndexError):
        c.primero()


def test_cola_len_bool():
    c: Cola[int] = Cola()
    assert len(c) == 0
    assert not c
    c.encolar(42)
    assert len(c) == 1
    assert c


# ── Tests de frecuencia_palabras ──────────────────────────────

def test_frecuencia_basica():
    resultado = frecuencia_palabras("hola mundo hola")
    assert resultado == {"hola": 2, "mundo": 1}


def test_frecuencia_case_insensitive():
    resultado = frecuencia_palabras("Hola hola HOLA")
    assert resultado == {"hola": 3}


def test_frecuencia_puntuacion():
    resultado = frecuencia_palabras("Hola, mundo. ¡Hola!")
    assert resultado.get("hola", 0) == 2
    assert resultado.get("mundo", 0) == 1


def test_frecuencia_vacia():
    assert frecuencia_palabras("") == {}


# ── Tests de Repositorio[T] ───────────────────────────────────

class ProductoMock:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

def test_repositorio_guardar_obtener():
    repo: Repositorio = Repositorio()
    p = ProductoMock(1, "Manzana")
    repo.guardar(p)
    assert repo.obtener(1) is p


def test_repositorio_obtener_inexistente():
    repo = Repositorio()
    assert repo.obtener(999) is None


def test_repositorio_todos():
    repo = Repositorio()
    p1 = ProductoMock(1, "A")
    p2 = ProductoMock(2, "B")
    repo.guardar(p1)
    repo.guardar(p2)
    assert len(repo.todos()) == 2


def test_repositorio_eliminar():
    repo = Repositorio()
    p = ProductoMock(1, "X")
    repo.guardar(p)
    assert repo.eliminar(1) is True
    assert repo.obtener(1) is None
    assert repo.eliminar(1) is False


def test_repositorio_len():
    repo = Repositorio()
    assert len(repo) == 0
    repo.guardar(ProductoMock(1, "A"))
    assert len(repo) == 1
