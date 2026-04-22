# ============================================================
# CLASE 3 — ITERADORES, GENERADORES Y CORRUTINAS
# ============================================================

import itertools


# ===== PROTOCOLO ITERADOR =====

# En Python, "iterable" = objeto que implementa __iter__
# "iterador" = objeto que implementa __iter__ + __next__
# Un for loop hace exactamente esto internamente:
#   it = iter(coleccion)
#   while True:
#       try: elemento = next(it)
#       except StopIteration: break

# Implementar un iterador propio:
class ContadorRegresivo:
    def __init__(self, inicio: int):
        self.actual = inicio

    def __iter__(self):
        return self  # el propio objeto es su iterador

    def __next__(self):
        if self.actual < 0:
            raise StopIteration
        valor = self.actual
        self.actual -= 1
        return valor

for n in ContadorRegresivo(3):
    print(n, end=" ")  # 3 2 1 0
print()


# ===== GENERADORES =====

# Un generador es una función que usa yield.
# Cuando se llama, devuelve un objeto generador (no ejecuta el cuerpo).
# Cada vez que se llama next() sobre él, ejecuta hasta el siguiente yield.
# El estado (variables locales) se conserva entre llamadas.

def contar_hasta(n: int):
    for i in range(n + 1):
        yield i

gen = contar_hasta(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(list(gen))  # [2, 3, 4, 5]

# Los generadores son perezosos: calculan bajo demanda.
# Esto los hace ideales para procesar colecciones enormes:

def leer_lineas_grandes(ruta: str):
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()
# Solo una línea en memoria a la vez, aunque el archivo tenga 10 GB.

# Expresiones generadoras (como list comprehensions pero perezosas):
cuadrados_gen = (x**2 for x in range(10))
print(sum(cuadrados_gen))  # 285

# yield from: delegar a otro generador
def cadena(*iterables):
    for it in iterables:
        yield from it  # equivale a: for elem in it: yield elem

print(list(cadena([1, 2], [3, 4], [5])))  # [1, 2, 3, 4, 5]


# ===== CORRUTINAS Y send() =====

# Una corrutina es un generador que puede RECIBIR valores además de producirlos.
# El valor se inyecta con send(valor), que es lo que devuelve el yield.

def acumulador():
    total = 0
    while True:
        numero = yield total  # yield publica total, y recibe el siguiente número
        if numero is None:
            break
        total += numero

acum = acumulador()
next(acum)        # inicializa el generador hasta el primer yield
acum.send(10)     # total = 10
acum.send(20)     # total = 30
print(acum.send(5))   # 35


# ===== ITERTOOLS =====

# chain: concatenar iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))

# islice: cortar un iterable (incluso infinito)
naturales = itertools.count(1)                      # 1, 2, 3, 4, ... ∞
primeros_diez = list(itertools.islice(naturales, 10))
print(primeros_diez)

# cycle: repetir indefinidamente
colores = itertools.cycle(["rojo", "verde", "azul"])
print([next(colores) for _ in range(7)])

# product: producto cartesiano
print(list(itertools.product("AB", "12")))

# combinations y permutations: combinatoria
print(list(itertools.combinations([1, 2, 3], 2)))
print(list(itertools.permutations([1, 2, 3], 2)))

# groupby: agrupa elementos CONSECUTIVOS iguales (requiere orden previo)
datos = [("ES", "Madrid"), ("ES", "Barcelona"), ("FR", "París"), ("FR", "Lyon")]
for pais, ciudades in itertools.groupby(datos, key=lambda x: x[0]):
    print(pais, [c[1] for c in ciudades])


print("\nApuntes de Clase 3 finalizados.")
