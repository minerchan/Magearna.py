import pyautogui
from time import sleep
import time
sleep(2)

passo = -1
primeiraVolta = True
posicaoCombate = [64, 720, 80, 26]
posicaoPikobola = [10, 9, 30, 32]
posicao_run = [781, 708, 300, 300]
pokemon_capturado = 0
posicaoDratini = [31, 12, 100, 100]
dratini_encontrado = 0
tempo_total_em_segundos = 0


def andar():
    global passo
    global primeiraVolta
    while True:
        pyautogui.keyDown('2')
        sleep(0.4)
        pyautogui.keyUp('2')
        if (passo == -1):  # personagem anda pra direita um passo
            pyautogui.keyDown('right')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 0
            if (combate != None):
                pyautogui.keyUp('right')
                print("Entrei em combate no passo 1")
                primeiraVolta = False
                break
        if (passo == 0 or passo == 5):  # se ele foi pego no primeiro passo que deu, volta aqui
            if (primeiraVolta == False):
                pyautogui.keyDown('right')
                pyautogui.keyDown('2')
                sleep(0.4)
                pyautogui.keyUp('2')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 1
            if (combate != None):
                pyautogui.keyUp('right')
                print("Entrei em combate no passo 2")
                primeiraVolta = False
                break
        if (passo == 1):  # se ele foi pego no 2 passo que deu volta aqui
            if (primeiraVolta == False):
                pyautogui.keyDown('right')
                pyautogui.keyDown('2')
                sleep(0.4)
                pyautogui.keyUp('2')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 2
            if (combate != None):
                pyautogui.keyUp('right')
                print("Entrei em combate no passo 3")
                primeiraVolta = False
                break
            pyautogui.keyUp('right')

        pyautogui.keyDown('2')
        sleep(0.4)
        pyautogui.keyUp('2')

        if (passo == 2):  # se ele foi pego no 3 passo que deu volta aqui
            pyautogui.keyDown('left')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 3
            if (combate != None):
                pyautogui.keyUp('left')
                print("Entrei em combate no passo 4")
                primeiraVolta = False
                break
        if (passo == 3):  # se ele foi pego no 4 passo que deu volta aqui
            if (primeiraVolta == False):
                pyautogui.keyDown('left')
                pyautogui.keyDown('2')
                sleep(0.4)
                pyautogui.keyUp('2')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 4
            if (combate != None):
                pyautogui.keyUp('left')
                print("Entrei em combate no passo 5")
                primeiraVolta = False
                break
        if (passo == 4):  # se ele foi pego no 5 passo que deu volta aqui
            if (primeiraVolta == False):
                pyautogui.keyDown('left')
                pyautogui.keyDown('2')
                sleep(0.4)
                pyautogui.keyUp('2')
            sleep(0.195)
            combate = pyautogui.locateOnScreen(
                'combate2.jpg', confidence=0.7, region=posicaoCombate, grayscale=True)
            passo = 5
            if (combate != None):
                pyautogui.keyUp('left')
                print("Entrei em combate no passo 6")
                primeiraVolta = False
                break
        pyautogui.keyUp('left')
        sleep(0.2)
        pikobola = pyautogui.locateOnScreen(
            'pikobola.JPG', confidence=0.9, region=posicaoPikobola)
        if (pikobola != None):
            pyautogui.moveTo(pikobola)
            print("PROTOCOLO DE SEGURANÇA ATIVADO")
            primeiraVolta = False
            break
        pyautogui.keyDown('right')
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate2.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        passo = 0


def corre():
    while True:
        run = pyautogui.locateOnScreen(
            'run.JPG', confidence=0.7, region=posicao_run)
        pyautogui.moveTo(run)
        sleep(0.5)
        pyautogui.click(run)
        sleep(3)
        break


def parasect():
    while True:
        troca = pyautogui.locateOnScreen(
            'pokemontroca.JPG', confidence=0.8)
        pyautogui.moveTo(troca)
        sleep(0.5)
        pyautogui.click(troca)

        sleep(1.5)

        parasect = pyautogui.locateOnScreen(
            'parasectchoose.JPG', confidence=0.8)
        pyautogui.moveTo(parasect)
        sleep(0.5)
        pyautogui.click(parasect)
        print("Parasect, eu escolho você!")
        break


def amaciar():
    while True:
        sleep(6)
        luta = pyautogui.locateOnScreen(
            'fight.JPG', confidence=0.8)
        pyautogui.moveTo(luta)
        sleep(0.5)
        pyautogui.click(luta)
        sleep(0.5)
        spore = pyautogui.locateOnScreen(
            'spore.JPG', confidence=0.8)
        pyautogui.moveTo(spore)
        sleep(0.5)
        pyautogui.click(spore)
        sleep(6)
        luta = pyautogui.locateOnScreen(
            'fight.JPG', confidence=0.8)
        pyautogui.moveTo(luta)
        sleep(0.5)
        pyautogui.click(luta)
        sleep(0.5)
        false_swipe = pyautogui.locateOnScreen(
            'falseswipe.JPG', confidence=0.8)
        pyautogui.moveTo(false_swipe)
        sleep(0.5)
        pyautogui.click(false_swipe)
        sleep(6)
        print("O pokémon adversário está amaciado")
        break


def capturar():
    while True:
        itens = pyautogui.locateOnScreen('itens.JPG', confidence=0.8)
        pyautogui.moveTo(itens)
        sleep(0.5)
        pyautogui.click(itens)
        sleep(0.5)
        pokebal_option = pyautogui.locateOnScreen(
            'pokeballoption.JPG', confidence=0.8)
        pyautogui.moveTo(pokebal_option)
        sleep(0.5)
        pyautogui.click(pokebal_option)
        sleep(0.5)
        pokebal_use = pyautogui.locateOnScreen(
            'pokeballusar.JPG', confidence=0.8)
        pyautogui.moveTo(pokebal_use)
        sleep(0.5)
        pyautogui.click(pokebal_use)
        captura = pyautogui.locateOnScreen(
            'captura.jpg', confidence=0.8, grayscale=True)
        if (captura != None):
            global pokemon_capturado
            pokemon_capturado = pokemon_capturado + 1
            print("Capturado com sucesso!")
            break


def e_um_dratini():
    global dratini_encontrado
    while True:
        dratini = pyautogui.locateOnScreen(
            'dratini.JPG', confidence=0.8, region=posicaoDratini)
        dragonair = pyautogui.locateOnScreen('dragonair.JPG', confidence=0.8)

        if (dratini or dragonair != None):
            print("Achei um!")
            dratini_encontrado = dratini_encontrado + 1
            sleep(1)
            ability = pyautogui.locateOnScreen(
                'marvelscale.jpg', confidence=0.8)
            if (ability != None):
                parasect()
                amaciar()
                capturar()
                break
            print("porém ele tinha a habilidade errada então vou sair")
            corre()
            break

        print("não é um dratini, vou correr")
        corre()
        break


def shiny():
    while True:
        shiny = pyautogui.locateOnScreen('shiny.jpg', confidence=0.8)
        if (shiny != None):
            parasect()
            amaciar()
            capturar()
        break


while True:
    start_time = time.time()
    andar()
    sleep(6.5)  # tempo para entrar em combate tranquilo
    shiny()  # confere se tem shiny, se sim, captura
    e_um_dratini()
    print("\033[32m Dratini's capturados: {}\033[0m".format(pokemon_capturado))
    print("\033[33mDratini's e Dragonair's encontrados: {}\033[0m".format(
        dratini_encontrado))
    end_time = time.time()
    tempo_passado = end_time - start_time  # 5 segundos exemplo
    tempo_total_em_segundos = tempo_total_em_segundos + \
        int(tempo_passado)  # 0 + 5 na 1º e 5 +5 na segunda
    if (tempo_total_em_segundos >= 60):
        tempo_passado_em_minutos = tempo_total_em_segundos / 60
        tempo_passado_em_minutos_inteiros = int(tempo_passado_em_minutos)
        tempo_passado_em_minutos_floats = tempo_passado_em_minutos - \
            tempo_passado_em_minutos_inteiros
        tempo_passado_em_minutos_floats = tempo_passado_em_minutos_floats * 60
    else:
        tempo_passado_em_minutos_floats = tempo_total_em_segundos  # 5 segundos
        tempo_passado_em_minutos_inteiros = 0
        print("Eu economizei \033[91m{} minutos e {} segundos\033[0m".format(
            tempo_passado_em_minutos_inteiros, int(round(tempo_passado_em_minutos_floats, 2))))
