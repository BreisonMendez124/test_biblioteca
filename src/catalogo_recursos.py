from src.panel_administrativo import PanelAdminstrativo

class CatologoRecursos():
    def __init__(self):
        self.ejemplares = {}

    def agregar_ejemplar(self, ejemplar):
        self.ejemplares[ejemplar.conseguir_nombre_libro()] = ejemplar

    def traer_ejemplar_por_estado(self, estado):
        ejemplares_filtrados = []
        ejemplares = PanelAdminstrativo().listar_ejemplares()
        for ejemplar in ejemplares:
            if ejemplar.conseguir_estado_libro() == estado:
                ejemplares_filtrados.append(ejemplar)
        if len(ejemplares_filtrados) == 0:
            return "No hay ejemplares con ese estado"
        return True

    def traer_ejemplar(self, nombreLibro):
        if nombreLibro not in self.ejemplares:
            return "El libro no existe"
        return self.ejemplares.get(nombreLibro, None)

    def listar_ejemplares(self):
        return self.ejemplares.values()

    

    

