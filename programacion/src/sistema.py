
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
                    
    def _registrar(self):
        print("\n--- Registro de Usuario ---")
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña: ")
        datos_personales = input("Ingrese sus datos personales (ej: Nombre Completo, email): ")
        rol = input("Ingrese rol (administrador/usuario): ").lower()
        if rol not in ["administrador", "usuario"]:
            print("Rol inválido. Se asignará 'usuario' por defecto.")
            rol = "usuario"
        self.gestor.registrar_usuario(nombre, contraseña, datos_personales, rol)

    def _iniciar_sesion(self):
        print("\n--- Inicio de Sesión ---")
        nombre = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")
        usuario = self.gestor.iniciar_sesion(nombre, contraseña)
        if usuario:
            self.usuario_actual = usuario