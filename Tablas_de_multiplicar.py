def generar_tabla():
    while True:
        print("\n--- Generador de Tablas de Multiplicar ---")
        print("1. Generar tabla")
        print("2. Salir")

        opcion = int(input("Selecciona una opción (1-2): "))

        if opcion == 2:
            print("¡Gracias por usar el generador de tablas! Hasta luego.")
            break  # Salir del bucle

        if opcion == 1:
            numero = int(input("Ingresa el número para generar su tabla de multiplicar: "))
            print(f"\nTabla de multiplicar del número {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
        else:
            print("Opción no válida. Intenta de nuevo.")

generar_tabla()
