def convertir_unidades():
    while True:
        print("\n--- Convertidor de Unidades ---")
        print("1. Metros a Kilómetros")
        print("2. Grados Celsius a Fahrenheit")
        print("3. Kilogramos a Libras")
        print("4. Salir")

        opcion = int(input("Selecciona una opción (1-4): "))

        if opcion == 4:
            print("¡Gracias por usar el convertidor! Hasta luego.")
            break  # Salir del bucle

        if opcion == 1:
            metros = float(input("Ingresa la cantidad en metros: "))
            kilometros = metros / 1000
            print(f"{metros} metros son {kilometros:.2f} kilómetros.")
        elif opcion == 2:
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C son {fahrenheit:.2f}°F.")
        elif opcion == 3:
            kilogramos = float(input("Ingresa la cantidad en kilogramos: "))
            libras = kilogramos * 2.20462
            print(f"{kilogramos} kg son {libras:.2f} libras.")
        else:
            print("Opción no válida. Intenta de nuevo.")

convertir_unidades()
