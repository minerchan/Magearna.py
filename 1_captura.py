# Bibliotecas externas necessárias
import pyautogui

# ferramentas de trabalho
from ferramentas import passo_direcao, fala, aperta_tecla, luta, usarRepelente, identificar, identificar_mover, identificar_mover_clicar, esperar, imprimir_vermelho, imprimir_verde, clica_no_go_to, ataque, healando, clica_arrasta_de_2parametro_pra_2parametro, identificar_printar, rare_candy, potion

posicao_pikobola_1 = [9, 9, 10, 12]
esperar(2)
while True:
    esperar(0.1)
    aperta_tecla('2')
    esperar(0.1)
    passo_direcao(5, 'right')
    esperar(0.1)
    aperta_tecla('2')
    esperar(0.1)
    passo_direcao(5, 'left')
    esperar(0.1)
    aperta_tecla('2')
    esperar(0.1)
    pikobola = pyautogui.locateOnScreen(
        './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
    if (pikobola != None):
        imprimir_verde('entrou em combate')
        esperar(0.5)
        dratini = pyautogui.locateOnScreen(
            './imagens/dratini.JPG', confidence=0.8)
        if (dratini != None):
            imprimir_verde('é um dratini')
            break
        imprimir_vermelho('não é um dratini')
        identificar_mover_clicar('./imagens/run.JPG')


# def parasect():
#     while True:
#         troca = pyautogui.locateOnScreen(
#             './imagens/pokemontroca.JPG', confidence=0.8)
#         pyautogui.moveTo(troca)
#         esperar(0.5)
#         pyautogui.click(troca)

#         esperar(1.5)

#         parasect = pyautogui.locateOnScreen(
#             './imagens/parasectchoose.JPG', confidence=0.8)
#         pyautogui.moveTo(parasect)
#         esperar(0.5)
#         pyautogui.click(parasect)
#         print("Parasect, eu escolho você!")
#         break
