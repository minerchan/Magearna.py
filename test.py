import pyautogui
import time
from time import sleep

# start_time = time.time()
# sleep(0.5)
# print(time.time() - start_time)

# segundos = 80
# if (segundos >= 60):
#     tempo_passado_em_minutos = segundos / 60
#     tempo_passado_em_minutos_inteiros = int(tempo_passado_em_minutos)
#     tempo_passado_em_minutos_floats = tempo_passado_em_minutos - \
#         tempo_passado_em_minutos_inteiros
#     tempo_passado_em_minutos_floats = tempo_passado_em_minutos_floats * 60

#     # resto_da_divisao = int(segundos) % 60
#     # resto_da_divisao = resto_da_divisao * 60

#     print(tempo_passado_em_minutos_inteiros)
#     print("os segundos são {}".format(
#         int(round(tempo_passado_em_minutos_floats, 2))))

# combate = 659, 412

# while True:
#     troca = pyautogui.locateOnScreen(
#         'pokemontroca.JPG', confidence=0.8)
#     pyautogui.moveTo(troca)
#     sleep(0.5)
#     pyautogui.click(troca)

#     sleep(1.5)

#     parasect = pyautogui.locateOnScreen('parasectchoose.JPG', confidence=0.8)
#     pyautogui.moveTo(parasect)
#     sleep(0.5)
#     pyautogui.click(parasect)
#     break

# left=781, top=708

# variavel = 0

# # if (variavel == 0 or variavel == 1):
# #     print("funciona")
# # else:
# #     print("nao funciona")

# while True:
#     print("comecou")
#     if (variavel == 0 or variavel == 1):
#         print("entrou aqui")
#         if (variavel == 0):
#             break
# while True:
#     combate2 = pyautogui.locateOnScreen('combate2.jpg', confidence=0.9)
#     pyautogui.moveTo(combate2)
#     print(combate2)


def aperta_tecla(tecla):
    pyautogui.keyDown(tecla)
    sleep(0.5)
    pyautogui.keyUp(tecla)
