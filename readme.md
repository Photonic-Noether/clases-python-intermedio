# Clase 3 — Iteradores, generadores y corrutinas

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_3
> ```

## ¿En qué rama estás?

Esta rama cubre el protocolo iterador de Python, los generadores y las corrutinas. También verás el módulo `itertools` y el patrón de diseño Iterador.

## Cómo cambiar de rama

```bash
git checkout Clase_2   # Ir a la clase anterior
git checkout Clase_4   # Ir a la siguiente clase
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

**Protocolo iterador**
- `__iter__` y `__next__`: cómo Python recorre un objeto
- `StopIteration`: cómo señalizar el fin de la iteración
- La diferencia entre iterable e iterador
- `iter()` y `next()` como funciones built-in
- Implementar un iterador propio como clase

**Generadores con `yield`**
- Qué es un generador: una función que "pausa" y "reanuda"
- `yield` vs `return`: el estado se conserva entre llamadas
- Generadores vs listas: eficiencia de memoria con colecciones grandes
- Expresiones generadoras: `(x**2 for x in range(10))`
- `yield from`: delegar a otro generador (composición)
- `send()`: pasar valores a un generador en ejecución
- `throw()` y `close()`: inyectar excepciones y terminar un generador

**`itertools`**
- `chain(*iterables)` — concatena varios iterables
- `islice(iterable, n)` — corta un iterable como una lista
- `cycle(iterable)` — repite un iterable infinitamente
- `count(start, step)` — contador infinito
- `product(*iterables)` — producto cartesiano
- `combinations(iterable, r)` y `permutations(iterable, r)` — combinatoria
- `groupby(iterable, key)` — agrupa elementos consecutivos

**Patrón de diseño Iterador**
- Separar la lógica de recorrido de la estructura de datos
- Cuándo implementarlo frente a usar generadores
- Implementación en Python con `__iter__` y `__next__`

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Implementar un lector de CSV grande con generadores:**

Crea un módulo que use generadores para procesar un archivo CSV de forma eficiente (sin cargar todo en memoria):

1. `leer_filas(ruta)` — generador que yield cada fila como diccionario
2. `filtrar_filas(generador, predicado)` — generador que filtra filas
3. `transformar_filas(generador, funcion)` — generador que transforma filas
4. `pipeline_csv(ruta, *pasos)` — compone los pasos anteriores
5. Prueba el pipeline con un CSV de 10.000 filas generado con `random`

El objetivo es que la cadena completa procese millones de filas con memoria constante.

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_3:ejercicios.py > ejercicios/clase_3/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_3/tu-nombre.py
git commit -m "Clase_3: ejercicios - tu-nombre"
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
