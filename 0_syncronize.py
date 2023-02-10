import pyautogui
from time import sleep
import time
sleep(2)


# range menor para caçar a imagem de batalha
posicaoCombate = [659, 412, 20, 10]
posicaoAbra = [34, 15, 70, 30]
posicaoPikobola = [10, 9, 30, 32]
posicao_run = [781, 708, 300, 300]
# posicao_ability = [246, 756, 100, 100]
contagemAbra = 0
contagemPokemon = 0
abra_capturado = 0
tempo_total_em_segundos = 0


def andar_inicio():
    while True:
        pyautogui.keyDown('right')
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 1
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 2
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 3
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        pyautogui.keyUp('right')
        sleep(0.2)
        pyautogui.keyDown('left')
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 4
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 5
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        sleep(0.195)
        combate = pyautogui.locateOnScreen(
            'combate.jpg', confidence=0.9, region=posicaoCombate, grayscale=True)
        pyautogui.moveTo(combate)
        if (combate != None):
            pause_movimento = 6
            pyautogui.keyUp('right')
            print("Entrei em combate")
            break
        pyautogui.keyUp('left')
        sleep(0.2)
        pikobola = pyautogui.locateOnScreen(
            'pikobola.JPG', confidence=0.9, region=posicaoPikobola)
        if (pikobola != None):
            pyautogui.moveTo(pikobola)
            print("PROTOCOLO DE SEGURANÇA ATIVADO")
            break


def e_um_abra_ou_corre():
    while True:

        global contagemPokemon
        contagemPokemon = contagemPokemon + 1
        print("Esse é o {} pokemon que encontro".format(contagemPokemon))
        sleep(5.5)
        abra = pyautogui.locateOnScreen(
            'abra.JPG', confidence=0.9, region=posicaoAbra, grayscale=True)
        pyautogui.moveTo(abra)

        if (abra != None):
            global contagemAbra
            contagemAbra = contagemAbra + 1
            print("é o {}º abra que encontro".format(contagemAbra))
            captura_efetiva()
            break
        print("Não é um abra, vou sair")
        run = pyautogui.locateOnScreen(
            'run.JPG', confidence=0.7, region=posicao_run)
        pyautogui.moveTo(run)
        sleep(0.5)
        pyautogui.click(run)
        break


def captura_efetiva():
    while True:
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

        global abra_capturado
        abra_capturado = abra_capturado + 1
        sleep(3)
        sleep(9)
        pikobola = pyautogui.locateOnScreen(
            'pikobola.JPG', confidence=0.6, region=posicaoPikobola)
        pyautogui.moveTo(pikobola)
        sleep(1)
        if (pikobola == None):
            break
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
        sleep(12)
        pikobola = pyautogui.locateOnScreen(
            'pikobola.JPG', confidence=0.6, region=posicaoPikobola)
        pyautogui.moveTo(pikobola)
        sleep(1)
        fugiu = pyautogui.locateOnScreen(
            'abrafugiu.JPG', confidence=0.7, grayscale=True)
        if (fugiu != None):
            print("O safado fugiu!")
            abra_capturado = abra_capturado - 1
            break
        if (pikobola == None):
            break


while True:
    start_time = time.time()
    andar_inicio()
    e_um_abra_ou_corre()
    print("\033[32m Abras capturados: {}\033[0m".format(abra_capturado))
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
    # tempo_passado = int(tempo_passado)
    # print(tempo_passado)
    # minutes, seconds = divmod(tempo_passado, 60)
    # tempo = datetime.timedelta(minutes=minutes, seconds=seconds)
    # tempo_em_minutos = time.strftime("%M:%S")
    print("Eu economizei \033[91m{} minutos e {} segundos\033[0m".format(
        tempo_passado_em_minutos_inteiros, int(round(tempo_passado_em_minutos_floats, 2))))
    # captura_efetiva()
# esse script executa 10 passos em 3.26 segundos, então cada passo é 0,326 segundos
# agora esse script executa 6 passos em 1.93 segundos, então cada passo é 0,321 segundos
# agora esse script executa 4 passos em 1.56 segundos, então cada passo é 0,39 segundos
