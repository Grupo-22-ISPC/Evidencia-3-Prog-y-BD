# Informe de Actividades del Proyecto - Distribución de Tareas

## Introducción

Este documento detalla la distribución de responsabilidades y las actividades asignadas a cada integrante del equipo para el desarrollo del proyecto de la Actividad Integradora. El trabajo se ha dividido en 5 roles principales para asegurar una contribución equitativa y organizada.

## Contribuciones por Integrante

### 1. Gastón Alonso -  Proyecto y Arquitectura de Software

**Rol Principal:** Encargado de la estructura general del proyecto y el flujo principal de la aplicación de consola.

* **Tareas Asignadas:**
    * Creación y configuración inicial del repositorio en GitHub, incluyendo el archivo `.gitignore`.
    * Definición de la estructura de carpetas del proyecto (`/src`, `/sql`, `/docs`).
    * Implementación del archivo `main.py`, que sirve como punto de entrada para iniciar la aplicación.
    * Desarrollo de la clase `Sistema` (`sistema.py`), responsable de gestionar la interfaz de usuario, los menús principales y la interacción con el usuario.
    * Coordinación general del equipo y seguimiento de tareas (gestión del tablero Kanban o similar).

### 2. Martín - Diseñador de Base de Datos (DBA)

**Rol Principal:** Responsable del análisis y diseño conceptual de la base de datos.

* **Tareas Asignadas:**
    * Identificación de las entidades (`usuarios`, `roles`), sus atributos y las relaciones entre ellas.
    * Aplicación del proceso de normalización para asegurar que el diseño alcance la Tercera Forma Normal (3FN).
    * Creación del Diagrama Entidad-Relación (DER) para visualizar el modelo. El entregable es el archivo `modelo_relacional.png`.
    * Redacción de la documentación técnica del diseño de la base de datos, explicando las tablas, columnas y decisiones tomadas. El entregable es el archivo `diseno_db.md`.

### 3. Gerardo - Desarrollador de Base de Datos (SQL)

**Rol Principal:** Encargado de traducir el diseño de la base de datos a código SQL funcional.

* **Tareas Asignadas:**
    * Desarrollo del script `crear_db.sql` para la creación de la base de datos y todas las tablas (`roles` y `usuarios`).
    * Inclusión en el script de los comandos para insertar los datos iniciales (roles y usuarios de prueba).
    * Desarrollo del script `crud_usuarios.sql` con consultas de ejemplo para cada operación CRUD (Crear, Leer, Actualizar, Eliminar).
    * Realización de pruebas para asegurar que los scripts SQL se ejecuten correctamente y sin errores.

### 4. Emilce - Desarrollador de Backend (Lógica de Negocio)

**Rol Principal:** Responsable de implementar el "corazón" de la lógica de la aplicación en Python.

* **Tareas Asignadas:**
    * Desarrollo de la clase `Usuario` (`usuario.py`), que define la estructura de datos para un usuario.
    * Implementación de la clase `GestorUsuarios` (`gestor_usuarios.py`), que contiene toda la lógica de negocio: registrar, iniciar sesión, listar, cambiar rol y eliminar usuarios.
    * Inclusión de validaciones de datos dentro del gestor (ej. contraseña segura, usuario no existente).
    * Asegurar que la lógica de negocio sea independiente de la interfaz de usuario.

### 5. Kevin - Líder de Documentación y Calidad (QA)

**Rol Principal:** Encargado de toda la documentación orientada al desarrollador y de asegurar la calidad de la presentación del proyecto.

* **Tareas Asignadas:**
    * Creación del Diagrama de Clases UML (`diagrama_clases.png`) que representa la estructura del código Python.
    * Redacción de la documentación del diseño de clases (`diseno_clases.md`), explicando el propósito de cada clase, sus atributos y métodos.
    * Configuración y redacción de todo el contenido de la **Wiki de GitHub**, creando las páginas y enlazándolas.
    * Redacción del archivo `README.md` principal del repositorio, que debe servir como una introducción general y guía de navegación del proyecto.
    * Revisión general de la coherencia entre las distintas partes del proyecto.

---

### Plan de Acción

Con esta distribución, cada integrante tiene un conjunto claro de archivos y responsabilidades. El siguiente paso es que cada uno trabaje en su parte asignada y, una vez completada, suba sus archivos correspondientes al repositorio de Git mediante un `commit` descriptivo.
