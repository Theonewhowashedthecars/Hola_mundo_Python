import math

def calculadora_avanzada():
    while True:
        print("\n--- Calculadora Avanzada ---")
        print("1. Potencia (base^exponente)")
        print("2. Raíz cuadrada")
        print("3. Módulo (resto de la división)")
        print("4. Salir")

        opcion = int(input("Selecciona una opción (1-4): "))

        if opcion == 4:
            print("¡Gracias por usar la calculadora avanzada! Hasta luego.")
            break

        if opcion == 1:
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            print(f"Resultado: {base}^{exponente} = {math.pow(base, exponente)}")
        elif opcion == 2:
            numero = float(input("Ingresa un número: "))
            if numero >= 0:
                print(f"Resultado: √{numero} = {math.sqrt(numero)}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        elif opcion == 3:
            dividendo = int(input("Ingresa el dividendo: "))
            divisor = int(input("Ingresa el divisor: "))
            if divisor != 0:
                print(f"Resultado: {dividendo} % {divisor} = {dividendo % divisor}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Intenta de nuevo.")

calculadora_avanzada()
