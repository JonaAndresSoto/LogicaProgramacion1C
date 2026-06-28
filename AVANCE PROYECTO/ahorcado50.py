
import random

palabras = ["perro", "software", "programacion", "uide"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas = 6
eleccion = input("Ingrese 1. Jugar o 2 Salir: ")


if eleccion != "1":
    print("Gracias por jugar")
else:
    while True:
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        print(f"\nPalabra actual: {progreso.strip()}")
    
        letra_ingresada = input("Ingrese la letra: ").lower()
    
        if letra_ingresada in palabra_secreta:
            letras_adivinadas.append(letra_ingresada)
            adivino_palabra = True
            for letra in palabra_secreta:
                if letra not in letras_adivinadas:
                    adivino_palabra = False
                    break
            
