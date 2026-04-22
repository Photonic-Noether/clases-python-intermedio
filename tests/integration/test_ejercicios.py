import pytest
from ejercicios.clase_8.ejercicios import Repositorio, RepositorioMemoria


# ── Tests de RepositorioMemoria ───────────────────────────────

class EntidadMock:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


def test_repositorio_es_abc():
    assert issubclass(RepositorioMemoria, Repositorio)


def test_repositorio_guardar_obtener():
    repo = RepositorioMemoria()
    e = EntidadMock(1, "test")
    repo.guardar(e)
    assert repo.obtener(1) is e


def test_repositorio_obtener_no_existe():
    repo = RepositorioMemoria()
    assert repo.obtener(999) is None


def test_repositorio_todos():
    repo = RepositorioMemoria()
    repo.guardar(EntidadMock(1, "A"))
    repo.guardar(EntidadMock(2, "B"))
    assert len(repo.todos()) == 2


def test_repositorio_eliminar():
    repo = RepositorioMemoria()
    repo.guardar(EntidadMock(1, "X"))
    assert repo.eliminar(1) is True
    assert repo.obtener(1) is None
    assert repo.eliminar(1) is False
