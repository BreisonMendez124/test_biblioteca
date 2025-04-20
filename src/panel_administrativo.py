class PanelAdminstrativo():
    def __init__(self):
        self.usuarios = {}
        self.ejemplares = {}

    def agregar_ejemplar(self, ejemplar):
        self.ejemplares[ejemplar.conseguir_nombre_libro()] = ejemplar

    def traer_ejemplar(self, nombre_libro):
        if nombre_libro not in self.ejemplares:
            return False
        return self.ejemplares.get(nombre_libro, None)

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.conseguir_numero_identificacion()] = usuario

    def traer_usuario(self, numero_identificacion):
        if numero_identificacion not in self.usuarios:
            return False       
        return self.usuarios.get(numero_identificacion, None)

    def listar_ejemplares(self):
        return self.ejemplares.values()

    def listar_usuarios(self):
        return self.usuarios.values()

  


    