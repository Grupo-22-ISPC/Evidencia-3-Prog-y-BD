# Sistema de Gestión de Usuarios 🧑💻

Este proyecto es un sistema de gestión de usuarios desarrollado como parte de la **Actividad Integradora N° 3** para la materia **Programación I**. El sistema permite el registro, inicio de sesión y la gestión de usuarios con diferentes roles.

> **Nota Importante sobre el Estado Actual:**
> El proyecto está compuesto por dos partes principales: (1) El diseño y los scripts de la Base de Datos y (2) la aplicación de consola en Python. En la fase actual, estos componentes **se entregan de forma separada**. La aplicación de consola **opera completamente en memoria**, lo que significa que cualquier usuario registrado se perderá al cerrar el programa. La integración para lograr la persistencia de datos es una mejora considerada a futuro.

---

## 👥 Integrantes del Equipo

* Martin Vijarra
* Luis Gerardo Catalas
* Emilce Agustia Torres
* Luis Gastón Alonso
* Kevin Cristofer Lorea Tannfeld

---

## ✨ Características Principales

* **Registro de Usuarios:** Permite la creación de nuevas cuentas en la sesión actual del programa.
* **Inicio de Sesión:** Autenticación de usuarios existentes en memoria.
* **Roles de Usuario:**
    * **Administrador:** Puede listar todos los usuarios, cambiar roles y eliminar cuentas durante la sesión.
    * **Usuario Estándar:** Puede visualizar sus propios datos personales.
* **Diseño de Persistencia:** Se incluye un diseño completo y scripts SQL (`base_de_datos/scripts/`) para crear una base de datos MySQL funcional. *(La conexión con la aplicación es un paso a futuro)*.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Base de Datos (Diseño):** MySQL

---

## 🚀 Cómo Empezar

El proyecto se compone de dos partes que se prueban por separado: el diseño de la base de datos y la aplicación de consola.

### 1. Base de Datos (Diseño y Scripts)

Esta parte define la estructura de la base de datos. **Actualmente no hay conexión con la aplicación de Python**, pero puedes probar que los scripts son funcionales de la siguiente manera:

1.  Asegúrate de tener un servidor MySQL en funcionamiento.
2.  Abre un cliente de MySQL (como MySQL Workbench, DBeaver, etc.).
3.  Copia y ejecuta el contenido del archivo `base_de_datos/scripts/01_creacion_db.sql`. Esto creará la base de datos `planificador_usuarios`, las tablas y los datos de prueba.

### 2. Aplicación de Consola (En Memoria)

La aplicación de Python funciona de forma independiente y **guarda los datos temporalmente en memoria** (se borran al cerrar).

1.  Clona el repositorio si aún no lo has hecho:
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/Grupo-22-ISPC/Evidencia-3-Prog-y-BD/tree/main)
    cd PLANIFICADOR_PROYECTOS_EMPRESARIALES
    ```
2.  Ejecuta la aplicación desde la carpeta raíz del proyecto con el siguiente comando:
    ```bash
    python -m src.main
    ```
¡Listo! Ya puedes interactuar con el sistema. 

---

## 📂 Estructura del Proyecto

El proyecto está organizado en dos carpetas principales para separar claramente la lógica de la base de datos de la aplicación:

* **base_de_datos/**: Contiene todo lo relacionado con el diseño y los scripts de la base de datos.
    * **/docs/**: Documentación específica de la base de datos (diseño, modelo relacional).
    * **/scripts/**: Scripts SQL para la creación (`DDL`) y manipulación (`DML`) de datos.

* **programacion/**: Contiene todo el código fuente y la documentación de la aplicación de consola.
    * **/docs/**: Documentación específica de la aplicación (diagrama de clases, etc.).
    * **/src/**: Código fuente en Python, organizado en clases (`Usuario`, `GestorUsuarios`, `Sistema`).

---

## 📚 Documentación Completa

Para una descripción más detallada de la arquitectura, el diseño de la base de datos y el código, por favor visita la **[Wiki del Proyecto](https://github.com/Grupo-22-ISPC/Evidencia-3-Prog-y-BD/wiki)**.