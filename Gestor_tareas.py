from datetime import datetime

def agregar_tarea(tareas, archivo_tareas):
    nueva_tarea = input("Ingresa la nueva tarea: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tarea_con_fecha = f"{nueva_tarea} (Añadida el {fecha})"
    tareas.append(tarea_con_fecha)
    guardar_tareas(archivo_tareas, tareas)
    print("Tarea agregada.")

def cargar_tareas(archivo):
    """Carga las tareas desde un archivo."""
    try:
        with open(archivo, "r") as f:
            tareas = [line.strip() for line in f.readlines()]
        return tareas
    except FileNotFoundError:
        return []

def guardar_tareas(archivo, tareas):
    """Guarda las tareas en un archivo."""
    with open(archivo, "w") as f:
        for tarea in tareas:
            f.write(tarea + "\n")

def mostrar_tareas(tareas):
    """Muestra las tareas con sus índices."""
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("\n--- Tareas Pendientes ---")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def gestor_de_tareas():
    archivo_tareas = "tareas.txt"
    tareas = cargar_tareas(archivo_tareas)

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Ver tareas pendientes")
        print("2. Agregar una nueva tarea")
        print("3. Marcar una tarea como completada")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas, archivo_tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
            if tareas:
                indice = int(input("Selecciona el número de la tarea completada: ")) - 1
                if 0 <= indice < len(tareas):
                    tareas[indice] += " (Completada)"
                    guardar_tareas(archivo_tareas, tareas)
                    print("Tarea marcada como completada.")
                else:
                    print("Índice no válido.")
        elif opcion == "4":
            mostrar_tareas(tareas)
            if tareas:
                indice = int(input("Selecciona el número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    guardar_tareas(archivo_tareas, tareas)
                    print(f"Tarea eliminada: {tarea_eliminada}")
                else:
                    print("Índice no válido.")
        elif opcion == "5":
            print("¡Gracias por usar el gestor de tareas!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

gestor_de_tareas()
