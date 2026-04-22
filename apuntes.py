# ============================================================
# CLASE 6 — LIBRERÍA ESTÁNDAR 1 + TYPE HINTING Y GENÉRICOS
# ============================================================

from collections import Counter, defaultdict, namedtuple, deque
from pathlib import Path
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import TypeVar, Generic


# ===== COLLECTIONS =====

# Counter: cuenta ocurrencias
texto = "banana"
conteo = Counter(texto)
print(conteo)              # Counter({'a': 3, 'n': 2, 'b': 1})
print(conteo.most_common(2))  # [('a', 3), ('n', 2)]

palabras = ["hola", "mundo", "hola", "python", "hola", "mundo"]
print(Counter(palabras).most_common(2))

# defaultdict: diccionario con valor por defecto al acceder clave inexistente
grupos = defaultdict(list)
datos = [("frutas", "manzana"), ("verduras", "zanahoria"), ("frutas", "pera")]
for categoria, item in datos:
    grupos[categoria].append(item)
print(dict(grupos))

# namedtuple: tupla inmutable con campos nombrados
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print(p.x, p.y)
print(p._asdict())  # {'x': 3, 'y': 4}

# deque: cola doblemente enlazada, append/appendleft en O(1)
cola = deque(maxlen=3)  # cola de tamaño máximo 3
for i in range(5):
    cola.append(i)
print(cola)  # deque([2, 3, 4], maxlen=3)


# ===== PATHLIB =====

# pathlib es la forma moderna de manejar rutas en Python.
# Funciona igual en Windows (\) y Unix (/) porque Path abstrae el separador.

ruta = Path("datos") / "archivo.txt"  # operador / para unir partes
print(ruta)              # datos/archivo.txt o datos\archivo.txt en Windows
print(ruta.suffix)       # .txt
print(ruta.stem)         # archivo
print(ruta.parent)       # datos

# Crear directorio y escribir archivo:
# ruta.parent.mkdir(parents=True, exist_ok=True)
# ruta.write_text("contenido", encoding="utf-8")
# contenido = ruta.read_text(encoding="utf-8")

# Buscar archivos con glob:
# archivos_py = list(Path(".").glob("**/*.py"))  # todos los .py recursivamente


# ===== ENUM =====

class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

class Direccion(Enum):
    NORTE = auto()
    SUR = auto()
    ESTE = auto()
    OESTE = auto()

print(Color.ROJO)           # Color.ROJO
print(Color.ROJO.value)     # 1
print(Color.ROJO.name)      # ROJO
print(list(Direccion))      # [Direccion.NORTE, ...]

# Los enums se comparan por identidad:
print(Color.ROJO is Color.ROJO)  # True
print(Color.ROJO == Color.VERDE) # False


# ===== DATACLASSES =====

@dataclass
class Punto3D:
    x: float
    y: float
    z: float = 0.0  # valor por defecto

    def distancia_al_origen(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

p1 = Punto3D(1, 2, 3)
p2 = Punto3D(1, 2, 3)
print(p1)           # Punto3D(x=1, y=2, z=3) — __repr__ gratis
print(p1 == p2)     # True — __eq__ gratis

@dataclass(frozen=True)    # inmutable: lanza FrozenInstanceError al modificar
class Coordenada:
    latitud: float
    longitud: float

# field() para opciones avanzadas:
@dataclass
class Configuracion:
    nombre: str
    puerto: int = 8080
    etiquetas: list = field(default_factory=list)  # lista mutable: necesita factory
    _cache: dict = field(default_factory=dict, repr=False, compare=False)

    def __post_init__(self):
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")


# ===== TYPE HINTING AVANZADO: GENERICS =====

T = TypeVar("T")

class Pila(Generic[T]):
    """Pila genérica que puede contener cualquier tipo."""

    def __init__(self) -> None:
        self._elementos: list[T] = []

    def push(self, elemento: T) -> None:
        self._elementos.append(elemento)

    def pop(self) -> T:
        if not self._elementos:
            raise IndexError("Pila vacía")
        return self._elementos.pop()

    def __len__(self) -> int:
        return len(self._elementos)

pila_int: Pila[int] = Pila()
pila_int.push(1)
pila_int.push(2)
print(pila_int.pop())  # 2

pila_str: Pila[str] = Pila()
pila_str.push("hola")
print(pila_str.pop())  # "hola"


# ===== TYPE HINTING: PROTOCOL =====

from typing import Protocol, runtime_checkable

@runtime_checkable
class Dibujable(Protocol):
    def dibujar(self) -> str: ...

class Circulo:
    def dibujar(self) -> str:
        return "○"

class Cuadrado:
    def dibujar(self) -> str:
        return "□"

class Texto:
    def mostrar(self) -> str:  # no implementa dibujar()
        return "abc"

def renderizar(forma: Dibujable) -> None:
    print(forma.dibujar())

renderizar(Circulo())   # funciona
renderizar(Cuadrado())  # funciona
# renderizar(Texto())   # el type checker lo marcaría como error
print(isinstance(Circulo(), Dibujable))  # True gracias a @runtime_checkable


print("\nApuntes de Clase 6 finalizados.")
