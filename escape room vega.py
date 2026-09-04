# TP Sala de escape
import string
import random

usuario= "capitan"
contraseña = "Tesoro.2026"
palabras_ahorcado = ["FANTASMA", "TESORO", "CAPITAN", "NAUFRAGIO", "MALDICION",
                      "TIMON", "BRUJULA", "ESQUELETO", "GALEON", "TORMENTA",
                      "ANCLA", "LEYENDA"]
intentos_ahorcado = 6
# Comienzo punto 3
def login():
    print("\n===== NO HAY SALIDA: BARCO EMBRUJADO =====")
    log_usuario= input("Ingrese el nombre de ususario:")
    log_contraseña= input("Ingrese la contraseña:")
    while log_usuario != usuario or log_contraseña != contraseña:
        print("Error. Usuario o contraseña incorrecto/s. Ingrese nuevamente:")
        log_usuario= input("Ingrese el nombre de ususario:")
        log_contraseña= input("Ingrese la contraseña:")
    print("Acceso concedido.")

#Final punto 3

# Comienzo punto 5
def cambiar_contraseña():
    global contraseña
    contraseña_vieja=input("Ingrese su contraseña actual:")
    while contraseña_vieja != contraseña:
        print("Error. Contraeña incorrecta, ingrese nuevamente.")
        contraseña_vieja=input("Ingrese su contraseña actual:")
    contraseña_nueva=input("Ingrese la contraseña nueva:")

    while (contraseña_nueva == contraseña or len(contraseña_nueva) < 8 or not any(c.isupper() for c in contraseña_nueva) or not any(c.islower() for c in contraseña_nueva) or not any(c.isdigit() for c in contraseña_nueva) or not any(c in string.punctuation for c in contraseña_nueva) or " " in contraseña_nueva):
        print("La contraseña no cumple con los requisitos o es igual a la anterior. Inténtalo de nuevo.")
        contraseña_nueva = input("Ingresa tu nueva contraseña: ")
    contraseña = contraseña_nueva
    print("Contraseña actualizada.")
# Final punto 5

#Comienzo punto 4
def menu():
    menu_jugador= ["1- Instrucciones", "2- Jugar", "3- Cambiar contraseña", "4- Cerrar sesion"]
    for lista in range(len(menu_jugador)):
        print(menu_jugador[lista])
    eleccion= int(input("Elija una opcion:"))
    while eleccion <1 or eleccion >4:
        print("Error. Ingrese una opcion del 1 al 4")
        eleccion= int(input("Elija una opcion:"))
    verificacion = input(f"Esta seguro que desea continuar con la opcion {menu_jugador[eleccion-1]}? (si/no): ").lower()
    while verificacion != "si" and verificacion != "no":
        print("Error. Ingrese si o no: ")
        verificacion = input(f"Esta seguro que desea continuar con la opcion {menu_jugador[eleccion-1]}? (si/no): ").lower()
    while verificacion == "no":
        for lista in range(len(menu_jugador)):
            print(menu_jugador[lista])
        eleccion= int(input("Elija una opcion:"))
        verificacion = input(f"Esta seguro que desea continuar con la opcion {menu_jugador[eleccion-1]}? (si/no): ").lower()
        while verificacion != "si" and verificacion != "no":
            print("Error. Ingrese si o no: ")
            verificacion = input(f"Esta seguro que desea continuar con la opcion {menu_jugador[eleccion-1]}? (si/no): ").lower()
    if eleccion == 1:
        instrucciones(eleccion)
    elif eleccion == 2:
        jugar(eleccion)
    elif eleccion == 3:
        cambiar_contraseña()
    elif eleccion == 4:
        print("Cerrando sesión...")
    return eleccion



def instrucciones(opcion):
    if opcion == 1:
        print("Bienvenido a NO HAY SALIDA: BARCO EMBRUJADO. Sos el capitan de un "
        "barco que zarpo en busca de un tesoro legendario, pero una noche de "
        "tormenta algo cambio a bordo. Las velas se mueven sin viento, el "
        "timon gira solo y las voces de una tripulacion que ya no esta se "
        "escuchan entre las bodegas. Para escapar del barco embrujado "
        "debes superar los desafios que el navio te va imponiendo. En la "
        "Sala 1 debes descubrir una palabra oculta relacionada con la "
        "leyenda del barco jugando al Ahorcado, ingresando una letra por "
        "turno antes de agotar tus intentos. En la Sala 2 debes localizar y "
        "hundir la pequenia flota fantasma escondida en un tablero de 5 "
        "por 5, disparando a coordenadas antes de quedarte sin disparos. "
        "Cada sala superada te acerca un poco mas a la salida. Buena "
        "suerte, capitan.")
    
#Comienzo punto 7
def ahorcado():
    palabra = random.choice(palabras_ahorcado)
    oculta = []
    for letra in palabra:
        oculta.append("_")
    letras_usadas = []
    intentos = intentos_ahorcado

    while intentos > 0 and "_" in oculta:
        print(" ".join(oculta))
        print("Intentos restantes:", intentos)
        letra = input("Ingrese una letra: ").upper()

        if len(letra) != 1 or not letra.isalpha():
            print("Ingrese una única letra.")
        elif letra in letras_usadas:
            print("Ya ingresó esa letra.")
        else:
            letras_usadas.append(letra)
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        oculta[i] = letra
            else:
                intentos -= 1
                print("Esa letra no está en la palabra.")

    if "_" not in oculta:
        print("¡Descubriste la palabra!", "".join(oculta))
        return True
    else:
        print("Se acabaron los intentos. La palabra era:", palabra)
        return False
#Final punto 7

#Comienzo punto 6
def jugar(opcion):  #
    if opcion == 2:
        print("La tormenta te desvio de rumbo y ahora tu barco esta varado en una "
        "niebla que no se disipa. Algo se metio a bordo esa noche: los "
        "faroles se encienden solos, el timon responde a manos que no son "
        "las tuyas y una risa lejana recorre las bodegas vacias. Cuentan "
        "que otro capitan busco el mismo tesoro hace anios y jamas volvio a "
        "puerto. Si queres escapar del Barco Embrujado y quedarte con el "
        "tesoro, primero vas a tener que ganarte el respeto del fantasma "
        "que todavia habita el barco.")

        if ahorcado():
            print("Superaste la Sala 1. (La Sala 2 se suma en la próxima entrega.)")
        else:
            print("El barco embrujado te retiene para siempre en la Sala 1...")
#Final punto 6

while True:
    login()
    while True:
        eleccion = menu()
        if eleccion == 4:
            break

#Final punto 4