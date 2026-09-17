import math

def clear_screen():
    import os
    """Limpa a tela do terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_title():
    """Exibe o título do jogo na tela."""
    print("##################################")
    print("#                                #")
    print("#        G  E  N  I  U  S        #")
    print("#                                #")
    print("##################################")
    print("")

def print_instructions():
    """Exibe as instruções do jogo na tela."""
    print("Bem-vindo ao jogo Genius!")
    print("")
    print("O objetivo do jogo é repetir a sequência de cores mostrada na tela.")
    print("A cada rodada a sequência ficará maior e mais rápida.")
    print("")
    print("As cores são: Vermelho, Azul, Verde, Amarelo.")
    print("Teclas mapeadas:")
    print("             [I] - Vermelho")
    print("  Verde - [J]   [L] - Azul")
    print("             [K] - Amarelo")
    print("")
    print("Pressione as teclas correspondentes às cores na sequência correta.")
    print("Boa sorte!")
    print("")
    print("Pressione [Enter] para começar o jogo ou 'Q' para sair a qualquer momento.")
    print("")

def tempo_espera(iteracao=0):
    import time
    """Retorna o tempo de espera entre as cores, mas não abaixo do mínimo."""
    tempo_minimo = 0.25
    tempo_maximo = 1
    novo_tempo = tempo_minimo + (tempo_maximo - tempo_minimo) * math.exp(-0.5 * iteracao)
    time.sleep(novo_tempo)

COR_VERMELHO = '\033[91m'
COR_VERDE    = '\033[92m'
COR_AZUL     = '\033[94m'
COR_AMARELO  = '\033[93m'
COR_RESET    = '\033[0m'
def pisca(cor, iteracao=0):
    import time

    # cor é 0 = Vermelho, 1 = Verde, 2 = Azul, 3 = Amarelo
    """Simula o piscar de uma cor na tela."""
    match cor:
        case 0:
            print(COR_VERMELHO, end="")
            print("    I    ")
            print("         ")
            print("         ")
            print(COR_RESET, end="")
        case 1:
            print(COR_VERDE, end="")
            print("         ")
            print(" J       ")
            print("         ")
            print(COR_RESET, end="")
        case 2:
            print(COR_AZUL, end="")
            print("         ")
            print("       L ")
            print("         ")
            print(COR_RESET, end="")
        case 3:
            print(COR_AMARELO, end="")
            print("         ")
            print("         ")
            print("    K    ")
            print(COR_RESET, end="")
    if iteracao >= 0:
        tempo_espera(iteracao)
        print("\033[3A", end="")
        print("         ")
        print("         ")
        print("         ")
    print("\033[3A", end="")

