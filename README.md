# Python Intermedio — Tajamar · Rama `development`

Repositorio del curso de Python Intermedio de Tajamar, impartido por Joaquín Hernández.

Esta rama (`development`) es la rama de integración del curso. Aquí se reciben todas las entregas de ejercicios mediante Pull Request desde el fork de cada alumno.

---

## Entrega de ejercicios — guía completa

> **Lee esto antes de nada.** Todo el flujo de entrega funciona sobre esta rama.

### Por qué `development` y no `main`

La rama `main` está protegida: solo el profesor puede escribir en ella. No aceptará Pull Requests de alumnos. La rama `development` es la rama de integración diseñada exactamente para recibir vuestras entregas — es donde el profesor revisa el trabajo y lo incorpora al historial del curso.

**Regla de oro: tus PRs siempre van de `tu-fork/development` → `upstream/development`.**

---

### Paso 1 — Haz un fork del repositorio

En GitHub, haz clic en **Fork** (arriba a la derecha). Esto crea una copia del repositorio bajo tu cuenta. Solo necesitas hacerlo una vez en todo el curso.

---

### Paso 2 — Clona tu fork

```bash
git clone https://github.com/TU-USUARIO/clases-python-intermedio.git
cd clases-python-intermedio
```

Sustituye `TU-USUARIO` por tu nombre de usuario de GitHub.

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

Cambia a la rama de la clase que toca y obtén los ejercicios:

```bash
git fetch upstream
git checkout Clase_1       # o Clase_2, Clase_3...
git reset --hard upstream/Clase_1
```

Copia el archivo de ejercicios a la carpeta de entregas de `development`:

```bash
git show Clase_1:ejercicios.py > /tmp/ejercicios_clase1.py
```

Vuelve a `development` en tu fork, pega el archivo y trabaja en él:

```bash
git checkout development
cp /tmp/ejercicios_clase1.py ejercicios/clase_1/tu-nombre.py
```

Implementa los ejercicios en `ejercicios/clase_1/tu-nombre.py`.

---

### Paso 6 — Comprueba que los tests pasan

Los tests están en la rama de clase. Para ejecutarlos, copia también el archivo de tests:

```bash
git show Clase_1:tests/test_ejercicios.py > /tmp/test_ejercicios.py
```

Luego corre pytest apuntando a tu archivo:

```bash
pytest /tmp/test_ejercicios.py --import-mode=importlib \
    --override-ini="python_files=test_*.py" \
    -v
```

O más sencillo: cambia temporalmente a la rama de clase, pega tu implementación en `ejercicios.py` y ejecuta `python run_tests.py`. Cuando pasen, vuelve a `development`.

---

### Paso 7 — Haz commit y sube a tu fork

```bash
git add ejercicios/clase_1/tu-nombre.py
git commit -m "Clase 1: ejercicios - tu-nombre"
git push origin development
```

---

### Paso 8 — Abre la Pull Request

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
git merge upstream/development   # o git reset --hard upstream/development
git push origin development
```

---

## Estructura de la carpeta `ejercicios/`

```
ejercicios/
├── clase_1/
│   ├── alumno1.py
│   ├── alumno2.py
│   └── ...
├── clase_2/
│   └── ...
├── clase_3/
│   └── ...
├── clase_4/
│   └── ...
├── clase_5/
│   └── ...
├── clase_6/
│   └── ...
├── clase_7/
│   └── ...
└── clase_8/
    └── ...
```

Cada alumno añade su archivo con el formato `tu-nombre.py` dentro de la subcarpeta de su clase. No toques los archivos de otros alumnos.

---

## Normas de entrega

- El archivo se llama `tu-nombre.py` (sin espacios, sin tildes)
- Va en la subcarpeta correcta: `ejercicios/clase_N/`
- La PR va siempre de `tu-fork/development` → `upstream/development`
- Asegúrate de que los tests pasan antes de abrir la PR
- No modifiques `apuntes.py`, `tests/` ni los archivos de otros alumnos

---

## Organización del repositorio

El repositorio usa **una rama por clase**. Esta rama (`development`) solo contiene este README y la carpeta `ejercicios/`. El código y los apuntes están en las ramas de clase.

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
