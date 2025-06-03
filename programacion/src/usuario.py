class registro:
    def __init__(self, nombre, apellido, edad, email, contraseña):
        # Constructor de la clase registro
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
        
class login:
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

# Crear instancia de login con los datos registrados
inicio = login(email, contraseña)
inicio.iniciar_sesion()
