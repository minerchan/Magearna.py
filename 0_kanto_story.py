# ATENÇÃO
# Necessário um poke pra duelos e tm's e coisas para os pokezin de ginásio
# O jogo inicia 3 passos abaixo da cama com lençol rosa, é preciso startar o bot daqui
# em sua mochila é necessário ter x super repel, colocar eles no número 2
# por favor entre em suas configurações e desabilite battle e friend request
# confira se as variáveis de posicao batem com sua tela
# o mouse tem que estar clicado na tela durante todo processo
# Por favor confira se as posições go to e posicao_fainted das ferramentas estão de acordo com sua tela

# Bibliotecas externas necessárias
import pyautogui

# ferramentas de trabalho
from ferramentas import passo_direcao, fala, aperta_tecla, luta, usarRepelente, identificar, identificar_mover, identificar_mover_clicar, esperar, imprimir_vermelho, imprimir_verde, clica_no_go_to, ataque, healando

# Funções de história


def andar_ate_a_mae():
    passo_direcao(1, "up")
    passo_direcao(5, "right")
    passo_direcao(2, "up")
    passo_direcao(1, "left")
    esperar(4)
    passo_direcao(1, "left")
    esperar(6)
    fala(3)
    clica_no_go_to()
    esperar(22)


def professor_oak():
    fala(9)
    identificar_mover_clicar('./imagens/bulbassalto.jpg')
    esperar(3)
    fala(1)
    aperta_tecla('1')
    esperar(0.5)
    fala(10)
    esperar(2)
    clica_no_go_to()
    esperar(24)


def gary():
    fala(3)
    esperar(6)
    luta('./imagens/growl.JPG')
    luta('./imagens/growl.JPG')
    ataque('./imagens/tackle.JPG')
    esperar(3)
    fala(5)
    esperar(5)
    passo_direcao(13, 'down')
    passo_direcao(7, 'left')
    passo_direcao(2, 'up')
    esperar(4)
    passo_direcao(1, 'right')
    passo_direcao(4, 'up')
    fala(1)
    esperar(4)
    fala(1)
    usarRepelente()
    clica_no_go_to()
    esperar(12)


# def # maozada():
#     luta = pyautogui.locateOnScreen(
#         'fight.JPG', confidence=0.8)
#     pyautogui.moveTo(luta)
#     esperar(0.5)
#     pyautogui.click(luta)
#     esperar(0.5)
#     outrage = pyautogui.locateOnScreen(
#         'outrage.JPG', confidence=0.8)
#     pyautogui.moveTo(outrage)
#     esperar(0.5)
#     pyautogui.click(outrage)


def batalha1():
    esperar(0.5)
    fala(2)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(6)
    fala(4)  # revisar
    clica_no_go_to()
    esperar(22)


def batalha2():
    fala(1)
    esperar(10)
    ataque('./imagens/sludgebomb.JPG')
    esperar(10)
    fala(1)
    esperar(1)
    clica_no_go_to()
    esperar(20)


def emma():
    fala(5)
    esperar(3)


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
    esperar(3)
    clica_no_go_to()
    esperar(20)
    fala(2)


def batalha3():
    clica_no_go_to()
    esperar(9)
    fala(1)
    esperar(10)
    ataque('./imagens/sludgebomb.JPG')
    esperar(10)
    fala(3)
    esperar(2)


def nurse_center():
    clica_no_go_to()
    esperar(18)
    fala(8)
    esperar(4)


def carl():
    clica_no_go_to()
    esperar(25)
    fala(8)
    esperar(3)


def dizzy():
    clica_no_go_to()
    esperar(24)
    fala(1)
    esperar(3)
    aperta_tecla('1')
    fala(2)
    esperar(2)
    clica_no_go_to()
    esperar(9)
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    fala(4)
    esperar(3)
    aperta_tecla('1')
    esperar(3)
    fala(2)
    esperar(3)
    aperta_tecla('1')
    esperar(4)
    fala(1)
    aperta_tecla('3')
    esperar(4)
    fala(1)
    aperta_tecla('2')
    esperar(4)
    fala(1)
    esperar(2)
    aperta_tecla('3')
    esperar(4)
    fala(2)
    esperar(2)
    aperta_tecla('1')
    esperar(3)
    fala(9)
    esperar(2)
    clica_no_go_to()
    esperar(25)


def old_man():
    fala(4)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    fala(1)
    esperar(3)


def batalha4():
    # passo_direcao(6, 'up')
    # passo_direcao(3, 'right')
    # passo_direcao(2, 'up')
    # passo_direcao(6, 'right')
    # passo_direcao(7, 'up')
    # passo_direcao(7, 'left')
    # passo_direcao(3, 'up')
    # fala(2)
    # esperar(5)
    # ataque('./imagens/sludgebomb.JPG')
    # fala(1)
    # esperar(2)
    usarRepelente()
    passo_direcao(2, 'up')
    passo_direcao(7, 'right')
    passo_direcao(4, 'up')
    passo_direcao(4, 'left')
    passo_direcao(8, 'up')
    esperar(5)
    passo_direcao(3, 'right')
    passo_direcao(3, 'up')
    passo_direcao(1, 'left')
    passo_direcao(6, 'up')
    passo_direcao(1, 'right')
    passo_direcao(2, 'up')
    passo_direcao(3, 'left')
    passo_direcao(1, 'up')
    esperar(2)


def viridian_forest():
    # passo_direcao(7, 'up')
    # esperar(8.5)
    # fala(5)
    # esperar(3)
    # clica_no_go_to()
    # esperar(28)
    # passo_direcao(7, 'left')
    # esperar(0.5)
    # fala(4)
    # esperar(5)
    # fala(3)
    # esperar(3)
    # clica_no_go_to()
    # esperar(20)
    # fala(1)
    # esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(10)
    fala(2)
    usarRepelente()
    esperar(3)
    clica_no_go_to()
    esperar(42)
    fala(2)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(10)
    fala(1)
    clica_no_go_to()
    esperar(15)
    passo_direcao(1, 'up')
    esperar(4)
    fala(6)
    esperar(3)


def Em_busca_do_primeiro_ginasio():  # revisar
    clica_no_go_to()
    esperar(30)
    fala(4)
    esperar(3)
    passo_direcao(7, 'right')
    passo_direcao(5, 'up')
    passo_direcao(6, 'right')
    passo_direcao(3, 'up')
    esperar(5)
    passo_direcao(4, 'right')
    passo_direcao(13, 'up')
    passo_direcao(3, 'left')
    passo_direcao(5, 'up')
    esperar(1)
    fala(2)
    aperta_tecla('1')
    fala(1)
    esperar(5)
    fala(1)
    healando()
    # NAO ESCREVER AQUI
    passo_direcao(9, 'down')
    passo_direcao(4, 'right')
    passo_direcao(8, 'down')
    passo_direcao(4, 'left')
    passo_direcao(1, 'down')
    esperar(5)
    ataque('./imagens/sludgebomb.JPG')
    # estou na porta aberta do pokecenter


# def batalha5():
#     fala(1)
#     esperar(6)
#     ataque('./imagens/ember.JPG')


def pokecenter_veio():
    passo_direcao(3, 'down')
    passo_direcao(1, 'right')
    passo_direcao(32, 'down')
    passo_direcao(1, 'left')
    passo_direcao(12, 'down')
    passo_direcao(5, 'right')
    passo_direcao(3, 'up')
    esperar(5)
    passo_direcao(8, 'up')
    healando()
    esperar(2)


def testezao():
    esperar(3)
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
    # pokecenter_veio()
    # batalha4()
    # viridian_forest()

    # Em_busca_do_primeiro_ginasio()
    passo_direcao(9, 'down')
    passo_direcao(3, 'right')
    passo_direcao(8, 'down')
    passo_direcao(4, 'left')
    passo_direcao(1, 'down')
    esperar(5)

    passo_direcao(3, 'down')
    passo_direcao(5, 'left')
    passo_direcao(5, 'down')
    passo_direcao(9, 'left')
    passo_direcao(13, 'down')
    passo_direcao(2, 'left')
    passo_direcao(7, 'down')
    passo_direcao(4, 'right')
    passo_direcao(3, 'down')
    passo_direcao(4, 'right')
    # esperar(3)
    # fala(1)
    # esperar(6)
    # ataque('./imagens/sludgebomb.JPG')
    # fala(1)

    # 3 pra baixo
    # 5 pra esquerda
    # 5 pra baixo
    # 9 pra esquerda
    # 13 pra baixo
    # 2 pra esquerda
    # 7 pra baixo
    # 4 pra direita
    # 3 pra baixo
    # 3 pra direita

    # passo_direcao(2, 'down')
    # passo_direcao(6, 'right')
    # passo_direcao(34, 'up')
    # passo_direcao(25, 'left')
    # passo_direcao(3, 'down')
    # fala(1)
    # esperar(6)
    # ataque('./imagens/sludgebomb.JPG')


testezao()
# 2 baixo
# 6 direita
# 32 pra cima
