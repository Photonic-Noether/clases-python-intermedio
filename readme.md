# Clase 2 — Programación funcional y OOP avanzada

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_2
> ```
> Si hiciste commits accidentales, `git pull` fallará. Este par de comandos siempre funciona.

## ¿En qué rama estás?

Esta rama cubre programación funcional avanzada (`functools`, `map`, `filter`, `any/all`) y los aspectos más potentes de la orientación a objetos: `property`, descriptores, métodos dunder, `classmethod`, `staticmethod` y `__new__`.

## Cómo cambiar de rama

```bash
git checkout Clase_1   # Ir a la clase anterior
git checkout Clase_3   # Ir a la siguiente clase
```

## Configuración del entorno

La primera vez que trabajes en este repositorio:

```bash
python -m venv .venv
```

Actívalo (hazlo una vez por sesión de terminal):

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

El entorno virtual vive en `.venv/` y no se sube a Git.


## Contenido de esta clase

**Programación funcional**
- `map(f, iterable)` — aplica una función a cada elemento
- `filter(f, iterable)` — filtra elementos según un predicado
- `sorted(iterable, key=f)` — ordena con criterio personalizado
- `any(iterable)` y `all(iterable)` — comprobaciones booleanas sobre colecciones
- `functools.reduce(f, iterable)` — acumula un iterable a un único valor
- `functools.partial(f, *args)` — fija argumentos de una función (aplicación parcial)
- `functools.lru_cache` — caché automática de resultados de funciones puras

**OOP avanzada — `property` y atributos gestionados**
- `@property` — convertir un método en un atributo de solo lectura
- `@atributo.setter` — validar valores al asignar un atributo
- `@atributo.deleter` — lógica al eliminar un atributo
- Descriptores: `__get__`, `__set__`, `__delete__` para control total

**OOP avanzada — métodos dunder**
- `__repr__` y `__str__` — representación para desarrolladores y usuarios
- `__len__`, `__getitem__`, `__setitem__`, `__contains__` — protocolo de secuencia
- `__add__`, `__mul__`, `__eq__`, `__lt__` — operadores aritméticos y de comparación
- `__bool__` — valor booleano del objeto
- `__enter__` y `__exit__` — protocolo de gestor de contexto (`with`)

**OOP avanzada — métodos de clase**
- `@classmethod` — recibe la clase como primer argumento, no la instancia
- `@staticmethod` — función que vive en la clase pero no necesita ni clase ni instancia
- `__new__` vs `__init__` — cuándo se usa cada uno y el patrón Singleton

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

Ejecuta `python run_tests.py` para comprobar si tu solución es correcta.

## Proyecto propuesto (~30 minutos)

**Implementar una clase `Matriz` con aritmética completa:**

Crea una clase `Matriz` que represente una matriz 2D de números y soporte:

1. Creación desde una lista de listas: `Matriz([[1,2],[3,4]])`
2. `__repr__` que muestre la matriz de forma legible
3. `__add__` para sumar dos matrices (lanza `ValueError` si las dimensiones no coinciden)
4. `__mul__` que multiplique por un escalar (`Matriz * 3`) y por otra matriz (producto matricial)
5. Una `@property` `transpuesta` que devuelva la transpuesta
6. Un `@classmethod` `identidad(n)` que cree la matriz identidad de tamaño n×n
7. `__eq__` para comparar dos matrices

Escribe tests de pytest para verificar cada operación.

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_2:ejercicios.py > ejercicios/clase_2/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_2/tu-nombre.py
git commit -m "Clase_2: ejercicios - tu-nombre"
git push origin development
```

Abre la PR en GitHub. Comprueba que el destino es `upstream/development`, no `main`.

Para el flujo completo (fork, configuración de `upstream`, sincronización), consulta el README de la rama `development`.

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
