"""Decoradores reutilizables de ejemplo."""
import functools
import time


def medir_tiempo(func):
    """Imprime cuánto tarda la función en ejecutarse."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.6f}s")
        return resultado
    return wrapper


def solo_enteros(*nombres_arg):
    """Valida que los argumentos especificados sean enteros."""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            parametros = list(inspect.signature(func).parameters.keys())
            for nombre in nombres_arg:
                idx = parametros.index(nombre)
                valor = args[idx] if idx < len(args) else kwargs.get(nombre)
                if not isinstance(valor, int):
                    raise TypeError(f"'{nombre}' debe ser int, no {type(valor).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorador


def cachear(func):
    """Memoización manual simple."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper


if __name__ == "__main__":
    @medir_tiempo
    def suma_grande(n):
        return sum(range(n))

    suma_grande(10_000_000)

    @solo_enteros("a", "b")
    def dividir(a, b):
        return a / b

    print(dividir(10, 2))
    try:
        dividir(10.5, 2)
    except TypeError as e:
        print("Error esperado:", e)
