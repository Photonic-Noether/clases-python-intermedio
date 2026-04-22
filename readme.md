# Clase 3 — Iteradores, generadores y corrutinas

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch origin
> git reset --hard origin/Clase_3
> ```

## ¿En qué rama estás?

Esta rama cubre el protocolo iterador de Python, los generadores y las corrutinas. También verás el módulo `itertools` y el patrón de diseño Iterador.

## Cómo cambiar de rama

```bash
git checkout Clase_2   # Ir a la clase anterior
git checkout Clase_4   # Ir a la siguiente clase
```

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

## Índice cronológico completo del temario

1. **Clase 1** — Herramientas de proyectos (ruff, precommit, linters) y git avanzado
2. **Clase 2** — Programación funcional y OOP avanzada
3. **Clase 3** — Iteradores, generadores y corrutinas
4. **Clase 4** — Closures, callbacks, memoization y decoradores
5. **Clase 5** — Unit testing e integration testing con pytest
6. **Clase 6** — Librería estándar 1 + Type hinting y genéricos
7. **Clase 7** — Concurrencia básica: Hilos
8. **Clase 8** — Librería estándar 2 + ABCs vs Protocolos + Docker
