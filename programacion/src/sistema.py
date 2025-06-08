
class Sistema:
    def __init__(self): 
        self.gestor = GestorUsuarios()
        self.usuario_actual = None

    def mostrar_menu (self):

        while True:
            if not self.usuario_actual:
                print("\n--- Menú Principal ---")
                print("1. Registrar usuario")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self._registrar()
                elif opcion == "2":
                    self._iniciar_sesion()
                elif opcion == "3":
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            else:
                if self.usuario_actual.rol == "administrador":
                    self._menu_administrador()
                else:
                    self._menu_usuario_estandar()
                    