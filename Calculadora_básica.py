def calculadora():
    print("-----Bienvenido-----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Selecciona una opción (1-5): "))
    if opcion == 5:
        print("Hasta luego...")
        exit()
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print(f"El resultado de la suma es: {num1+num2}") 
    elif opcion == 2:
        print(f"El resultado de la resta es: {num1-num2}")
    elif opcion == 3:
        print(f"El resultado de la multiplicación es: {num1*num2}")
    elif opcion == 4:
        if num2 != 0:       
            print(f"El resultado de la división es: {num1/num2}")
        else:
            print("Error, no se puede dividir entre cero. ")     
    
    else:
        print("Error!! número no válido")
calculadora()