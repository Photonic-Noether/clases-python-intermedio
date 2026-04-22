# Python Intermedio — Tajamar

Repositorio del curso de Python Intermedio de Tajamar, impartido por Joaquín Hernández.

## Cómo está organizado este repositorio

El repositorio usa **una rama de Git por clase**. La rama `main` solo contiene este README; el código y los ejercicios están en las ramas de clase. Las entregas se hacen mediante Pull Request a `development`.

| Rama | Contenido |
|------|-----------|
| `main` | README del curso completo |
| `development` | Carpeta de entregas (`ejercicios/`) + guía de entrega |
| `Clase_1` | Herramientas de proyectos y git avanzado |
| `Clase_2` | Programación funcional y OOP avanzada |
| `Clase_3` | Iteradores, generadores y corrutinas |
| `Clase_4` | Closures, callbacks, memoization y decoradores |
| `Clase_5` | Unit testing e integration testing con pytest |
| `Clase_6` | Librería estándar 1 + Type hinting y genéricos |
| `Clase_7` | Concurrencia básica: Hilos |
| `Clase_8` | Librería estándar 2 + ABCs vs Protocolos + Docker |
| `alumnos` | Sandbox de práctica libre |

Cada rama de clase contiene:
- `readme.md` — instrucciones y descripción de la clase
- `apuntes.py` — teoría con código ejecutable y comentarios extensos
- `codigo/` — módulos Python importables con los ejemplos de la clase
- `ejercicios/clase_N/ejercicios.py` — 3 ejercicios sin solución para practicar
- `tests/unit/` — tests unitarios
- `tests/integration/` — tests de integración
- `tests/conftest.py` — fixtures compartidas
- `run_tests.py` — lanza los tests con un solo comando (`pytest`)
- `pyproject.toml` — configuración de pytest, ruff y mypy
- `requirements.txt` — dependencias (pytest, pre-commit desde Clase 2)
- `.pre-commit-config.yaml` — hooks de ruff y mypy (Clase 2 en adelante)

---

## Configuración inicial (solo una vez)

### 1. Haz un fork del repositorio

En GitHub, haz clic en **Fork** (arriba a la derecha). Esto crea una copia del repositorio bajo tu cuenta.

### 2. Clona tu fork

```bash
git clone https://github.com/TU-USUARIO/clases-python-intermedio.git
cd clases-python-intermedio
```

### 3. Añade el repositorio original como `upstream`

```bash
git remote add upstream https://github.com/Photonic-Noether/clases-python-intermedio.git
```

### 4. Crea el entorno virtual

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

El entorno virtual vive en `.venv/` y **no se sube a Git** (está en `.gitignore`). Actívalo una vez por sesión de terminal.

---

## Cómo cambiar de rama

```bash
git checkout Clase_1     # Ir a la clase 1
git checkout Clase_2     # Ir a la clase 2
git checkout alumnos     # Ir a la rama de práctica
git checkout main        # Volver al README general
```

---

## Cómo actualizar una rama (método seguro)

**No uses `git pull` directamente.** Si has modificado algún archivo accidentalmente y luego haces `git pull`, Git puede fallar por conflictos de ramas divergentes. Usa siempre este método:

```bash
git fetch upstream
git reset --hard upstream/Clase_1   # Sustituye Clase_1 por la rama que quieras
```

`git fetch upstream` descarga los cambios del servidor sin aplicarlos. `git reset --hard` descarta cualquier cambio local y deja la rama exactamente igual que el servidor. **Este método siempre funciona**, incluso si tienes commits accidentales o el historial divergió.

---

## Si `git pull` da error

Si ves algo como esto:

```
hint: You have divergent branches and need to specify how to reconcile them.
fatal: Need to specify how to reconcile divergent branches.
```

No entres en pánico. Significa que tu rama local y la del servidor han divergido. La solución:

```bash
git fetch upstream
git reset --hard upstream/Clase_N   # Sustituye Clase_N por la rama donde estás
```

Si tenías trabajo que no quieres perder, guárdalo antes de hacer el reset:

```bash
git stash                            # Guarda los cambios en un área temporal
git fetch upstream
git reset --hard upstream/Clase_N
git stash pop                        # Recupera los cambios guardados
```

---

## Cómo ejecutar los tests

En cada rama de clase hay un archivo `run_tests.py`. Con el entorno virtual activado:

```bash
python run_tests.py
```

Verás los tests en verde (pasan) o rojo (fallan). Cuando implementes los ejercicios en `ejercicios/clase_N/ejercicios.py` y todos los tests pasen, tu solución es correcta. El `pyproject.toml` ya está configurado para que `pytest` encuentre los tests en `tests/unit/` y `tests/integration/` automáticamente.

---

## Cómo entregar ejercicios

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**. La rama `main` está protegida y no recibe PRs de alumnos.

### Por qué `development` y no `main`

La rama `main` está protegida: solo el profesor puede escribir en ella. La rama `development` es la rama de integración diseñada para recibir vuestras entregas.

### Estructura de entregas

En `development` hay una carpeta `ejercicios/` con una subcarpeta por clase:

```
ejercicios/
├── clase_1/   ← deposita aquí tu archivo para la Clase 1
├── clase_2/
├── clase_3/
├── clase_4/
├── clase_5/
├── clase_6/
├── clase_7/
└── clase_8/
```

### Flujo completo de entrega

```bash
# 1. Sincroniza tu fork con el repositorio original
git fetch upstream
git checkout development
git merge upstream/development
git push origin development

# 2. Obtén el archivo de ejercicios de la clase
git show Clase_1:ejercicios/clase_1/ejercicios.py > ejercicios/clase_1/tu-nombre.py

# 3. Implementa los ejercicios en ejercicios/clase_1/tu-nombre.py

# 4. Comprueba que los tests pasan (cambia temporalmente a la rama de clase)
git stash
git checkout Clase_1
cp ejercicios/clase_1/tu-nombre.py ejercicios/clase_1/ejercicios.py
pytest            # pyproject.toml lo configura todo automáticamente
git checkout development
git stash pop

# 5. Haz commit y sube a tu fork
git add ejercicios/clase_1/tu-nombre.py
git commit -m "Clase 1: ejercicios - tu-nombre"
git push origin development
```

Luego ve a tu fork en GitHub y abre la Pull Request. Asegúrate de que el destino es `development`, **no `main`**.

**Normas de entrega:**
- El archivo se llama `tu-nombre.py` (sin espacios ni tildes)
- Va en la subcarpeta correcta: `ejercicios/clase_N/`
- La PR va de `tu-fork/development` → `upstream/development`
- Asegúrate de que los tests pasan antes de abrir la PR
- No toques los archivos de otros alumnos

Para la guía completa del flujo fork+PR, consulta el README de la rama `development`.

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

---

## Objetivos de aprendizaje

Al terminar el curso serás capaz de:

- Configurar un proyecto Python profesional con linters, formateadores y hooks de pre-commit
- Usar técnicas de programación funcional avanzada y OOP robusta
- Implementar iteradores, generadores y corrutinas propios
- Crear y combinar decoradores complejos con y sin argumentos
- Escribir tests unitarios y de integración con pytest siguiendo buenas prácticas
- Usar type hints y genéricos para escribir código más robusto y mantenible
- Aplicar los patrones de diseño más usados en Python
- Escribir código concurrente básico con hilos
- Contenerizar una aplicación Python con Docker

---

## Requisitos previos

- Python 3.11 o superior instalado
- Git instalado y configurado (`git config --global user.name "Tu Nombre"` y `git config --global user.email "tu@email.com"`)
- Cuenta en GitHub
- Conocimientos básicos de Python: funciones, clases, listas, diccionarios

---

## Recursos adicionales

- [Documentación oficial de Python 3](https://docs.python.org/3/)
- [pytest — documentación oficial](https://docs.pytest.org/)
- [ruff — linter y formateador](https://docs.astral.sh/ruff/)
- [Real Python — tutoriales avanzados](https://realpython.com/)
- [Python Patterns — patrones de diseño en Python](https://python-patterns.guide/)
- [Fluent Python 2ª edición (libro recomendado)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
