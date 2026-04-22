import threading
import pytest
from ejercicios.clase_7.ejercicios import ContadorThread


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
    hilos = [
        threading.Thread(target=lambda: [c.incrementar() for _ in range(1000)])
        for _ in range(10)
    ]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
    assert c.valor == 10000


def test_contador_resetear():
    c = ContadorThread(50)
    c.resetear()
    assert c.valor == 0
