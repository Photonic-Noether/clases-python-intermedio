# Python Intermedio — Tajamar · Rama `development`

Repositorio del curso de Python Intermedio de Tajamar, impartido por Joaquín Hernández.

Esta rama (`development`) es la rama de integración del curso. Aquí se reciben todas las entregas de ejercicios mediante Pull Request desde el fork de cada alumno.

---

## Cómo quedan los ejercicios en el repositorio

Este es el aspecto que tiene la carpeta `ejercicios/` en `upstream/development` conforme los alumnos van entregando. Cada alumno añade **su propio archivo** con su nombre — nunca modifica los de los demás. Por eso nunca hay conflictos de merge.

```
upstream/development
└── ejercicios/
    ├── clase_1/
    │   ├── .gitkeep           ← placeholder del profesor
    │   ├── juan-garcia.py     ← PR de Juan
    │   ├── ana-lopez.py       ← PR de Ana
    │   └── marta-ruiz.py      ← PR de Marta
    ├── clase_2/
    │   ├── .gitkeep
    │   ├── juan-garcia.py
    │   └── ana-lopez.py
    ├── clase_3/
    │   ├── .gitkeep
    │   └── juan-garcia.py
    ...

rama Clase_3 (separada)
└── ejercicios/
    └── clase_3/
        └── ejercicios.py      ← stubs del profesor (punto de partida)
```

**Por qué no hay conflictos:** `ejercicios.py` (rama Clase_3) y `juan-garcia.py` (development) son nombres distintos en la misma carpeta — git los combina sin problema. Y cada alumno usa su propio nombre, así que ninguna PR choca con otra.

---

## Entrega de ejercicios — guía completa

> **Regla de oro: tus PRs siempre van de `tu-fork/development` → `upstream/development`.**

### Por qué `development` y no `main`

La rama `main` está protegida: solo el profesor puede escribir en ella. La rama `development` es la rama de integración diseñada para recibir vuestras entregas.

---

### Paso 1 — Haz un fork del repositorio

En GitHub, haz clic en **Fork** (arriba a la derecha). Esto crea una copia del repositorio bajo tu cuenta. Solo necesitas hacerlo una vez en todo el curso.

---

### Paso 2 — Clona tu fork

```bash
git clone https://github.com/TU-USUARIO/clases-python-intermedio.git
cd clases-python-intermedio
```

---

### Paso 3 — Añade el repositorio original como `upstream`

```bash
git remote add upstream https://github.com/Photonic-Noether/clases-python-intermedio.git
```

Verifica que tienes los dos remotos:

```bash
git remote -v
# origin    https://github.com/TU-USUARIO/clases-python-intermedio.git (fetch)
# origin    https://github.com/TU-USUARIO/clases-python-intermedio.git (push)
# upstream  https://github.com/Photonic-Noether/clases-python-intermedio.git (fetch)
# upstream  https://github.com/Photonic-Noether/clases-python-intermedio.git (push)
```

Solo necesitas hacer esto una vez.

---

### Paso 4 — Configura el entorno virtual

```bash
python -m venv .venv
```

Actívalo:

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

---

### Paso 5 — Trabaja en la clase

Tienes dos métodos equivalentes para obtener los ejercicios y testearlos. Elige el que prefieras.

#### Método A — copiar el archivo con `git show`

```bash
# Estás en development. Copia el archivo de stubs con tu nombre:
git fetch upstream
git show upstream/Clase_1:ejercicios/clase_1/ejercicios.py > ejercicios/clase_1/tu-nombre.py

# Implementa los ejercicios en tu-nombre.py

# Para testear, cambia temporalmente a la rama de clase:
git stash
git checkout Clase_1
cp ejercicios/clase_1/tu-nombre.py ejercicios/clase_1/ejercicios.py
pytest                      # pyproject.toml configura todo automáticamente
git checkout development
git stash pop
```

#### Método B — trabajar en la rama de clase y copiar solo el resultado

Implementas y testeas directamente en la rama de clase (donde ya están los tests). Al final copias **únicamente** el archivo de ejercicios a `development`, sin ensuciar la rama con archivos que no corresponden.

```bash
# 1. Crea una rama local de trabajo basada en la clase
git fetch upstream
git checkout -b trabajo-clase-1 upstream/Clase_1

# 2. Implementa los ejercicios en ejercicios/clase_1/ejercicios.py

# 3. Testea directamente — los tests ya están en tests/unit/ e integration/
pytest

# 4. Cuando todo pase, ve a development y trae SOLO el archivo de ejercicios
git checkout development
git checkout trabajo-clase-1 -- ejercicios/clase_1/ejercicios.py

# 5. Renómbralo con tu nombre y elimina el original
cp ejercicios/clase_1/ejercicios.py ejercicios/clase_1/tu-nombre.py
git restore --staged ejercicios/clase_1/ejercicios.py
rm ejercicios/clase_1/ejercicios.py
```

> `git checkout rama -- ruta/archivo` trae **únicamente ese archivo** desde otra rama, sin hacer merge. La PR a `upstream/development` solo contendrá `tu-nombre.py`.

---

### Paso 6 — Haz commit y sube a tu fork

```bash
git add ejercicios/clase_1/tu-nombre.py
git commit -m "Clase 1: ejercicios - tu-nombre"
git push origin development
```

---

### Paso 7 — Abre la Pull Request

Ve a tu fork en GitHub. Verás un botón **"Compare & pull request"**. Haz clic.

Comprueba que los campos son:

| Campo | Valor |
|-------|-------|
| **base repository** | `Photonic-Noether/clases-python-intermedio` |
| **base** | `development` |
| **head repository** | `TU-USUARIO/clases-python-intermedio` |
| **compare** | `development` |

Escribe un título claro (`Clase 1: ejercicios - tu-nombre`) y haz clic en **Create pull request**.

---

### Mantener tu fork actualizado

Antes de empezar cada clase, sincroniza tu fork con el repositorio original:

```bash
git fetch upstream
git checkout development
git merge upstream/development
git push origin development
```

---

## Normas de entrega

- El archivo se llama `tu-nombre.py` (sin espacios, sin tildes) — p.ej. `juan-garcia.py`
- Va en la subcarpeta correcta: `ejercicios/clase_N/`
- La PR va siempre de `tu-fork/development` → `upstream/development`
- Asegúrate de que los tests pasan (`pytest`) antes de abrir la PR
- No modifiques los archivos de otros alumnos

---

## Organización del repositorio

El repositorio usa **una rama por clase**. Esta rama (`development`) contiene este README y la carpeta `ejercicios/`. El código y los apuntes están en las ramas de clase.

| Rama | Contenido |
|------|-----------|
| `main` | README del curso completo |
| `development` | Carpeta de entregas + este README |
| `Clase_1` | Herramientas de proyectos y git avanzado |
| `Clase_2` | Programación funcional y OOP avanzada |
| `Clase_3` | Iteradores, generadores y corrutinas |
| `Clase_4` | Closures, callbacks, memoization y decoradores |
| `Clase_5` | Unit testing e integration testing con pytest |
| `Clase_6` | Librería estándar 1 + Type hinting y genéricos |
| `Clase_7` | Concurrencia básica: Hilos |
| `Clase_8` | Librería estándar 2 + ABCs vs Protocolos + Docker |
| `alumnos` | Sandbox de práctica libre |

---

## Temario

| Clase | Contenido |
|-------|-----------|
| **Clase 1** | Herramientas de proyectos (ruff, precommit, linters) y git avanzado |
| **Clase 2** | Programación funcional y OOP avanzada (`functools`, `any/all`, `reduce`, `map`, `property`, atributos gestionados, métodos dunder, `classmethod`, `__new__`) |
| **Clase 3** | Iteradores, generadores y corrutinas. Patrón de diseño Iterador (`itertools`) |
| **Clase 4** | Closures, callbacks, memoization y decoradores. Patrones Fábrica y Decorador |
| **Clase 5** | Unit testing e integration testing con pytest. Patrones Estrategia y Constructor |
| **Clase 6** | Librería estándar 1 + Type hinting y genéricos. Patrón Puente |
| **Clase 7** | Concurrencia básica: Hilos (`threading`) |
| **Clase 8** | Librería estándar 2 + ABCs vs Protocolos. Introducción a Docker |
