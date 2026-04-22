"""Utilidades de concurrencia con hilos."""
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, TypeVar

T = TypeVar("T")


def ejecutar_en_paralelo(funciones: list[Callable[[], T]], max_workers: int = 4) -> list[T]:
    """Ejecuta una lista de callables en paralelo y devuelve sus resultados en orden."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futuros = [executor.submit(f) for f in funciones]
        return [f.result() for f in futuros]


def ejecutar_con_timeout(funcion: Callable, timeout: float, *args):
    """
    Ejecuta una función en un hilo con timeout.
    Devuelve el resultado o lanza TimeoutError si supera el timeout.
    """
    resultado = [None]
    excepcion = [None]

    def objetivo():
        try:
            resultado[0] = funcion(*args)
        except Exception as e:
            excepcion[0] = e

    hilo = threading.Thread(target=objetivo, daemon=True)
    hilo.start()
    hilo.join(timeout=timeout)

    if hilo.is_alive():
        raise TimeoutError(f"La función no terminó en {timeout}s")
    if excepcion[0]:
        raise excepcion[0]
    return resultado[0]


class BarreraGrupal:
    """
    Barrera de sincronización: N hilos esperan hasta que todos lleguen.
    Similar a threading.Barrier pero más didáctica.
    """

    def __init__(self, participantes: int):
        self._total = participantes
        self._llegados = 0
        self._lock = threading.Lock()
        self._evento = threading.Event()

    def esperar(self):
        with self._lock:
            self._llegados += 1
            if self._llegados == self._total:
                self._evento.set()
        self._evento.wait()


if __name__ == "__main__":
    def tarea_lenta(n):
        time.sleep(0.1)
        return n ** 2

    inicio = time.perf_counter()
    resultados = ejecutar_en_paralelo([lambda n=i: tarea_lenta(n) for i in range(10)])
    fin = time.perf_counter()
    print(f"Resultados: {resultados}")
    print(f"Tiempo: {fin - inicio:.2f}s (debería ser ~0.1s, no 1s)")
