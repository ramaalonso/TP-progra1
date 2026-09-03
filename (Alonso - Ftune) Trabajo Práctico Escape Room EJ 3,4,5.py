# TP Sala de escape
import string

# Comienzo punto 3
def login():
    usuario= "capitan"
    contraseña = "Tesoro.2026"
    print("\n===== NO HAY SALIDA: BARCO EMBRUJADO =====")
    log_usuario= input("Ingrese el nombre de ususario:")
    log_contraseña= input("Ingrese la contraseña:")
    while log_usuario != usuario or log_contraseña != contraseña:
        print("Error. Usuario o contraseña incorrecto/s. Ingrese nuevamente:")
        log_usuario= input("Ingrese el nombre de ususario:")
        log_contraseña= input("Ingrese la contraseña:")
        print("Acceso concedido. (Acá seguirá el menú en la próxima entrega.)")
#Final punto 3

# Comienzo punto 5
def cambiar_contraseña(contraseña):
    contraseña_vieja=input("Ingrese su contraseña actual:")
    while contraseña_vieja != contraseña:
        print("Error. Contraeña incorrecta, ingrese nuevamente.")
        contraseña_vieja=input("Ingrese su contraseña actual:")
    contraseña_nueva=input("Ingrese la contraseña nueva:")

    while (contraseña_nueva == contraseña or len(contraseña_nueva) < 8 or not any(c.isupper() for c in contraseña_nueva) or not any(c.islower() for c in contraseña_nueva) or not any(c.isdigit() for c in contraseña_nueva) or not any(c in string.punctuation for c in contraseña_nueva) or " " in contraseña_nueva):
        print("La contraseña no cumple con los requisitos o es igual a la anterior. Inténtalo de nuevo.")
        contraseña_nueva = input("Ingresa tu nueva contraseña: ")
    l_contraseña_nueva = list(contraseña_nueva)
    print("Contraseña actualizada.")
    return contraseña_nueva
# Final punto 5

#Comienzo punto 4
def menu():
    menu_jugador= ["1- Instrucciones","2- Jugar","3- Cambiar contraseña", "4- Cerrar sesion"]
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
    return eleccion

def instrucciones(eleccion):
    if eleccion = 1:
#INSTRUCCIONES (PREGUNTAR COMO HACERLO CORRECTAMENTE)
#FALTA AGREGAR QUE HACE CADA OPCION
        


#Final punto 4