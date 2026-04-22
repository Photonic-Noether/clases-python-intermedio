# ============================================================
# EJERCICIOS — CLASE 4
# Closures, callbacks, memoization y decoradores
# ============================================================


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa el decorador `retry(max_intentos, excepcion)`.
#
# Cuando una función decorada lanza `excepcion`, el decorador
# la reintenta automáticamente hasta `max_intentos` veces.
# Si tras todos los intentos sigue fallando, relanza la excepción.
# Debe preservar el nombre y docstring de la función original.
#
# Ejemplo de uso:
#   @retry(max_intentos=3, excepcion=ValueError)
#   def mi_funcion(): ...
#
# Si en el intento 2 tiene éxito, devuelve el resultado normalmente.
# Si falla 3 veces, relanza el ValueError.


def retry(max_intentos: int = 3, excepcion: type = Exception):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa el decorador `log_llamadas`.
#
# Cada vez que se llama a la función decorada, registra en una
# lista global REGISTRO una entrada con:
#   {"funcion": nombre, "args": args, "kwargs": kwargs, "resultado": resultado}
#
# La función debe seguir devolviendo su resultado normal.
# El decorador debe preservar el nombre y docstring originales.
#
# Tras las llamadas, el desarrollador puede inspeccionar REGISTRO.

REGISTRO = []

def log_llamadas(func):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa `hacer_multiplicador(factor)`.
#
# Devuelve una función que multiplica su argumento por `factor`.
# La función devuelta debe ser una closure: no uses clases ni
# variables globales.
#
# Después implementa `componer(f, g)`, que devuelve una nueva
# función h tal que h(x) == f(g(x)).
#
# Ejemplos:
#   doble = hacer_multiplicador(2)
#   triple = hacer_multiplicador(3)
#   doble(5)      → 10
#   triple(5)     → 15
#   seis_veces = componer(doble, triple)
#   seis_veces(4) → 24   (triple(4)=12, doble(12)=24)


def hacer_multiplicador(factor: float):
    pass  # escribe tu implementación aquí


def componer(f, g):
    pass  # escribe tu implementación aquí
