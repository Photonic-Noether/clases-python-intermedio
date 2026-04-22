# ============================================================
# EJERCICIOS — CLASE 1
# Herramientas de proyectos y git avanzado
# ============================================================
# Implementa las tres funciones de abajo.
# Ejecuta `python run_tests.py` para comprobar tu solución.
# Los tests están en tests/test_ejercicios.py.
# ============================================================


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa `validar_version(version)`.
#
# Una versión semántica válida tiene el formato "X.Y.Z" donde
# X, Y y Z son números enteros no negativos (sin ceros a la izquierda
# salvo el propio 0, y sin prefijos como "v").
#
# Ejemplos:
#   validar_version("1.0.0")    → True
#   validar_version("10.20.30") → True
#   validar_version("v1.0.0")   → False  (tiene prefijo "v")
#   validar_version("1.0")      → False  (solo dos partes)
#   validar_version("1.0.0.0")  → False  (cuatro partes)
#   validar_version("abc")      → False


def validar_version(version: str) -> bool:
    pass  # escribe tu solución aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa `incrementar_version(version, tipo)`.
#
# Dado una versión semántica válida y un tipo de incremento
# ("major", "minor" o "patch"), devuelve la nueva versión.
# Reglas del versionado semántico:
#   - "patch": incrementa Z, deja X e Y iguales → "1.2.3" → "1.2.4"
#   - "minor": incrementa Y, resetea Z a 0, deja X igual → "1.2.3" → "1.3.0"
#   - "major": incrementa X, resetea Y y Z a 0 → "1.2.3" → "2.0.0"
#
# Si `tipo` no es uno de los tres valores válidos, lanza ValueError.
# Puedes asumir que `version` siempre es una versión semántica válida.


def incrementar_version(version: str, tipo: str) -> str:
    pass  # escribe tu solución aquí


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa `parsear_commits(texto)`.
#
# La función recibe un texto con una línea por commit en formato:
#   "<hash_corto> <mensaje>"
# donde el hash tiene exactamente 7 caracteres y el mensaje es
# el resto de la línea (puede contener espacios).
#
# Devuelve una lista de diccionarios con las claves "hash" y "mensaje".
# Si el texto está vacío o es solo espacios, devuelve una lista vacía.
#
# Ejemplo:
#   texto = "abc1234 Arreglar bug en login\ndef5678 Añadir tests"
#   parsear_commits(texto) →
#     [
#       {"hash": "abc1234", "mensaje": "Arreglar bug en login"},
#       {"hash": "def5678", "mensaje": "Añadir tests"},
#     ]


def parsear_commits(texto: str) -> list[dict]:
    pass  # escribe tu solución aquí
