# ============================================================
# CLASE 7 — CONCURRENCIA BÁSICA: HILOS
# ============================================================

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed


# ===== CREAR Y ARRANCAR HILOS =====

def tarea(nombre: str, duracion: float):
    print(f"[{nombre}] Empezando...")
    time.sleep(duracion)
    print(f"[{nombre}] Terminado tras {duracion}s")

# Crear un hilo: target es la función, args son sus argumentos
hilo1 = threading.Thread(target=tarea, args=("Hilo-A", 1))
hilo2 = threading.Thread(target=tarea, args=("Hilo-B", 0.5))

# start() lanza el hilo. NO espera a que termine.
hilo1.start()
hilo2.start()

# join() espera a que el hilo termine antes de continuar.
hilo1.join()
hilo2.join()
print("Los dos hilos han terminado.")


# ===== EL GIL =====
# Python tiene un GIL (Global Interpreter Lock) en CPython.
# Significa que solo un hilo ejecuta bytecode Python a la vez.
# CONSECUENCIA:
#   - Hilos NO aceleran cómputo intensivo (CPU-bound): usa multiprocessing
#   - Hilos SÍ aceleran I/O bloqueante (red, disco): mientras un hilo espera,
#     el GIL se libera y otro hilo puede ejecutar

# Ejemplo: descargar 10 URLs en paralelo es ~10x más rápido con hilos
# que hacerlo secuencialmente, aunque tengas un solo núcleo.


# ===== RACE CONDITIONS Y LOCKS =====

# Problema: dos hilos modifican la misma variable a la vez
contador_sin_lock = 0

def incrementar_sin_lock():
    global contador_sin_lock
    for _ in range(100_000):
        contador_sin_lock += 1  # no es atómica: read → modify → write

# Si dos hilos corren esto a la vez, el resultado final puede ser menor
# que 200_000 por condiciones de carrera (race condition).

# Solución: usar un Lock
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100_000):
        with lock:  # adquiere el lock; lo libera al salir (incluso con excepciones)
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(2)]
for h in hilos: h.start()
for h in hilos: h.join()
print(f"Contador final: {contador}")  # Siempre 200000 con lock


# ===== EVENTO: SEÑALIZAR ENTRE HILOS =====

listo = threading.Event()

def productor():
    time.sleep(0.5)
    print("Productor: datos listos")
    listo.set()  # señaliza que los datos están listos

def consumidor():
    print("Consumidor: esperando datos...")
    listo.wait()  # bloquea hasta que listo.set() sea llamado
    print("Consumidor: procesando datos")

threading.Thread(target=productor).start()
threading.Thread(target=consumidor).start()


# ===== PATRÓN PRODUCTOR-CONSUMIDOR CON QUEUE =====

cola: queue.Queue[int] = queue.Queue()
CENTINELA = None  # señal de fin

def productor_queue(n: int):
    for i in range(n):
        cola.put(i)
        time.sleep(0.01)
    cola.put(CENTINELA)  # señal de fin

def consumidor_queue():
    while True:
        item = cola.get()
        if item is CENTINELA:
            break
        print(f"Procesando: {item}")
        cola.task_done()

p = threading.Thread(target=productor_queue, args=(5,))
c = threading.Thread(target=consumidor_queue)
p.start(); c.start()
p.join(); c.join()


# ===== THREADPOOLEXECUTOR =====

def simular_descarga(url: str) -> str:
    time.sleep(0.1)  # simular latencia de red
    return f"Contenido de {url}"

urls = [f"https://ejemplo.com/pagina/{i}" for i in range(10)]

inicio = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as executor:
    # submit devuelve un Future; map devuelve resultados en orden
    resultados = list(executor.map(simular_descarga, urls))
fin = time.perf_counter()
print(f"10 descargas paralelas en {fin - inicio:.2f}s")
print(f"Primeros dos resultados: {resultados[:2]}")


print("\nApuntes de Clase 7 finalizados.")
