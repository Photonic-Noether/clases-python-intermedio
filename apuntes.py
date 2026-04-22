# ============================================================
# CLASE 1 — HERRAMIENTAS DE PROYECTOS Y GIT AVANZADO
# ============================================================
# Este archivo es ejecutable de arriba a abajo.
# Léelo como un documento o ejecútalo para ver los outputs.
# ============================================================


# ===== RUFF: LINTER Y FORMATEADOR =====

# Un linter analiza el código sin ejecutarlo y avisa de problemas:
# - variables definidas pero nunca usadas
# - imports que no se usan
# - código inalcanzable (después de un return)
# - comparaciones siempre verdaderas o falsas

# Un formateador reescribe el código siguiendo un estilo consistente:
# - longitud máxima de línea
# - espacios alrededor de operadores
# - comillas simples vs dobles
# - líneas en blanco entre funciones

# Ruff hace las dos cosas, y es mucho más rápido que las alternativas
# (flake8, pylint, black, isort) porque está escrito en Rust.

# Instalación:
#   pip install ruff

# Uso básico:
#   ruff check .          → analiza todos los archivos .py del directorio
#   ruff check . --fix    → intenta corregir los problemas automáticamente
#   ruff format .         → reformatea todos los archivos

# Ejemplo de código que ruff marcaría:
def funcion_mal_formateada(x,y,z):
    resultado=x+y+z  # sin espacios alrededor de =
    import os  # import dentro de una función (error E401)
    variable_sin_usar = 42  # F841: variable asignada pero nunca usada
    return resultado

# Configuración en pyproject.toml:
# [tool.ruff]
# line-length = 88
# [tool.ruff.lint]
# select = ["E", "F", "I"]   # E=pycodestyle, F=pyflakes, I=isort
# ignore = ["E501"]           # ignorar líneas largas en algún caso concreto


# ===== PRE-COMMIT HOOKS =====

# Un hook de git es un script que git ejecuta automáticamente antes o
# después de operaciones como commit, push, etc.
# El hook pre-commit se ejecuta ANTES de que el commit se cree.
# Si el hook falla (exit code != 0), el commit no se crea.

# pre-commit es una herramienta que gestiona estos hooks de forma declarativa.

# Instalación:
#   pip install pre-commit

# Archivo .pre-commit-config.yaml en la raíz del repo:
# ─────────────────────────────────────────────────
# repos:
#   - repo: https://github.com/astral-sh/ruff-pre-commit
#     rev: v0.4.0
#     hooks:
#       - id: ruff            # ejecuta ruff check --fix
#       - id: ruff-format     # ejecuta ruff format
#   - repo: https://github.com/pre-commit/pre-commit-hooks
#     rev: v4.6.0
#     hooks:
#       - id: trailing-whitespace   # elimina espacios al final de línea
#       - id: end-of-file-fixer     # añade newline al final del archivo
#       - id: check-yaml            # valida archivos YAML
# ─────────────────────────────────────────────────

# Activar los hooks en el repositorio local:
#   pre-commit install

# Ejecutar los hooks manualmente sobre todos los archivos:
#   pre-commit run --all-files

# Saltar los hooks en un commit concreto (usar con cuidado):
#   git commit --no-verify -m "mensaje"


# ===== GIT AVANZADO =====

# --- git log avanzado ---
# Ver el historial como árbol de ramas (muy útil con múltiples ramas):
#   git log --graph --oneline --all --decorate

# --- git stash: guardar trabajo sin commitear ---
# Estás en mitad de algo y necesitas cambiar de rama urgentemente.
# No quieres commitear algo incompleto. Usas stash:

#   git stash              → guarda los cambios en un área temporal
#   git stash pop          → recupera el último stash y lo borra
#   git stash list         → lista todos los stashes guardados
#   git stash apply stash@{2}  → aplica el stash número 2 sin borrarlo
#   git stash drop stash@{0}   → borra el stash más reciente

# --- git rebase vs git merge ---
# Tienes la rama "feature" creada desde main, y main ha avanzado.
# Quieres integrar los cambios de main en tu feature.

# Con merge:
#   git checkout feature
#   git merge main
# Resultado: crea un commit de merge. Preserva la historia exacta.
# Pega cuando: quieres conservar la historia real del proyecto.

# Con rebase:
#   git checkout feature
#   git rebase main
# Resultado: mueve los commits de feature ENCIMA de main.
# La historia queda lineal (no hay commits de merge).
# Pega cuando: quieres un historial limpio y lineal.
# ¡Nunca hagas rebase de ramas ya publicadas (origin/X)!

# --- git cherry-pick ---
# Copiar un commit concreto de otra rama a la rama actual:
#   git cherry-pick abc1234   → aplica el commit abc1234 aquí
# Útil para traer un bugfix de una rama sin hacer merge completo.

# --- git reflog: recuperar commits "perdidos" ---
# Si hiciste git reset --hard y perdiste commits:
#   git reflog             → muestra el historial de HEAD
#   git checkout abc1234   → vas al commit perdido
#   git checkout -b rescate   → creas una rama desde ahí
# El reflog guarda todo lo que HEAD ha apuntado en los últimos 90 días.

# --- Resolución de conflictos ---
# Cuando git no puede fusionar automáticamente, marca el conflicto:
# <<<<<<< HEAD
# tu versión del código
# =======
# versión de la otra rama
# >>>>>>> otra-rama
#
# Editas el archivo, dejas la versión correcta, eliminas los marcadores,
# y luego: git add archivo.py → git commit

# --- git bisect: encontrar el commit que rompió algo ---
#   git bisect start
#   git bisect bad           → el estado actual está roto
#   git bisect good v1.0     → en v1.0 funcionaba
# Git va haciendo checkout de commits intermedios para que los pruebes.
# En cada uno dices "good" o "bad" hasta encontrar el commit culpable.


print("Apuntes de Clase 1 cargados correctamente.")
print("Explora el módulo 'codigo/herramientas.py' para ver funciones importables.")
