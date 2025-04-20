import pytest
from src.prestamos_reservas import PrestamosReservas
from src.gestion_ejemplares import GestionEjemplares
from src.gestion_usuarios import GestionUsuarios

def test_crear_reserva():
    #Crear usuario
    gestorUsuario = GestionUsuarios(
        "123456789",
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )
    assert gestorUsuario.numero_identificacion == "123456789"
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

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

    #Crear prestamo
    prestamo = PrestamosReservas("Biblioteca" , "123456789", "Juan" , "Perez" , "El principito")
    assert prestamo.gestion_de_prestamos == "Biblioteca"
    assert prestamo.identificacion == "123456789"
    assert prestamo.nombre == "Juan"
    assert prestamo.apellido == "Perez"
    assert prestamo.ejemplar_solicitado == "El principito"

def validar_usuario_identificacion_exite():
    #Crear prestamo
    prestamo = PrestamosReservas("Biblioteca" , "123456789", "Juan" , "Perez" , "El principito")
    assert prestamo.gestion_de_prestamos == "Biblioteca"
    assert prestamo.identificacion == "123456789"
    assert prestamo.nombre == "Juan"
    assert prestamo.apellido == "Perez"
    assert prestamo.ejemplar_solicitado == "El principito"
    prestamo.validar_usuario_identificacion_exite( "123456789123" ) #Devuelve false ya que el usuario no esta creado

def test_vallidar_ejemplar_existe():
    #Crear prestamo
    prestamo = PrestamosReservas("Biblioteca" , "123456789", "Juan" , "Perez" , "El principito")
    assert prestamo.gestion_de_prestamos == "Biblioteca"
    assert prestamo.identificacion == "123456789"
    assert prestamo.nombre == "Juan"
    assert prestamo.apellido == "Perez"
    assert prestamo.ejemplar_solicitado == "El principito 2"
    prestamo.vallidar_ejemplar_existe( "El principito 2" ) #Devuelve false ya que el ejemplar no esta creado    


def test_validar_fecha_vencimiento():
    prestamo = PrestamosReservas("Biblioteca" , "123456789", "Juan" , "Perez" , "El principito")
    assert prestamo.gestion_de_prestamos == "Biblioteca"
    assert prestamo.identificacion == "123456789"
    assert prestamo.nombre == "Juan"
    assert prestamo.apellido == "Perez"
    assert prestamo.ejemplar_solicitado == "El principito"

    prestamo.validar_fecha_vencimiento( prestamo.conseguir_fecha_solicitud_ejemplar( ) )



