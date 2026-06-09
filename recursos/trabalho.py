import pygame

tamanho_concha = 80.0
crescendo = True
concha_base = None


def desenhar_concha(superficie_tela, concha_base_local=None):
    global tamanho_concha, crescendo, concha_base

    if concha_base_local is not None:
        concha_base = concha_base_local

    if concha_base is None:
        concha_base = pygame.image.load("bases/concha.png").convert_alpha()

    if crescendo:
        tamanho_concha += 0.2
        if tamanho_concha >= 85.0:
            crescendo = False
    else:
        tamanho_concha -= 0.2
        if tamanho_concha <= 75.0:
            crescendo = True

    tamanho_inteiro = int(tamanho_concha)
    concha_atual = pygame.transform.scale(concha_base, (tamanho_inteiro, tamanho_inteiro))

    posicao_x = 1000 - tamanho_inteiro - 30
    posicao_y = 700 - tamanho_inteiro - 30

    superficie_tela.blit(concha_atual, (posicao_x, posicao_y))
