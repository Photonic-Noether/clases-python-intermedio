"""
Diferencia entre ABCs y Protocolos en Python.
ABCs = herencia nominal: el subtipo debe declarar que hereda.
Protocols = tipado estructural: cualquier clase con los métodos correctos sirve.
"""
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ── ABC: contrato explícito con herencia ──

class Notificador(ABC):
    """Contrato: cualquier Notificador debe poder enviar mensajes."""

    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> bool:
        """Envía el mensaje. Devuelve True si tiene éxito."""
        ...

    @abstractmethod
    def verificar_conexion(self) -> bool: ...

class NotificadorEmail(Notificador):
    def enviar(self, destinatario: str, mensaje: str) -> bool:
        print(f"Email a {destinatario}: {mensaje}")
        return True

    def verificar_conexion(self) -> bool:
        return True  # en producción: verifica SMTP

class NotificadorSMS(Notificador):
    def enviar(self, destinatario: str, mensaje: str) -> bool:
        print(f"SMS a {destinatario}: {mensaje[:160]}")
        return True

    def verificar_conexion(self) -> bool:
        return True


# ── Protocol: contrato implícito por estructura ──

@runtime_checkable
class Procesable(Protocol):
    """Cualquier objeto con estos métodos es Procesable, sin herencia."""

    def procesar(self) -> dict: ...
    def validar(self) -> bool: ...

class PedidoOnline:
    def procesar(self) -> dict:
        return {"tipo": "online", "estado": "procesado"}

    def validar(self) -> bool:
        return True

class PedidoFisico:
    def procesar(self) -> dict:
        return {"tipo": "fisico", "estado": "procesado"}

    def validar(self) -> bool:
        return True

class DocumentoInvalido:
    # No implementa procesar() ni validar()
    def firmar(self) -> bool:
        return True


def ejecutar_procesamiento(procesable: Procesable) -> dict:
    if not procesable.validar():
        raise ValueError("El objeto no es válido para procesar")
    return procesable.procesar()


if __name__ == "__main__":
    notif = NotificadorEmail()
    notif.enviar("ana@ejemplo.com", "Hola Ana!")

    pedido = PedidoOnline()
    print(isinstance(pedido, Procesable))  # True gracias a @runtime_checkable
    print(ejecutar_procesamiento(pedido))

    doc = DocumentoInvalido()
    print(isinstance(doc, Procesable))  # False
