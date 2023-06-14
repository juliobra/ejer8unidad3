class SistemaUniversitario:

    def __init__(self):
        self.lista_agentes = ListaAgentes()
        self.tesorero_usuario = "uTesoreso"
        self.tesorero_contrasena = "ag@74ck"
        self.director_usuario = "uDirector"
        self.director_contrasena = "ufC77#!1"

    def autenticar_usuario(self):
        usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        if usuario == self.tesorero_usuario and contrasena == self.tesorero_contrasena:
            self.menu_tesorero()
        elif usuario == self.director_usuario and contrasena == self.director_contrasena:
            self.menu_director()
        else:
            print("Usuario o contraseña incorrectos")

   