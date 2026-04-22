# ============================================================
# CLASE 4 — CLOSURES, CALLBACKS, MEMOIZATION Y DECORADORES
# ============================================================

import functools
import time


# ===== CLOSURES =====

# Una closure es una función que captura variables de su entorno de definición.
# Esas variables "viven" mientras la función exista, aunque el ámbito original
# ya haya terminado.

def hacer_sumador(n: int):
    def sumar(x: int) -> int:
        return x + n  # n es una "variable libre": no está en sumar(), sino en hacer_sumador()
    return sumar

sumar_5 = hacer_sumador(5)
sumar_10 = hacer_sumador(10)
print(sumar_5(3))   # 8
print(sumar_10(3))  # 13

# La función conserva n aunque hacer_sumador() ya terminó:
print(sumar_5.__closure__[0].cell_contents)   # 5

# nonlocal: modificar una variable del ámbito superior
def contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta  # sin esto, Python crearía una nueva cuenta local
        cuenta += 1
        return cuenta
    return incrementar

c = contador()
print(c(), c(), c())  # 1 2 3


# ===== CALLBACKS =====

def ordenar_por(lista, criterio):
    return sorted(lista, key=criterio)

personas = [("Ana", 30), ("Bob", 25), ("Carlos", 35)]
por_edad = ordenar_por(personas, criterio=lambda p: p[1])
print(por_edad)

# Los callbacks son funciones de primera clase: se pasan como argumentos
def aplicar_con_log(func, valor):
    print(f"Llamando a {func.__name__} con {valor}")
    resultado = func(valor)
    print(f"Resultado: {resultado}")
    return resultado

aplicar_con_log(abs, -42)


# ===== MEMOIZACIÓN =====

# Manual:
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci_lento(n):
    if n <= 1:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)

# Con lru_cache (más robusto: maneja kwargs, límite de caché, thread-safe):
@functools.lru_cache(maxsize=128)
def fibonacci_rapido(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_rapido(n - 1) + fibonacci_rapido(n - 2)

print(fibonacci_rapido(50))


# ===== DECORADORES =====

# Un decorador es simplemente una función que recibe una función y devuelve otra.
# La sintaxis @decorador es azúcar sintáctico para: f = decorador(f)

def medir_tiempo(func):
    @functools.wraps(func)  # preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta(n: int) -> int:
    return sum(range(n))

operacion_lenta(1_000_000)


# Decoradores con argumentos: función que devuelve un decorador
def reintentar(max_intentos: int = 3, excepcion: type = Exception):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(1, max_intentos + 1):
                try:
                    return func(*args, **kwargs)
                except excepcion as e:
                    if intento == max_intentos:
                        raise
                    print(f"Intento {intento} fallido: {e}. Reintentando...")
        return wrapper
    return decorador

@reintentar(max_intentos=3, excepcion=ValueError)
def operacion_poco_fiable(x):
    import random
    if random.random() < 0.7:
        raise ValueError("falló")
    return x * 2


# Decorador basado en clase (útil cuando el decorador necesita estado)
class Contador:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.llamadas = 0

    def __call__(self, *args, **kwargs):
        self.llamadas += 1
        return self.func(*args, **kwargs)

@Contador
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"

saludar("Ana")
saludar("Bob")
print(f"saludar fue llamada {saludar.llamadas} veces")


# ===== PATRÓN FÁBRICA =====

class Animal:
    def hablar(self) -> str: ...

class Perro(Animal):
    def hablar(self) -> str: return "¡Guau!"

class Gato(Animal):
    def hablar(self) -> str: return "¡Miau!"

class Pajaro(Animal):
    def hablar(self) -> str: return "¡Pío!"

def fabrica_animal(tipo: str) -> Animal:
    animales = {"perro": Perro, "gato": Gato, "pájaro": Pajaro}
    if tipo not in animales:
        raise ValueError(f"Tipo desconocido: {tipo!r}")
    return animales[tipo]()

animal = fabrica_animal("gato")
print(animal.hablar())


print("\nApuntes de Clase 4 finalizados.")
