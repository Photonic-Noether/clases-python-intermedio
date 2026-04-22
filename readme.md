# Clase 8 — Librería estándar 2 + ABCs vs Protocolos + Introducción a Docker

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_8
> ```

## ¿En qué rama estás?

Esta es la última clase del curso. Cubre los módulos más avanzados de la librería estándar (`contextlib`, `logging`, `json`), la diferencia entre ABCs y Protocolos en Python, y una introducción práctica a Docker.

## Cómo cambiar de rama

```bash
git checkout Clase_7   # Ir a la clase anterior
git checkout main      # Volver al README general del curso
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

**Librería estándar 2**
- `contextlib.contextmanager`: crear gestores de contexto con generadores
- `contextlib.suppress(*excepciones)`: ignorar excepciones específicas de forma explícita
- `contextlib.ExitStack`: combinar múltiples gestores de contexto dinámicamente
- `logging`: logger, handlers, formatters, niveles (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `logging.basicConfig` y `logging.getLogger`
- `json`: `dumps`, `loads`, `JSONEncoder` personalizado para tipos no estándar
- `functools.singledispatch`: sobrecargar funciones según el tipo del primer argumento

**ABCs vs Protocolos**
- `abc.ABC` y `@abc.abstractmethod`: herencia nominal, fuerza la implementación en subclases
- `typing.Protocol`: tipado estructural — "si camina como un pato, es un pato"
- Diferencias clave:
  - ABC: el subclase debe declarar explícitamente `class MiClase(MiABC)`
  - Protocol: cualquier clase con los métodos correctos pasa la verificación
- `@runtime_checkable`: permite usar `isinstance()` con Protocols
- Cuándo usar cada uno: ABCs para jerarquías fijas, Protocols para interfaces abiertas

**Introducción a Docker**
- Qué es Docker y para qué sirve: "funciona en mi máquina" → funciona en cualquier máquina
- Imagen vs contenedor: la imagen es la receta, el contenedor es la instancia
- `Dockerfile`: instrucciones para construir una imagen
  - `FROM python:3.12-slim`
  - `WORKDIR`, `COPY`, `RUN pip install`, `CMD`
- Comandos esenciales:
  - `docker build -t nombre .`
  - `docker run -p 8080:8080 nombre`
  - `docker ps` y `docker logs`
- `docker-compose.yml`: orquestar múltiples contenedores
- Ejemplo: contenedorizar una aplicación Python simple

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Contenedorizar una aplicación Python:**

1. Crea una pequeña API con `http.server` (sin frameworks externos) que devuelva JSON
2. Escribe un `Dockerfile` para contenedorizarla
3. Usa `logging` con nivel configurable por variable de entorno
4. Serializa/deserializa datos con un `JSONEncoder` personalizado que soporte `datetime`
5. Define una `Protocol` para las "vistas" de tu API
6. Construye la imagen con `docker build` y prueba que funciona con `docker run`

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_8:ejercicios/clase_8/ejercicios.py > ejercicios/clase_8/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_8/tu-nombre.py
git commit -m "Clase_8: ejercicios - tu-nombre"
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
