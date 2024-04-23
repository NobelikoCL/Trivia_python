def verificar(alternativas, eleccion):
    if alternativas[eleccion][1] == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    alternativas = [['Santiago', 1], ['Lima', 0], ['Bogotá', 0]]
    eleccion = 0  # El índice de la respuesta elegida
    verificar(alternativas, eleccion)
