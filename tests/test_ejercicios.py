import threading
import time
import pytest
from ejercicios import ContadorThread, ProductorConsumidor, temporizador


# ── Tests de ContadorThread ───────────────────────────────────

def test_contador_valor_inicial():
    c = ContadorThread()
    assert c.valor == 0

def test_contador_valor_inicial_personalizado():
    c = ContadorThread(100)
    assert c.valor == 100

def test_contador_incrementar():
    c = ContadorThread()
    c.incrementar()
    assert c.valor == 1
    c.incrementar(5)
    assert c.valor == 6

def test_contador_decrementar():
    c = ContadorThread(10)
    c.decrementar(3)
    assert c.valor == 7

def test_contador_thread_safe():
    c = ContadorThread()
    hilos = [threading.Thread(target=lambda: [c.incrementar() for _ in range(1000)])
             for _ in range(10)]
    for h in hilos: h.start()
    for h in hilos: h.join()
    assert c.valor == 10000

def test_contador_resetear():
    c = ContadorThread(50)
    c.resetear()
    assert c.valor == 0


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
