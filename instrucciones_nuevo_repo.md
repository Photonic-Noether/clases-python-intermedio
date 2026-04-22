# Instrucciones para montar el nuevo repositorio de curso

Este documento es un briefing para un agente Claude. Describe el estilo y estructura de un repositorio de curso de Python ya existente, y especifica cómo debe ser el nuevo repositorio que hay que crear desde cero.

---

## Contexto: repositorio de referencia

El repositorio de referencia es un curso de Python para alumnos españoles de nivel principiante-intermedio (Tajamar). Tiene estas características fundamentales:

- **Todo en español**: README, comentarios, nombres de proyectos, mensajes de error explicados, etc.
- **Audiencia**: alumnos que están aprendiendo Python y Git simultáneamente, con poca experiencia técnica.
- **Tono**: directo, sin condescendencia, con ejemplos prácticos concretos.

---

## Estructura del repositorio de referencia

### Ramas

El repositorio usa **una rama de Git por clase**. La rama `main` es la raíz y no contiene código de clase.

| Rama | Contenido |
|------|-----------|
| `main` | Solo README del curso completo |
| `Clase_1` … `Clase_N` | Contenido de cada clase |
| `alumnos` | Sandbox de práctica para alumnos (archivos vacíos + guía de Git) |

### Archivos por rama de clase

Cada rama `Clase_N` contiene:

```
Clase_N/
  codigo/          ← notebooks Jupyter (.ipynb) con apuntes y ejemplos
  ejercicios.py    ← 3 ejercicios propuestos sin solución
  readme.md        ← README específico de la clase
  .gitignore
```

### README de `main`

El README de main cubre:

- Cómo está organizado el repositorio
- Tabla de ramas disponibles con descripción de cada una
- **Cómo actualizar una rama** (método seguro: `git fetch origin` + `git reset --hard origin/Clase_N`)
- **Sección de troubleshooting** "Si `git pull` da error": explica el error de ramas divergentes y da exactamente los mismos dos comandos para arreglarlo
- Sección de rama `alumnos`
- Temario completo del curso (todos los temas de todas las clases)
- Objetivos de aprendizaje
- Requisitos previos
- Recursos adicionales

### README de cada clase (`readme.md`)

Estructura fija, en este orden:

1. **`# Clase N - Título`** (h1)
2. **`## Antes de empezar: actualiza esta rama`** — justo debajo del título, con blockquote en negrita instando a hacerlo antes de mirar el código, y los dos comandos:
   ```bash
   git fetch origin
   git reset --hard origin/Clase_N
   ```
   Explicación breve de por qué: si hiciste commits accidentales, `git pull` falla; este comando siempre funciona.
3. **`## ¿En qué rama estás?`** — una línea describiendo qué cubre esta rama
4. **`## Cómo cambiar de rama`** — comandos `git checkout` a la clase siguiente y anterior
5. **`## Contenido de esta clase`** — lista detallada de lo que cubren los notebooks/módulos, agrupada por subtemas con negrita
6. **`## Ejercicios propuestos`** — frase estándar: "En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!"
7. **`## Proyecto propuesto (~30 minutos)`** — un proyecto integrador en negrita con descripción detallada de qué implementar
8. **`---`**
9. **`## Índice cronológico completo del temario`** — lista numerada de todas las clases del curso

### Contenido de `ejercicios.py`

Tres ejercicios propuestos en comentarios, sin código de solución. Dificultad ligeramente superior al temario de la clase. El alumno escribe su solución debajo de cada enunciado.

### Rama `alumnos`

Contiene `practica.py`, `mis_notas.py`, y un `readme.md` con guía completa de Git (commits, deshacer cambios, `git pull`, cómo hacer fork). No tiene código de clase. Es el sandbox donde los alumnos pueden commitear sin romper las ramas del curso.

---

## Nuevo repositorio: qué cambia

El nuevo repositorio sigue **exactamente el mismo estilo** (español, misma estructura de ramas, mismo formato de README), con estos cambios en el contenido de cada rama de clase:

### Estructura de archivos por rama (nueva)

```
Clase_N/
  codigo/          ← módulos Python (.py) importables, no notebooks
  apuntes.py       ← archivo de teoría: código ejecutable con comentarios explicativos extensos
                      (reemplaza la función didáctica de los notebooks)
  ejercicios.py    ← igual que antes: 3 ejercicios sin solución
  tests/           ← carpeta con tests de pytest para los ejercicios o módulos de la clase
  run_tests.py     ← archivo compartido en todas las ramas (contenido idéntico)
  requirements.txt ← solo pytest (igual en todas las ramas)
  .gitignore       ← incluye .venv/
  readme.md        ← mismo formato que antes, adaptado a la nueva estructura
```

### `apuntes.py`

Reemplaza los notebooks Jupyter. Es un archivo Python ejecutable de arriba a abajo, con:
- Comentarios extensos explicando la teoría
- Código de ejemplo intercalado con la explicación
- Se puede leer como documento o ejecutar para ver los outputs
- Agrupa los temas en bloques con separadores visuales (`# ===== TEMA =====`)

### `codigo/`

Módulos Python importables que implementan los conceptos de la clase. No son scripts sueltos, sino módulos con funciones/clases bien definidas que los tests pueden importar. Ejemplo para una clase de funciones:

```
codigo/
  funciones_basicas.py
  lambdas.py
  orden_superior.py
```

### `tests/`

Tests de pytest. Importan desde `codigo/` y validan el comportamiento. Los tests de los ejercicios tienen los asserts completos pero las funciones que testean en `ejercicios.py` están vacías (el alumno las implementa). Ejemplo:

```
tests/
  test_funciones_basicas.py
  test_ejercicios.py
```

### `run_tests.py`

Archivo **idéntico en todas las ramas**. Lanza pytest sobre la carpeta `tests/` de la rama actual:

```python
import subprocess, sys
subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], check=False)
```

El alumno lo ejecuta con `python run_tests.py` sin necesidad de conocer pytest.

### Entorno virtual compartido

- La carpeta `.venv/` está en `.gitignore` y **no se versiona**.
- Se crea una sola vez en la raíz del repositorio y sirve para todas las ramas (git no la borra al cambiar de rama porque está ignorada).
- Contiene únicamente `pytest` (y sus dependencias).
- Las instrucciones de setup están en el README de main:
  ```bash
  python -m venv .venv
  # Windows:
  .venv\Scripts\activate
  # Mac/Linux:
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Se activa una vez; mientras la sesión de terminal esté abierta, no hace falta volver a activarla.

### `requirements.txt`

```
pytest
```

Igual en todas las ramas. Cuando el alumno hace `git checkout Clase_2`, el archivo cambia si el contenido fuera diferente, pero como es idéntico no hay problema.

---

## Lo que el agente debe crear

### Paso 1: estructura de `main`

- Inicializar el repo con `main` como rama principal
- README de main completo (mismo estilo que el de referencia): tabla de ramas, método de actualización seguro, troubleshooting de git pull, temario completo, objetivos, requisitos con instrucciones del venv, recursos
- `.gitignore` con `.venv/`

### Paso 2: rama `alumnos`

- Igual que en el repo de referencia: `practica.py`, `mis_notas.py`, `readme.md` con guía de Git

### Paso 3: cada rama `Clase_N`

Para cada clase, crear la rama y añadir:
1. `readme.md` con el formato descrito (sección "Antes de empezar" al inicio, contenido detallado, proyecto propuesto, índice)
2. `apuntes.py` con teoría y ejemplos ejecutables del tema
3. `codigo/` con los módulos Python del tema
4. `ejercicios.py` con 3 ejercicios sin solución
5. `tests/` con los tests de pytest (los de ejercicios tienen asserts completos, la función a implementar está vacía en `ejercicios.py`)
6. `run_tests.py` (idéntico en todas las ramas)
7. `requirements.txt` (idéntico en todas las ramas)
8. `.gitignore` (incluye `.venv/`, `__pycache__/`, `*.pyc`)

### Paso 4: push

Hacer push de todas las ramas al remoto.

---

## Convenciones de estilo de commits

Los commits siguen el patrón `Rama: descripción en español`:

```
main: README completo del curso
Clase_1: apuntes, módulos, ejercicios y tests
Clase_1: limpieza y correcciones
alumnos: rama de práctica con guía de Git
```

---

## Notas importantes para el agente

- **No crear `README.md` en las ramas de clase** — solo `readme.md` (minúsculas). En Windows el sistema de archivos es case-insensitive, tener ambos en el índice de git causa problemas al hacer checkout.
- El método de pull recomendado siempre es `git fetch origin` + `git reset --hard origin/Clase_N`, nunca solo `git pull`. Debe aparecer en el README de main y al inicio de cada `readme.md` de clase.
- Los ejercicios no tienen solución en el repo. El alumno escribe la solución y ejecuta `python run_tests.py` para ver si pasan los tests.
- El tono es el de un profesor directo: explica el porqué, no solo el qué.
