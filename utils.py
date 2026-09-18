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

def print_final_jogo(sequencia_jogo, sequencia_usuario):
    print("\nFim do jogo.")
    print("\n    Sequência correta: ", sequencia_jogo)
    print("Sequência pressionada: ", sequencia_usuario)
    print(f"\nSua pontuação foi (nível.acertos): {len(sequencia_jogo)}.{len(sequencia_usuario) - 1}")
    print("Obrigado por jogar!")

def tempo_espera(iteracao=0):
    import time
    """Retorna o tempo de espera entre as cores, mas não abaixo do mínimo."""
    tempo_minimo = 0.2
    tempo_maximo = 1
    novo_tempo = tempo_minimo + (tempo_maximo - tempo_minimo) * math.exp(-0.5 * iteracao)
    time.sleep(novo_tempo)

COR_VERMELHO = '\033[91m'
COR_VERDE    = '\033[92m'
COR_AZUL     = '\033[94m'
COR_AMARELO  = '\033[93m'
COR_RESET    = '\033[0m'
def pisca(letra, iteracao=0):
    import time
    # letra é "I" = Vermelho, "J" = Verde, "L" = Azul, "K" = Amarelo
    """Simula o piscar de uma cor na tela."""
    match letra:
        case "I": # Vermelho
            print(COR_VERMELHO, end="")
            print("    I    ")
            print("         ")
            print("         ")
        case "J": # Verde
            print(COR_VERDE, end="")
            print("         ")
            print(" J       ")
            print("         ")
            print(COR_RESET, end="")
        case "L": # Azul
            print(COR_AZUL, end="")
            print("         ")
            print("       L ")
            print("         ")
            print(COR_RESET, end="")
        case "K": # Amarelo
            print(COR_AMARELO, end="")
            print("         ")
            print("         ")
            print("    K    ")
            print(COR_RESET, end="")

    print(COR_RESET, end="")
    print("\033[3A", end="")
    if iteracao >= 0:
        tempo_espera(iteracao)
        print("         ")
        print("         ")
        print("         ")
        print("\033[3A", end="")
        time.sleep(0.075)
    