# Clase 6 — Librería estándar 1 + Type hinting y genéricos

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch origin
> git reset --hard origin/Clase_6
> ```

## ¿En qué rama estás?

Esta rama cubre los módulos más útiles de la librería estándar (`collections`, `pathlib`, `enum`, `dataclasses`), type hinting avanzado con genéricos, y el patrón de diseño Puente.

## Cómo cambiar de rama

```bash
git checkout Clase_5   # Ir a la clase anterior
git checkout Clase_7   # Ir a la siguiente clase
```

## Contenido de esta clase

**`collections` — estructuras de datos especializadas**
- `Counter`: contar elementos en un iterable
- `defaultdict`: diccionario con valor por defecto
- `OrderedDict`: diccionario que recuerda el orden de inserción
- `namedtuple`: tupla con campos nombrados (inmutable)
- `deque`: cola doblemente enlazada con `append`/`appendleft` en O(1)

**`pathlib` — rutas de archivos orientadas a objetos**
- `Path`: representación de rutas que funciona en Windows, Mac y Linux
- `Path.read_text()`, `Path.write_text()`, `Path.mkdir()`, `Path.glob()`
- Por qué pathlib es mejor que `os.path`

**`enum` — enumeraciones**
- `Enum`: tipo enumerado básico
- `auto()`: asignación automática de valores
- `IntEnum` y `Flag`: variantes especiales

**`dataclasses` — clases de datos sin boilerplate**
- `@dataclass`: genera `__init__`, `__repr__`, `__eq__` automáticamente
- `field()`: personalizar el comportamiento de un campo
- `__post_init__`: validación tras la inicialización
- `frozen=True`: dataclass inmutable (con `__hash__`)
- `dataclasses.asdict()` y `dataclasses.replace()`

**Type hinting avanzado**
- `TypeVar` y `Generic[T]`: escribir código genérico
- `Protocol`: tipado estructural (duck typing con tipos)
- `Literal`, `Union`, `Optional`, `TypeAlias`
- `Final`: constantes que no cambian
- `overload`: sobrecargar firmas de funciones para el type checker

**Patrón de diseño Puente**
- Separar la abstracción de la implementación para que evolucionen independientemente
- Composición sobre herencia: la abstracción tiene una referencia a la implementación

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Implementar un sistema de inventario con dataclasses y pathlib:**

1. Define un `@dataclass frozen=True` `Producto` con `id`, `nombre`, `precio`, `stock`
2. Define `Inventario` que gestiona una lista de productos
3. Persiste el inventario en JSON usando `pathlib.Path`
4. Usa `Counter` para obtener los 5 productos más vendidos
5. Añade type hints con `Generic[T]` a una clase `Repositorio[T]` genérica
6. Escribe tests de las operaciones de inventario

---

## Índice cronológico completo del temario

1. **Clase 1** — Herramientas de proyectos (ruff, precommit, linters) y git avanzado
2. **Clase 2** — Programación funcional y OOP avanzada
3. **Clase 3** — Iteradores, generadores y corrutinas
4. **Clase 4** — Closures, callbacks, memoization y decoradores
5. **Clase 5** — Unit testing e integration testing con pytest
6. **Clase 6** — Librería estándar 1 + Type hinting y genéricos
7. **Clase 7** — Concurrencia básica: Hilos
8. **Clase 8** — Librería estándar 2 + ABCs vs Protocolos + Docker
