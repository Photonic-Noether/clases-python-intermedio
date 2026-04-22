# Clase 4 — Closures, callbacks, memoization y decoradores

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_4
> ```

## ¿En qué rama estás?

Esta rama cubre las técnicas más avanzadas de programación funcional en Python: closures, callbacks, memoización manual, y decoradores (simples, con argumentos, basados en clases). También verás los patrones de diseño Fábrica y Decorador.

## Cómo cambiar de rama

```bash
git checkout Clase_3   # Ir a la clase anterior
git checkout Clase_5   # Ir a la siguiente clase
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

**Closures y variables libres**
- Qué es una closure: una función que "recuerda" su entorno de definición
- Variables libres: variables referenciadas en la función pero definidas fuera de ella
- `nonlocal`: modificar una variable del ámbito superior desde dentro de la función
- Cuándo usar closures vs clases
- `__closure__` y `__code__.co_freevars`: inspeccionar una closure

**Callbacks**
- Pasar funciones como argumentos (funciones de primera clase)
- Callbacks en sorting, event listeners, y pipelines
- Lambdas como callbacks inline

**Memoización**
- Memoización manual con un diccionario
- `functools.lru_cache` y `functools.cache`: memoización automática
- `functools.wraps`: preservar metadatos de la función original
- Cuándo memoizar y cuándo no (efectos secundarios, mutabilidad)

**Decoradores**
- Decoradores simples: función que recibe una función y devuelve otra
- `functools.wraps` para preservar `__name__`, `__doc__`, etc.
- Decoradores con argumentos: función que devuelve un decorador
- Decoradores basados en clases: implementar `__call__`
- Apilar decoradores: el orden importa (de abajo a arriba)
- Casos de uso reales: logging, timing, retry, autenticación

**Patrones de diseño**
- **Fábrica**: una función o clase que crea objetos sin exponer la lógica de creación
- **Decorador (patrón GoF)**: envolver un objeto para añadir comportamiento sin modificar la clase

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Implementar un mini-framework de validación con decoradores:**

Crea un sistema donde las funciones declaran sus validaciones con decoradores:

1. `@validar_tipo(argname, tipo)` — lanza `TypeError` si el argumento no es del tipo esperado
2. `@validar_rango(argname, minimo, maximo)` — lanza `ValueError` si el argumento está fuera del rango
3. `@registro` — registra cada llamada (función, argumentos, resultado) en una lista global
4. Apila los tres decoradores sobre una función `calcular_precio(cantidad, precio_unitario)`
5. Escribe tests que verifiquen que los errores se lanzan correctamente y el registro funciona

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_4:ejercicios.py > ejercicios/clase_4/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_4/tu-nombre.py
git commit -m "Clase_4: ejercicios - tu-nombre"
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
