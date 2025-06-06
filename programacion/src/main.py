
contactos = {}

while True:
    print("\n--- Bienvenido al Sistema de Gestión de Usuarios ---")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. registros de usuarios")
    print("4. Salir")
   
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
                sistema.iniciar_sesion()
    elif opcion == "2":
                sistema.registrar_usuario()
    elif opcion == "3":
                if not sistema.registros_usuarios():
                    print("No hay usuarios registrados.")
                else:
                    for usuario in sistema.usuarios:
                        print(f"Usuario: {usuario.nombre}, Rol: {usuario.rol}")
    elif opcion == "4":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
    else:
                print("Opción no válida. Intente de nuevo.")
else:
            # Ya hay sesión iniciada, se redirige según el rol
            if sistema.usuario_actual.rol == ROL_ADMIN:
                sistema.menu_admin()
            elif sistema.usuario_actual.rol == ROL_ESTANDAR:
                sistema.menu_usuario_estandar()
            else:
                print("Rol desconocido. Cerrando sesión por seguridad.")
                sistema.cerrar_sesion()

if __name__ == "__main__":
    main_consola()


