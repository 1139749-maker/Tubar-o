import pygame
import random
from datetime import datetime
import pyttsx3
import recursos.trabalho
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador
from recursos.trabalho import desenhar_concha

##Luana esteve aqui!!
limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.init()

def dar_boas_vindas(nome_jogador):
    engine = pyttsx3.init()
    engine.say(f"Bem-vindo, {nome_jogador}. Nade se puder!")
    engine.runAndWait()

while True:
    nome = input("Informe Nome Competidor:")
    if len(nome) > 0: 
        dar_boas_vindas(nome)
        break
    else:
        print("Nome Inválido!")

tamanho = (1000,700)
pygame.display.set_caption("Nade Se Puder - Luiza")
icone  = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)

fundo = pygame.image.load("bases/background.jpg")
fundoDead = pygame.image.load("bases/backgroundDead.jpg")
fundoStart = pygame.image.load("bases/backgroundStart.jpg")
persona = pygame.image.load("bases/nadador.png")
persona = pygame.transform.scale(persona, (120,120))
tubarao = pygame.image.load("bases/tubarao.png")
tubarao = pygame.transform.scale(tubarao, (300,150))
peixe = pygame.image.load("bases/peixe.png")
peixe = pygame.transform.scale(peixe, (100, 50))
explosaoSound = pygame.mixer.Sound("bases/deadSound.mp3")
pygame.mixer.music.load("bases/backSound.mp3")
fonteMenu = pygame.font.SysFont("comicsans",18)
fonteTitulo = pygame.font.SysFont("comicsans",30)
fonteDescricao = pygame.font.SysFont("comicsans",22)

concha_base = pygame.image.load("bases/concha.png").convert_alpha()
tamanho_concha = 80.0 
crescendo = True

def salvar_log(nome_jogador, pontos_jogador):
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    hora_formatada = agora.strftime("%H:%M:%S")
    
    with open("log.dat", "a", encoding="utf-8") as arquivo_log:
        arquivo_log.write(f"Nome: {nome_jogador} | Pontuação: {pontos_jogador} | Data: {data_formatada} | Hora: {hora_formatada}\n")

def desenhar_concha(superficie_tela, concha_base_local=None):
    global tamanho_concha, crescendo

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

recursos.trabalho.desenhar_concha = desenhar_concha

def jogar():
    fundoMov1 = 0
    fundoMov2 = 1000
    posicaoXPersona = 100
    posicaoYPersona = 300
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    velocidadeMovPersona = 5

    posicaoXTubarao = 1000
    posicaoYTubarao = random.randint(0, 570)
    velocidadeTubarao = 7
    pontos = 0
    pygame.mixer.music.play(-1)
    dificuldade = 10
    posicaoXPeixe = random.randint(1000, 1200) 
    posicaoYPeixe = random.randint(50, 550)

    pausado = False 

    while True:
        # 1. Os eventos agora SÓ cuidam de fechar o jogo ou pausar
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = not pausado 
        
        if not pausado:
    
            teclas = pygame.key.get_pressed()
            movimentoYPersona = 0 # Zera o movimento se nada estiver pressionado
            
            if teclas[pygame.K_UP]:
                movimentoYPersona = -velocidadeMovPersona
            if teclas[pygame.K_DOWN]:
                movimentoYPersona = velocidadeMovPersona
                
            posicaoXPersona = posicaoXPersona + movimentoXPersona          
            posicaoYPersona = posicaoYPersona + movimentoYPersona            
            
            if posicaoXPersona < 0 :
                posicaoXPersona = 0
            elif posicaoXPersona > 800:
                posicaoXPersona = 800
            if posicaoYPersona < 0 :
                posicaoYPersona = 0
            elif posicaoYPersona > 570:
                posicaoYPersona = 570
                
            posicaoXTubarao = posicaoXTubarao - velocidadeTubarao
            if posicaoXTubarao < -300:
                posicaoXTubarao = 1000
                pontos = pontos + 1
                velocidadeTubarao = velocidadeTubarao + 1
                posicaoYTubarao = random.randint(0,570)

            posicaoXPeixe -= random.randint(2, 7)   
            posicaoYPeixe += random.randint(-1, 1) 
            
            if posicaoYPeixe < 0:
                posicaoYPeixe = 0
            elif posicaoYPeixe > 650:
                posicaoYPeixe = 650
                
            if posicaoXPeixe < -100:
                posicaoXPeixe = random.randint(1000, 1500)
                posicaoYPeixe = random.randint(50, 550)

            fundoMov1 -= 1
            fundoMov2 -= 1
            if fundoMov1 <= -1000:
                fundoMov1 = 1000
            elif fundoMov2 <= -1000:
                fundoMov2 = 1000

        tela.fill(branco)
        tela.blit(fundo, (fundoMov1,0) )
        tela.blit(fundo, (fundoMov2,0) )
        tela.blit(peixe, (posicaoXPeixe, posicaoYPeixe))
        tela.blit(persona, (posicaoXPersona,posicaoYPersona))
        tela.blit(tubarao, (posicaoXTubarao, posicaoYTubarao) )
        
        texto = fonteMenu.render("Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (800,15))

        texto_dica = fonteMenu.render("Press Space to Pause Game ", True, branco)
        tela.blit(texto_dica, (530, 15))

        if not pausado:
            rect_persona = pygame.Rect(posicaoXPersona, posicaoYPersona, 120, 120).inflate(-20, -20)
            rect_tubarao = pygame.Rect(posicaoXTubarao, posicaoYTubarao, 300, 150).inflate(-30, -30)

            if rect_persona.colliderect(rect_tubarao):
                data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
                escreverDados(nome, pontos, data_hora_atual) 
                dead()
        
        if pausado:
            texto_pause = fonteTitulo.render("PAUSE", True, (255, 255, 255))
            texto_pause_rect = texto_pause.get_rect(center=(500, 350)) 
            tela.blit(texto_pause, texto_pause_rect)
        
        desenhar_concha(tela, concha_base)

        pygame.display.update()
        relogio.tick(60)


def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    rec_nome, rec_pontos, rec_data = maior_pontuador()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
    
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        
        textoFim = fonteTitulo.render("GAME OVER", True, (255, 0, 0))
        textoFimRect = textoFim.get_rect(center=(500, 100))
        tela.blit(textoFim, textoFimRect)
        
        if rec_nome is not None:
            textoRecorde = fonteMenu.render(f"Recorde Atual: {rec_nome} - {rec_pontos} pts ({rec_data})", True, branco)
        else:
            textoRecorde = fonteMenu.render("Nenhum recorde registrado ainda.", True, branco)
        textoRecordeRect = textoRecorde.get_rect(center=(500, 150))
        tela.blit(textoRecorde, textoRecordeRect)

        pygame.display.update()
        relogio.tick(60)

def start():
    larguraButtonStart = 150
    alturaButtonStart  = 40
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
            
        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        
        saudacao = fonteTitulo.render(f"Bem-vindo, {nome}!", True, branco)
        saudacaoRect = saudacao.get_rect(center=(500, 120))
        tela.blit(saudacao, saudacaoRect)
        
        descricao1 = fonteDescricao.render("     Use as teclas up e down para desviar do tubarão.", True, branco)
        descricao2 = fonteDescricao.render("         Cada tubarão ultrapassado gera 1 ponto.", True, branco)
        descricao3 = fonteDescricao.render("         Clique em Iniciar Jogo e Nade Se Puder.", True, branco)
        tela.blit(descricao1, (220, 180))
        tela.blit(descricao2, (220, 220))
        tela.blit(descricao3, (220, 260))
        
        startButton = pygame.draw.rect(tela, branco, (425, 330, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Jogo", True, preto)
        
        startTextoRect = startTexto.get_rect()
        startTextoRect.center = startButton.center
        tela.blit(startTexto, startTextoRect)
        
        if nome_maior is not None:
            textoMelhor = fonteMenu.render(f"Melhor pontuador: {nome_maior} - {maior_pontos} pts - {dataJogada}", True, branco)
        else:
            textoMelhor = fonteMenu.render("Nenhum recorde registrado ainda.", True, branco)
        textoMelhorRect = textoMelhor.get_rect(center=(500, 50))
        tela.blit(textoMelhor, textoMelhorRect)
        
        pygame.display.update()
        relogio.tick(60)

start()


