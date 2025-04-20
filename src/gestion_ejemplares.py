##ejemplares son libros

class GestionEjemplares():
    def __init__(self , nombre_libro , numero_paginas , formato_libro , nombre_autor , apellido_autor , fecha_registro , email_autor_libro , clave_libro , estado = "En revisión"):
        self.nombre_libro = nombre_libro
        self.numero_paginas = numero_paginas
        self.formato_libro = formato_libro
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.fecha_registro = fecha_registro
        self.email_autor_libro = email_autor_libro
        self.clave_libro = clave_libro
        self.estado = estado


    def conseguir_nombre_libro( self ):
        return self.nombre_libro

    def conseguir_estado_libro( self ):
        return self.estado


    def editar_estado( self , estado ):
        estados_validos = ["Sin publicar", "En revisión" , "Publicado" , "No disponible"]
        if self.estado in estados_validos:
            self.estado = estado
            return True
        else:
            return "El estado no es valido"

    def editar_ejemplar( self, nombre_libro, numero_paginas, formato_libro, nombre_autor, apellido_autor, fecha_registro, email_autor_libro):
        self.nombre_libro = nombre_libro
        self.numero_paginas = numero_paginas
        self.formato_libro = formato_libro
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.fecha_registro = fecha_registro
        self.email_autor_libro = email_autor_libro

    def deshabilitar_ejemplar( self ):
        self.estado = "No disponible"
        return True