import pyautogui
from time import sleep

# Essa função calcula o número de passos de acordo com o parâmetro passos, usando o tempo de 0.283 para cada passo


def calculo(passos):
    passos = passos * 0.283
    passos = round(passos, 4)
    return passos

# Essa função utiliza a função calcula, usando como parâmetros o número de passos e direção que o personagem vai andar


def passo_direcao(passo, direcao):
    pyautogui.keyDown(direcao)
    sleep(calculo(passo))
    pyautogui.keyUp(direcao)
    sleep(0.2)

# Essa função utiliza de parâmetro o número de balões de chats que a conversa vai ter e conversa com o personagem


def fala(numero):
    numero = int(numero)
    i = 0
    while (i < numero):
        pyautogui.keyDown('space')
        sleep(0.4)
        pyautogui.keyUp('space')
        sleep(4)
        i = i + 1

# Essa função aperta a tecla passada como parâmetro


def aperta_tecla(tecla):
    pyautogui.keyDown(tecla)
    sleep(0.5)
    pyautogui.keyUp(tecla)

# Essa função recebe como parâmetro a imagem do ataque que vai usar


def luta(imagem):
    luta = pyautogui.locateOnScreen(
        './imagens/fight.JPG', confidence=0.8)
    pyautogui.moveTo(luta)
    sleep(0.5)
    pyautogui.click(luta)
    sleep(0.5)
    movimento = pyautogui.locateOnScreen(
        imagem, confidence=0.8)
    pyautogui.moveTo(movimento)
    sleep(0.5)
    pyautogui.click(movimento)
    sleep(7.5)


def identificar(imagem):
    pyautogui.locateOnScreen(
        imagem, confidence=0.8)


def identificar_printar(imagem):
    pyautogui.locateOnScreen(
        imagem, confidence=0.8)
    print(pyautogui.locateOnScreen(
        imagem, confidence=0.8))


def identificar_mover(imagem):
    pyautogui.locateOnScreen(
        imagem, confidence=0.8)
    pyautogui.moveTo(pyautogui.locateOnScreen(
        imagem, confidence=0.8))


def identificar_mover_printar(imagem, posicao):
    pyautogui.locateOnScreen(
        imagem, confidence=0.8, region=posicao, grayscale=True)
    pyautogui.moveTo(pyautogui.locateOnScreen(
        imagem, confidence=0.8, region=posicao, grayscale=True))
    print(pyautogui.locateOnScreen(
        imagem, confidence=0.8, region=posicao, grayscale=True))


def identificar_mover_clicar(imagem):
    pyautogui.locateOnScreen(
        imagem, confidence=0.8)
    pyautogui.moveTo(pyautogui.locateOnScreen(
        imagem, confidence=0.8))
    sleep(0.4)
    pyautogui.click(pyautogui.locateOnScreen(
        imagem, confidence=0.8))


def usarRepelente():
    pyautogui.keyDown('2')
    sleep(0.4)
    pyautogui.keyUp('2')
    okay = pyautogui.locateOnScreen(
        './imagens/okay.JPG', confidence=0.8, grayscale=True)
    pyautogui.moveTo(okay)
    sleep(0.5)
    pyautogui.click(okay)


def esperar(segundos):
    sleep(segundos)


def imprimir_vermelho(nome):
    print("\033[91m" + nome + "\033[0m")


def imprimir_verde(nome):
    print("\033[32m" + nome + "\033[0m")


posicao_goto = [1323, 78, 100, 100]


def clica_no_go_to():
    goto = pyautogui.locateOnScreen(
        './imagens/Goto.JPG', confidence=0.8, region=posicao_goto)
    pyautogui.moveTo(goto)
    esperar(0.5)
    pyautogui.click(goto)


posicao_pikobola_1 = [9, 9, 10, 12]

# Essa função ataca é o pokémon inimigo cair, uma por poke


def ataque(imagem):
    while True:
        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        sleep(0.2)
        if (pikobola == None):
            imprimir_verde("pokemon morreu entao vou parar")
            break
        imprimir_vermelho("pokemon não morreu vou atacar de novo")
        luta(imagem)


def healando():
    fala(2)
    aperta_tecla('1')
    esperar(2)
    fala(1)
    esperar(7)
    fala(1)
