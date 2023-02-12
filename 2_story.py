import pyautogui
from time import sleep
import time

sleep(3)
# O jogo inicia 3 passos abaixo da cama com lençol rosa
# necessário super repel no número 2
# necessário um dragonite com outrage
# desabilitar battle e friend request
# o mouse tem que estar clicado na tela durante todo processo

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
passo8 = 2.264
passo13 = 3.679

# 1 up
# 5 right
# 3 up
# 1 left
# wait...
# 1
# FUNÇÕES FACILITADORAS


def calculo(passos):
    passos = passos * 0.283
    passos = round(passos, 4)
    return passos


def passo_direcao(passo, direcao):
    pyautogui.keyDown(direcao)
    sleep(calculo(passo))
    pyautogui.keyUp(direcao)
    sleep(0.2)


def fala(numero):
    numero = int(numero)
    i = 0
    while (i < numero):
        pyautogui.keyDown('space')
        sleep(0.4)
        pyautogui.keyUp('space')
        sleep(4)
        i = i + 1


def aperta_tecla(tecla):
    pyautogui.keyDown(tecla)
    sleep(0.5)
    pyautogui.keyUp(tecla)


def andar_ate_a_mae():
    passo_direcao(1, "up")
    passo_direcao(5, "right")
    passo_direcao(2, "up")
    passo_direcao(1, "left")
    sleep(4)
    passo_direcao(1, "left")
    sleep(6)
    fala(3)
    clica_no_go_to()
    sleep(22)


def professor_oak():
    fala(9)
    print("acabou os 9 chats")
    charmander_choose = pyautogui.locateOnScreen(
        'charmander.JPG', confidence=0.8)
    pyautogui.moveTo(charmander_choose)
    sleep(0.5)
    pyautogui.click(charmander_choose)
    sleep(3)
    fala(1)
    aperta_tecla('1')

    sleep(0.5)
    fala(10)
    sleep(2)
    clica_no_go_to()
    sleep(24)


def gary():
    fala(3)
    sleep(10)
    maozada()
    sleep(0.5)
    sleep(10)
    fala(5)
    sleep(5)
    usarRepelente()
    clica_no_go_to()
    sleep(12)


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
    fala(2)
    sleep(6)
    maozada()
    sleep(6)
    fala(5)
    clica_no_go_to()
    sleep(22)


def batalha2():
    fala(1)
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    fala(1)
    sleep(2)
    clica_no_go_to()
    sleep(20)


def emma():
    fala(5)
    sleep(3)


def pegar_pokebola_emma():
    usarRepelente()
    passo_direcao(7, 'right')
    passo_direcao(1, 'down')
    passo_direcao(6, 'right')
    passo_direcao(7, 'down')
    passo_direcao(2, 'left')
    passo_direcao(7, 'down')
    passo_direcao(1, 'right')
    passo_direcao(6, 'down')
    passo_direcao(1, 'right')
    fala(3)
    sleep(3)
    clica_no_go_to()
    sleep(20)
    fala(2)


def batalha3():
    clica_no_go_to()
    sleep(9)
    fala(1)
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    fala(3)
    sleep(2)


def nurse_center():
    clica_no_go_to()
    sleep(18)
    fala(8)
    sleep(4)


def carl():
    clica_no_go_to()
    sleep(25)
    fala(8)
    sleep(3)


def dizzy():
    clica_no_go_to()
    sleep(24)
    fala(1)
    sleep(3)
    aperta_tecla('1')
    fala(1)
    sleep(2)
    clica_no_go_to()
    sleep(9)
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    fala(4)
    sleep(3)
    aperta_tecla('1')
    sleep(3)
    fala(2)
    sleep(3)
    aperta_tecla('1')
    sleep(4)
    fala(1)
    aperta_tecla('3')
    sleep(4)
    fala(1)
    aperta_tecla('2')
    sleep(4)
    fala(1)
    sleep(2)
    aperta_tecla('3')
    sleep(4)
    fala(2)
    sleep(2)
    aperta_tecla('1')
    sleep(3)
    fala(9)
    sleep(2)
    clica_no_go_to()
    sleep(25)


def old_man():
    fala(4)
    sleep(6)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    fala(1)
    sleep(3)
    passo_direcao(6, 'up')
    passo_direcao(3, 'right')
    passo_direcao(2, 'up')
    passo_direcao(6, 'right')
    passo_direcao(7, 'up')
    passo_direcao(7, 'left')
    passo_direcao(3, 'up')


def batalha4():
    fala(2)
    sleep(10)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    fala(1)
    sleep(2)
    usarRepelente()
    passo_direcao(2, 'up')
    passo_direcao(7, 'right')
    passo_direcao(4, 'up')
    passo_direcao(4, 'left')
    passo_direcao(8, 'up')
    sleep(5)
    passo_direcao(3, 'right')
    passo_direcao(3, 'up')
    passo_direcao(1, 'left')
    passo_direcao(6, 'up')
    passo_direcao(1, 'right')
    passo_direcao(2, 'up')
    passo_direcao(3, 'left')
    passo_direcao(1, 'up')
    sleep(2)


def viridian_forest():
    pyautogui.keyDown('up')
    sleep(passo7)
    pyautogui.keyUp('up')
    sleep(0.5)
    sleep(8)
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(3)
    clica_no_go_to()
    sleep(28)
    pyautogui.keyDown('left')
    sleep(passo7)
    pyautogui.keyUp('left')
    sleep(0.5)
    chat()
    chat()
    chat()
    chat()
    sleep(5)
    chat()
    chat()
    chat()
    sleep(3)
    clica_no_go_to()
    sleep(20)
    chat()
    sleep(6)
    maozada()
    sleep(10)
    maozada()
    sleep(10)
    chat()
    chat()
    chat()
    usarRepelente()
    sleep(3)
    clica_no_go_to()
    sleep(42)
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
    clica_no_go_to()
    sleep(15)
    pyautogui.keyDown('up')
    sleep(passo1)
    pyautogui.keyUp('up')
    sleep(4)
    chat()
    chat()
    chat()
    chat()
    chat()
    chat()
    sleep(3)


def Em_busca_do_primeiro_ginasio():
    clica_no_go_to()
    sleep(30)
    chat()
    chat()
    chat()
    chat()
    sleep(3)
    pyautogui.keyDown('right')
    sleep(passo7)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('up')
    sleep(passo5)
    pyautogui.keyUp('up')
    sleep(0.5)
    pyautogui.keyDown('right')
    sleep(passo6)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('up')
    sleep(passo3)
    pyautogui.keyUp('up')  # aqui entrou
    sleep(5)
    pyautogui.keyDown('right')
    sleep(passo4)
    pyautogui.keyUp('right')
    sleep(0.5)
    pyautogui.keyDown('up')
    sleep(passo13)
    pyautogui.keyUp('up')
    sleep(0.5)
    pyautogui.keyDown('left')
    sleep(passo4)
    pyautogui.keyUp('left')
    sleep(0.5)
    pyautogui.keyDown('up')
    sleep(passo5)
    pyautogui.keyUp('up')
    sleep(0.5)


def usarRepelente():
    pyautogui.keyDown('2')
    sleep(0.4)
    pyautogui.keyUp('2')
    okay = pyautogui.locateOnScreen('okay.JPG', confidence=0.8, grayscale=True)
    pyautogui.moveTo(okay)
    sleep(0.5)
    pyautogui.click(okay)
    # NAO ESCREVER AQUI


# def testezao():

    # andar_ate_a_mae()
    # professor_oak()
    # gary()
    # batalha1()
    # batalha2()
    # emma()
    # pegar_pokebola_emma()
    # batalha3()
    # nurse_center()
    # carl()
    # dizzy()
    # old_man()
    # batalha4()
    # viridian_forest()
    # Em_busca_do_primeiro_ginasio():
# testezao()

# 6 passos pra cima
# 4 direita
# 2 pra cima
# 6 direita
# 7 pra cima
# 7 esquerda
# 3 pra cima
