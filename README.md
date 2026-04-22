# Python Intermedio — Tajamar

Repositorio del curso de Python Intermedio de Tajamar, impartido por Joaquín Hernández.

## Cómo está organizado este repositorio

El repositorio usa **una rama de Git por clase**. La rama `main` solo contiene este README; el código y los ejercicios están en las ramas de clase.

| Rama | Contenido |
|------|-----------|
| `main` | README del curso completo |
| `development` | Rama de integración — aquí se entregan los ejercicios |
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
- `apuntes.py` — teoría con código ejecutable y comentarios extensos
- `codigo/` — módulos Python importables con los ejemplos de la clase
- `ejercicios.py` — 3 ejercicios sin solución para practicar
- `tests/` — tests de pytest que validan tu solución
- `run_tests.py` — lanza los tests con un solo comando

---

## Configuración inicial (solo una vez)

Clona el repositorio:

```bash
git clone https://github.com/Photonic-Noether/clases-python-intermedio.git
cd clases-python-intermedio
```

Crea el entorno virtual en la raíz del repositorio:

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

Cambia a la primera clase e instala las dependencias:

```bash
git checkout Clase_1
pip install -r requirements.txt
```

El entorno virtual vive en `.venv/` y **no se sube a Git** (está en `.gitignore`). Puedes cambiar de rama libremente y el `.venv/` permanece porque Git lo ignora. Actívalo una vez por sesión de terminal.

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

**No uses `git pull` directamente en las ramas de clase.** Si has modificado algún archivo accidentalmente y luego haces `git pull`, Git puede fallar por conflictos de ramas divergentes. Usa siempre este método en su lugar:

```bash
git fetch origin
git reset --hard origin/Clase_1   # Sustituye Clase_1 por la rama que quieras
```

`git fetch origin` descarga los cambios del servidor sin aplicarlos. `git reset --hard` descarta cualquier cambio local y deja la rama exactamente igual que el servidor. **Este método siempre funciona**, incluso si tienes commits accidentales o el historial divergió.

---

## Si `git pull` da error

Si ves algo como esto:

```
hint: You have divergent branches and need to specify how to reconcile them.
fatal: Need to specify how to reconcile divergent branches.
```

No entres en pánico. Significa que tu rama local y la del servidor han divergido. La solución:

```bash
git fetch origin
git reset --hard origin/Clase_N   # Sustituye Clase_N por la rama donde estás
```

Si tenías trabajo que no quieres perder, guárdalo antes de hacer el reset:

```bash
git stash                          # Guarda los cambios en un área temporal
git fetch origin
git reset --hard origin/Clase_N
git stash pop                      # Recupera los cambios guardados
```

---

## Cómo ejecutar los tests

En cada rama de clase hay un archivo `run_tests.py`. Con el entorno virtual activado, desde la raíz de la rama:

```bash
python run_tests.py
```

Verás los tests en verde (pasan) o rojo (fallan). Cuando implementes los ejercicios en `ejercicios.py` y todos los tests pasen, tu solución es correcta.

---

## Cómo entregar ejercicios

Los ejercicios se entregan mediante **Pull Request a la rama `development`**. La rama `main` está protegida y no recibe PRs de alumnos.

Flujo completo paso a paso:

```bash
# 1. Ve a la rama de tu clase y actualízala
git checkout Clase_1
git fetch origin
git reset --hard origin/Clase_1

# 2. Crea una rama personal para tu entrega
git checkout -b entrega/Clase_1-tu-nombre

# 3. Implementa los ejercicios en ejercicios.py

# 4. Comprueba que los tests pasan
python run_tests.py

# 5. Sube tu rama y abre la PR
git add ejercicios.py
git commit -m "Clase 1: ejercicios - tu-nombre"
git push origin entrega/Clase_1-tu-nombre
```

Luego ve a GitHub — verás un botón para abrir la Pull Request. Asegúrate de que el destino es `development`, **no `main`**.

**Normas de entrega:**
- Las PR van siempre a `development`, nunca a `main`
- El nombre de la rama de entrega sigue el formato `entrega/Clase_N-tu-nombre`
- Solo modifica `ejercicios.py` — no toques `apuntes.py`, `codigo/` ni `tests/`
- Asegúrate de que `python run_tests.py` no da errores antes de abrir la PR

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
