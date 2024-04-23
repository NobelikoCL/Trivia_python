from level import choose_level
from question import choose_q, preguntas
from shuffle import shuffle_alt
from print_preguntas import print_pregunta
from verify import verificar

def main():
    print("Desea jugar? Opcion 1 = SI, Opcion 0 = NO:")
    iniciar = input().strip()
    if iniciar == '0':
        print("Nos vemos pronto!")
        return

    nivel = choose_level()  # Obtiene el nivel del usuario
    preguntas_nivel = preguntas[nivel]

    for pregunta in preguntas_nivel:
        enunciado, alternativas_lista = pregunta['enunciado'], pregunta['alternativas']
        alternativas_mezcladas = shuffle_alt(alternativas_lista)  # Asegúrate de pasar solo la lista de alternativas
        print_pregunta(enunciado, alternativas_mezcladas)  # Asegúrate de que esta línea esté correctamente indentada

        respuesta_usuario = input("Ingrese su opción: ").strip().upper()
        # Convertir letras (A, B, C) a índice (0, 1, 2)
        if respuesta_usuario in ['A', 'B', 'C']:
            indice_respuesta = ord(respuesta_usuario) - ord('A')
            if verificar(alternativas_mezcladas, indice_respuesta):
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta.")
        else:
            print("Ingrese una opción válida: A, B, o C.")

        print("Desea continuar jugando? Opcion 1 = SI, Opcion 0 = NO:")
        continuar = input().strip()
        if continuar == '0':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
