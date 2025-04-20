import pytest
from src.panel_administrativo import PanelAdminstrativo
from src.gestion_ejemplares import GestionEjemplares


def test_editar_estado():
    panel = PanelAdminstrativo()
    #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "EMAIL" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "EMAIL"
    assert ejemplar1.clave_libro == "1234"
    #Cambiar estado
    nuevo_estado = "Nuevo estado"
    assert ejemplar1.editar_estado(nuevo_estado)
    #Agregar ejemplar al panel
    panel.agregar_ejemplar(ejemplar1)

def test_editar_ejemplar():
    panel = PanelAdminstrativo()
    #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "email@correo.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "email@correo.com"
    assert ejemplar1.clave_libro == "1234"

    #Datos del ejemplar a editar
    nombre_libro = "El principito - editado"
    numero_paginas = 170
    formato_libro = "WORD"
    nombre_autor = "Antoine - editado"
    apellido_autor = "Saint-Exupéry - editado"
    fecha_registro = "2021-10-12"
    email_autor_libro = "email@correo.com - editado"

    ejemplar1.editar_ejemplar(
        nombre_libro,
        numero_paginas,
        formato_libro,
        nombre_autor,
        apellido_autor,
        fecha_registro,
        email_autor_libro
    )


def test_deshabilitar_ejemplar():
    panel = PanelAdminstrativo()
    #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "email@correo.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "email@correo.com"
    assert ejemplar1.clave_libro == "1234"
    assert ejemplar1.deshabilitar_ejemplar()


def test_conseguir_nombre_libro():
    #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "email@correo.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "email@correo.com"
    assert ejemplar1.clave_libro == "1234"
    ejemplar1.conseguir_nombre_libro()

def test_conseguir_estado_libro():
    #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "email@correo.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "email@correo.com"
    assert ejemplar1.clave_libro == "1234"
    ejemplar1.conseguir_estado_libro()


