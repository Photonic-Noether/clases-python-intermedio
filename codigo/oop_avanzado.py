"""OOP avanzada: property, descriptores, dunders, classmethod."""


class RangoValidado:
    """Descriptor que valida que un valor esté dentro de un rango."""

    def __init__(self, minimo, maximo, nombre="valor"):
        self.minimo = minimo
        self.maximo = maximo
        self.nombre = nombre
        self._atributo = f"_{nombre}"

    def __set_name__(self, owner, name):
        self._atributo = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self._atributo, None)

    def __set__(self, obj, valor):
        if not (self.minimo <= valor <= self.maximo):
            raise ValueError(
                f"{self.nombre} debe estar entre {self.minimo} y {self.maximo}, got {valor}"
            )
        setattr(obj, self._atributo, valor)


class Persona:
    edad = RangoValidado(0, 150, "edad")

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad  # pasa por el descriptor

    @classmethod
    def desde_dict(cls, datos: dict) -> "Persona":
        return cls(datos["nombre"], datos["edad"])

    def __repr__(self) -> str:
        return f"Persona({self.nombre!r}, {self.edad})"


if __name__ == "__main__":
    p = Persona("Ana", 30)
    print(p)
    p2 = Persona.desde_dict({"nombre": "Bob", "edad": 25})
    print(p2)
    try:
        p.edad = 200
    except ValueError as e:
        print("Error esperado:", e)
