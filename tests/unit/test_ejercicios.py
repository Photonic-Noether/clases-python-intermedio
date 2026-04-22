import json
import time
import pytest
from datetime import datetime
from ejercicios.clase_8.ejercicios import cronometro, EncoderPersonalizado


# ── Tests de cronometro ───────────────────────────────────────

def test_cronometro_mide_tiempo():
    with cronometro() as t:
        time.sleep(0.1)
    assert t.segundos is not None
    assert t.segundos >= 0.05


def test_cronometro_segundos_antes_de_salir():
    with cronometro() as t:
        dentro = t.segundos
    assert dentro is None
    assert t.segundos is not None


# ── Tests de EncoderPersonalizado ─────────────────────────────

def test_encoder_datetime():
    fecha = datetime(2025, 6, 15, 10, 30, 0)
    resultado = json.dumps({"fecha": fecha}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["fecha"] == "2025-06-15T10:30:00"


def test_encoder_set():
    resultado = json.dumps({"tags": {3, 1, 2}}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["tags"] == [1, 2, 3]


def test_encoder_bytes():
    resultado = json.dumps({"datos": b"hola"}, cls=EncoderPersonalizado)
    datos = json.loads(resultado)
    assert datos["datos"] == "hola"


def test_encoder_tipo_invalido():
    class NoSerializable:
        pass
    with pytest.raises(TypeError):
        json.dumps({"x": NoSerializable()}, cls=EncoderPersonalizado)
