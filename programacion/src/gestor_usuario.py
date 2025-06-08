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
    
        # inisio de secion 
class login(registro):
    def __init__(self, email_registrado, contraseña_registrada):
        self.email_registrado = email_registrado
        self.contraseña_registrada = contraseña_registrada

    def iniciar_sesion(self):
        email1 = input("Ingrese su email: ")
        contraseña1 = input("Ingrese su contraseña: ")
        if email1 == self.email_registrado and contraseña1 == self.contraseña_registrada:
            print("Bienvenido al sistema")
        else:
            print("Email o contraseña incorrectos, intente nuevamente")

inicio = login(email, contraseña)
inicio.iniciar_sesion()
            
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