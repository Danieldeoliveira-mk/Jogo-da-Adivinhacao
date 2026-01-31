import random
import time
import readchar
from colorama import Fore, Style, init
print("Esse é o Jogo da Adivinhação\nCriado por Daniel de Oliveira")

def Jogo():
    while True:
        numero_maquina = random.randint(0, 100)
        print("\nVou pensar em um numero e você tenta descobrir, OK?\nAperte algo para continuar")
        key = readchar.readkey()
        print("Pensando...")
        time.sleep(1.5)
        print("\nPensei em um numero!")
        tentativa = 0
        while True:
            player_chute = int(input("\nQual numero estou pensando?\nNumero de 1 até 100\n"))
            tentativa += 1
            tentativa_string = f"Tentativa {Fore.MAGENTA}{tentativa}{Style.RESET_ALL} | "
            if player_chute == numero_maquina:
                print(f"{tentativa_string}{Fore.GREEN}Você acertou! Parabens!{Style.RESET_ALL}")
                nome_player = input("Qual é o seu nome? ")
                while True:
                    escolha_final = input("Quer jogar denovo? [s/n]")
                    if escolha_final == "n":
                        print("Tchau")
                        return
                    elif escolha_final == "s":
                        break
                break
            else:
                    print(f"{tentativa_string}Você errou, o numero que pensei é {f"{Fore.BLUE}MAIOR" if player_chute < numero_maquina else f"{Fore.YELLOW}MENOR"}{Style.RESET_ALL} que o numero {player_chute}")

Jogo()