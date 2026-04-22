# Repaso — Python Intermedio

Cheatsheet de referencia rápida. Explicación mínima + ejemplos ejecutables.

---

## 1. Variables y tipos

### `int` y `float`

```python
x = 42
y = 3.14
z = int("10")        # 10 — convierte string a entero
w = float("3.14")    # 3.14

abs(-5)              # 5 — valor absoluto
round(3.7)           # 4
round(3.14159, 2)    # 3.14
divmod(10, 3)        # (3, 1) — cociente y resto a la vez
```

### `str`

```python
s = "Hola, mundo"

s.upper()             # "HOLA, MUNDO"
s.lower()             # "hola, mundo"
s.strip()             # elimina espacios al inicio y al final
s.strip(".")          # elimina "." de los extremos
s.replace("o", "0")  # "H0la, mund0"
s.split(", ")         # ["Hola", "mundo"]
", ".join(["a", "b", "c"])  # "a, b, c"
s.startswith("Hola")  # True
s.endswith("mundo")   # True
s.find("mundo")       # 6 — índice de la primera aparición, -1 si no existe
"42".zfill(5)         # "00042" — rellena con ceros a la izquierda
s.count("o")          # 2 — número de apariciones

# f-strings (forma moderna de formatear)
nombre, edad = "Ana", 30
f"{nombre} tiene {edad} años"          # "Ana tiene 30 años"
f"{3.14159:.2f}"                       # "3.14"
f"{1000000:,}"                         # "1,000,000"
f"{'centrado':^20}"                    # "      centrado      "
```

### `list`

```python
lista = [3, 1, 4, 1, 5, 9]

lista.append(2)           # añade al final
lista.insert(0, 99)       # inserta en la posición 0
lista.pop()               # elimina y devuelve el último
lista.pop(0)              # elimina y devuelve el índice 0
lista.remove(1)           # elimina la primera aparición de 1
lista.sort()              # ordena en sitio (modifica la lista)
lista.sort(reverse=True)  # ordena descendente
lista.reverse()           # invierte en sitio
lista.index(4)            # índice de la primera aparición de 4
lista.count(1)            # cuántas veces aparece 1
lista.extend([10, 11])    # añade todos los elementos de otro iterable
lista.copy()              # copia superficial
lista.clear()             # vacía la lista

sorted([3, 1, 2])                         # [1, 2, 3] — nueva lista, no modifica
sorted(["banana", "kiwi"], key=len)       # ordena por longitud
len(lista)                                 # número de elementos

# Slicing
lista = [0, 1, 2, 3, 4, 5]
lista[1:4]     # [1, 2, 3]
lista[::2]     # [0, 2, 4] — cada dos
lista[::-1]    # [5, 4, 3, 2, 1, 0] — invertida

# List comprehensions
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

### `tuple`

```python
t = (1, 2, 3)
t.count(1)   # 1 — cuántas veces aparece
t.index(2)   # 1 — índice de la primera aparición

# Desempaquetado
a, b, c = t
primero, *resto = (1, 2, 3, 4)   # primero=1, resto=[2, 3, 4]
```

### `dict`

```python
d = {"a": 1, "b": 2, "c": 3}

d.get("a")              # 1
d.get("z", 0)           # 0 — valor por defecto si la clave no existe
d.keys()                # dict_keys(["a", "b", "c"])
d.values()              # dict_values([1, 2, 3])
d.items()               # dict_items([("a", 1), ("b", 2), ("c", 3)])
d.update({"d": 4})      # añade o sobreescribe claves
d.pop("a")              # elimina y devuelve el valor de "a"
d.pop("z", None)        # elimina "z"; devuelve None si no existe
d.setdefault("e", 0)    # devuelve el valor si existe; si no, lo crea con 0
"a" in d                # True — comprueba si la clave existe

# Dict comprehension
cuadrados = {x: x**2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Unir dos dicts (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
unido = d1 | d2   # {"a": 1, "b": 2}
```

### `set`

```python
s = {1, 2, 3, 4}

s.add(5)
s.remove(1)      # lanza KeyError si no existe
s.discard(99)    # no lanza error si no existe
s.pop()          # elimina y devuelve un elemento arbitrario

# Operaciones de conjuntos
{1, 2, 3} | {3, 4, 5}    # {1, 2, 3, 4, 5} — unión
{1, 2, 3} & {3, 4, 5}    # {3} — intersección
{1, 2, 3} - {3, 4, 5}    # {1, 2} — diferencia
{1, 2} <= {1, 2, 3}      # True — subconjunto

2 in s                    # True — pertenencia en O(1)
```

### `bool` y `None`

```python
bool(0)       # False — también: "", [], {}, set(), None
bool(1)       # True  — cualquier otro valor
None          # el "no valor" de Python; tipo NoneType

# Operadores lógicos
True and False   # False
True or False    # True
not True         # False
```

---

## 2. Bucles y condicionales

### `if / elif / else`

```python
x = 42

if x > 100:
    print("grande")
elif x > 10:
    print("mediano")       # se imprime esto
else:
    print("pequeño")

# Expresión ternaria (en una línea)
resultado = "par" if x % 2 == 0 else "impar"
```

### `for`

```python
# Sobre cualquier iterable
for fruta in ["manzana", "pera", "uva"]:
    print(fruta)

# enumerate: índice + valor
for i, fruta in enumerate(["manzana", "pera"]):
    print(i, fruta)   # 0 manzana / 1 pera

# zip: iterar varios a la vez
nombres = ["Ana", "Bob"]
edades = [30, 25]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad}")

# range
for i in range(5):       # 0, 1, 2, 3, 4
    pass
for i in range(2, 10, 2):  # 2, 4, 6, 8
    pass
```

### `while`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break: salir del bucle antes de tiempo
while True:
    entrada = input("Escribe 'salir': ")
    if entrada == "salir":
        break

# continue: saltar al siguiente ciclo
for i in range(10):
    if i % 2 == 0:
        continue   # salta los pares
    print(i)       # imprime solo impares
```

### Desempaquetado `*` y `**`

```python
# * desempaqueta iterables
a, *resto, ultimo = [1, 2, 3, 4, 5]
# a=1, resto=[2, 3, 4], ultimo=5

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = [*lista1, *lista2]     # [1, 2, 3, 4, 5, 6]

# ** desempaqueta diccionarios
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}
unido = {**d1, **d2}               # {"a": 1, "b": 2, "c": 3}

# En llamadas a funciones
def suma(a, b, c):
    return a + b + c

args = [1, 2, 3]
suma(*args)                        # equivale a suma(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
suma(**kwargs)                     # equivale a suma(a=1, b=2, c=3)
```

---

## 3. Funciones

### Definición básica y valores por defecto

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

saludar("Ana")           # "Hola, Ana!"
saludar("Bob", "Buenos días")  # "Buenos días, Bob!"
```

### Funciones variádicas (`*args` y `**kwargs`)

```python
# *args: número variable de argumentos posicionales → tupla
def sumar(*numeros):
    return sum(numeros)

sumar(1, 2, 3)       # 6
sumar(1, 2, 3, 4, 5) # 15

# **kwargs: número variable de argumentos con nombre → diccionario
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")

# Combinados: primero posicionales fijos, luego *args, luego **, luego **kwargs
def funcion_completa(obligatorio, *args, solo_keyword=False, **kwargs):
    print(obligatorio, args, solo_keyword, kwargs)

funcion_completa("hola", 1, 2, solo_keyword=True, extra="dato")
```

### Scope (ámbito) — regla LEGB

```python
# Python busca nombres en este orden: Local → Enclosing → Global → Built-in

x = "global"

def exterior():
    x = "enclosing"

    def interior():
        # x = "local"   ← si existiera, usaría esta
        print(x)        # usa "enclosing" (ámbito envolvente)

    interior()

# global: modificar una variable global desde dentro de una función
contador = 0

def incrementar():
    global contador
    contador += 1

# nonlocal: modificar la variable del ámbito envolvente (no global)
def hacer_contador():
    cuenta = 0
    def sumar_uno():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return sumar_uno
```

### Closures

Una closure es una función que recuerda las variables del ámbito donde fue definida,
aunque ese ámbito ya haya terminado.

```python
def hacer_multiplicador(factor):
    def multiplicar(x):
        return x * factor   # "factor" es una variable libre (closure)
    return multiplicar

doble = hacer_multiplicador(2)
triple = hacer_multiplicador(3)

doble(5)    # 10  — recuerda que factor=2
triple(5)   # 15  — recuerda que factor=3
```

### Callbacks

Las funciones son objetos de primera clase: se pueden pasar como argumentos.

```python
def aplicar(funcion, valor):
    return funcion(valor)

aplicar(abs, -42)            # 42
aplicar(lambda x: x**2, 5)  # 25

# Callback en sorted
personas = [("Ana", 30), ("Bob", 25), ("Carlos", 35)]
sorted(personas, key=lambda p: p[1])  # ordena por edad
```

---

## 4. Orientación a objetos

### Clases e instancias

```python
class Persona:
    especie = "Homo sapiens"    # variable de clase — compartida por todas las instancias

    def __init__(self, nombre, edad):
        self.nombre = nombre    # variable de instancia — única por objeto
        self.edad = edad

    def saludar(self):          # método de instancia — recibe self
        return f"Soy {self.nombre}, tengo {self.edad} años"

    @classmethod
    def desde_texto(cls, texto):    # método de clase — recibe la clase, no la instancia
        nombre, edad = texto.split(",")
        return cls(nombre.strip(), int(edad))

    @staticmethod
    def es_mayor_de_edad(edad):     # método estático — no recibe ni clase ni instancia
        return edad >= 18

# Instancias
ana = Persona("Ana", 30)
bob = Persona.desde_texto("Bob, 25")

ana.saludar()                  # "Soy Ana, tengo 30 años"
Persona.especie                # "Homo sapiens"
ana.especie                    # también funciona, pero no es la misma cosa
Persona.es_mayor_de_edad(17)   # False
```

### Variables de clase vs instancia

```python
class Contador:
    total = 0           # de clase: la comparten todas las instancias

    def __init__(self):
        Contador.total += 1     # modifica la variable de CLASE
        self.id = Contador.total  # de instancia: única para este objeto

a = Contador()   # total=1, a.id=1
b = Contador()   # total=2, b.id=2
```

### Herencia básica

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Perro(Animal):
    def hablar(self):               # sobreescribe el método del padre
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

perro = Perro("Rex")
perro.hablar()          # "Rex dice: ¡Guau!"
isinstance(perro, Animal)  # True — Perro ES un Animal

# super(): llamar al método del padre
class AnimalDomestico(Animal):
    def __init__(self, nombre, dueño):
        super().__init__(nombre)    # llama a Animal.__init__
        self.dueño = dueño
```

### Herencia VS Composición

```python
# ── HERENCIA (es-un): Moto ES UN Vehículo ──
class Vehiculo:
    def __init__(self, velocidad_max):
        self.velocidad_max = velocidad_max

    def mover(self):
        return f"Moviéndome a {self.velocidad_max} km/h"

class Moto(Vehiculo):
    def wheelie(self):
        return "¡Caballito!"

# ── COMPOSICIÓN (tiene-un): Coche TIENE UN Motor ──
class Motor:
    def __init__(self, cilindros):
        self.cilindros = cilindros

    def arrancar(self):
        return f"Motor de {self.cilindros} cilindros arrancando"

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor      # composición: tiene un motor

    def arrancar(self):
        return self.motor.arrancar()

# La composición es más flexible: puedes cambiar el motor sin cambiar Coche
motor_diesel = Motor(4)
coche = Coche(motor_diesel)
coche.arrancar()   # "Motor de 4 cilindros arrancando"

# ¿Cuándo usar cada uno?
# Herencia → cuando hay una relación clara "es-un" (Perro es un Animal)
# Composición → cuando hay una relación "tiene-un" (Coche tiene un Motor)
# Regla práctica: preferir composición. La herencia crea acoplamiento fuerte.
```

---

## 5. Excepciones

### Capturar excepciones

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except (TypeError, ValueError) as e:
    print(f"Error de tipo o valor: {e}")
except Exception as e:
    print(f"Cualquier otro error: {e}")
else:
    print("Se ejecuta SOLO si no hubo excepción")
finally:
    print("Se ejecuta SIEMPRE, haya o no excepción")

# raise: lanzar una excepción manualmente
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b
```

### Excepciones propias

```python
# Hereda de Exception (o de una más específica)
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_actual, cantidad_pedida):
        self.saldo_actual = saldo_actual
        self.cantidad_pedida = cantidad_pedida
        super().__init__(
            f"Saldo insuficiente: tienes {saldo_actual}€, intentas retirar {cantidad_pedida}€"
        )

class CuentaBloqueadaError(Exception):
    pass    # a veces basta con el nombre para diferenciarlo

# Uso
def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError(saldo, cantidad)
    return saldo - cantidad

try:
    retirar(100, 200)
except SaldoInsuficienteError as e:
    print(e)               # el mensaje de __init__
    print(e.saldo_actual)  # acceso a los atributos
```

---

## 6. Módulos, paquetes e imports

### Imports

```python
import math                         # importa el módulo entero
import math as m                    # alias
from math import sqrt, pi           # importa nombres concretos
from math import sqrt as raiz       # alias del nombre

# Importar todo (evitar en producción — contamina el namespace)
from math import *
```

### Paquetes

Un paquete es un directorio con un archivo `__init__.py`.

```
mi_paquete/
    __init__.py          ← hace que el directorio sea un paquete
    modulo_a.py
    modulo_b.py
    subpaquete/
        __init__.py
        modulo_c.py
```

```python
from mi_paquete import modulo_a
from mi_paquete.subpaquete import modulo_c
from mi_paquete.modulo_a import mi_funcion
```

### `random`

```python
import random

random.random()              # float entre 0.0 y 1.0
random.randint(1, 10)        # entero entre 1 y 10 (ambos incluidos)
random.choice(["a", "b", "c"])   # elemento aleatorio de una lista
random.choices(["a", "b"], k=5)  # 5 elementos con repetición
random.sample(range(100), 10)    # 10 elementos sin repetición
random.shuffle(lista)            # baraja la lista en sitio
random.seed(42)                  # fijar la semilla para reproducibilidad
```

### `math`

```python
import math

math.sqrt(16)        # 4.0 — raíz cuadrada
math.pow(2, 10)      # 1024.0 — potencia
math.floor(3.7)      # 3 — redondeo hacia abajo
math.ceil(3.2)       # 4 — redondeo hacia arriba
math.pi              # 3.141592653589793
math.e               # 2.718281828459045
math.log(100, 10)    # 2.0 — logaritmo en base 10
math.log(math.e)     # 1.0 — logaritmo natural
math.factorial(5)    # 120
math.gcd(12, 8)      # 4 — máximo común divisor
math.inf             # infinito positivo
math.isnan(float("nan"))  # True
```

---

## 7. Librería estándar — módulos más usados

### `os` — sistema operativo y archivos

```python
import os

os.getcwd()                    # directorio de trabajo actual
os.listdir(".")                # lista archivos y carpetas del directorio
os.makedirs("ruta/nueva", exist_ok=True)   # crea directorios recursivamente
os.remove("archivo.txt")       # elimina un archivo
os.rename("viejo.txt", "nuevo.txt")
os.path.exists("archivo.txt")  # True si existe
os.path.join("carpeta", "archivo.txt")  # une rutas correctamente
os.environ.get("HOME", "/tmp")  # leer variables de entorno
```

### `sys` — intérprete de Python

```python
import sys

sys.argv           # lista de argumentos de línea de comandos
sys.argv[0]        # nombre del script
sys.exit(0)        # termina el proceso (0 = éxito, otro = error)
sys.path           # lista de directorios donde Python busca módulos
sys.version        # versión de Python como string
sys.platform       # "win32", "linux", "darwin"
```

### `datetime` — fechas y horas

```python
from datetime import datetime, date, timedelta

hoy = date.today()                         # 2025-06-15
ahora = datetime.now()                     # 2025-06-15 10:30:00.123456
ahora.strftime("%d/%m/%Y %H:%M")           # "15/06/2025 10:30"
datetime.strptime("15/06/2025", "%d/%m/%Y")  # parsear un string a datetime

# Aritmética con fechas
manana = hoy + timedelta(days=1)
hace_una_semana = hoy - timedelta(weeks=1)
diferencia = datetime(2025, 12, 31) - datetime.now()
diferencia.days    # días hasta fin de año
```

### `pickle` — serialización binaria

```python
import pickle

# Python → bytes (serializar)
datos = {"nombre": "Ana", "edad": 30, "lista": [1, 2, 3]}
bytes_datos = pickle.dumps(datos)              # bytes en memoria
pickle.dump(datos, open("datos.pkl", "wb"))    # escribir a archivo binario

# bytes → Python (deserializar)
datos = pickle.loads(bytes_datos)
datos = pickle.load(open("datos.pkl", "rb"))

# Cualquier objeto Python es serializable (clases, funciones, lambdas...)
# ⚠️  Nunca cargues un .pkl de fuente no confiable — puede ejecutar código arbitrario

# pickle vs json:
# - pickle: cualquier objeto Python, binario, solo Python
# - json:   tipos básicos, texto legible, interoperable entre lenguajes
```

### `json` — serialización JSON

```python
import json

# Python → JSON (serializar)
datos = {"nombre": "Ana", "edad": 30, "activo": True, "tags": ["python", "dev"]}
texto_json = json.dumps(datos)              # string JSON
texto_json = json.dumps(datos, indent=2)    # con formato bonito
json.dump(datos, open("datos.json", "w"))   # escribir directamente a archivo

# JSON → Python (deserializar)
datos = json.loads(texto_json)
datos = json.load(open("datos.json"))

# Tipos: str↔str, int/float↔number, bool↔true/false, None↔null, list↔array, dict↔object
```

### `re` — expresiones regulares

```python
import re

re.match(r"^\d+$", "123")       # match al inicio del string
re.search(r"\d+", "abc123def")  # busca en cualquier parte; devuelve Match o None
re.findall(r"\d+", "a1b2c3")    # ["1", "2", "3"] — todos los matches
re.sub(r"\s+", " ", "hola  mundo")  # "hola mundo" — sustituir
re.split(r"[,;]", "a,b;c")     # ["a", "b", "c"] — dividir

# Patrones más comunes
r"\d"       # un dígito
r"\w"       # letra, dígito o _
r"\s"       # espacio, tab, newline
r"."        # cualquier carácter (excepto newline)
r"+"        # uno o más
r"*"        # cero o más
r"?"        # cero o uno
r"^"        # inicio de línea
r"$"        # fin de línea
r"(grupo)"  # captura un grupo
```

### `pathlib` — rutas como objetos

```python
from pathlib import Path

ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"   # concatenar con /
ruta.exists()           # True si existe
ruta.is_file()          # True si es un archivo
ruta.is_dir()           # True si es un directorio
ruta.suffix             # ".txt"
ruta.stem               # "archivo"
ruta.parent             # Path("carpeta/subcarpeta")
ruta.name               # "archivo.txt"

ruta.read_text(encoding="utf-8")           # lee el contenido completo
ruta.write_text("contenido", encoding="utf-8")
ruta.mkdir(parents=True, exist_ok=True)    # crea el directorio
list(Path(".").glob("**/*.py"))            # todos los .py recursivamente
```

### `collections` — estructuras de datos especializadas

```python
from collections import Counter, defaultdict, deque

# Counter: contar elementos
Counter("banana")                   # Counter({'a': 3, 'n': 2, 'b': 1})
Counter(["a", "b", "a"]).most_common(1)  # [('a', 2)]

# defaultdict: valor por defecto para claves nuevas
grupos = defaultdict(list)
grupos["frutas"].append("manzana")  # no lanza KeyError si "frutas" no existe
grupos["frutas"].append("pera")

# deque: cola doblemente enlazada, O(1) en ambos extremos
cola = deque([1, 2, 3], maxlen=5)
cola.appendleft(0)   # añade a la izquierda
cola.popleft()       # elimina de la izquierda
```

### `enum` — enumeraciones

```python
from enum import Enum, auto

class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

class Direccion(Enum):
    NORTE = auto()   # asigna valores automáticamente: 1, 2, 3...
    SUR = auto()
    ESTE = auto()

Color.ROJO.name      # "ROJO"
Color.ROJO.value     # 1
Color(2)             # Color.VERDE — buscar por valor
list(Color)          # [Color.ROJO, Color.VERDE, Color.AZUL]

# En vez de constantes mágicas:
# MAL:  if estado == 1: ...
# BIEN: if estado == Color.ROJO: ...
```

### `dataclasses` — clases de datos sin boilerplate

```python
from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0                          # valor por defecto
    etiquetas: list = field(default_factory=list)  # mutable: necesita factory

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

p1 = Producto("Manzana", 0.99, 100)
p2 = Producto("Manzana", 0.99, 100)
p1 == p2    # True — __eq__ generado automáticamente
repr(p1)    # Producto(nombre='Manzana', precio=0.99, stock=100, etiquetas=[])

@dataclass(frozen=True)   # inmutable: lanza error al intentar modificar
class Punto:
    x: float
    y: float
```

### `typing` — anotaciones de tipo

```python
from typing import Optional, Union, Any, Callable

def buscar(id: int) -> Optional[str]:   # puede devolver str o None
    ...

def procesar(valor: Union[int, str]) -> str:  # acepta int o str (Python 3.10+: int | str)
    ...

# Colecciones con tipo (Python 3.9+ puede usar list[int] directamente)
from typing import List, Dict, Tuple, Set
numeros: List[int] = [1, 2, 3]
mapa: Dict[str, int] = {"a": 1}

# Callable: tipo de función
from typing import Callable
def aplicar(func: Callable[[int], str], valor: int) -> str:
    return func(valor)
```

---

## 8. Principios SOLID

Los principios SOLID son guías para escribir código orientado a objetos que sea fácil de mantener y extender.

---

### S — Single Responsibility (Responsabilidad Única)

> Una clase debe tener un solo motivo para cambiar.

```python
# ❌ MAL: una clase hace demasiadas cosas
class Pedido:
    def __init__(self, items):
        self.items = items

    def calcular_total(self):          # lógica de negocio — ok
        return sum(i.precio for i in self.items)

    def guardar_en_base_de_datos(self):  # persistencia — NO es su trabajo
        ...

    def enviar_email_confirmacion(self): # comunicación — tampoco
        ...

# ✅ BIEN: cada clase hace una cosa
class Pedido:
    def __init__(self, items):
        self.items = items

    def calcular_total(self):
        return sum(i.precio for i in self.items)

class RepositorioPedidos:
    def guardar(self, pedido): ...      # solo persiste

class NotificadorEmail:
    def confirmar(self, pedido): ...    # solo notifica
```

---

### O — Open/Closed (Abierto/Cerrado)

> El código debe estar abierto a extensión pero cerrado a modificación.

```python
# ❌ MAL: añadir un descuento nuevo obliga a modificar la función
def calcular_descuento(tipo, precio):
    if tipo == "estudiante":
        return precio * 0.9
    elif tipo == "jubilado":
        return precio * 0.8
    # Para añadir "empleado" hay que modificar esta función — peligroso

# ✅ BIEN: añadir un descuento nuevo NO modifica el código existente
from abc import ABC, abstractmethod

class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio: float) -> float: ...

class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9

class DescuentoJubilado(Descuento):
    def aplicar(self, precio):
        return precio * 0.8

class DescuentoEmpleado(Descuento):    # nuevo descuento: sin tocar nada anterior
    def aplicar(self, precio):
        return precio * 0.7

def calcular_precio(descuento: Descuento, precio: float) -> float:
    return descuento.aplicar(precio)
```

---

### L — Liskov Substitution (Sustitución de Liskov)

> Si B hereda de A, deberías poder usar B en cualquier lugar donde usas A sin que nada se rompa.

```python
# ❌ MAL: Cuadrado hereda de Rectangulo pero viola el contrato
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def set_ancho(self, ancho):
        self.ancho = ancho
        self.alto = ancho    # en un cuadrado ambos lados son iguales... pero esto rompe el contrato

# Esta función espera un Rectangulo, pero Cuadrado la rompe:
def duplicar_ancho(figura: Rectangulo):
    figura.ancho *= 2
    # si figura es Cuadrado, también cambia el alto — ¡sorpresa!

# ✅ BIEN: clases separadas, sin herencia forzada
class Figura(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
```

---

### I — Interface Segregation (Segregación de Interfaces)

> Una clase no debe estar obligada a implementar métodos que no usa.

```python
from abc import ABC, abstractmethod

# ❌ MAL: una interfaz enorme que no todos necesitan
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self): ...
    @abstractmethod
    def comer(self): ...
    @abstractmethod
    def dormir(self): ...

class RobotIndustrial(Trabajador):
    def trabajar(self): return "soldando"
    def comer(self): raise NotImplementedError("¡Soy un robot!")   # absurdo
    def dormir(self): raise NotImplementedError("¡Soy un robot!")  # absurdo

# ✅ BIEN: interfaces pequeñas y específicas
class Trabajable(ABC):
    @abstractmethod
    def trabajar(self): ...

class Biologico(ABC):
    @abstractmethod
    def comer(self): ...
    @abstractmethod
    def dormir(self): ...

class Robot(Trabajable):
    def trabajar(self): return "soldando"   # solo implementa lo que necesita

class Humano(Trabajable, Biologico):
    def trabajar(self): return "programando"
    def comer(self): return "comiendo"
    def dormir(self): return "durmiendo"
```

---

### D — Dependency Inversion (Inversión de Dependencias)

> Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones.

```python
# ❌ MAL: la clase de alto nivel depende directamente de la de bajo nivel
class EnvioEmail:
    def enviar(self, mensaje):
        print(f"[Email] {mensaje}")

class Notificador:
    def __init__(self):
        self.servicio = EnvioEmail()    # acoplado a Email — no puedes cambiarlo

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)

# ✅ BIEN: Notificador depende de una abstracción, no de una clase concreta
from abc import ABC, abstractmethod

class ServicioMensajeria(ABC):
    @abstractmethod
    def enviar(self, mensaje: str): ...

class Email(ServicioMensajeria):
    def enviar(self, mensaje):
        print(f"[Email] {mensaje}")

class SMS(ServicioMensajeria):
    def enviar(self, mensaje):
        print(f"[SMS] {mensaje}")

class Notificador:
    def __init__(self, servicio: ServicioMensajeria):   # inyección de dependencias
        self.servicio = servicio

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)

# Puedes cambiar el servicio sin tocar Notificador:
n1 = Notificador(Email())
n2 = Notificador(SMS())
```

---

### Qué es un patrón de diseño

Un **patrón de diseño** es una solución reutilizable a un problema recurrente en el diseño de software. No es código concreto: es una plantilla que describes cómo resolver un problema en un contexto específico.

Los patrones más conocidos vienen del libro _Design Patterns_ (Gang of Four, 1994): Fábrica, Singleton, Estrategia, Decorador, Observador, etc.

### Patrón Fábrica (Factory)

**Problema**: tienes varias clases similares y necesitas crear objetos de una u otra según una condición, sin que el código que los usa sepa qué clase concreta se instancia.

**Solución**: una función (o clase) centraliza la lógica de creación.

```python
from abc import ABC, abstractmethod

# 1. La abstracción: todos los animales tienen el mismo contrato
class Animal(ABC):
    @abstractmethod
    def hablar(self) -> str: ...

# 2. Las implementaciones concretas
class Perro(Animal):
    def hablar(self) -> str:
        return "¡Guau!"

class Gato(Animal):
    def hablar(self) -> str:
        return "¡Miau!"

class Pajaro(Animal):
    def hablar(self) -> str:
        return "¡Pío!"

# 3. La fábrica: aquí está toda la lógica de "qué clase crear"
def crear_animal(tipo: str) -> Animal:
    catalogo = {          # un dict es más limpio que un if/elif largo
        "perro": Perro,
        "gato": Gato,
        "pájaro": Pajaro,
    }
    if tipo not in catalogo:
        raise ValueError(f"Tipo desconocido: {tipo!r}")
    ClaseAnimal = catalogo[tipo]   # obtiene la CLASE (no la instancia)
    return ClaseAnimal()           # ahora sí la instancia y la devuelve

# 4. El código que usa la fábrica no sabe qué clase concreta recibe
for tipo in ["perro", "gato", "pájaro"]:
    animal = crear_animal(tipo)   # solo sabe que es un Animal
    print(animal.hablar())        # ¡Guau! / ¡Miau! / ¡Pío!

# Ventaja: para añadir un nuevo animal, solo tocas el dict de la fábrica.
# El código que llama a crear_animal() no cambia nunca.
```

---

## 9. Protocolo de iteración en Python

### Qué ocurre internamente en un `for`

Python traduce `for elemento in coleccion:` en algo equivalente a esto:

```python
lista = [10, 20, 30]

# Lo que hace for internamente:
iterador = iter(lista)        # pide un iterador a la colección
while True:
    try:
        elemento = next(iterador)   # pide el siguiente elemento
        print(elemento)
    except StopIteration:           # el iterador señala que ya no hay más
        break
```

### Diferencia entre iterable e iterador

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Iterable** | Objeto del que puedes obtener un iterador con `iter()` | `list`, `str`, `dict`, `range` |
| **Iterador** | Objeto que produce valores uno a uno con `next()`; cuando se agota lanza `StopIteration` | Lo que devuelve `iter(lista)` |

```python
lista = [1, 2, 3]

# lista es iterable, no iterador
iter(lista)           # ok — devuelve un iterador
next(lista)           # ERROR — lista no tiene next()

# El iterador que devuelve iter() sí tiene next()
it = iter(lista)
next(it)   # 1
next(it)   # 2
next(it)   # 3
next(it)   # StopIteration — se agotó

# Puedes llamar a iter() sobre un iterador y devuelve el mismo objeto
iter(it) is it   # True — los iteradores son su propio iterador
```

### `iter()` y `next()` con valor por defecto

```python
it = iter([1, 2, 3])
next(it, "agotado")   # 1
next(it, "agotado")   # 2
next(it, "agotado")   # 3
next(it, "agotado")   # "agotado" — en vez de lanzar StopIteration
```

### Generadores

Un generador es una función con `yield`. Cada vez que se llama a `next()`, ejecuta hasta el siguiente `yield`, devuelve ese valor, y pausa. Recuerda su estado entre llamadas.

```python
# Ejemplo 1: contador simple
def contar_hasta(n):
    i = 0
    while i <= n:
        yield i       # pausa aquí y devuelve i
        i += 1        # continúa desde aquí en el siguiente next()

gen = contar_hasta(3)
next(gen)   # 0
next(gen)   # 1
list(gen)   # [2, 3] — consume el resto

# Ejemplo 2: leer un archivo grande línea a línea (sin cargar todo en memoria)
def leer_lineas(ruta):
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()

# for linea in leer_lineas("enorme.txt"):   # solo una línea en memoria a la vez
#     procesar(linea)

# Ejemplo 3: generador infinito
def numeros_pares():
    n = 0
    while True:        # bucle infinito — está bien porque yield pausa
        yield n
        n += 2

pares = numeros_pares()
[next(pares) for _ in range(5)]   # [0, 2, 4, 6, 8]
```

### Expresiones generadoras

Como las list comprehensions pero entre paréntesis. Son perezosas: no calculan nada hasta que se pide.

```python
cuadrados_lista = [x**2 for x in range(1000000)]    # crea la lista entera en memoria
cuadrados_gen   = (x**2 for x in range(1000000))    # no crea nada todavía

sum(cuadrados_gen)   # calcula sobre la marcha, sin lista en memoria
```
