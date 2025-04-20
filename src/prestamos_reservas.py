import datetime
from typing import Self
from src.panel_administrativo import PanelAdminstrativo
from src.catalogo_recursos import CatologoRecursos

class PrestamosReservas():
    def __init__(self , gestion_de_prestamos , identificacion , nombre , apellido , ejemplar_solicitado  , estado = "Prestado"):
        self.gestion_de_prestamos = gestion_de_prestamos
        self.identificacion = self.validar_usuario_identificacion_exite( identificacion ) 
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_solicitud = datetime.datetime.now()
        self.ejemplar_solicitado = self.vallidar_ejemplar_existe(ejemplar_solicitado)
        self.estado = estado
        self.diasHabiles = 90

    def validar_usuario_identificacion_exite( self , numero_identificacion):
        if PanelAdminstrativo().traer_usuario( numero_identificacion ) is not None:
            return True
        else:
            return "El usuario no existe"

    def vallidar_ejemplar_existe( self , nombre_ejemplar ):
       if CatologoRecursos().traer_ejemplar( nombre_ejemplar ) is not None:
            return True
       else:
            return "El ejemplar no existe"

    def conseguir_fecha_solicitud_ejemplar(self):
        return self.fecha_solicitud

    def validar_fecha_vencimiento( self , fecha_solicitud):
        fecha_vencimiento = self.fecha_solicitud + datetime.timedelta(days=self.diasHabiles)
        if fecha_solicitud < fecha_vencimiento :
            return True
        else:
            self.estado = "Prestamo caducado"
            return "La fecha de prestamo a caducado"

        


    