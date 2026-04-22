import pytest
from ejercicios.clase_5.ejercicios import Conversor


# ── Tests de Conversor ────────────────────────────────────────

def test_km_a_millas(conversor):
    assert abs(conversor.km_a_millas(1) - 0.621371) < 0.0001


def test_millas_a_km(conversor):
    assert abs(conversor.millas_a_km(1) - 1.60934) < 0.001


def test_kg_a_libras(conversor):
    assert abs(conversor.kg_a_libras(1) - 2.20462) < 0.0001


def test_celsius_a_fahrenheit(conversor):
    assert conversor.celsius_a_fahrenheit(0) == 32.0
    assert conversor.celsius_a_fahrenheit(100) == 212.0


def test_fahrenheit_a_celsius(conversor):
    assert conversor.fahrenheit_a_celsius(32) == 0.0
    assert conversor.fahrenheit_a_celsius(212) == 100.0


def test_km_negativo_lanza_error(conversor):
    with pytest.raises(ValueError):
        conversor.km_a_millas(-1)
