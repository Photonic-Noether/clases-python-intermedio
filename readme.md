# Clase 7 — Concurrencia básica: Hilos

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_7
> ```

## ¿En qué rama estás?

Esta rama cubre concurrencia básica en Python con el módulo `threading`: cómo crear hilos, sincronizarlos, comunicarlos, y cuándo usar hilos vs otras estrategias.

## Cómo cambiar de rama

```bash
git checkout Clase_6   # Ir a la clase anterior
git checkout Clase_8   # Ir a la siguiente clase
```

## Configuración del entorno

La primera vez que trabajes en este repositorio:

```bash
python -m venv .venv
```

Actívalo (hazlo una vez por sesión de terminal):

```bash
# Windows
.venv\ Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

El entorno virtual vive en `.venv/` y no se sube a Git.


## Contenido de esta clase

**`threading` — hilos en Python**
- Qué es un hilo y para qué sirve
- `threading.Thread`: crear y arrancar un hilo
- `target` y `args`: qué función ejecuta y con qué argumentos
- `thread.start()` vs `thread.run()`
- `thread.join()`: esperar a que un hilo termine
- `daemon=True`: hilos que mueren cuando el proceso principal termina

**El GIL (Global Interpreter Lock)**
- Qué es el GIL y por qué existe en CPython
- Consecuencia: los hilos de Python NO ejecutan código Python en paralelo real
- Cuándo SÍ ayudan los hilos: operaciones bloqueantes (I/O, red, disco)
- Cuándo NO ayudan: cómputo intensivo (CPU-bound) → usa `multiprocessing`

**Sincronización**
- Race condition: qué pasa cuando dos hilos modifican el mismo dato a la vez
- `threading.Lock()`: garantizar acceso exclusivo a una sección crítica
- `with lock:` — la forma idiomática de usar locks (libera siempre, incluso con excepciones)
- `threading.RLock()`: lock reentrante (el mismo hilo puede adquirirlo varias veces)
- `threading.Event()`: señalizar entre hilos (wait/set/clear)

**Comunicación entre hilos**
- `queue.Queue`: la forma segura de pasar datos entre hilos
- Patrón productor-consumidor con `Queue`
- `queue.Queue.put()` y `queue.Queue.get(block=True, timeout=...)`

**`concurrent.futures`**
- `ThreadPoolExecutor`: pool de hilos reutilizables
- `executor.submit(f, *args)` → `Future`
- `executor.map(f, iterables)` — map paralelo
- `as_completed(futures)` — procesar resultados conforme llegan

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Descargador paralelo de URLs simulado:**

Simula descargar contenido de varias URLs en paralelo (sin red real):

1. Crea una función `simular_descarga(url, delay)` que duerme `delay` segundos y devuelve un dict con url y contenido simulado
2. Implementa `descargar_secuencial(urls)` — descarga una a una
3. Implementa `descargar_paralelo(urls)` — usa `ThreadPoolExecutor`
4. Mide el tiempo de cada versión con `time.perf_counter()`
5. Verifica que el paralelo es ~N veces más rápido con un patrón productor-consumidor usando `Queue`

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_7:ejercicios.py > ejercicios/clase_7/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_7/tu-nombre.py
git commit -m "Clase_7: ejercicios - tu-nombre"
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
