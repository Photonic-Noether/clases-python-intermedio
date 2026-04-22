"""Iteradores personalizados como clases."""


class Rango:
    """Reimplementación didáctica de range()."""

    def __init__(self, inicio: int, fin: int, paso: int = 1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso

    def __iter__(self):
        return _RangoIterador(self.inicio, self.fin, self.paso)

    def __len__(self):
        if self.paso > 0:
            return max(0, (self.fin - self.inicio + self.paso - 1) // self.paso)
        return max(0, (self.inicio - self.fin - self.paso - 1) // (-self.paso))


class _RangoIterador:
    def __init__(self, inicio, fin, paso):
        self.actual = inicio
        self.fin = fin
        self.paso = paso

    def __iter__(self):
        return self

    def __next__(self):
        if self.paso > 0 and self.actual >= self.fin:
            raise StopIteration
        if self.paso < 0 and self.actual <= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += self.paso
        return valor


class ArbolBinario:
    """Árbol binario de búsqueda con recorrido in-order como iterador."""

    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierda is None:
                self.izquierda = ArbolBinario(valor)
            else:
                self.izquierda.insertar(valor)
        else:
            if self.derecha is None:
                self.derecha = ArbolBinario(valor)
            else:
                self.derecha.insertar(valor)

    def __iter__(self):
        # In-order: izquierda → raíz → derecha
        if self.izquierda:
            yield from self.izquierda
        yield self.valor
        if self.derecha:
            yield from self.derecha


if __name__ == "__main__":
    r = Rango(0, 10, 2)
    print("Rango par:", list(r))

    arbol = ArbolBinario(5)
    for v in [3, 7, 1, 4, 6, 8]:
        arbol.insertar(v)
    print("In-order:", list(arbol))  # [1, 3, 4, 5, 6, 7, 8]
