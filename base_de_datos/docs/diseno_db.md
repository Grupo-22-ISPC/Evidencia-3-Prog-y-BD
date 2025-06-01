# Documentación del Diseño de la Base de Datos

A continuación, se detalla la documentación de cada tabla del modelo relacional resultante, incluyendo una descripción de su propósito, sus columnas y cualquier aclaración relevante sobre las decisiones de diseño tomadas.

## Tabla: `Roles`

### Descripción
Esta tabla almacena los diferentes roles que pueden tener los usuarios dentro del sistema. Separar los roles en su propia tabla permite una gestión más flexible de los permisos y tipos de usuario, y asegura la consistencia de los nombres de los roles, evitando redundancias y errores de tipeo.

### Columnas

| Nombre de Columna | Tipo de Dato (Ejemplo) | Restricciones      | Descripción                                                                 |
|-------------------|------------------------|--------------------|-----------------------------------------------------------------------------|
| `id_rol`          | `INT`                  | `PRIMARY KEY`, `AUTO_INCREMENT` | Identificador numérico único para cada rol. Es la clave primaria.       |
| `nombre_rol`      | `VARCHAR(50)`          | `NOT NULL`, `UNIQUE` | Nombre descriptivo del rol (ej. "ESTANDAR", "ADMIN"). Debe ser único. |

### Aclaraciones
* Se asume que la cantidad de roles en el sistema será relativamente pequeña (por ejemplo, "ESTANDAR", "ADMIN") y no cambiará con extrema frecuencia.
* La restricción `UNIQUE` en `nombre_rol` asegura que no haya dos roles con el mismo nombre.

## Tabla: `Usuarios`

### Descripción
Esta tabla almacena la información esencial de todos los usuarios registrados en el sistema, incluyendo sus credenciales de acceso, datos personales básicos y el rol que se les ha asignado.

### Columnas

| Nombre de Columna  | Tipo de Dato (Ejemplo) | Restricciones                       | Descripción                                                                                                                               |
|--------------------|------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `id_usuario`       | `INT`                  | `PRIMARY KEY`, `AUTO_INCREMENT`     | Identificador numérico único para cada usuario. Es la clave primaria.                                                                     |
| `nombre_usuario`   | `VARCHAR(100)`         | `NOT NULL`, `UNIQUE`                | Nombre único que el usuario utilizará para el inicio de sesión.                                                                           |
| `contrasena`       | `VARCHAR(255)`         | `NOT NULL`                          | Contraseña del usuario. **Importante**: En un sistema real, este campo debe almacenar un hash seguro de la contraseña, no la contraseña en texto plano. |
| `datos_personales` | `TEXT`                 | `NULL`                              | Campo de texto libre para almacenar información adicional del usuario (ej. nombre completo, email, etc.). Puede ser nulo si no se proveen. |
| `id_rol`           | `INT`                  | `NOT NULL`, `FOREIGN KEY (Roles.id_rol)` | Clave foránea que referencia al `id_rol` en la tabla `Roles`. Indica el rol asignado al usuario.                                    |

### Aclaraciones
* **Unicidad de `nombre_usuario`**: Es crucial para el proceso de inicio de sesión, garantizando que cada usuario tenga un identificador único para acceder al sistema.
* **Seguridad de `contrasena`**: Se reitera la importancia de almacenar las contraseñas de forma segura (hasheadas y salteadas) en una implementación real para proteger la información de los usuarios.
* **Campo `datos_personales`**: Para los requerimientos actuales, se mantiene como un campo de texto simple. Si las necesidades de almacenamiento de datos personales fueran más complejas (ej. múltiples campos estructurados como dirección, teléfono, fecha de nacimiento), se podría considerar normalizar esta información en una tabla separada (`DatosPersonalesUsuarios`) relacionada con la tabla `Usuarios`. Sin embargo, para este ejercicio, se mantiene simple.
* **Relación con `Roles` y `id_rol`**:
    * La columna `id_rol` es una clave foránea que establece la relación entre un usuario y su rol.
    * Se ha definido como `NOT NULL` porque se asume que cada usuario **debe tener obligatoriamente un rol** asignado en el sistema.
    * La relación es de **muchos a uno (N:1)** desde `Usuarios` hacia `Roles`. Esto significa que muchos usuarios pueden compartir el mismo rol (ej. muchos usuarios "ESTANDAR"), pero cada usuario individual está asociado a un único rol.
    * Esta decisión de diseño (un usuario, un rol) se basa en la simplicidad de los requerimientos presentados ("Usuario estándar" o "Admin"). Si los requerimientos futuros indicaran que un usuario puede tener múltiples roles simultáneamente, el diseño debería cambiar para incluir una tabla intermedia (tabla de unión) para modelar una relación muchos a muchos (N:M) entre `Usuarios` y `Roles`.