import random

# Diccionario de preguntas disponible globalmente
preguntas = {
    'básica': [
        {'enunciado': '¿Cuál es la capital de Chile?', 'alternativas': [['Santiago', 1], ['Lima', 0], ['Bogotá', 0]]},
        {'enunciado': '¿Cuántos lados tiene un cuadrado?', 'alternativas': [['Cuatro', 1], ['Cinco', 0], ['Seis', 0]]}
    ],
    'intermedia': [
        {'enunciado': '¿Qué elemento tiene el símbolo químico Fe?', 'alternativas': [['Hierro', 1], ['Oro', 0], ['Plata', 0]]}
    ],
    'avanzada': [
        {'enunciado': '¿Cuál es la teoría de cuerdas en física?', 'alternativas': [['Una teoría física', 1], ['Una ecuación', 0], ['Una hipótesis', 0]]}
    ]
}

def choose_q(dificultad, preguntas_por_dificultad):
    if preguntas_por_dificultad:
        pregunta = random.choice(preguntas_por_dificultad)
        preguntas_por_dificultad.remove(pregunta)
        return pregunta['enunciado'], pregunta['alternativas']
    else:
        return None, None
