class Usuario:
    def Usuar(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

class SistemLogin:
    def Login(self):
        self.usuarios = []

    def registrar_usuario(self, nombre_usuario, contrasena):
        nuevo_usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                print(f"Bienvenido, {nombre_usuario}!")
                return True
        print("Nombre de usuario o contraseña incorrectos.")
        return False