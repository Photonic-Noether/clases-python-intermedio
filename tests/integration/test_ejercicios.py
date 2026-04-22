import time
import pytest
from ejercicios.clase_7.ejercicios import ProductorConsumidor, temporizador


# ── Tests de ProductorConsumidor ──────────────────────────────

def test_productor_consumidor_basico():
    pc = ProductorConsumidor(num_consumidores=2)
    pc.iniciar()
    pc.producir(lambda: 1 + 1)
    pc.producir(lambda: 2 * 3)
    pc.esperar()
    assert 2 in pc.resultados
    assert 6 in pc.resultados


def test_productor_consumidor_muchas_tareas():
    pc = ProductorConsumidor(num_consumidores=4)
    pc.iniciar()
    for i in range(20):
        pc.producir(lambda n=i: n * 2)
    pc.esperar()
    assert len(pc.resultados) == 20


# ── Tests de temporizador ─────────────────────────────────────

def test_temporizador_ejecuta():
    resultados = []
    t = temporizador(0.1, resultados.append, "hecho")
    time.sleep(0.3)
    assert "hecho" in resultados


def test_temporizador_cancelar():
    resultados = []
    t = temporizador(0.5, resultados.append, "no_debe_aparecer")
    t.cancelar()
    time.sleep(0.7)
    assert "no_debe_aparecer" not in resultados
