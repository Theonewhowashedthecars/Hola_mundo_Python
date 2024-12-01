def calcular_factorial():
    print("\n--- Calculadora de Factoriales ---")
    while True:
        numero = int(input("Ingresa un número entero no negativo (o -1 para salir): "))
        if numero == -1:
            print("¡Gracias por usar la calculadora de factoriales!")
            break
        elif numero < 0:
            print("Error: El número debe ser no negativo.")
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es: {factorial}")

calcular_factorial()
