# ------NO CAMBIAR ---------
from autoHerramientas import *
# ---------------------------
# puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "autos1"

# puede cambiar la forma de la lista entre:
# lista de diccionario -> tipo_lista = "diccionario"
# lista de listas -> tipo_lista = "lista"
tipo_lista = "diccionario"

lista_autos = obtenerAutos(nombre_archivo, tipo_lista)

# ------------
usuario = {}

nombre_usuario = input("Ingrese su nombre: ")
usuario["Nombre"] = nombre_usuario

fecha_actual = input("Ingrese la fecha actual: ")
usuario["Fecha"] = fecha_actual

color_favorito = input("Ingrese su color fav: ")
usuario["Color"] = color_favorito


def buscar_modelo(lista):
    modelo = input("¿Cuál modelo busca?: ")
    for auto in lista:
        if "modelo" in auto and auto["modelo"].lower() == modelo:
            print(f"Se encontró el auto con modelo {modelo}: {auto}")
            return
    print(f"No se encontró el auto con modelo {modelo} en la lista.")


def imprimir_certificado(lista):
    patente = input("Ingrese su patente: ").lower()
    for auto in lista:
        if "patente" in auto and auto["patente"].lower() == patente:
            print(usuario['Nombre'], "emite certificado que:\nEl vehiculo", auto["marca"], auto["modelo"],
                  "con patente ", auto["patente"], "De color", auto["color"], "Queda registrado oficialmente a la fecha de", usuario["Fecha"])


while True:
    print("----- MENÚ -----")
    print("1. Buscar autos por modelo")
    print("2. Imprimir certificado")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        buscar_modelo(lista_autos)
        break
    if opcion == 2:
        imprimir_certificado(lista_autos)
        break
    if opcion == 3:
        print("Adios")
        break
