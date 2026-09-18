import os
import sys
import time
import utils
import random

# Verifica o sistema operacional e importa os módulos corretos
if os.name == "nt":
  print(f"Running on Windows ({os.name})")
  import msvcrt
else:
  print(f"Running on Linux or macOS ({os.name})")
  import termios
  import tty
BUFFER_TECLA = []
def ler_tecla():
  if BUFFER_TECLA:
    return BUFFER_TECLA.pop()
  """Lê uma única tecla sem precisar apertar Enter."""
  # Código para Windows
  if os.name == "nt":
    # getch() retorna bytes, .decode() transforma em texto (str)
    return msvcrt.getch().decode("utf-8", errors="ignore")

  # Código para Linux / macOS
  else:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      # tty.setraw(sys.stdin.fileno())
      tty.setcbreak(fd)
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def send_space():
  BUFFER_TECLA.append(' ')  # Adiciona Sspace ao buffer de teclas

utils.clear_screen()
utils.print_title()
utils.print_instructions()

sequencia_jogo = []
sequencia_usuario = []
teclas_validas = ["I", "J", "L", "K"]

jogo_iniciado = False
tecla_raw = ''

while True:
  tecla_raw = ler_tecla()
  tecla = tecla_raw.upper()
  if (tecla_raw == "\r" or tecla_raw == "\n"):
    print("\nIniciando o jogo...")
    jogo_iniciado = True
  if tecla == "Q":
    print("\nSaindo do programa...")
    break
  if jogo_iniciado:
    if len(sequencia_usuario) == len(sequencia_jogo):
      sequencia_jogo.append(teclas_validas[random.randint(0, 3)])
      for cor in sequencia_jogo:
        utils.pisca(cor, len(sequencia_jogo))
      sequencia_usuario = []
    if tecla in teclas_validas:
      utils.pisca(tecla, -1)
      sequencia_usuario.append(tecla)
      if sequencia_usuario[len(sequencia_usuario)-1] != sequencia_jogo[len(sequencia_usuario)-1]:
        print("\nVocê errou!")
        break
      if len(sequencia_usuario) == len(sequencia_jogo):
        time.sleep(.5)
        send_space()  # Simula o pressionamento de Space para iniciar a próxima rodada

utils.print_final_jogo(sequencia_jogo, sequencia_usuario)

exit(0)