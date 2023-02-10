import pyautogui
from time import sleep
import time

sleep(3)
# necessário super repel no número 2
# necessário um dragonite com outrage

# o passo é 0,283
# Variáveis
posicao_goto = [1323, 78, 100, 100]
passo1 = 0.283
passo2 = 0.566
passo3 = 0.849
passo4 = 1.132
passo5 = 1.415
passo6 = 1.698
passo7 = 1.981
# começa a 3 passos pra baixo da cama com coberta rosa


def andar_ate_a_mae():
    pyautogui.keyDown('up')  # 2 passos pra cima
    sleep(0.195)
    sleep(0.195)
    pyautogui.keyUp('up')

    sleep(0.2)  # resfriamento

    pyautogui.keyDown('right')  # 5 passos para a direita
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    sleep(0.195)
    pyautogui.keyUp('right')

    sleep(0.2)  # resfriamento

    pyautogui.keyDown('up')  # 2 passos pra cima
    sleep(0.195)
    sleep(0.195)
    pyautogui.keyUp('up')

    sleep(0.2)  # resfriamento

    pyautogui.keyDown('left')
    sleep(0.195)
    pyautogui.keyUp('left')

    sleep(3)
    pyautogui.keyDown('left')
    sleep(0.195)
    pyautogui.keyUp('left')
    sleep(7)
    chat()
    chat()
    chat()
    sleep(3)
    clica_no_go_to()
    sleep(20)


def professor_oak():
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    charmander_choose = pyautogui.locateOnScreen(
        'charmander.JPG', confidence=0.8)
    pyautogui.moveTo(charmander_choose)
    sleep(0.5)
    pyautogui.click(charmander_choose)
    sleep(0.5)
    chat()
    sleep(2)
    pyautogui.keyDown("1")
    sleep(0.195)
    pyautogui.keyUp("1")
    sleep(0.5)
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    clica_no_go_to()
    sleep(22)


def gary():
    chat()
    chat()
    chat()
    sleep(6)
    maozada()
    sleep(0.5)
    sleep(6)
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(5)
    usarRepelente()
    clica_no_go_to()
    sleep(11)


def maozada():
    luta = pyautogui.locateOnScreen(
        'fight.JPG', confidence=0.8)
    pyautogui.moveTo(luta)
    sleep(0.5)
    pyautogui.click(luta)
    sleep(0.5)
    outrage = pyautogui.locateOnScreen(
        'outrage.JPG', confidence=0.8)
    pyautogui.moveTo(outrage)
    sleep(0.5)
    pyautogui.click(outrage)

# Esta função é para pular um balão de chat de conversa


def chat():
    pyautogui.keyDown('space')
    sleep(0.4)
    pyautogui.keyUp('space')
    sleep(3)


def clica_no_go_to():
    goto = pyautogui.locateOnScreen(
        'Goto.JPG', confidence=0.8, region=posicao_goto)
    pyautogui.moveTo(goto)
    sleep(0.5)
    pyautogui.click(goto)


def batalha1():
    sleep(0.5)
    chat()
    chat()
    sleep(6)
    maozada()
    sleep(6)
    chat()
    chat()
    chat()
    chat()
    chat()
    clica_no_go_to()
    sleep(22)


def batalha2():
    chat()
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    chat()
    sleep(2)
    clica_no_go_to()
    sleep(20)


def emma():
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(3)


def pegar_pokebola_emma():
    usarRepelente()
    pyautogui.keyDown('right')
    sleep(passo7)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('down')
    sleep(passo1)
    pyautogui.keyUp('down')
    sleep(0.5)
    pyautogui.keyDown('right')
    sleep(passo6)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('down')
    sleep(passo7)
    pyautogui.keyUp('down')
    sleep(0.5)
    pyautogui.keyDown('left')
    sleep(passo2)
    pyautogui.keyUp('left')
    sleep(0.5)
    pyautogui.keyDown('down')
    sleep(passo7)
    pyautogui.keyUp('down')
    sleep(0.5)
    pyautogui.keyDown('right')
    sleep(passo1)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('down')
    sleep(passo6)
    pyautogui.keyUp('down')
    sleep(0.5)
    pyautogui.keyDown('right')
    sleep(passo1)
    pyautogui.keyUp('right')
    sleep(0.5)
    chat()
    chat()
    chat()
    sleep(3)
    clica_no_go_to()
    sleep(20)
    chat()
    chat()


def batalha3():
    clica_no_go_to()
    sleep(6)
    sleep(3)
    chat()
    sleep(6)
    maozada()
    sleep(10)
    maozada()
    sleep(6)
    chat()
    chat()
    chat()
    sleep(2)


def nurse_center():
    clica_no_go_to()
    sleep(18)
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(4)
# def teste():
#     usarRepelente()
#     clica_no_go_to()


def carl():
    clica_no_go_to()
    sleep(25)
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(3)


def dizzy():
    clica_no_go_to()
    sleep(22)
    chat()
    sleep(5)
    pyautogui.keyDown("2")
    sleep(0.195)
    pyautogui.keyUp("2")
    chat()
    sleep(1)
    clica_no_go_to()
    sleep(9)
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    chat()
    chat()
    chat()
    chat()
    sleep(3)
    pyautogui.keyDown("1")
    sleep(0.195)
    pyautogui.keyUp("1")
    sleep(3)
    chat()
    chat()
    sleep(3)
    pyautogui.keyDown("1")
    sleep(0.195)
    pyautogui.keyUp("1")
    sleep(4)
    chat()
    pyautogui.keyDown("3")
    sleep(0.195)
    pyautogui.keyUp("3")
    sleep(4)
    chat()
    pyautogui.keyDown("2")
    sleep(0.195)
    pyautogui.keyUp("2")
    sleep(4)
    chat()
    sleep(2)
    pyautogui.keyDown("3")
    sleep(0.195)
    pyautogui.keyUp("3")
    sleep(4)
    chat()
    chat()
    sleep(2)
    pyautogui.keyDown("1")
    sleep(0.195)
    pyautogui.keyUp("1")
    sleep(3)
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(2)
    clica_no_go_to()
    sleep(25)


def old_man():
    chat()
    chat()
    chat()
    chat()
    sleep(6)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    chat()
    sleep(3)
    pyautogui.keyDown('left')
    sleep(passo3)
    pyautogui.keyUp('left')
    sleep(0.5)
    pyautogui.keyDown('down')
    sleep(9.622)
    pyautogui.keyUp('down')
    sleep(0.5)
    pyautogui.keyDown('right')
    sleep(passo1)
    pyautogui.keyUp('right')
    sleep(0.5)
    clica_no_go_to()


# 3 pra esquerda
# 34 passo pra baixo 9,622
# 1 direita
# go to

    # clica_no_go_to()
    # sleep(44)
    # usarRepelente()
    # clica_no_go_to()


def usarRepelente():
    pyautogui.keyDown('2')
    sleep(0.4)
    pyautogui.keyUp('2')
    okay = pyautogui.locateOnScreen('okay.JPG', confidence=0.8, grayscale=True)
    pyautogui.moveTo(okay)
    sleep(0.5)
    pyautogui.click(okay)
    # NAO ESCREVER AQUI


# andar_ate_a_mae()
# professor_oak()
# gary()
# batalha1()
# batalha2()
# clica_no_go_to()
# sleep(20)
# emma()
# pegar_pokebola_emma()
# batalha3()
# nurse_center()
# carl()
# old_man()
