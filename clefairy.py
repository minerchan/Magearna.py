import pyautogui
import sys

# ferramentas de trabalho
from ferramentas import passo_direcao, fala, aperta_tecla, luta, usarRepelente, identificar, identificar_mover, identificar_mover_clicar, esperar, imprimir_vermelho, imprimir_verde, clica_no_go_to, ataque, healando, clica_arrasta_de_2parametro_pra_2parametro, identificar_printar, rare_candy, potion, sair_da_luta, conferindo_habilidade_que_nao_quer, o_bicho_que_quero_hab_que_nao_quero, trocar_pokemon, tampar_pokeball, anda_ate_entrar_em_combate, anda_ate_entrar_em_combate_na_agua, anda_ate_entrar_em_combate_na_agua_direita, anda_ate_entrar_em_combate_direita, e_shiny

esperar(2)
pokemon_encontrado = 0

while True:
    anda_ate_entrar_em_combate()
    pokemon_encontrado = pokemon_encontrado + 1
    esperar(2)
    o_bicho_que_quero_hab_que_nao_quero(
        './imagens/eeve.JPG', './imagens/run_away.JPG', './imagens/adaptability.JPG')

    imprimir_verde(
        "Já encontrei {} pokémons até agora".format(pokemon_encontrado))

# variavel = True
