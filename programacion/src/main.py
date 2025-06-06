
contactos = {}

while True:
    print("\n--- Bienvenido al Sistema de Gestión de Usuarios ---")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
   
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
                sistema.iniciar_sesion()
    elif opcion == "2":
                sistema.registrar_usuario()
    elif opcion == "3":
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


