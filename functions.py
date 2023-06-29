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
    
def AndarMapa3():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos3 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos3)
    mapa3 = os.path.join('images/mapa/mapa3.png')
    mapa_pos3 = pyautogui.locateOnScreen(mapa3,confidence=0.7)
    pyautogui.click(mapa_pos3)
    pyautogui.press('f1')

def AndarMapa4():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos4 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos4)
    mapa4 = os.path.join('images/mapa/mapa4.png')
    mapa_pos4 = pyautogui.locateOnScreen(mapa4,confidence=0.7)
    pyautogui.click(mapa_pos4)
    pyautogui.press('f1')

def AndarMapa5():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos5 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos5)
    mapa5 = os.path.join('images/mapa/mapa5.png')
    mapa_pos5 = pyautogui.locateOnScreen(mapa5,confidence=0.7)
    pyautogui.click(mapa_pos5)
    pyautogui.press('f1')
    
def AndarMapa6():
    mapa = os.path.join('images/mapa/mapa.png')
    mapa_pos6 = pyautogui.locateOnScreen(mapa,confidence=0.7)
    pyautogui.click(mapa_pos6)
    mapa6 = os.path.join('images/mapa/mapa6.png')
    mapa_pos6 = pyautogui.locateOnScreen(mapa6,confidence=0.7)
    pyautogui.click(mapa_pos6)
    pyautogui.press('f1')
      
def verificarMana():
    mana = os.path.join('images/player/mana.png')
    # Verificar se a imagem "mana.png" está presente na tela
    mana_pos = pyautogui.locateOnScreen(mana,confidence=0.7)
    
    if mana_pos is not None:
        # Se a imagem for encontrada, pressionará a tecla '2'
        pyautogui.press('2')
    time.sleep(6)

def verificarlife():
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

    # Capturar a imagem da região desejada
    pyautogui.screenshot(region=region)
    for image in lizard_images:
        # Verificar se a imagem atual está presente na captura da região
        liz = os.path.join("images/lizard/", image)
        lizard_pos = pyautogui.locateOnScreen(liz, region=region, confidence=0.6)
        if lizard_pos is not None:
            flecha = os.path.join('images/skills/sword.png')
            pyautogui.locateOnScreen(flecha, confidence=0.6)
            pyautogui.press('1')
               
def andar():
    while True:
        lizard()
        AndarMapa1()
        lizard()
        lizard()
        
        lizard()
        AndarMapa2()
        lizard()
        lizard()
        lizard()
        lizard()
        
        lizard()
        AndarMapa3()
        lizard()
        lizard()
        lizard()

        lizard()
        AndarMapa4()
        lizard()
        lizard()
        lizard()
        
        lizard()
        AndarMapa5()
        lizard()
        lizard()
        
        lizard()
        AndarMapa6()
        lizard()
        lizard()
        
        lizard()
        AndarMapa5()
        lizard()
        lizard()

        lizard()
        AndarMapa4()
        lizard()
        lizard()

        lizard()
        AndarMapa3()
        lizard()
        lizard()
         
        lizard()
        AndarMapa2()
        lizard()
        lizard()
        lizard()
        
        lizard()
        AndarMapa1()
        lizard()
        lizard()

def reconnect():
    rec = os.path.join('images/server/reconnect.png')
    rec_position = pyautogui.locateOnScreen(rec, confidence=0.6)
    if rec_position is not None:
        pyautogui.click(rec_position)
    time.sleep(1)

def capturar_screenshot():
    # Pasta para salvar as screenshots
    pasta_destino = "screenshots"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Verificar se a imagem "level.png" está presente na tela
    level = os.path.join("images/player/level.png")
    level_pos = pyautogui.locateOnScreen(level, confidence=0.6)

    if level_pos is not None:
        # Capturar a screenshot da tela
        screenshot = pyautogui.screenshot()

        # Definir o nome do arquivo destino
        contador = 1
        arquivo_destino = os.path.join(pasta_destino, f"screenshot{contador}.png")
        
        # Verificar se o arquivo destino já existe e incrementar o contador se necessário
        while os.path.exists(arquivo_destino):
            contador += 1
            arquivo_destino = os.path.join(pasta_destino, f"screenshot{contador}.png")

        # Salvar a screenshot com o nome sequencial na pasta destino
        screenshot.save(arquivo_destino)

        print(f"Screenshot capturada e salva: {arquivo_destino}")
    time.sleep(6)