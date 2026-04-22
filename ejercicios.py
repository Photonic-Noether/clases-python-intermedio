# ============================================================
# EJERCICIOS — CLASE 8
# Librería estándar 2 + ABCs vs Protocolos + Docker
# ============================================================

import contextlib
import json
import logging
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Protocol


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa `cronometro()` como gestor de contexto.
#
# Al salir del bloque `with`, debe retornar el tiempo transcurrido
# en segundos a través del objeto yielded.
#
# Uso esperado:
#   with cronometro() as t:
#       time.sleep(0.1)
#   print(t.segundos)  # ~0.1
#
# El objeto yielded debe tener un atributo `segundos` que solo
# tenga valor DESPUÉS de que el bloque `with` termine.
# Antes de terminar, `segundos` es None.
#
# Implementa usando @contextlib.contextmanager.


@contextlib.contextmanager
def cronometro():
    pass  # escribe tu implementación aquí
    # yield un objeto con atributo segundos


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa `EncoderPersonalizado`.
#
# Un JSONEncoder que soporta los siguientes tipos adicionales:
#   - datetime → string ISO 8601 ("2025-06-15T10:30:00")
#   - set       → lista ordenada
#   - bytes     → string decodificado como UTF-8
#
# Para cualquier otro tipo no estándar, debe llamar al encoder por defecto
# (que lanzará TypeError).
#
# Ejemplo de uso:
#   json.dumps({"fecha": datetime.now(), "tags": {1, 3, 2}},
#              cls=EncoderPersonalizado)


class EncoderPersonalizado(json.JSONEncoder):
    pass  # escribe tu implementación aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa la ABC `Repositorio` y una implementación en memoria.
#
# Define una ABC `Repositorio` con estos métodos abstractos:
#   - guardar(elemento): almacena el elemento
#   - obtener(id): devuelve el elemento o None
#   - eliminar(id): elimina el elemento, devuelve True si existía
#   - todos(): devuelve todos los elementos como lista
#
# Luego implementa `RepositorioMemoria(Repositorio)` que almacena
# los elementos en un diccionario en memoria.
# Los elementos deben tener un atributo `id`.
#
# BONUS: define también un `Protocol` llamado `TieneId` que describe
# el requisito de que los elementos tengan un atributo `id`.


class Repositorio(ABC):
    pass  # escribe tu implementación aquí


class RepositorioMemoria(Repositorio):
    pass  # escribe tu implementación aquí
