import random
import time
import readchar
from colorama import Fore, Style, init
import json
import os

init(autoreset=True)
print("Esse é o Jogo da Adivinhação\nCriado por Daniel de Oliveira")

def Jogo():
    while True:
        numero_maquina = random.randint(1, 100)
        tentativa_maxima = 0
        print("\nVou pensar em um numero e você tenta descobrir, OK?")
        while True:
            dificuldade_escolha = input("Você quer jogar o modo difícil?\nO modo difícil tem o limite de 10 tentativas [s/n]")
            if dificuldade_escolha == "s":
                tentativa_maxima = 10
                print("Você escolheu o modo dificil")
                break
            elif dificuldade_escolha == "n":
                print("Você escolheu o modo normal")
                break
            else:
                print(f"{Fore.RED}Escolha Sim (s) ou Não (n){Style.RESET_ALL}")
        print("\nAperte algo para continuar")
        key = readchar.readkey()
        print("Pensando...")
        time.sleep(1.5)
        print("\nPensei em um numero!")
        tentativa = 0
        while tentativa < tentativa_maxima or tentativa_maxima == 0:
            while True:
                try:
                    player_chute = int(input("\nQual numero estou pensando?\nNumero de 1 até 100\n"))
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite apenas numeros{Style.RESET_ALL}")
                    continue
                if not 0 < player_chute < 101:
                    print(f"{Fore.RED}Escolha um numero entre 1 e 100{Style.RESET_ALL}\n")
                else:
                    break
            tentativa += 1
            tentativa_string = f"Tentativa {Fore.MAGENTA}{tentativa}{Style.RESET_ALL} | "
            if player_chute == numero_maquina:
                print(f"{tentativa_string}{Fore.GREEN}Você acertou! Parabens!{Style.RESET_ALL}")
                nome_player = input("Qual é o seu nome? ")
                incluir_player(nome_player, tentativa)
                while True:
                    escolha_final = input("\nQuer jogar denovo? [s/n]")
                    if escolha_final == "n":
                        print("Tchau")
                        return
                    elif escolha_final == "s":
                        break
                    else:
                        print(f"\n{Fore.RED}Escolha entre Sim (s) ou Não (n){Style.RESET_ALL}\n")
                break
            else:
                    print(f"{tentativa_string}Você errou, o numero que pensei é {f"{Fore.BLUE}MAIOR" if player_chute < numero_maquina else f"{Fore.YELLOW}MENOR"}{Style.RESET_ALL} que o numero {player_chute}")
                    if numero_maquina - 5 < player_chute < numero_maquina + 5:
                        print(f"{Fore.RED}Ta fervendo!{Style.RESET_ALL}")
                    elif numero_maquina - 25 < player_chute < numero_maquina + 25:
                        print(f"{Fore.LIGHTRED_EX}Ta quente{Style.RESET_ALL}")
                    elif numero_maquina - 50 < player_chute < numero_maquina + 50:
                        print(f"{Fore.LIGHTBLUE_EX}Tá frio{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.BLUE}Tá congelando{Style.RESET_ALL}")
        if tentativa == 10 and tentativa_maxima != 0:
            print("\nGAME OVER\nVocê não conseguiu acertar em 10 tentantivas")
            print("\nAperte algo para continuar")
            key = readchar.readkey()

def criar_ranking():
    if not os.path.exists("ranking.json"):
        dados_jogadores = []
        with open("ranking.json", "w", encoding="utf-8") as ranking:
            json.dump(dados_jogadores, ranking, indent=4)

def incluir_player(nome, pontos):
    with open("ranking.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    dados.append({"nome" : nome, "pontos" : pontos})
    dados.sort(key= lambda x: x["pontos"])
    if len(dados) > 10:
        dados = dados[:10]
    with open("ranking.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
    while True:
        perguntar = input("Quer ver o ranking? [s/n]")
        if perguntar == "s":
            print("\nO ranking é:")
            for x, y in enumerate(dados, 1):
                print(f"{x}. {y["nome"]}, {y["pontos"]} tentativas")
            break
        elif not perguntar == "n":
            print(f"{Fore.RED}Escolha Sim (s) ou Não (n){Style.RESET_ALL}")
        else:
            break

criar_ranking()
Jogo()