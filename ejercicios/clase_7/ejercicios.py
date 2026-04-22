# ============================================================
# EJERCICIOS — CLASE 7
# Concurrencia básica: Hilos
# ============================================================

import threading
import queue
import time


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa `ContadorThread`.
#
# Una clase que gestiona un contador que puede ser incrementado
# de forma segura desde múltiples hilos simultáneamente.
#
# Métodos:
#   - __init__(valor_inicial=0)
#   - incrementar(cantidad=1): suma `cantidad` al contador
#   - decrementar(cantidad=1): resta `cantidad` al contador
#   - valor (property): devuelve el valor actual
#   - resetear(): pone el valor a 0
#
# IMPORTANTE: los métodos deben ser thread-safe (usa threading.Lock).
#
# Prueba: si 10 hilos llaman a incrementar() 1000 veces cada uno,
# el valor final debe ser exactamente 10000.


class ContadorThread:
    pass  # escribe tu implementación aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa el productor-consumidor `ProductorConsumidor`.
#
# La clase gestiona un pool de tareas entre un productor y múltiples
# consumidores usando queue.Queue.
#
# Métodos:
#   - __init__(num_consumidores: int = 2)
#   - producir(tarea): añade una tarea a la cola
#   - iniciar(): arranca los hilos consumidores
#   - esperar(): bloquea hasta que todas las tareas estén procesadas
#   - resultados: lista con los resultados procesados
#
# Las "tareas" son callables sin argumentos.
# Los consumidores deben ejecutarlas y guardar el resultado.
# Usa una cola con centinela (None) para señalizar el fin.


class ProductorConsumidor:
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa `temporizador(segundos, funcion, *args)`.
#
# Ejecuta `funcion(*args)` en un hilo separado tras esperar `segundos`.
# Devuelve un objeto con un método `cancelar()` que impide la ejecución
# si se llama antes de que pase el tiempo.
#
# Ejemplo:
#   t = temporizador(2.0, print, "¡Han pasado 2 segundos!")
#   # Si llamamos t.cancelar() antes de 2s, print no se ejecuta
#   # Si esperamos 2s, print se ejecuta en un hilo separado
#
# Usa threading.Event para la señal de cancelación.


def temporizador(segundos: float, funcion, *args):
    pass  # escribe tu implementación aquí
    # debe devolver un objeto con método cancelar()
