
pizzas = ["Tradicional", "Pepperoni", "Margarita", "Napolitana", "Carnes"]
precio_pizzas = [12000, 14000, 12500, 11000, 17000]
tipo_usuario = ["Estudiante", "Profesor"]
producto_elegido = []
contador = 0
subtotal = 0
total = 0

descuentos = {
    "estudiante": 0.2,
    "profesor": 0.1,
    "3_Napolitanas": 11000,
    "2_Pepperoni": 0.1
}


def imprimir_lista(producto: str, precio: int):
    print("Estas son las pizzas disponibles:")
    count = 0
    for q, w in zip(producto, precio):
        count += 1
        print(f"{count} | {q} : ${w}")


def imprimir_usuario(persona: list):
    print("Los usuarios son:", end=" ")
    for i in persona:
        print(i, end=" ")


imprimir_lista(pizzas, precio_pizzas)
print("-----------------------------------")
imprimir_usuario(tipo_usuario)
print()
while True:
    contador += 1
    usuario = input("¿Qué tipo de usuario es usted?: ").lower()

    while usuario != "estudiante" and usuario != "profesor":
        print("Error")
        usuario = input("¿Qué tipo de usuario es usted?: ").lower()

    if usuario == "estudiante":
        print("Felicidades, por ser Estudiante tiene un descuento del 20%")
    elif usuario == "profesor":
        print("Felicidades, por ser Profesor tiene un descuento del 10%")
    print("-----------------------------------")
    print("Escriba el Numero de la pizza que desee: ")
    print("Si desea dejar de elegir, seleccione 0")

    while True:
        sel = int(input(">>>"))
        if sel == 0:
            break
        producto_elegido.append(pizzas[sel-1])
        subtotal += precio_pizzas[sel-1]

    print(f"Subtotal sin descuento: ${subtotal}")

    if producto_elegido.count("Napolitana") == 3:
        print("Felicidades, Si lleva 3 pizzas Napolitanas, solo paga 2")
        subtotal = subtotal - descuentos["3_Napolitanas"]

    if producto_elegido.count("Pepperoni") == 2:
        print("Felicidades, Si lleva 2 pizzas Pepperoni, tiene un descuento del 10%")
        subtotal -= subtotal * descuentos["2_Pepperoni"]

    if usuario == "estudiante":
        subtotal -= subtotal * descuentos["estudiante"]
        print(f"Su subtotal con descuento es ${subtotal}")
    elif usuario == "profesor":
        subtotal -= subtotal * descuentos["profesor"]
        print(f"Su subtotal con descuento es ${subtotal}")

    salir = input("Hay otro usuario?: ")
    while salir != "si" and salir != "no":
        print("Error, responder con <si> o <no>")
        salir = input("Hay otro usuario?: ")
    if salir == "no":
        print("-----------------------------------")
        print("Gracias por su compra")
        print(f"Su total es ${subtotal}")
        print("-----------------------------------")
        break
