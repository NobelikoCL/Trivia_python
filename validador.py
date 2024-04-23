def validate(options):
    while True:
        choice = input("Desea Jugar, Opcion 1 = SI, Opcion 0 = NO: ").strip().upper()  # Convertir a mayúsculas
        if choice not in options:
            print(f"Opción no válida, ingrese una de las opciones válidas: {', '.join(options)}")
        else:
            return choice
