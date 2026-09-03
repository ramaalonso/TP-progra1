def login():       #punto 3
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
        
        
def jugar(opcion):   #punto 6
    if opcion == 1:
        print("La tormenta te desvio de rumbo y ahora tu barco esta varado en una "
        "niebla que no se disipa. Algo se metio a bordo esa noche: los "
        "faroles se encienden solos, el timon responde a manos que no son "
        "las tuyas y una risa lejana recorre las bodegas vacias. Cuentan "
        "que otro capitan busco el mismo tesoro hace anios y jamas volvio a "
        "puerto. Si queres escapar del Barco Embrujado y quedarte con el "
        "tesoro, primero vas a tener que ganarte el respeto del fantasma "
        "que todavia habita el barco.")
login()