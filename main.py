import time
import pyautogui
from functions import verificarMana
from functions import andar
from functions import verificarlife
from functions import capturar_screenshot
from functions import reconnect
import threading

pyautogui.hotkey('alt','tab')

time.sleep(1)

execucao = True

def func1():
    global execucao
    while execucao:
        andar()
        time.sleep(3)
        
def func2():
    global execucao
    while execucao:
        reconnect()
        time.sleep(1)
        
def func3():
    global execucao
    while execucao:
        verificarMana()
        time.sleep(6)

def func4():
    global execucao
    while execucao:
        verificarlife()
        time.sleep(3)
        
def func5():
    global execucao
    while execucao:
        capturar_screenshot()
        time.sleep(1)

# Criar as threads para as funções andar e lizard
thread_andar = threading.Thread(target=func1)
thread_reconnect = threading.Thread(target=func2)
thread_mana = threading.Thread(target=func3)
thread_life = threading.Thread(target=func4)
thread_screenshot = threading.Thread(target=func5)

# Iniciar as threads
thread_andar.start()
thread_mana.start()
thread_life.start()
thread_screenshot.start()
thread_reconnect.start()

print('Executando...')
print('Desenvolvido by Swth Discord: .swth')
input("Pressione enter para interromper...")
execucao = False

# Esperar que as threads terminem a execução
thread_andar.join()
thread_mana.join()
thread_life.join()
thread_screenshot.join()
thread_reconnect.join()