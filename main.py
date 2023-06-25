import pyautogui
import time
import threading
import os

# Lista de nomes de arquivo para as diferentes imagens de "lizard"
lizard_images = [
    'lizardADown.png', 'lizardAleft.png', 'lizardARight.png', 'lizardAUp.png',
    'lizardMDown.png', 'lizardMLeft.png', 'lizardMRight.png', 'lizardMUp.png',
    'lizardWDown.png', 'lizardWLeft.png', 'lizardWRight.png', 'lizardWUp.png'
]
pyautogui.hotkey('Alt','tab')

time.sleep(3)

def andarMapa():
        mapa = pyautogui.locateOnScreen('mapa.png') #Abrir o mapa
        pyautogui.click(mapa)  
        pyautogui.click()
          

def verificarMana():
    while True:
        mana = os.path.join('player/mana.png')
        # Verificar se a imagem "mana.png" está presente na tela
        mana_pos = pyautogui.locateOnScreen(mana,confidence=0.7)
        
        if mana_pos is not None:
            # Se a imagem for encontrada, pressione a tecla '2'
            pyautogui.press('2')
            time.sleep(60)
        
def verificar_e_clicar_lizard():
    while True:
        for image in lizard_images:
            # Verificar se a imagem atual está presente na tela
            caminho_pasta = os.path.join("images/lizard/", image)
            lizard_pos = pyautogui.locateOnScreen(caminho_pasta, confidence=0.6)
            if lizard_pos is not None:
                # Se a imagem for encontrada, clique nela
                pyautogui.click(lizard_pos)
                # Pressione a tecla '1'
                pyautogui.press('1')
        
        time.sleep(1)

# Criar e iniciar uma thread para a função verificar_e_clicar_lizard()
thread_andar = threading.Thread(target=andarMapa)
thread_mana = threading.Thread(target=verificarMana)
thread_lizard = threading.Thread(target=verificar_e_clicar_lizard)

thread_lizard.start()
thread_mana.start()
thread_andar.start()



thread_lizard.join()