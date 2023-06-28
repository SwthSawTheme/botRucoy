import pyautogui
import time
import os

def AndarMapa1():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos)
    mapa1 = os.path.join('images/mapa/mapa1.png')
    mapa_pos = pyautogui.locateOnScreen(mapa1,confidence=0.7)
    pyautogui.click(mapa_pos)
    pyautogui.press('f1')
    
def AndarMapa2():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos2 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos2)
    mapa2 = os.path.join('images/mapa/mapa2.png')
    mapa_pos2 = pyautogui.locateOnScreen(mapa2,confidence=0.7)
    pyautogui.click(mapa_pos2)
    pyautogui.press('f1')
    pyautogui.press('3')
    
def AndarMapa3():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos3 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos3)
    mapa3 = os.path.join('images/mapa/mapa3.png')
    mapa_pos3 = pyautogui.locateOnScreen(mapa3,confidence=0.7)
    pyautogui.click(mapa_pos3)
    pyautogui.press('f1')
    pyautogui.press('3')

def AndarMapa4():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos4 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos4)
    mapa4 = os.path.join('images/mapa/mapa4.png')
    mapa_pos4 = pyautogui.locateOnScreen(mapa4,confidence=0.7)
    pyautogui.click(mapa_pos4)
    pyautogui.press('f1')
    pyautogui.press('3')

def AndarMapa5():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos5 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos5)
    mapa5 = os.path.join('images/mapa/mapa5.png')
    mapa_pos5 = pyautogui.locateOnScreen(mapa5,confidence=0.7)
    pyautogui.click(mapa_pos5)
    pyautogui.press('f1')
    pyautogui.press('3')
    
def AndarMapa6():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos6 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos6)
    mapa6 = os.path.join('images/mapa/mapa6.png')
    mapa_pos6 = pyautogui.locateOnScreen(mapa6,confidence=0.7)
    pyautogui.click(mapa_pos6)
    pyautogui.press('f1')
      
def verificarMana():
    while True:
        mana = os.path.join('images/player/mana.png')
        # Verificar se a imagem "mana.png" está presente na tela
        mana_pos = pyautogui.locateOnScreen(mana,confidence=0.7)
        
        if mana_pos is not None:
            # Se a imagem for encontrada, pressionará a tecla '2'
            pyautogui.press('2')
            time.sleep(6)

def verificarlife():
    while True:
        life = os.path.join('images/player/life.png')
        life_pos = pyautogui.locateCenterOnScreen(life, confidence=0.7)
        if life_pos is not None:
            pyautogui.press('3')
            time.sleep(3)

lizard_images = [
    'lizardADown.png', 'lizardAleft.png', 'lizardARight.png', 'lizardAUp.png',
    'lizardMDown.png', 'lizardMLeft.png', 'lizardMRight.png', 'lizardMUp.png',
    'lizardWDown.png', 'lizardWLeft.png', 'lizardWRight.png', 'lizardWUp.png',
    'lizardCDown.png', 'lizardCLeft.png', 'lizardCRight.png', 'lizardCUp.png',
    'lizardHDown.png', 'lizardHLeft.png', 'lizardHRight.png', 'lizardHUp.png'
    
]

def lizard():
    # Coordenadas da região retangular desejada (x, y, largura, altura)
    region = (350, 200, 766, 469)

    while True:
        # Capturar a imagem da região desejada
        screenshot = pyautogui.screenshot(region=region)

        for image in lizard_images:
            # Verificar se a imagem atual está presente na captura da região
            liz = os.path.join("images/lizard/", image)
            lizard_pos = pyautogui.locateOnScreen(liz, region=region, confidence=0.6)
            
            if lizard_pos is not None:
                flecha = os.path.join('images/skills/flecha.png')
                pyautogui.locateOnScreen(flecha, confidence=0.7)
                pyautogui.press('1')
        
        time.sleep(1)

def andar():
    while True:
        AndarMapa1()
        time.sleep(3)
        
        AndarMapa2()
        time.sleep(10)
        
        AndarMapa3()
        time.sleep(12)
        AndarMapa3()
        time.sleep(1)

        AndarMapa4()
        time.sleep(10)
        
        AndarMapa5()
        time.sleep(6)
        AndarMapa5()
        time.sleep(1)
        
        AndarMapa6()
        time.sleep(6)
        
        AndarMapa5()
        time.sleep(6)
        
        AndarMapa4()
        time.sleep(6)
        
        AndarMapa3()
        time.sleep(8)
        
        AndarMapa2()
        time.sleep(6)
        AndarMapa2()
        time.sleep(1)
        
        AndarMapa1()
        time.sleep(8)

def capturar_screenshot():
    # Pasta para salvar as screenshots
    pasta_destino = "screenshots"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    contador = 1
    while True:
        # Verificar se a imagem "level.png" está presente na tela
        level = os.path.join("images/player/level.png")
        level_pos = pyautogui.locateOnScreen(level, confidence=0.8)

        if level_pos is not None:
            # Capturar a screenshot da tela
            screenshot = pyautogui.screenshot()

            # Salvar a screenshot com nome sequencial na pasta destino
            arquivo_destino = os.path.join(pasta_destino, f"screenshot{contador}.png")
            screenshot.save(arquivo_destino)

            print(f"Screenshot capturada e salva: {arquivo_destino}")

            contador += 1

        # Esperar um tempo antes de verificar novamente
        time.sleep(10)