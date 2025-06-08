# registro del usuario 
class registro:
    def __init__(self, nombre, apellido, edad, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.contraseña = contraseña

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: ")) 
email = input("Ingrese su email: ")
contraseña = input("Ingrese su contraseña: ")
persona = registro(nombre, apellido, edad, email, contraseña)
print(f"sus datos an sido cargados correctamente")
       
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