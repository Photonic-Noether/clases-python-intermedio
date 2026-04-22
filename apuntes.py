# ============================================================
# CLASE 2 — PROGRAMACIÓN FUNCIONAL Y OOP AVANZADA
# ============================================================

from functools import reduce, partial, lru_cache


# ===== PROGRAMACIÓN FUNCIONAL =====

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: aplica una función a cada elemento, devuelve un iterador
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

# filter: conserva solo los elementos que cumplen el predicado
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# sorted con key: ordena con criterio personalizado
palabras = ["banana", "kiwi", "manzana", "uva"]
por_longitud = sorted(palabras, key=len)
print("Por longitud:", por_longitud)

# any/all: comprobaciones booleanas
print(any(x > 8 for x in numeros))   # True: al menos uno > 8
print(all(x > 0 for x in numeros))   # True: todos > 0

# reduce: acumula el iterable a un único valor
producto = reduce(lambda a, b: a * b, numeros)
print("Producto de 1 a 10:", producto)

# partial: fijar argumentos de una función
def potencia(base, exponente):
    return base ** exponente

cuadrado = partial(potencia, exponente=2)
cubo = partial(potencia, exponente=3)
print("5 al cuadrado:", cuadrado(5))
print("3 al cubo:", cubo(3))

# lru_cache: caché automática (muy útil en recursión)
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fib(30):", fibonacci(30))  # rápido gracias a la caché


# ===== PROPERTY Y ATRIBUTOS GESTIONADOS =====

class Temperatura:
    def __init__(self, celsius: float):
        self._celsius = celsius  # atributo privado

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float):
        if valor < -273.15:
            raise ValueError(f"Temperatura {valor}°C por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    def __repr__(self) -> str:
        return f"Temperatura({self._celsius}°C)"

t = Temperatura(100)
print(t)
print("En Fahrenheit:", t.fahrenheit)
print("En Kelvin:", t.kelvin)
t.celsius = 0
print("Ahora:", t)


# ===== MÉTODOS DUNDER =====

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, otro: "Vector") -> "Vector":
        return Vector(self.x + otro.x, self.y + otro.y)

    def __mul__(self, escalar: float) -> "Vector":
        return Vector(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar: float) -> "Vector":
        # Permite tanto v * 3 como 3 * v
        return self.__mul__(escalar)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Vector):
            return NotImplemented
        return self.x == otro.x and self.y == otro.y

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0  # vector nulo es falsy

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * 3)
print(3 * v1)
print(abs(v2))   # 5.0


# ===== CLASSMETHOD, STATICMETHOD Y __new__ =====

class Fecha:
    def __init__(self, año: int, mes: int, dia: int):
        self.año = año
        self.mes = mes
        self.dia = dia

    @classmethod
    def desde_texto(cls, texto: str) -> "Fecha":
        # Constructor alternativo: "2025-01-15" → Fecha(2025, 1, 15)
        año, mes, dia = texto.split("-")
        return cls(int(año), int(mes), int(dia))

    @staticmethod
    def es_bisiesto(año: int) -> bool:
        # No necesita ni la clase ni la instancia: es una función de utilidad
        return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

    def __repr__(self) -> str:
        return f"Fecha({self.año}-{self.mes:02d}-{self.dia:02d})"

f = Fecha.desde_texto("2025-06-15")
print(f)
print("2024 es bisiesto:", Fecha.es_bisiesto(2024))
print("2025 es bisiesto:", Fecha.es_bisiesto(2025))


# __new__: se llama ANTES de __init__, crea el objeto
# El patrón Singleton usa __new__ para garantizar una única instancia:
class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

a = Singleton()
b = Singleton()
print("¿Son el mismo objeto?", a is b)  # True


print("\nApuntes de Clase 2 finalizados.")
