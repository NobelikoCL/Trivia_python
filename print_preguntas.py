def print_pregunta(enunciado, alternativas):
    print(enunciado)
    print()
    letras = ['A', 'B', 'C', 'D']  # Letras para las opciones
    for index, alt in enumerate(alternativas):
        print(f"{letras[index]}. {alt[0]}")

if __name__ == "__main__":
    enunciado = '¿Cuál es la capital de Chile?'
    alternativas = [['Santiago', 1], ['Lima', 0], ['Bogotá', 0]]
    print_pregunta(enunciado, alternativas)
