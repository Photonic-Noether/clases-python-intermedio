import pytest
from ejercicios import retry, log_llamadas, REGISTRO, hacer_multiplicador, componer


# ── Tests de retry ────────────────────────────────────────────

def test_retry_exito_al_primer_intento():
    @retry(max_intentos=3, excepcion=ValueError)
    def siempre_funciona():
        return 42

    assert siempre_funciona() == 42


def test_retry_reintenta_y_tiene_exito():
    intentos = [0]

    @retry(max_intentos=3, excepcion=ValueError)
    def falla_dos_veces():
        intentos[0] += 1
        if intentos[0] < 3:
            raise ValueError("fallo temporal")
        return "ok"

    assert falla_dos_veces() == "ok"
    assert intentos[0] == 3


def test_retry_relanza_si_supera_intentos():
    @retry(max_intentos=2, excepcion=ValueError)
    def siempre_falla():
        raise ValueError("fallo permanente")

    with pytest.raises(ValueError, match="fallo permanente"):
        siempre_falla()


def test_retry_preserva_nombre():
    @retry(max_intentos=2)
    def mi_funcion():
        """Docstring original."""
        return 1

    assert mi_funcion.__name__ == "mi_funcion"
    assert "Docstring" in mi_funcion.__doc__


# ── Tests de log_llamadas ─────────────────────────────────────

def test_log_registra_llamadas():
    REGISTRO.clear()

    @log_llamadas
    def sumar(a, b):
        return a + b

    resultado = sumar(3, 4)
    assert resultado == 7
    assert len(REGISTRO) == 1
    entrada = REGISTRO[0]
    assert entrada["funcion"] == "sumar"
    assert entrada["resultado"] == 7


def test_log_multiples_llamadas():
    REGISTRO.clear()

    @log_llamadas
    def cuadrado(x):
        return x ** 2

    cuadrado(3)
    cuadrado(5)
    assert len(REGISTRO) == 2
    assert REGISTRO[0]["resultado"] == 9
    assert REGISTRO[1]["resultado"] == 25


# ── Tests de hacer_multiplicador y componer ───────────────────

def test_hacer_multiplicador():
    doble = hacer_multiplicador(2)
    triple = hacer_multiplicador(3)
    assert doble(5) == 10
    assert triple(5) == 15
    assert doble(0) == 0


def test_componer():
    doble = hacer_multiplicador(2)
    triple = hacer_multiplicador(3)
    seis_veces = componer(doble, triple)
    assert seis_veces(4) == 24
    assert seis_veces(1) == 6


def test_componer_con_lambda():
    sumar_uno = lambda x: x + 1
    cuadrado = lambda x: x ** 2
    cuadrado_mas_uno = componer(sumar_uno, cuadrado)
    assert cuadrado_mas_uno(3) == 10  # 3**2 = 9, 9+1 = 10
