import pytest
from src.gestion_usuarios import GestionUsuarios

def test_validar_correo():
    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "EMAIL",
        "+57 31245678974",
        "Bogota"
    )

    #Al crear el usuario , se valida el formato del correo electronico
    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "EMAIL"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"

def test_validar_rol():

    gestorUsuario = GestionUsuarios(
        12345678,
        "Juan",
        "Perez",
        "correo@correo.com",
        "+57 31245678974",
        "Bogota"
    )

    #Al crear el usuario , se valida el rol
    assert gestorUsuario.numero_identificacion == 12345678
    assert gestorUsuario.nombres == "Juan"
    assert gestorUsuario.apellidos == "Perez"
    assert gestorUsuario.correo_electronico == "correo@correo.com"
    assert gestorUsuario.telefono == "+57 31245678974"
    assert gestorUsuario.ubicacion == "Bogota"
    assert gestorUsuario.rol == "Nuevo usuario" ##Se envia un rol invalido para verificar la validacion del rol

def test_validar_estado():

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
    assert gestorUsuario.estado == "Activo e inactivo" ##Se envia un estado invalido para verificar la validacion del estado

def test_deshabilitar_usuario():
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
    assert gestorUsuario.deshabiltar_usuario()

def test_editar_usuario():
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

    #Datos del usuario para editar
    nombres = "Juan - editado"
    apellidos = "Perez -  editado"
    telefono = "+57 3124544444"
    ubicacion = "Bogota - editado"

    #Se edita el usuario
    gestorUsuario.editar_usuario(
        nombres, 
        apellidos, 
        telefono, 
        ubicacion,
        "Autor",
        "Inactivo"
        )



    

    
