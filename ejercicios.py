# ============================================================
# EJERCICIOS — CLASE 5
# Unit testing e integration testing con pytest
# ============================================================


# ── EJERCICIO 1 ──────────────────────────────────────────────
# Implementa la clase `Pila` (stack — estructura LIFO).
#
# Métodos requeridos:
#   - push(elemento): añade un elemento a la cima
#   - pop(): elimina y devuelve el elemento de la cima.
#            Lanza IndexError si la pila está vacía.
#   - peek(): devuelve el elemento de la cima sin eliminarlo.
#             Lanza IndexError si la pila está vacía.
#   - is_empty(): devuelve True si la pila está vacía
#   - __len__(): número de elementos en la pila


class Pila:
    pass  # escribe tu implementación aquí


# ── EJERCICIO 2 ──────────────────────────────────────────────
# Implementa `ValidadorContrasena`.
#
# La clase valida contraseñas según una serie de reglas configurables.
# Se construye con las reglas activas:
#   v = ValidadorContrasena(minimo_longitud=8, requiere_mayuscula=True,
#                           requiere_numero=True, requiere_simbolo=False)
#   v.validar("MiPass1")   → True
#   v.validar("abc")       → False  (muy corta)
#   v.validar("mipassword1") → False  (sin mayúscula)
#
# El método `validar(contrasena)` devuelve True/False.
# Hay un método `errores(contrasena)` que devuelve una lista de strings
# describiendo qué reglas no se cumplen (lista vacía si es válida).


class ValidadorContrasena:
    def __init__(
        self,
        minimo_longitud: int = 8,
        requiere_mayuscula: bool = True,
        requiere_numero: bool = True,
        requiere_simbolo: bool = False,
    ):
        pass  # escribe tu implementación aquí

    def validar(self, contrasena: str) -> bool:
        pass

    def errores(self, contrasena: str) -> list[str]:
        pass


# ── EJERCICIO 3 ──────────────────────────────────────────────
# Implementa `Conversor`.
#
# Clase que convierte entre unidades de medida.
# Debe soportar:
#   - km ↔ millas:    1 km = 0.621371 millas
#   - kg ↔ libras:    1 kg = 2.20462 libras
#   - celsius ↔ fahrenheit:   F = C * 9/5 + 32
#
# Métodos:
#   - km_a_millas(km) → float
#   - millas_a_km(millas) → float
#   - kg_a_libras(kg) → float
#   - libras_a_kg(libras) → float
#   - celsius_a_fahrenheit(c) → float
#   - fahrenheit_a_celsius(f) → float
#
# Todos los valores negativos en distancia/peso lanzan ValueError.


class Conversor:
    pass  # escribe tu implementación aquí
