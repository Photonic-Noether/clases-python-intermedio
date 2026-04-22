# ============================================================
# CLASE 8 — LIBRERÍA ESTÁNDAR 2 + ABCs VS PROTOCOLOS + DOCKER
# ============================================================

import contextlib
import logging
import json
import functools
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from datetime import datetime


# ===== CONTEXTLIB =====

# contextmanager: convertir un generador en un gestor de contexto
@contextlib.contextmanager
def medir_tiempo(nombre: str):
    """Gestor de contexto que mide el tiempo de ejecución de un bloque."""
    import time
    inicio = time.perf_counter()
    try:
        yield  # aquí se ejecuta el bloque `with`
    finally:
        fin = time.perf_counter()
        print(f"[{nombre}] {fin - inicio:.4f}s")

with medir_tiempo("operación lenta"):
    resultado = sum(range(1_000_000))

# suppress: ignorar excepciones específicas de forma explícita
# En lugar de:
#   try:
#       os.remove("archivo_que_puede_no_existir.txt")
#   except FileNotFoundError:
#       pass
# Puedes escribir:
import os
with contextlib.suppress(FileNotFoundError):
    os.remove("archivo_que_puede_no_existir.txt")

# ExitStack: combinar gestores dinámicamente
def abrir_archivos(rutas: list[str]):
    with contextlib.ExitStack() as stack:
        archivos = [stack.enter_context(open(r)) for r in rutas]
        # todos los archivos se cierran al salir del with, incluso si falla


# ===== LOGGING =====

# El módulo logging es la forma correcta de registrar información en Python.
# No uses print() en aplicaciones reales.

# Configuración básica:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("mi_aplicacion")

logger.debug("Mensaje de depuración — solo visible en DEV")
logger.info("Aplicación iniciada correctamente")
logger.warning("Memoria al 85% — considera limpiar cachés")
logger.error("No se pudo conectar a la base de datos")
# logger.critical("Fallo irrecuperable")
# logger.exception("Error con traceback:")  # dentro de un except

# En aplicaciones reales, configuras el nivel por entorno:
# - DEV: logging.DEBUG
# - PROD: logging.WARNING


# ===== JSON =====

# Serialización básica:
datos = {"nombre": "Ana", "edad": 30, "activo": True}
json_texto = json.dumps(datos, indent=2, ensure_ascii=False)
print(json_texto)
datos_recuperados = json.loads(json_texto)

# Tipos no estándar necesitan un encoder personalizado:
class EncoderFecha(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # "2025-06-15T10:30:00"
        return super().default(obj)

evento = {"nombre": "Clase 8", "fecha": datetime.now()}
print(json.dumps(evento, cls=EncoderFecha, indent=2))

# singledispatch: sobrecargar por tipo del primer argumento
@functools.singledispatch
def serializar(obj):
    raise TypeError(f"No sé cómo serializar {type(obj)}")

@serializar.register(datetime)
def _(obj: datetime) -> str:
    return obj.isoformat()

@serializar.register(set)
def _(obj: set) -> list:
    return sorted(obj)

print(serializar(datetime.now()))
print(serializar({3, 1, 2}))


# ===== ABCs vs PROTOCOLOS =====

# ── ABC: herencia nominal ──
# La subclase DEBE declarar que hereda de la ABC.
# Si no implementa los métodos abstractos, no se puede instanciar.

class FiguraABC(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

class CirculoABC(FiguraABC):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return 3.14159 * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * 3.14159 * self.radio

# Si olvidamos implementar un método abstracto:
# class FiguraMal(FiguraABC): pass
# FiguraMal()  →  TypeError: Can't instantiate abstract class FiguraMal

# ── Protocol: tipado estructural ──
# Cualquier clase que tenga los métodos correctos es compatible.
# No necesita heredar de Protocol ni declarar nada.

@runtime_checkable  # permite isinstance() en tiempo de ejecución
class Serializable(Protocol):
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...

class Usuario:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def to_dict(self) -> dict:
        return {"nombre": self.nombre, "email": self.email}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

class Producto:
    def __init__(self, sku: str, precio: float):
        self.sku = sku
        self.precio = precio

    def to_dict(self) -> dict:
        return {"sku": self.sku, "precio": self.precio}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

# Ambas clases son Serializable sin haber heredado nada:
print(isinstance(Usuario("Ana", "ana@email.com"), Serializable))  # True
print(isinstance(Producto("ABC123", 9.99), Serializable))         # True

def exportar(obj: Serializable) -> str:
    return obj.to_json()

print(exportar(Usuario("Bob", "bob@email.com")))


# ===== DOCKER: CONCEPTOS CLAVE =====
# (No es código Python — se explica en comentarios)

# Un contenedor Docker es un proceso aislado con su propio sistema de archivos.
# La imagen es la receta; el contenedor es la instancia en ejecución.

# Dockerfile mínimo para una app Python:
# ─────────────────────────────────────────
# FROM python:3.12-slim          # imagen base oficial
# WORKDIR /app                   # directorio de trabajo
# COPY requirements.txt .        # copiar dependencias
# RUN pip install -r requirements.txt  # instalar
# COPY . .                       # copiar el código
# CMD ["python", "app.py"]       # comando por defecto
# ─────────────────────────────────────────

# Construir la imagen:  docker build -t mi-app .
# Ejecutar:             docker run -p 8080:8080 mi-app
# Ver contenedores:     docker ps
# Ver logs:             docker logs <container_id>

# docker-compose.yml permite orquestar varios servicios:
# (app + base de datos + redis, etc.)


print("\nApuntes de Clase 8 finalizados. ¡Enhorabuena por terminar el curso!")
