import random

def juego_adivinanza():
    print("\n--- Juego de Adivinanza ---")
    print("Adivina un número entre 1 y 100.")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Ingresa tu adivinanza: "))
        intentos += 1

        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

juego_adivinanza()
