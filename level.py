def choose_level():
    print("Seleccione el nivel de dificultad:")
    print("1. Básico")
    print("2. Intermedio")
    print("3. Avanzado")
    nivel_map = {'1': 'básica', '2': 'intermedia', '3': 'avanzada'}
    while True:
        opcion = input("Ingrese el número del nivel deseado: ").strip()
        if opcion in nivel_map:
            return nivel_map[opcion]
        else:
            print("Opción no válida, por favor ingrese 1, 2, o 3.")
