# ============================================================
# CLASE 5 — UNIT TESTING E INTEGRATION TESTING CON PYTEST
# ============================================================

# pytest no es parte de la librería estándar. Instala con:
#   pip install pytest


# ===== FUNDAMENTOS DE PYTEST =====

# pytest busca:
#   - archivos que empiezan por test_ o acaban en _test.py
#   - dentro de esos archivos, funciones que empiezan por test_
#   - o clases que empiezan por Test con métodos que empiezan por test_

# La magia de pytest: convierte assert en mensajes de error útiles.
# Con unittest: self.assertEqual(a, b) → "AssertionError: 1 != 2"
# Con pytest:   assert a == b         → "AssertionError: assert 1 == 2\n  where 1 = ..."

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def test_dividir_normal():
    assert dividir(10, 2) == 5.0

def test_dividir_cero():
    import pytest
    with pytest.raises(ValueError, match="cero"):
        dividir(10, 0)


# ===== FIXTURES =====

# Una fixture es una función que prepara el estado para el test.
# Se declara con @pytest.fixture y se usa como argumento del test.
# pytest inyecta automáticamente la fixture correcta por nombre.

import pytest

@pytest.fixture
def lista_vacia():
    return []

@pytest.fixture
def lista_con_elementos():
    return [1, 2, 3, 4, 5]

def test_append(lista_vacia):
    lista_vacia.append(42)
    assert 42 in lista_vacia

# Fixtures con limpieza (yield): el código tras yield se ejecuta al final
@pytest.fixture
def archivo_temporal(tmp_path):
    ruta = tmp_path / "datos.txt"
    ruta.write_text("hola mundo")
    yield ruta           # el test recibe la ruta
    # aquí limpiarías si fuera necesario (tmp_path lo hace automáticamente)

def test_leer_archivo(archivo_temporal):
    contenido = archivo_temporal.read_text()
    assert "hola" in contenido


# ===== PARAMETRIZE =====

# Ejecutar el mismo test con múltiples entradas:
@pytest.mark.parametrize("a, b, resultado", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (1, 1, 1.0),
    (-6, 2, -3.0),
])
def test_dividir_parametrizado(a, b, resultado):
    assert dividir(a, b) == resultado


# ===== MARKS =====

@pytest.mark.skip(reason="No implementado aún")
def test_pendiente():
    assert False

@pytest.mark.xfail(reason="Bug conocido #42")
def test_bug_conocido():
    assert 1 + 1 == 3  # sabemos que falla, no queremos que rompa la suite


# ===== MONKEYPATCH =====

# monkeypatch reemplaza temporalmente atributos, funciones o variables.
# Se restaura automáticamente al final del test.

def obtener_usuario_activo() -> str:
    import os
    return os.getenv("USUARIO_ACTIVO", "anonimo")

def test_usuario_activo(monkeypatch):
    monkeypatch.setenv("USUARIO_ACTIVO", "ana")
    assert obtener_usuario_activo() == "ana"

# Parchear una función de un módulo:
import time as time_module

def esperar_un_segundo():
    time_module.sleep(1)
    return "listo"

def test_esperar_rapido(monkeypatch):
    monkeypatch.setattr(time_module, "sleep", lambda s: None)  # sleep no duerme
    resultado = esperar_un_segundo()
    assert resultado == "listo"


# ===== UNIT TEST VS INTEGRATION TEST =====

# Unit test: prueba una única unidad (función, método, clase) en aislamiento.
# Todas las dependencias externas se mockean.
# Rápido, determinista, fácil de depurar.

# Integration test: prueba cómo colaboran varias unidades.
# Puede tocar bases de datos, sistema de archivos, APIs reales (o de test).
# Más lento, pero captura problemas de integración que los unit tests no ven.

# Organización recomendada:
# tests/
#   unit/
#     test_calculadora.py
#     test_usuario.py
#   integration/
#     test_flujo_registro.py
#     test_api_pagos.py
#   conftest.py   ← fixtures compartidas entre unit e integration


# ===== PATRÓN ESTRATEGIA =====

# Encapsula un algoritmo en una clase intercambiable.
# El contexto no sabe qué algoritmo está usando; solo lo ejecuta.

from abc import ABC, abstractmethod

class EstrategiaOrdenacion(ABC):
    @abstractmethod
    def ordenar(self, lista: list) -> list: ...

class BubbleSort(EstrategiaOrdenacion):
    def ordenar(self, lista: list) -> list:
        lista = lista[:]
        n = len(lista)
        for i in range(n):
            for j in range(n - 1 - i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

class SortIntegrado(EstrategiaOrdenacion):
    def ordenar(self, lista: list) -> list:
        return sorted(lista)

class Sorteador:
    def __init__(self, estrategia: EstrategiaOrdenacion):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaOrdenacion):
        self._estrategia = estrategia

    def ordenar(self, lista: list) -> list:
        return self._estrategia.ordenar(lista)

datos = [3, 1, 4, 1, 5, 9, 2, 6]
sorteador = Sorteador(BubbleSort())
print("BubbleSort:", sorteador.ordenar(datos))
sorteador.cambiar_estrategia(SortIntegrado())
print("Built-in sort:", sorteador.ordenar(datos))


print("\nApuntes de Clase 5 finalizados.")
