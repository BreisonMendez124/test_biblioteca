class GestionUsuarios():
    def __init__(self , numero_identificacion , nombres , apellidos , correo_electronico , telefono , ubicacion , rol = "Estudiante" , estado = "Activo"):
        self.numero_identificacion = numero_identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo_electronico = self.validar_correo( correo_electronico )
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.rol = self.validar_rol( rol )
        self.estado = self.validar_estados(estado)
    
    def validar_correo(self , correo ):
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, correo) is not None:
            return correo
        else:
            return "El correo no tiene un formato valido"

    def validar_rol( self , rol_pametro ):
        roles_validos = ["Estudiante", "Autor"]
        if rol_pametro in roles_validos:
            return rol_pametro
        else:
            return "El rol no es valido"

    def validar_estados( self , estado ):
        estados_validos = ["Activo", "Inactivo"]    
        if estado in estados_validos: 
            return estado
        else:
            return "El estado no es valido"

    def deshabiltar_usuario( self ):
        self.estado = "Inactivo"
        return True

    def conseguir_numero_identificacion( self ):
        return self.numero_identificacion

    def editar_usuario( self , nombres , apellidos, telefono, ubicacion, rol, estado ):
        # self.numero_identificacion = self.numero_identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        # self.correo_electronico = self.correo_electronico
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.rol = self.validar_correo( rol )
        self.estado = self.validar_estados( estado )  


    
