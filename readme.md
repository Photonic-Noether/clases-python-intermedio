# Clase 5 — Unit testing e integration testing con pytest

> **Antes de mirar el código, actualiza esta rama:**
> ```bash
> git fetch upstream
> git reset --hard upstream/Clase_5
> ```

## ¿En qué rama estás?

Esta rama cubre unit testing e integration testing con pytest: fixtures, parametrize, mocking, conftest.py, y los patrones de diseño Estrategia y Constructor.

## Cómo cambiar de rama

```bash
git checkout Clase_4   # Ir a la clase anterior
git checkout Clase_6   # Ir a la siguiente clase
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

**pytest — fundamentos**
- `assert` en pytest: cómo pytest mejora los mensajes de error
- Convenciones: archivos `test_*.py`, funciones `test_*`, clases `Test*`
- Ejecutar tests: `pytest`, `pytest -v`, `pytest -k "nombre"`

**Fixtures**
- `@pytest.fixture`: preparar el estado antes del test y limpiarlo después
- Scope: `function` (por defecto), `class`, `module`, `session`
- `conftest.py`: compartir fixtures entre varios archivos de test
- Fixtures como dependencias de otras fixtures
- `yield` en fixtures: configurar y limpiar (setup/teardown)

**Parametrize**
- `@pytest.mark.parametrize`: ejecutar el mismo test con múltiples entradas
- Parametrizar con múltiples argumentos
- Combinar parametrize con fixtures

**Marks**
- `@pytest.mark.skip` y `@pytest.mark.skipif`: saltar tests condicionalmente
- `@pytest.mark.xfail`: tests que se espera que fallen
- Marks personalizados: `@pytest.mark.lento`, `@pytest.mark.integracion`

**Mocking**
- `monkeypatch`: parchear funciones y atributos durante el test
- `unittest.mock.MagicMock` y `unittest.mock.patch`
- Cuándo mockear: dependencias externas (API, DB, sistema de archivos)
- Cuándo NO mockear: la lógica de negocio que queremos probar

**Tests de integración**
- Diferencia entre unit test (una unidad aislada) e integration test (varias juntas)
- Organización: carpeta `tests/unit/` y `tests/integration/`
- Fixtures de integración: bases de datos en memoria, servidores de test

**Patrones de diseño**
- **Estrategia**: encapsular un algoritmo intercambiable en una clase
- **Constructor**: construir un objeto complejo paso a paso con un builder

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos. Ejecuta `python run_tests.py` para comprobar tu solución.

## Proyecto propuesto (~30 minutos)

**Testear un sistema bancario con pytest:**

El módulo `codigo/banco.py` tiene una clase `CuentaBancaria` con bugs. Tu misión:

1. Lee la clase y escribe tests que describan su comportamiento correcto
2. Ejecuta los tests y observa cuáles fallan (eso revela los bugs)
3. Corrige los bugs en `codigo/banco.py` hasta que todos los tests pasen
4. Añade al menos 3 fixtures y usa `@pytest.mark.parametrize` en algún test
5. Usa `monkeypatch` para testear el método que llama a una API externa

---

## Cómo entregar esta clase

Las entregas se hacen mediante **Pull Request de `tu-fork/development` a `upstream/development`**.

### Flujo rápido

```bash
# 1. Asegúrate de estar en tu fork y en development
git checkout development

# 2. Copia el archivo de ejercicios a la carpeta de entregas
git show Clase_5:ejercicios.py > ejercicios/clase_5/tu-nombre.py

# 3. Implementa los ejercicios en ese archivo

# 4. Commit y push a tu fork
git add ejercicios/clase_5/tu-nombre.py
git commit -m "Clase_5: ejercicios - tu-nombre"
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
