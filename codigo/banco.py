"""
Módulo de demostración para la clase de testing.
Implementa una cuenta bancaria simple para ser testeada.
"""


class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self._saldo = saldo_inicial
        self._historial: list[dict] = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def ingresar(self, cantidad: float) -> float:
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser positiva")
        self._saldo += cantidad
        self._historial.append({"tipo": "ingreso", "cantidad": cantidad, "saldo": self._saldo})
        return self._saldo

    def retirar(self, cantidad: float) -> float:
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        if cantidad > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente: tienes {self._saldo:.2f}, intentas retirar {cantidad:.2f}"
            )
        self._saldo -= cantidad
        self._historial.append({"tipo": "retirada", "cantidad": cantidad, "saldo": self._saldo})
        return self._saldo

    def transferir_a(self, destino: "CuentaBancaria", cantidad: float) -> None:
        self.retirar(cantidad)
        destino.ingresar(cantidad)

    @property
    def historial(self) -> list[dict]:
        return list(self._historial)

    def __repr__(self) -> str:
        return f"CuentaBancaria({self.titular!r}, saldo={self._saldo:.2f})"


if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana", 1000.0)
    cuenta.ingresar(500)
    cuenta.retirar(200)
    print(cuenta)
    print("Historial:", cuenta.historial)
