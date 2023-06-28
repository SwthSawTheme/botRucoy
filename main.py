import time
import pyautogui
from functions import lizard
from functions import verificarMana
from functions import andar
from functions import verificarlife
from functions import capturar_screenshot
import threading

pyautogui.hotkey('alt','tab')

time.sleep(3)

execucao = True

def func1():
    global execucao
    while execucao:
        # Lógica da função andar
        andar()
        time.sleep(1)

def func2():
    global execucao
    while execucao:
        lizard()
        time.sleep(1)

def func3():
    global execucao
    while execucao:
        verificarMana()
        time.sleep(1)

def func4():
    global execucao
    while execucao:
        verificarlife()
        time.sleep(1)
def func5():
    global execucao
    while execucao:
        capturar_screenshot()
        time.sleep(1)

# Criar as threads para as funções andar e lizard
thread_andar = threading.Thread(target=andar)
thread_lizard = threading.Thread(target=lizard)
thread_mana = threading.Thread(target=verificarMana)
thread_life = threading.Thread(target=verificarlife)
thread_screenshot = threading.Thread(target=capturar_screenshot)

# Iniciar as threads
thread_andar.start()
thread_lizard.start()
thread_mana.start()
thread_life.start()
thread_screenshot.start()

input("Pressione enter para interromper...")
execucao = False

# Esperar que as threads terminem a execução
thread_andar.join()
thread_lizard.join()
thread_mana.join()
thread_life.join()
thread_screenshot.join()