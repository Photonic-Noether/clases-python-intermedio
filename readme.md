# Clase 1 — Herramientas de proyectos y git avanzado

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_1
> ```
> Si has hecho commits accidentales, `git pull` fallará con un error de ramas divergentes. Este par de comandos siempre funciona: descarga el estado del servidor y descarta cualquier cambio local.

## ¿En qué rama estás?

Esta rama cubre cómo configurar un proyecto Python de forma profesional (ruff, pre-commit, linters) y las herramientas avanzadas de Git que usarás en el día a día de cualquier equipo.

## Cómo cambiar de rama

```bash
git checkout main      # Volver al README general del curso
git checkout Clase_2   # Ir a la siguiente clase
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

**Ruff — linter y formateador todo-en-uno**
- Qué son los linters y para qué sirven (detectar errores antes de ejecutar)
- Diferencia entre linter (detecta problemas) y formateador (los corrige automáticamente)
- Instalar ruff: `pip install ruff`
- `ruff check .` — analiza el código en busca de problemas
- `ruff format .` — formatea el código automáticamente
- `pyproject.toml` — cómo configurar las reglas activas, longitud de línea, exclusiones

**Pre-commit hooks**
- Qué es un hook de git: un script que se ejecuta automáticamente antes/después de un commit
- Instalar pre-commit: `pip install pre-commit`
- `.pre-commit-config.yaml` — qué hooks usar y en qué versión
- `pre-commit install` — conectar los hooks al repositorio git local
- Hooks más útiles: `ruff`, `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`
- Cómo saltarse un hook puntualmente: `git commit --no-verify` (úsalo con cabeza)

**Git avanzado**
- `git log --graph --oneline --all` — ver el historial como árbol de ramas
- `git stash` y `git stash pop` — guardar trabajo a medias sin commitear
- `git stash list` y `git stash apply stash@{N}` — gestionar múltiples stashes
- `git rebase` vs `git merge` — diferencias, ventajas e inconvenientes de cada uno
- `git cherry-pick <hash>` — copiar un commit concreto a la rama actual
- `git reflog` — recuperar commits "perdidos" tras un reset o rebase
- Resolución de conflictos: `<<<<<<`, `=======`, `>>>>>>>` y cómo resolverlos
- `git bisect` — encontrar el commit que introdujo un bug

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

Ejecuta `python run_tests.py` para comprobar si tu solución es correcta.

## Proyecto propuesto (~30 minutos)

**Configurar un proyecto Python profesional desde cero:**

Crea un directorio nuevo fuera de este repositorio y haz lo siguiente:

1. Inicializa un repositorio git (`git init`)
2. Crea y activa un entorno virtual
3. Crea un `pyproject.toml` con la configuración de ruff: máx. 88 caracteres por línea, activa las reglas `E`, `F` e `I` (isort)
4. Instala ruff y pre-commit
5. Crea un `.pre-commit-config.yaml` que ejecute `ruff check` y `ruff format` antes de cada commit
6. Ejecuta `pre-commit install` para conectar los hooks
7. Escribe un módulo Python con al menos 3 funciones con algún error de estilo intencional
8. Intenta hacer un commit y observa cómo ruff lo bloquea y corrige automáticamente
9. Confirma el commit una vez el código pase los checks

El objetivo es que el flujo `escribir código → git commit → pre-commit hook → ruff check → ruff format → commit exitoso` funcione de principio a fin.

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_1:ejercicios.py > ejercicios/clase_1/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_1/tu-nombre.py
git commit -m "Clase_1: ejercicios - tu-nombre"
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
