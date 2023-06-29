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

color_favorito = input("Ingrese su color fav: ").lower()
usuario["Color"] = color_favorito


def buscar_modelo(lista):
    modelo = input("¿Cuál modelo busca?: ")
    for auto in lista:
        if "modelo" in auto and auto["modelo"].lower() == modelo:
            print(f"Se encontró el auto con modelo {modelo}: {auto}")
            return
    print(f"No se encontró el auto con modelo {modelo} en la lista.")


def imprimir_lista(lista):
    llave = input("Ingrese la llave: ")
    parametro = input("Ingrese el valor: ")
    print("Auto con esas caracteristicas:")
    for auto in lista:
        if llave in auto and auto[llave].lower() == parametro.lower():
            print(auto)


def imprimir_certificado(lista):
    i = 0
    for auto in lista:
        i += 1
        print(i, auto)
    seleccion = int(input("Seleccione un vehiculo >>> "))
    sel = seleccion - 1
    auto_seleccionado = lista[sel]
    if sel <= len(lista):
        print(auto_seleccionado)
        print(usuario['Nombre'], "emite certificado que:\nEl vehiculo", auto_seleccionado["marca"], auto_seleccionado["modelo"],
              "con patente", auto_seleccionado["patente"] + "\n" "De color", auto_seleccionado["color"], "\nQueda registrado oficialmente a la fecha de", usuario["Fecha"])


def buscar_patente(lista):
    patente = input("Ingrese su patente: ").lower()
    for auto in lista:
        if "patente" in auto and auto["patente"].lower() == patente:
            auto_selec = auto
            print(f"Su auto es: {auto}")
            return auto_selec


def buscar_año(lista):
    año = input("¿Cual año busca?: ")
    ultimos_2_digitos = año[-2:]
    for auto in lista:
        if "año" in auto and str(auto["año"])[-2:] == ultimos_2_digitos:
            print(auto)


def agregar_info_dueño(lista):
    auto_seleccionado = buscar_patente(lista)
    auto_seleccionado["nombre_propietario"] = input(
        "Ingrese el nombre del usuario: ")
    print("--- Ingreso realizado con exito ---")
    return auto_seleccionado


def buscar_por_color(lista):
    encontrado = False
    for auto in lista:
        if "color" in auto and usuario["Color"] == auto["color"].lower():
            if not encontrado:
                print("Autos con su color favorito: ")
                encontrado = True
            print(auto)


def buscar_por_nombre(lista):
    propietario = input("Ingrese el propietario: ").lower()
    for auto in lista:
        if "nombre_propietario" in auto and auto["nombre_propietario"].lower() == propietario:
            print(f"Auto asociado al propietario {propietario} : {auto}")
        elif "nombre_propietario" in auto and auto["nombre_propietario"].lower() == usuario["Nombre"].lower():
            print(f"Auto asociado al propietario {usuario['Nombre']} : {auto}")


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
        imprimir_lista(lista_autos)
        break
    if opcion == 3:
        imprimir_certificado(lista_autos)
        break
    if opcion == 4:
        buscar_patente(lista_autos)
        break
    if opcion == 5:
        buscar_año(lista_autos)
        break
    if opcion == 6:
        auto_con_dueño = agregar_info_dueño(lista_autos)
        break
    if opcion == 7:
        buscar_por_color(lista_autos)
        break
    if opcion == 8:
        break

# agregar_info_dueño(lista_autos)
buscar_por_nombre(lista_autos)
