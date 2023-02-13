# ATENÇÃO
# revisar o código, sempre que tiver uma imagem no meio da tela ou depender do meio da tela, checar se tem party e se sim clicar em cancel
# choice band,sludge bomb, energy ball, 8x rare candy, 50 pokebola, 6 potion
# clica no chat e coloca pm disabled
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
from ferramentas import passo_direcao, fala, aperta_tecla, luta, usarRepelente, identificar, identificar_mover, identificar_mover_clicar, esperar, imprimir_vermelho, imprimir_verde, clica_no_go_to, ataque, healando, clica_arrasta_de_2parametro_pra_2parametro, identificar_printar, rare_candy, potion

# Funções de história
esperar(3)


def andar_ate_a_mae():
    passo_direcao(1, "up")
    passo_direcao(5, "right")
    passo_direcao(3, "up")
    passo_direcao(1, "left")
    esperar(5)
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
    identificar_mover_clicar('./imagens/mochila.JPG')
    esperar(3)
    identificar_mover_clicar('./imagens/tmhm.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/tmsludge.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/bulba.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/energ.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/bulba.JPG')
    esperar(2)

    identificar_mover_clicar('./imagens/held.JPG')
    esperar(2)
    clica_arrasta_de_2parametro_pra_2parametro(536, 258, 1247, 480)
    identificar_mover_clicar("./imagens/okay2.JPG")
    esperar(3)
    identificar_mover_clicar("./imagens/x.JPG")
    esperar(2)
    clica_no_go_to()
    esperar(24)


def gary():
    fala(3)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(3)
    fala(5)
    esperar(5)
    usarRepelente()
    clica_no_go_to()
    esperar(13)


def batalha1():
    fala(2)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(6)
    identificar_mover_clicar('./imagens/donot.JPG')
    identificar_mover_clicar('./imagens/okay2.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/donot.JPG')
    identificar_mover_clicar('./imagens/okay2.JPG')
    fala(4)
    clica_no_go_to()
    esperar(24)


def batalha2():
    fala(1)
    esperar(8)
    ataque('./imagens/sludgebomb.JPG')
    esperar(8)
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
    esperar(3)
    clica_no_go_to()
    esperar(9)
    fala(1)
    esperar(7)
    ataque('./imagens/energyball.JPG')
    esperar(7)
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
    identificar_mover_clicar('./imagens/yes.JPG')
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
    esperar(25)  # ate aqui ta certo


def old_man():
    fala(4)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    identificar_mover_clicar('./imagens/donot.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/okay2.JPG')
    esperar(3)
    fala(1)
    esperar(3)


def to_passando_mal():
    passo_direcao(3, 'down')
    passo_direcao(1, 'right')
    passo_direcao(30, 'down')
    passo_direcao(1, 'left')
    passo_direcao(13, 'down')
    passo_direcao(5, 'right')
    passo_direcao(3, 'up')
    esperar(5)
    passo_direcao(8, 'up')
    fala(2)
    esperar(5)
    aperta_tecla('1')
    fala(1)
    esperar(5)
    fala(10)
    esperar(3)
    passo_direcao(9, 'down')
    esperar(5)
    passo_direcao(1, 'down')
    passo_direcao(5, 'left')
    passo_direcao(13, 'up')
    passo_direcao(1, 'right')
    passo_direcao(30, 'up')
    passo_direcao(1, 'left')
    passo_direcao(3, 'up')


def batalha4():
    usarRepelente()
    passo_direcao(6, 'up')
    passo_direcao(3, 'right')
    passo_direcao(2, 'up')
    passo_direcao(7, 'right')
    passo_direcao(7, 'up')
    passo_direcao(7, 'left')
    passo_direcao(3, 'up')
    esperar(5)
    fala(2)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(6)
    fala(1)
    passo_direcao(2, 'up')
    passo_direcao(8, 'right')
    passo_direcao(4, 'up')
    passo_direcao(5, 'left')
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
    esperar(5)


def viridian_forest():
    passo_direcao(7, 'up')
    esperar(8.5)
    fala(5)
    esperar(3)
    clica_no_go_to()
    esperar(28)
    passo_direcao(7, 'left')
    esperar(0.5)
    fala(4)
    esperar(5)
    fala(3)
    esperar(3)
    clica_no_go_to()
    esperar(10)
    usarRepelente()
    clica_no_go_to()
    esperar(15)
    fala(1)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(10)
    fala(2)
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

    # na frente do guarda da encruzilhada


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
    passo_direcao(4, 'left')
    passo_direcao(4, 'up')
    esperar(1)
    fala(2)
    esperar(4)
    aperta_tecla('1')
    esperar(3)
    fala(1)
    esperar(7)
    fala(1)
    passo_direcao(9, 'down')
    passo_direcao(4, 'right')
    passo_direcao(8, 'down')
    passo_direcao(4, 'left')
    passo_direcao(1, 'down')
    esperar(5)  # estou na porta aberta do pokecenter
    passo_direcao(2, 'down')
    passo_direcao(6, 'right')
    passo_direcao(34, 'up')
    passo_direcao(26, 'left')
    rare_candy('./imagens/bulba.JPG')
    rare_candy('./imagens/bulba.JPG')
    identificar_mover_clicar('./imagens/donot.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/okay2.JPG')
    esperar(3)
    identificar_mover_clicar('./imagens/donot.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/okay2.JPG')
    rare_candy('./imagens/bulba.JPG')
    rare_candy('./imagens/bulba.JPG')
    identificar_mover_clicar('./imagens/donot.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/okay2.JPG')
    rare_candy('./imagens/bulba.JPG')
    identificar_mover_clicar('./imagens/yes2.JPG')
    esperar(2)
    passo_direcao(3, 'down')


def batalha5():
    esperar(4)
    fala(1)
    esperar(6)
    ataque('./imagens/sludgebomb.JPG')
    esperar(7)
    fala(1)
    potion('./imagens/ivysaur.JPG')
    potion('./imagens/ivysaur.JPG')
    passo_direcao(16, 'down')
    passo_direcao(7, 'right')
    passo_direcao(1, 'up')
    passo_direcao(13, 'right')
    passo_direcao(7, 'up')
    passo_direcao(2, 'right')
    passo_direcao(3, 'up')
    passo_direcao(8, 'left')
    passo_direcao(2, 'up')
    esperar(8)


def ginasio_brock():
    passo_direcao(8, 'up')
    esperar(5)
    fala(2)
    esperar(7)
    ataque('./imagens/sludgebomb.JPG')
    esperar(6)
    fala(1)
    esperar(12)  # medir quanto tempo o cara anda ali ciclo completo
    fala(1)
    esperar(6)
    ataque('./imagens/energyball.JPG')
    esperar(2)
    fala(1)
    esperar(2)
    passo_direcao(1, 'right')
    passo_direcao(5, 'up')
    passo_direcao(1, 'left')
    passo_direcao(1, 'up')
    esperar(3)
    fala(2)
    ataque('./imagens/energyball.JPG')
    esperar(4)
    fala(1)
    potion('./imagens/ivysaur.JPG')
    esperar(2)
    passo_direcao(8, 'up')
    fala(8)
    esperar(7)
    ataque('./imagens/energyball.JPG')
    esperar(6)
    fala(4)
    esperar(5)
    fala(2)
    esperar(3)


def continuar():
    esperar(5)


def testezao():

    # gary()
    # usarRepelente()
    # clica_no_go_to()
    # esperar(13)
    # batalha1()
    # batalha2()
    # emma()
    # pegar_pokebola_emma()
    # batalha3()
    # nurse_center()
    # carl()
    # dizzy()
    # old_man()
    # to_passando_mal()
    # batalha4()
    # viridian_forest()
    # Em_busca_do_primeiro_ginasio()
    # batalha5()
    # ginasio_brock()
    continuar()


testezao()
