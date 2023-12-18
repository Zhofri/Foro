# Importar la biblioteca para generar elecciones aleatorias
import random

# Iniciar el juego
print("¡Bienvenido al juego de Piedra, Papel y Tijera!")

# Definir las opciones del juego
opciones = {1: "piedra", 2: "papel", 3: "tijera"}

# Función para obtener la elección del jugador
def obtener_eleccion_jugador():
    print("Elige 1 para piedra, 2 para papel o 3 para tijera:")
    eleccion_numero = int(input())
    
    while eleccion_numero not in opciones:
        print("Número no válido. Intenta nuevamente.")
        print("Elige 1 para piedra, 2 para papel o 3 para tijera:")
        eleccion_numero = int(input())

    eleccion = opciones[eleccion_numero]
    return eleccion

# Función para obtener la elección de la computadora
def obtener_eleccion_computadora():
    return opciones[random.randint(1, 3)]

# Obtener elecciones
eleccion_jugador = obtener_eleccion_jugador()
eleccion_computadora = obtener_eleccion_computadora()

# Imprimir elecciones
print(f"El jugador eligió: {eleccion_jugador}")
print(f"La computadora eligió: {eleccion_computadora}")
