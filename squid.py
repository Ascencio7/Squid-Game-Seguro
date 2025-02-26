import random # Librería para que la computadora elija una opcion aleatoria
import sys # Librería para poder salir del programa en caso de perder


"""
    Función que permite jugar la partidad contra la computadora. El jugador (usuario) elige la opcion
    y la computadora selecciona otra aleatoriamente. Y se determina el resultado según las reglas del juego.
"""

def roock_paper_scissors():
    print("\nBienvenido a Piedra, Papel y Tijera.")
    
    # Es una lista de opciones validas del juego
    choices = ["piedra", "papel", "tijera"]
    
    # Y se pide al usuario ingresar la opcion y se permite la conversion a minusculas
    player_choice = input("\nIngresa una opción (piedra, papel, tijera): ").lower()
    
    # Se verifica la opcion ingresada fue incorrecta
    if player_choice not in choices:
        print("Opción inválida. Intente de nuevo.")
        return # se vuelve a pedir el ingreso de la opcion
    
    # La computadora elige una opción aleatoria de la lista
    computer_choice = random.choice(choices)
    
    # Se muestra la opcion elegida por la computadora
    print(f"La computadora escogio {computer_choice}.")
    
    # Se comparan las opciones para determinar el resultado
    if player_choice == computer_choice:
        print("Empate!") # Se muestra si ambas opciones fueron iguales
    elif (player_choice == "piedra" and computer_choice == "tijera") or \
         (player_choice == "papel" and computer_choice == "piedra") or \
         (player_choice == "tijera" and computer_choice == "papel"):
        print("Ganaste!") # Si se gana seguna la regla se muestra el mensaje de ganador
    else:
        # Si la computadora gana se muestra el siguiente mensaje
        print("\n¡Perdiste! ¡El sistema se autodestruira en 3... 2... 1...!")
        sys.exit() # Se termina la ejecución del programa de forma abrupta
        
# Se llama la función para iniciar el juego. 
roock_paper_scissors()