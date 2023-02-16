import pyautogui
from time import sleep
from playsound import playsound
import sys
# Essa função calcula o número de passos de acordo com o parâmetro passos, usando o tempo de 0.283 para cada passo

posicao_combate_novo = [629, 410, 59, 11]


def calculo(passos):
    passos = passos * 0.283
    # passos = round(passos, 6)
    return passos

# Essa função utiliza a função calcula, usando como parâmetros o número de passos e direção que o personagem vai andar


def passo_direcao(passo, direcao):
    pyautogui.keyDown(direcao)
    sleep(calculo(passo))
    pyautogui.keyUp(direcao)
    sleep(0.7)


def passo_direcao_rapido_andando(passo, direcao):
    pyautogui.keyDown(direcao)
    esperar(0.2 * passo)
    pyautogui.keyUp(direcao)
    sleep(0.5)


def passo_direcao_rapido_correndo(passo, direcao):
    pyautogui.keyDown(direcao)
    esperar(0.2 * passo)
    pyautogui.keyUp(direcao)
    sleep(0.1)

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
    sleep(9)


def luta2(imagem):
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
    sleep(5)


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


def imprimir_azul(nome):
    print("\033[34m" + nome + "\033[0m")


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


def ataque2(imagem):
    while True:
        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        sleep(0.2)
        if (pikobola == None):
            imprimir_verde("pokemon morreu entao vou parar")
            break
        imprimir_vermelho("pokemon não morreu vou atacar de novo")
        luta2(imagem)


def healando():
    esperar(1)
    fala(2)
    esperar(4)
    aperta_tecla('1')
    esperar(3)
    fala(1)
    esperar(7)
    fala(1)


def clica_arrasta_de_2parametro_pra_2parametro(a, b, c, d):
    # aqui é a duração que o mouse leva pra ir até a pasta
    pyautogui.moveTo(a, b, duration=0.25)
    # aqui é a duração que o mouse carrega a pasta do ponto a,b ao c,d
    pyautogui.dragTo(c, d, duration=0.5)


def fechar_mochila():
    identificar_mover_clicar("./imagens/x.JPG")


def rare_candy(imagem):
    identificar_mover_clicar('./imagens/mochila.JPG')
    esperar(3)
    identificar_mover_clicar('./imagens/medicine.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/rarecandy.JPG')
    esperar(2)
    identificar_mover_clicar(imagem)
    esperar(2)
    fechar_mochila()
    esperar(2)


def potion(imagem):
    identificar_mover_clicar('./imagens/mochila.JPG')
    esperar(3)
    identificar_mover_clicar('./imagens/medicine.JPG')
    esperar(2)
    identificar_mover_clicar('./imagens/potion.JPG')
    esperar(2)
    identificar_mover_clicar(imagem)
    esperar(2)
    fechar_mochila()
    esperar(2)


posicao_do_chat = [12, 722, 600, 13]


def sair_da_luta():
    identificar_mover_clicar('./imagens/run.JPG')


# def estou_em_combate():
#     pikobola = pyautogui.locateOnScreen(
#         './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
#     pyautogui.moveTo(pikobola)
#     esperar(0.2)
#     if (pikobola != None):
#         imprimir_verde('estou em combate')
#         return True


# './imagens/parasectchoose.JPG'


def trocar_pokemon(imagem):
    identificar_mover_clicar('./imagens/pokemontroca.JPG')
    esperar(0.5)
    identificar_mover_clicar(imagem)
    esperar(7)


def tampar_pokeball():
    identificar_mover_clicar('./imagens/itens.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/pokeballoption.JPG')
    esperar(1)
    identificar_mover_clicar('./imagens/pokeballusar.JPG')
    esperar(9)


def anda_ate_entrar_em_combate():
    while True:
        passo_direcao_rapido_correndo(2, 'up')
        passo_direcao_rapido_correndo(2, 'down')
        esperar(0.2)
        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        if (pikobola != None):
            imprimir_verde("estou em combate")
            break


def anda_ate_entrar_em_combate_direita():
    while True:
        # passo_direcao_rapido(1, 'right')
        # passo_direcao_rapido(1, 'left')
        esperar(0.2)
        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        if (pikobola != None):
            imprimir_verde("estou em combate")
            break


def anda_ate_entrar_em_combate_na_agua():
    while True:
        passo_direcao(5, 'left')
        aperta_tecla('2')
        esperar(0.4)
        passo_direcao(3, 'right')
        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        if (pikobola != None):
            imprimir_verde("estou em combate")
            break


def o_bicho_que_quero_hab_que_nao_quero(imagem, hab, hab2):
    while True:
        variavel = pyautogui.locateOnScreen(imagem, confidence=0.8)
        if (variavel != None):
            imprimir_verde("é o bicho que quero!")
            esperar(2)
            conferindo_habilidade_que_nao_quer(hab, hab2)
            break
        imprimir_vermelho("não é o bicho que quero")
        esperar(2)
        sair_da_luta()
        break


def conferindo_habilidade_que_nao_quer(hab, hab2):
    while True:
        variavel = pyautogui.locateOnScreen(
            hab, confidence=0.8, region=posicao_do_chat, grayscale=True)
        variavel2 = pyautogui.locateOnScreen(
            hab2, confidence=0.8, region=posicao_do_chat, grayscale=True)
        if (variavel != None or variavel2 != None):
            imprimir_vermelho("não é a habilidade que quero, vou embora")
            sair_da_luta()
            break
        imprimir_azul("é a habilidade que quero")
        # playsound('pikomon.mp3')
        sys.exit()


def anda_ate_entrar_em_combate_na_agua_direita():
    while True:
        passo_direcao(5, 'right')
        aperta_tecla('2')
        esperar(0.4)
        passo_direcao(3, 'left')

        pikobola = pyautogui.locateOnScreen(
            './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
        pyautogui.moveTo(pikobola)
        if (pikobola != None):
            imprimir_verde("estou em combate")
            break


def e_shiny():
    while True:
        variavel = pyautogui.locateOnScreen(
            './imagens/shiny.jpg', confidence=0.8)
        if (variavel != None):
            imprimir_azul("Achei um shiny")
            sys.exit()
        imprimir_vermelho("não achei um shiny")
        break


def checar_combate_novo():
    variavel = pyautogui.locateOnScreen(
        './imagens/combate_novo.JPG', confidence=0.8, grayscale=True)
    pyautogui.moveTo(variavel)
    return variavel
