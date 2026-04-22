import pytest
from ejercicios import validar_version, incrementar_version, parsear_commits


# ── Tests de validar_version ─────────────────────────────────

def test_validar_version_correcta():
    assert validar_version("1.0.0") is True
    assert validar_version("10.20.30") is True
    assert validar_version("0.0.1") is True
    assert validar_version("0.0.0") is True


def test_validar_version_incorrecta():
    assert validar_version("1.0") is False
    assert validar_version("v1.0.0") is False
    assert validar_version("1.0.0.0") is False
    assert validar_version("abc") is False
    assert validar_version("") is False
    assert validar_version("1.0.a") is False


# ── Tests de incrementar_version ─────────────────────────────

def test_incrementar_patch():
    assert incrementar_version("1.0.0", "patch") == "1.0.1"
    assert incrementar_version("1.2.3", "patch") == "1.2.4"
    assert incrementar_version("0.0.9", "patch") == "0.0.10"


def test_incrementar_minor():
    assert incrementar_version("1.2.3", "minor") == "1.3.0"
    assert incrementar_version("0.9.5", "minor") == "0.10.0"


def test_incrementar_major():
    assert incrementar_version("1.2.3", "major") == "2.0.0"
    assert incrementar_version("0.1.0", "major") == "1.0.0"


def test_incrementar_tipo_invalido():
    with pytest.raises(ValueError):
        incrementar_version("1.0.0", "hotfix")


# ── Tests de parsear_commits ──────────────────────────────────

def test_parsear_commits_basico():
    texto = "abc1234 Arreglar bug en login\ndef5678 Añadir tests"
    resultado = parsear_commits(texto)
    assert len(resultado) == 2
    assert resultado[0] == {"hash": "abc1234", "mensaje": "Arreglar bug en login"}
    assert resultado[1] == {"hash": "def5678", "mensaje": "Añadir tests"}


def test_parsear_commits_mensaje_con_espacios():
    texto = "aaa1111 Refactor: mover lógica al módulo de utils"
    resultado = parsear_commits(texto)
    assert resultado[0]["mensaje"] == "Refactor: mover lógica al módulo de utils"


def test_parsear_commits_vacio():
    assert parsear_commits("") == []
    assert parsear_commits("   ") == []
