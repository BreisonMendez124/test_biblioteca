import pytest
from src.panel_administrativo import PanelAdminstrativo
from src.gestion_ejemplares import GestionEjemplares
from src.gestion_usuarios import GestionUsuarios



def test_agregar_ejemplar():
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
    panel.agregar_ejemplar( ejemplar1 )


def test_traer_ejemplar():
    panel = PanelAdminstrativo()
     #Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "correo@correo.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "correo@correo.com"
    assert ejemplar1.clave_libro == "1234"

    panel.traer_ejemplar( ejemplar1.conseguir_nombre_libro( ) )

def test_agregar_usuario():
    panel = PanelAdminstrativo()
    #Crear usuario
    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )
    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

    panel.agregar_usuario( gestorUsuario )

def test_traer_usuario():
    panel = PanelAdminstrativo()
    #Crear usuario
    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )

    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

    panel.traer_usuario( 12345678 )

def test_listar_ejemplares():
    panel = PanelAdminstrativo()
    #Crear usuario
    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )

    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

    panel.listar_ejemplares()

def test_listar_usuarios():
    panel = PanelAdminstrativo()
    #Crear usuario
    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )

    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

    panel.listar_usuarios()
