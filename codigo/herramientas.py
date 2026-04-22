"""
Módulo de utilidades para gestión de versiones y análisis de git.
Importable desde tests y desde otros módulos.
"""
import re


def es_version_valida(version: str) -> bool:
    """Verifica que una cadena es una versión semántica válida (X.Y.Z)."""
    patron = r"^\d+\.\d+\.\d+$"
    return bool(re.match(patron, version))


def descomponer_version(version: str) -> tuple[int, int, int]:
    """Descompone '1.2.3' en (1, 2, 3). Lanza ValueError si no es válida."""
    if not es_version_valida(version):
        raise ValueError(f"Versión no válida: {version!r}")
    partes = version.split(".")
    return int(partes[0]), int(partes[1]), int(partes[2])


def comparar_versiones(v1: str, v2: str) -> int:
    """
    Compara dos versiones semánticas.
    Devuelve -1 si v1 < v2, 0 si son iguales, 1 si v1 > v2.
    """
    t1 = descomponer_version(v1)
    t2 = descomponer_version(v2)
    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    return 0


def ordenar_versiones(versiones: list[str]) -> list[str]:
    """Ordena una lista de versiones semánticas de menor a mayor."""
    return sorted(versiones, key=lambda v: descomponer_version(v))


if __name__ == "__main__":
    ejemplos = ["1.0.0", "2.0.0", "1.10.0", "1.2.3", "0.9.9"]
    print("Versiones ordenadas:", ordenar_versiones(ejemplos))
    print("1.0.0 vs 1.0.1:", comparar_versiones("1.0.0", "1.0.1"))
