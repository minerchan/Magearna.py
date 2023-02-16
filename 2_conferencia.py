import pyautogui

# ferramentas de trabalho
from ferramentas import passo_direcao, fala, aperta_tecla, luta, usarRepelente, identificar, identificar_mover, identificar_mover_clicar, esperar, imprimir_vermelho, imprimir_verde, clica_no_go_to, ataque, healando, clica_arrasta_de_2parametro_pra_2parametro, identificar_printar, rare_candy, potion, sair_da_luta, conferindo_habilidade_que_nao_quer, o_bicho_que_quero_hab_que_nao_quero, trocar_pokemon, tampar_pokeball, anda_ate_entrar_em_combate, anda_ate_entrar_em_combate_na_agua, anda_ate_entrar_em_combate_na_agua_direita, e_shiny

# posicao_pikobola_1 = [9, 9, 10, 12]

# pikobola = pyautogui.locateOnScreen(
#     './imagens/pikobola.JPG', confidence=0.8, region=posicao_pikobola_1)
# if (pikobola != None):
#     imprimir_verde('entrou em combate')


# identificar_mover('./imagens/testegigante.JPG')

esperar(2)
pokemon_encontrado = 0


def esquerda():
    global pokemon_encontrado
    i = 0
    while i < 3:
        anda_ate_entrar_em_combate_na_agua()
        pokemon_encontrado = pokemon_encontrado + 1
        esperar(2)
        e_shiny()
        o_bicho_que_quero_hab_que_nao_quero(
            './imagens/dratini.JPG', './imagens/shedskin.JPG')
        i = i + 1

        imprimir_verde(
            "Já encontrei {} pokémons até agora".format(pokemon_encontrado))


def direita():
    global pokemon_encontrado
    i = 0
    while i < 3:
        anda_ate_entrar_em_combate_na_agua_direita()
        pokemon_encontrado = pokemon_encontrado + 1
        esperar(2)
        e_shiny()
        o_bicho_que_quero_hab_que_nao_quero(
            './imagens/dratini.JPG', './imagens/shedskin.JPG')
        i = i + 1

        imprimir_verde(
            "Já encontrei {} pokémons até agora".format(pokemon_encontrado))


while True:
    direita()
    esquerda()
