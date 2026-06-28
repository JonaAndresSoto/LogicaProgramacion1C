import random
eleccion = input("Ingrese 1. Jugar  o 2 Salir: ")

if eleccion != "1":
    print("Gracias por jugar")
else:
    #Grupo de palabras a adivinar 
    palabras = ("perro", "gato", "vaca", "oveja", "cuy", "caballo", "pato","gallo","gallina")
    #random para escoger cualquier palabra en aleatorio
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    vidas = 6

    while True:
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        #menu interactivo para el usuario
        print(f"\n=============================")
        print(f"Vidas restantes: {vidas}")
        print(f"\n=============================")
        print(f"Palabra actual: {progreso.strip()}")
        print(f"\n=============================")
        print(f"Pista = Animales domesticos")
        print(f"\n=============================")
        print("\nEscoge una opcion")
        print("1. Ingresar una letra")
        print("2. Descubrir la palabra")
        print("3. Pedir nueva palabra")
        print("4. Salir del juego")
        print(f"\n=============================")
        
        opcion = input("Elige una opción (1-4): ").strip()
        
        if opcion == "1":
            letra_ingresada = input("Ingresa la letra: ").lower().strip()
            
            if len(letra_ingresada) != 1:
                print("Solo ingresa una letra.")
                continue
                
            if letra_ingresada in palabra_secreta:
                if letra_ingresada not in letras_adivinadas:
                    letras_adivinadas.append(letra_ingresada)
                
                adivino_palabra = True
                for letra in palabra_secreta:
                    if letra not in letras_adivinadas:
                        adivino_palabra = False
                        break
                
                if adivino_palabra:
                    print(f"\n Felicidades Juego Ganado, Palabra: {palabra_secreta}")
                    break 
            else:
                vidas -= 1
                if vidas > 0:
                    print("\nLetra Incorrecta")
                else:
                    print(f"\n Intentos agotados. La palabra era: {palabra_secreta}")
                    break 

        elif opcion == "2":
            print(f"\n La palabra fue: {palabra_secreta}")
            break 
                    
        elif opcion == "3":
            print("\nBuscando nueva palabra")
            palabra_secreta = random.choice(palabras)
            letras_adivinadas = []
            vidas = 6 
            continue 
            
        elif opcion == "4":
            print("\nSaliendo del juego")
            break 
            
        else:
            print("\nPor favor elige 1, 2, 3 o 4.")

print("\nFin del programa")