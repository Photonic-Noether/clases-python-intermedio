# Rama alumnos — Sandbox de práctica

Esta rama es tu espacio personal. Aquí puedes practicar Git y Python sin miedo a romper nada del curso.

## Qué hay aquí

- `practica.py` — archivo en blanco para que experimentes con código Python
- `mis_notas.py` — archivo para que apuntes tus notas de clase

## Para qué sirve esta rama

- Practicar los comandos de Git sin tocar las ramas del curso
- Probar código suelto que no quieres commitear en `Clase_N`
- Guardar apuntes propios, snippets, experimentos

## Guía de Git para esta rama

### Configuración inicial (si aún no lo has hecho)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Comandos que usarás más

```bash
# Ver en qué estado está tu repositorio
git status

# Ver qué cambios has hecho (aún no están en staging)
git diff

# Añadir un archivo al staging area (prepararlo para commit)
git add practica.py
git add .          # añade TODOS los archivos modificados (úsalo con cuidado)

# Crear un commit (guardar los cambios con un mensaje)
git commit -m "Mi primer experimento con closures"

# Ver el historial de commits
git log --oneline

# Cambiar a otra rama
git checkout Clase_1
git checkout alumnos   # volver aquí
```

### Deshacer cambios

```bash
# Deshacer cambios en un archivo (que aún no están en staging)
git restore practica.py

# Sacar un archivo del staging (sin perder los cambios)
git restore --staged practica.py

# Deshacer el último commit (mantiene los cambios en el working tree)
git reset HEAD~1

# Ver cómo estaba un archivo en un commit anterior
git show abc1234:practica.py
```

### Guardar trabajo a medias sin commitear

```bash
# Guardar el trabajo actual en un área temporal
git stash

# Recuperarlo
git stash pop

# Ver qué tienes guardado
git stash list
```

### Sincronizar con el servidor

```bash
# Descargar cambios del servidor sin aplicarlos
git fetch origin

# Actualizar esta rama con lo que hay en el servidor (método seguro)
git reset --hard origin/alumnos

# Subir tus commits al servidor
git push origin alumnos
```

### Si `git pull` da error

```bash
# Solución segura: descarga y aplica el estado del servidor
git fetch origin
git reset --hard origin/alumnos
```

### Hacer un fork y una Pull Request

1. Ve a GitHub y haz clic en "Fork" — crea una copia del repo en tu cuenta
2. Clona TU fork: `git clone https://github.com/TU-USUARIO/clases-python-intermedio.git`
3. Crea una rama para tus ejercicios: `git checkout -b entrega/Clase_1-tu-nombre`
4. Haz tus cambios, commits, y push
5. En GitHub, abre una Pull Request desde tu rama hacia `development` del repo original

### Recursos de Git

- [Pro Git (libro gratuito en español)](https://git-scm.com/book/es/v2)
- [Learn Git Branching (interactivo)](https://learngitbranching.js.org/?locale=es_ES)
- [GitHub Docs](https://docs.github.com/es)
