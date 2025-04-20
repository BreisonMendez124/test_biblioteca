import pytest
from src.catalogo_recursos import CatologoRecursos
from src.gestion_ejemplares import GestionEjemplares
from src.panel_administrativo import PanelAdminstrativo


def test_traer_ejemplar_por_estado():
    catalogo = CatologoRecursos()
    ##Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "antoine@email.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "antoine@email.com"
    assert ejemplar1.clave_libro == "1234"
    #Agregar ejemplar al catalogo
    catalogo.agregar_ejemplar(ejemplar1)
    #Conseguir ejemplares por estado
    estado_filtrar = "En revisión"
    ejemplares_filtrados = catalogo.traer_ejemplar_por_estado(estado_filtrar)
    return ejemplares_filtrados

def test_traer_ejemplar():
    catalogo = CatologoRecursos()
     ##Crear ejemplar
    ejemplar1 = GestionEjemplares("El principito" , 100 , "PDF" , "Antoine" , "Saint-Exupéry" , "2021-10-10" , "antoine@email.com" , "1234")
    assert ejemplar1.nombre_libro == "El principito"
    assert ejemplar1.numero_paginas == 100
    assert ejemplar1.formato_libro == "PDF"
    assert ejemplar1.nombre_autor == "Antoine"
    assert ejemplar1.apellido_autor == "Saint-Exupéry"
    assert ejemplar1.fecha_registro == "2021-10-10"
    assert ejemplar1.email_autor_libro == "antoine@email.com"
    assert ejemplar1.clave_libro == "1234"
    #Agregar ejemplar al catalogo
    catalogo.agregar_ejemplar(ejemplar1)
    nombre_libro = "El principito"    
    ejemplar = catalogo.traer_ejemplar(nombre_libro)
    return ejemplar

def test_listar_ejemplares():
    catalogo = CatologoRecursos()
    ejemplares = catalogo.listar_ejemplares()
    return ejemplares