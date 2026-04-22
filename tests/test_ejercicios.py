import json
import time
import pytest
from datetime import datetime
from ejercicios import cronometro, EncoderPersonalizado, Repositorio, RepositorioMemoria


# ── Tests de cronometro ───────────────────────────────────────

def test_cronometro_mide_tiempo():
    with cronometro() as t:
        time.sleep(0.1)
    assert t.segundos is not None
    assert t.segundos >= 0.05  # al menos algo de tiempo


def test_cronometro_segundos_antes_de_salir():
    with cronometro() as t:
        dentro = t.segundos  # antes de salir del bloque
    assert dentro is None  # dentro del bloque, aún no hay valor
    assert t.segundos is not None  # fuera, sí lo hay


# ── Tests de EncoderPersonalizado ─────────────────────────────

def test_encoder_datetime():
    fecha = datetime(2025, 6, 15, 10, 30, 0)
    resultado = json.dumps({"fecha": fecha}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["fecha"] == "2025-06-15T10:30:00"


def test_encoder_set():
    resultado = json.dumps({"tags": {3, 1, 2}}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["tags"] == [1, 2, 3]  # ordenado


def test_encoder_bytes():
    resultado = json.dumps({"datos": b"hola"}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["datos"] == "hola"


def test_encoder_tipo_invalido():
    class NoSerializable:
        pass
    with pytest.raises(TypeError):
        json.dumps({"x": NoSerializable()}, cls=EncoderPersonalizado)


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
