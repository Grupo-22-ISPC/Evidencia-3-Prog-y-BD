# registro del usuario 
from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.next_id = 1  # Para simular autoincremento

    def registrar_usuario(self, nombre_usuario, contraseña, datos_personales, rol):
        if self._existe_usuario(nombre_usuario):
            print(f"El usuario '{nombre_usuario}' ya existe.")
            return None
        if not self._validar_contraseña(contraseña):
            print("La contraseña debe tener al menos 6 caracteres y contener letras y números.")
            return None
        usuario = Usuario(self.next_id, nombre_usuario, contraseña, datos_personales, rol)
        self.usuarios.append(usuario)
        self.next_id += 1
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        return usuario
    
    def _existe_usuario(self, nombre_usuario):
        return any(u.nombre_usuario == nombre_usuario for u in self.usuarios)

    def _validar_contraseña(self, contraseña):
        if len(contraseña) < 6:
            return False
        has_letter = any(c.isalpha() for c in contraseña)
        has_number = any(c.isdigit() for c in contraseña)
        return has_letter and has_number
    
        # inisio de secion 
    def iniciar_sesion(self, nombre_usuario, contraseña):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
                print(f"Bienvenido, {usuario.nombre_usuario}!")
                return usuario
        print("Nombre de usuario o contraseña incorrectos.")
        return None
            
    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.usuarios:
            print(usuario)

    def cambiar_rol(self, nombre_usuario, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                usuario.rol = nuevo_rol
                print(f"Rol de '{nombre_usuario}' cambiado a '{nuevo_rol}'.")
                return True
        print(f"No se encontró usuario con nombre '{nombre_usuario}'.")
        return False
    
            # visualizacion de informacion del usuario
class VisualizacionDeInformacionDelUsuario(registro):
    def __init__(self, usuario):
        self.usuario = usuario
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.usuario.nombre}")
        print(f"Apellido: {self.usuario.apellido}")
        print(f"Edad: {self.usuario.edad}")
        print(f"Email: {self.usuario.email}")

datos_usuario = VisualizacionDeInformacionDelUsuario(persona)
datos_usuario.mostrar_informacion()

# Actualizacion de informacion del usuario
class ActualizacionDeInformacionDelUsuario(registro):
    def __init__(self, usuario):
        self.usuario = usuario
        
    def actualizar_informacion(self):
        self.usuario.nombre = input("Ingrese su nuevo nombre: ")
        self.usuario.apellido = input("Ingrese su nuevo apellido: ")
        self.usuario.edad = int(input("Ingrese su nueva edad: "))
        self.usuario.email = input("Ingrese su nuevo email: ")
        self.usuario.contraseña = input("Ingrese su nueva contraseña: ")
        print("Sus datos han sido actualizados correctamente")
datos_actualizados = ActualizacionDeInformacionDelUsuario(persona)
datos_actualizados.actualizar_informacion()

# Eliminacion de cuenta del usuario
class EliminacionDeCuenta(registro):
    def __init__(self, usuario):
        self.usuario = usuario
        
    def eliminar_cuenta(self):
        confirmacion = input("¿Está seguro de que desea eliminar su cuenta? (si/no): ")
        if confirmacion.lower() == 'si':
            print("Su cuenta ha sido eliminada.")
            self.usuario = None  # Elimina la referencia al usuario
        else:
            print("La cuenta no ha sido eliminada.")
datos_eliminacion = EliminacionDeCuenta(persona)
datos_eliminacion.eliminar_cuenta()