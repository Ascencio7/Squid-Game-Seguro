import random
import sys

def roock_paper_scissors():
    print("\nBienvenido a Piedra, Papel y Tijera.")
    
    choices = ["piedra", "papel", "tijera"]
    player_choice = input("\nIngresa una opción (piedra, papel, tijera): ").lower()
    
    if player_choice not in choices:
        print("Opción inválida. Intente de nuevo.")
        return
    
    computer_choice = random.choice(choices)
    print(f"La computadora escogio {computer_choice}.")
    
    if player_choice == computer_choice:
        print("Empate!")
    elif (player_choice == "piedra" and computer_choice == "tijera") or \
         (player_choice == "papel" and computer_choice == "piedra") or \
         (player_choice == "tijera" and computer_choice == "papel"):
        print("Ganaste!")
    else:
        print("\n¡Perdiste! ¡El sistema se autodestruira en 3... 2... 1...!")
        sys.exit()
        
roock_paper_scissors()