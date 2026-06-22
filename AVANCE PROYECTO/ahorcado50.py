import random
# libreria para la funcion de aleatorio 

def iniciar():
    print("***************************")
    print("    JUEGO DEL AHORCADO     ")
    print("***************************")
    print("1. Jugar")
    print("2. Salir")
    
    eleccion = input("Elige la opción 1 o 2: ")
    
    if eleccion == "1":
        print("¡Iniciando partida!")
        jugar(obtener_palabra(), "", 0)
        
        iniciar()
    elif eleccion == "2":
        print("gracias por jugar")
    else:
        print("Opción incorrecta. Intenta de nuevo.")
        iniciar()

# 2. LOS ERRORES (El estado del muñeco)

def mostrar_estado_muneco(errores):

    estados = [
        "Perfecto, quedan 6 intentos.",
        "Error 1: Se dibujó la cabeza.",
        "Error 2: Se dibujó el cuerpo.",
        "Error 3: Se dibujó un brazo.",
        "Error 4: Se dibujaron ambos brazos.",
        "Error 5: Se dibujó una pierna. ¡Cuidado!",
        "Error 6: Se dibujó la otra pierna. ¡Ahorcado!"
    ]
    print(estados[errores])



def jugar(palabra, letras_usadas, errores):
    # numero de intentos
    if errores == 6:
        mostrar_estado_muneco(errores)
        print("¡Perdiste! Te quedaste sin intentos.")
        print("La palabra correcta era:")
        print(palabra)
        return

    progreso = armar_palabra(palabra, letras_usadas, 0)
    
    print("=============================")
    mostrar_estado_muneco(errores)
    print("Palabra:")
    print(progreso)

    if "_" not in progreso:
        print("¡Felicidades, ganaste el juego!")
        return

    print("Opciones: 1=Adivinar palabra, 2=Nueva palabra, 3=Salir al menú")
    opcion = input("Ingresa una letra o un número de opción: ").upper()


# inicializador 

if __name__ == "__main__":
    iniciar()