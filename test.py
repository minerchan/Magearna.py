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

while True:
    run = pyautogui.locateOnScreen(
        'run.JPG', confidence=0.7)
    print(run)

# left=781, top=708
