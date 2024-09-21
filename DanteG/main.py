#Importações
import pygame
from random import randint
from random import choice

#Resolução
resolucao = (980, 720)

#Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (102, 0, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
LARANJA = (255, 85, 0)


#area do jogo/iniciar
pygame.init()
pygame.font.init()
pygame.mixer.init()
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption('TELINHA SHOW')

#Fonte
font1 = pygame.font.Font('assents/COMICSANS.TTF', 40)
font2 = pygame.font.Font('assents/COMICSANS.TTF', 30)
font3 = pygame.font.Font('assents/COMICSANS.TTF', 60)

#Velocidade e etc do rato
vida = 6
vel_prota = 4
vel_prota_x = 0
vel_prota_y = 0
loq_prota_x = (980 * 0.50) - 40
loq_prota_y = (720 * 0.50)

#Invencibilidade
invencibilidade = True
tempo_inven = 3

altura_rato = 35
largura_rato = 40

rato_img = pygame.image.load("assents/Ratodobalacobaco1.png")
rato = rato_img.get_rect(center= [loq_prota_x, loq_prota_y])
rato_img = pygame.transform.scale(rato_img, [largura_rato, altura_rato])

#Enemies

#Bills do eixo X

#Altura e largura
largura = 70
altura = 30

#Localização
loq_bil_x = 50
loq_bil_Ly = randint(50, 700)
loq_bil_Ay = randint(240, 450)
loq_bil_VDy = choice([randint(40, 80), randint(550, 680)])
loq_bil_Ry = randint(480, 680)
loq_bil_VMy = randint(50, 300)

#Velocidades
vel_bill_X_laranja = 9
vel_bill_X_verde = 2
vel_bill_X_roxo = 3
vel_bill_X_azul = 4
vel_bill_X_vermelho = 5

Apa_lar = True

#Laranja
bil_img_esq_laranja = pygame.image.load("assents/BilEsqLarP.png")
bill_esq_laranja = bil_img_esq_laranja.get_rect(left= loq_bil_x, top= loq_bil_Ly)
bil_img_esq_laranja = pygame.transform.scale(bil_img_esq_laranja, [largura, altura])

#Azul
bil_img_esq_azul = pygame.image.load("assents/BilEsqAzuP.png")
bill_esq_azul = bil_img_esq_azul.get_rect(left= loq_bil_x, top= loq_bil_Ay)
bil_img_esq_azul = pygame.transform.scale(bil_img_esq_azul, [largura, altura])

#Roxo
bil_img_esq_roxo = pygame.image.load("assents/BilEsqRoxP.png")
bill_esq_roxo = bil_img_esq_roxo.get_rect(left= loq_bil_x, top= loq_bil_Ry)
bil_img_esq_roxo = pygame.transform.scale(bil_img_esq_roxo, [largura, altura])

#Verde
bil_img_esq_verde = pygame.image.load("assents/BilEsqVerdP.png")
bill_esq_verde = bil_img_esq_verde.get_rect(left= loq_bil_x, top= loq_bil_VDy)
bil_img_esq_verde = pygame.transform.scale(bil_img_esq_verde, [largura, altura])

#Vermelho
bil_img_esq_vermelho = pygame.image.load("assents/BilEsqVermP.png")
bill_esq_vermelho = bil_img_esq_vermelho.get_rect(left= loq_bil_x, top= loq_bil_VMy)
bil_img_esq_vermelho = pygame.transform.scale(bil_img_esq_vermelho, [largura, altura])

#Bills do eixo Y

#Altura e largura
largura2 = 30
altura2 = 70

#Localização
loq_bil_y = 610
loq_bil_Sx = randint(420, 650)
loq_bil_Rx = randint(540, 950)
loq_bil_Cx = loq_opo_x4 = choice([randint(50, 150), randint(800, 950)])
loq_bil_Ax = randint(80, 450)

#Velocidades
vel_bill_Y_amarelo = 4
vel_bill_Y_ciano = 6
vel_bill_Y_rosa = 3
vel_bill_Y_salmao = 2

#Salmão
bil_img_ret_salmao = pygame.image.load("assents/BilRetSalP.png")
bill_ret_salmao = bil_img_ret_salmao.get_rect(left= loq_bil_Sx, top= loq_bil_y)
bil_img_ret_salmao = pygame.transform.scale(bil_img_ret_salmao, [largura2, altura2])

#Rosa
bil_img_ret_rosa = pygame.image.load("assents/BilRetRosP.png")
bill_ret_rosa = bil_img_ret_rosa.get_rect(left= loq_bil_Rx, top= loq_bil_y)
bil_img_ret_rosa = pygame.transform.scale(bil_img_ret_rosa, [largura2, altura2])

#Ciano
bil_img_ret_ciano = pygame.image.load("assents/BilRetCiaP.png")
bill_ret_ciano = bil_img_ret_ciano.get_rect(left= loq_bil_Cx, top= loq_bil_y)
bil_img_ret_ciano = pygame.transform.scale(bil_img_ret_ciano, [largura2, altura2])

#Amarelo
bil_img_ret_amarelo = pygame.image.load("assents/BilRetAmaP.png")
bill_ret_amarelo = bil_img_ret_amarelo.get_rect(left= loq_bil_Ax, top= loq_bil_y)
bil_img_ret_amarelo = pygame.transform.scale(bil_img_ret_amarelo, [largura2, altura2])

#Barreiras
left_pad = pygame.Rect(-1, -1, 30, 730)
right_pad = pygame.Rect(950, 1, 30, 730)
up_pad = pygame.Rect(-1, -1, 990, 30)
down_pad = pygame.Rect(-1, 690, 990, 30)
pads = [left_pad, right_pad, up_pad, down_pad]

#Verificadores boleanos
gameover = False
reco = False
Menu = True

#Tempo
mili_temp = 0
segundos = 0

#Rounds
round = 1
tempo_round = 0

#Textos
texto_vida = font1.render('VIDAS:', True, PRETO)
num_vida = font1.render(str(vida), True, PRETO)

game_over= font3.render('GAME OVER', True, PRETO)
game_over2 = font2.render('(Precione Esc para sair ou R para reestarta)', True, PRETO)

texto_round = font1.render('Round:', True, PRETO)
num_round = font1.render(str(round), True, PRETO)

texto_tempo = font1.render('Tempo:', True, PRETO)
num_tempo = font1.render(str(segundos), True, PRETO)

#Musica
pygame.mixer.music.load('assents/Jogo.mp3')
pygame.mixer.music.play(loops=100000000)


#Quantidades de frames/ variavel pra sair
frames = pygame.time.Clock()
sair = False

#loopin do jogo
while not sair:

    #Frames
    frames.tick(60)

    #Tela
    tela.fill(BRANCO)

    #Verifica reco
    if reco:
        vida = 6
        segundos = 0
        round = 1
        tempo_round = 0
        mili_temp = 0

        largura = 70
        altura = 30

        largura2 = 30
        altura2 = 70


        vel_bill_X_laranja = 9
        vel_bill_X_verde = 2
        vel_bill_X_roxo = 3
        vel_bill_X_azul = 4
        vel_bill_X_vermelho = 5

        vel_bill_Y_amarelo = 4
        vel_bill_Y_ciano = 6
        vel_bill_Y_rosa = 3
        vel_bill_Y_salmao = 2

        bill_esq_laranja.x = loq_bil_x = 50
        bill_esq_roxo.x = loq_bil_x = 50
        bill_esq_verde.x = loq_bil_x = 50
        bill_esq_vermelho.x = loq_bil_x = 50
        bill_esq_azul.x = loq_bil_x = 50

        bill_ret_amarelo.y = loq_bil_y = 610
        bill_ret_ciano.y = loq_bil_y = 610
        bill_ret_salmao.y = loq_bil_y = 610
        bill_ret_rosa.y = loq_bil_y = 610

        bil_img_esq_vermelho = pygame.transform.scale(bil_img_esq_vermelho, [largura, altura])
        bil_img_esq_laranja = pygame.transform.scale(bil_img_esq_laranja, [largura, altura])
        bil_img_esq_azul = pygame.transform.scale(bil_img_esq_azul, [largura, altura])
        bil_img_esq_verde = pygame.transform.scale(bil_img_esq_verde, [largura, altura])
        bil_img_esq_roxo = pygame.transform.scale(bil_img_esq_roxo, [largura, altura])

        bil_img_ret_rosa = pygame.transform.scale(bil_img_ret_rosa, [largura2, altura2])
        bil_img_ret_amarelo = pygame.transform.scale(bil_img_ret_amarelo, [largura2, altura2])
        bil_img_ret_ciano = pygame.transform.scale(bil_img_ret_ciano, [largura2, altura2])
        bil_img_ret_salmao = pygame.transform.scale(bil_img_ret_salmao, [largura2, altura2])

        Apa_lar = True

        num_vida = font1.render(str(vida), True, PRETO)
        num_round = font1.render(str(round), True, PRETO)
        gameover = False
        reco = False
    
    #Sistema de invencibilidade
    if invencibilidade:
        if mili_temp == 30:
            rato_img = pygame.image.load("assents/Xerox.png")
            altura_rato = 35
            largura_rato = 40
            rato_img = pygame.transform.scale(rato_img, [largura_rato, altura_rato])

        if mili_temp == 60:
            rato_img = pygame.image.load("assents/Xerox2.png")
            altura_rato = 35
            largura_rato = 40
            rato_img = pygame.transform.scale(rato_img, [largura_rato, altura_rato])
            tempo_inven -= 1

        if tempo_inven < 0:
            invencibilidade = False
            altura_rato = 35
            largura_rato = 40
            rato_img = pygame.image.load("assents/Ratodobalacobaco1.png")
            rato_img = pygame.transform.scale(rato_img, [largura_rato, altura_rato])
            


    #Verifica a vida
    if vida <= 0:
        gameover = True
    
    #Verifica os rounds
    if tempo_round == 10:
        if not gameover:
            if round < 5:
                largura += 3
                altura += 3

                altura2 += 3
                largura2 += 3

                bil_img_esq_vermelho = pygame.transform.scale(bil_img_esq_vermelho, [largura, altura])
                bil_img_esq_laranja = pygame.transform.scale(bil_img_esq_laranja, [largura, altura])
                bil_img_esq_azul = pygame.transform.scale(bil_img_esq_azul, [largura, altura])
                bil_img_esq_verde = pygame.transform.scale(bil_img_esq_verde, [largura, altura])
                bil_img_esq_roxo = pygame.transform.scale(bil_img_esq_roxo, [largura, altura])

                bil_img_ret_rosa = pygame.transform.scale(bil_img_ret_rosa, [largura2, altura2])
                bil_img_ret_amarelo = pygame.transform.scale(bil_img_ret_amarelo, [largura2, altura2])
                bil_img_ret_ciano = pygame.transform.scale(bil_img_ret_ciano, [largura2, altura2])
                bil_img_ret_salmao = pygame.transform.scale(bil_img_ret_salmao, [largura2, altura2])

            if round <= 10:
                vel_bill_X_azul += 1
                vel_bill_X_vermelho += 1
                vel_bill_X_verde += 1
                vel_bill_X_roxo += 1

                vel_bill_Y_amarelo += 1
                vel_bill_Y_ciano += 1
                vel_bill_Y_rosa += 1
                vel_bill_Y_salmao += 1

            vel_bill_X_laranja += 9
            
                    
            
            round += 1
            num_round = font1.render(str(round), True, PRETO)
            tempo_round = 0
            

            Apa_lar = True
            

    #Eventos de botões e saida
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sair = True
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sair = True
            if gameover:
                if evento.key == pygame.K_r:
                    reco = True
            if Menu:
                if evento.key == pygame.K_c:
                    Menu = False

            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                vel_prota_y = -vel_prota
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                vel_prota_y = vel_prota
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                vel_prota_x = -vel_prota
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                vel_prota_x = vel_prota

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                vel_prota_y = 0
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                vel_prota_y = 0
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                vel_prota_x = 0
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                vel_prota_x = 0


    #Velocidade do rato
    rato.x += vel_prota_x
    rato.y += vel_prota_y

    #Velocidade dos Bill da esquerda
    if Apa_lar:
        bill_esq_laranja.x += vel_bill_X_laranja
    bill_esq_azul.x += vel_bill_X_azul
    bill_esq_roxo.x += vel_bill_X_roxo
    bill_esq_vermelho.x += vel_bill_X_vermelho
    bill_esq_verde.x += vel_bill_X_verde

    bill_ret_amarelo.y -= vel_bill_Y_amarelo
    bill_ret_ciano.y -= vel_bill_Y_ciano
    bill_ret_rosa.y -= vel_bill_Y_rosa
    bill_ret_salmao.y -= vel_bill_Y_salmao

    #desenhando o personagens
    if not gameover:
        tela.blit(rato_img, rato)

        #Cria os Bill da esquerda
        if Apa_lar:
            if loq_bil_Ly != loq_bil_Ay and loq_bil_Ly != loq_bil_Ry:
                if loq_bil_Ly != loq_bil_VDy and loq_bil_Ly != loq_bil_VMy:
                    tela.blit(bil_img_esq_laranja, bill_esq_laranja)
            
        if loq_bil_Ry != loq_bil_Ly and loq_bil_Ry != loq_bil_Ay:
            if loq_bil_Ry != loq_bil_VMy and loq_bil_Ry != loq_bil_VDy:
                tela.blit(bil_img_esq_roxo, bill_esq_roxo)
        
        if loq_bil_VDy != loq_bil_Ly and loq_bil_VDy != loq_bil_Ry:
            if loq_bil_VDy != loq_bil_Ay and loq_bil_VDy != loq_bil_VMy:
                tela.blit(bil_img_esq_verde, bill_esq_verde)
        
        if loq_bil_Ay != loq_bil_Ly and loq_bil_Ay != loq_bil_Ry:
            if loq_bil_Ay != loq_bil_VMy and loq_bil_Ay != loq_bil_VDy:
                tela.blit(bil_img_esq_azul, bill_esq_azul)
        
        if loq_bil_VMy != loq_bil_Ly and loq_bil_VMy != loq_bil_Ry:
            if loq_bil_VMy != loq_bil_VDy and loq_bil_VMy != loq_bil_Ay:
                tela.blit(bil_img_esq_vermelho, bill_esq_vermelho)

        #Cria os Bill de Baixo
        if loq_bil_Sx != loq_bil_Ax and loq_bil_Sx != loq_bil_Cx and loq_bil_Sx != loq_bil_Rx:
            tela.blit(bil_img_ret_salmao, bill_ret_salmao)

        if loq_bil_Ax != loq_bil_Sx and loq_bil_Ax != loq_bil_Cx and loq_bil_Ax != loq_bil_Rx:
            tela.blit(bil_img_ret_amarelo, bill_ret_amarelo)

        if loq_bil_Cx != loq_bil_Ax and loq_bil_Cx != loq_bil_Sx and loq_bil_Cx != loq_bil_Rx:
            tela.blit(bil_img_ret_ciano, bill_ret_ciano)

        if loq_bil_Rx != loq_bil_Ax and loq_bil_Rx != loq_bil_Cx and loq_bil_Rx != loq_bil_Sx:
            tela.blit(bil_img_ret_rosa, bill_ret_rosa)

    
    #Cria as barreiras
    for pad in pads:
            pygame.draw.rect(tela, VERMELHO, pad)
    
    #Colisão rato/Barreira
    if rato.collidelist(pads) >= 0:
        rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
        vida -= 1
        invencibilidade = True
        tempo_inven = 3
        num_vida = font1.render(str(vida), True, PRETO)
    
    #Colisão Bill da esquerda/Barreira
    if bill_esq_laranja.collidelist(pads) >= 0:
        bill_esq_laranja = bil_img_esq_laranja.get_rect(left= loq_bil_x, top= loq_bil_Ly)
        loq_bil_Ly = randint(50, 700)
        Apa_lar = False

    if bill_esq_roxo.collidelist(pads) >= 0:
        bill_esq_roxo = bil_img_esq_roxo.get_rect(left= loq_bil_x, top= loq_bil_Ry)
        loq_bil_Ry = randint(480, 680)

    if bill_esq_azul.collidelist(pads) >= 0:
        bill_esq_azul = bil_img_esq_azul.get_rect(left= loq_bil_x, top= loq_bil_Ay)
        loq_bil_Ay = randint(240, 450)

    if bill_esq_verde.collidelist(pads) >= 0:
        bill_esq_verde = bil_img_esq_verde.get_rect(left= loq_bil_x, top= loq_bil_VDy)
        loq_bil_VDy = choice([randint(40, 80), randint(550, 680)])

    if bill_esq_vermelho.collidelist(pads) >= 0:
        bill_esq_vermelho = bil_img_esq_vermelho.get_rect(left= loq_bil_x, top= loq_bil_VMy)
        loq_bil_VMy = randint(50, 300)
    
    #Colisão Bill de baixo/Barreira
    if bill_ret_rosa.collidelist(pads) >= 0:
        bill_ret_rosa = bil_img_ret_rosa.get_rect(left= loq_bil_Rx, top= loq_bil_y)
        loq_bil_Rx = randint(540, 950)

    if bill_ret_amarelo.collidelist(pads) >= 0:
        bill_ret_amarelo = bil_img_ret_amarelo.get_rect(left= loq_bil_Ax, top= loq_bil_y)
        loq_bil_Ax = randint(80, 450)

    if bill_ret_ciano.collidelist(pads) >= 0:
        bill_ret_ciano = bil_img_ret_ciano.get_rect(left= loq_bil_Cx, top= loq_bil_y)
        loq_bil_Cx = loq_opo_x4 = choice([randint(50, 150), randint(800, 950)])

    if bill_ret_salmao.collidelist(pads) >= 0:
        bill_ret_salmao = bil_img_ret_salmao.get_rect(left= loq_bil_Sx, top= loq_bil_y)
        loq_bil_Sx = randint(420, 650)
    
    #Colisão Rato/Bill da esquerda
    if not invencibilidade:
        if rato.colliderect(bill_esq_laranja) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_esq_vermelho) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_esq_roxo) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_esq_azul) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_esq_verde) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
    
    #Colisão Rato/Bill de baixo
        if rato.colliderect(bill_ret_salmao) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_ret_rosa) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_ret_ciano) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)
        if rato.colliderect(bill_ret_amarelo) > 0:
            rato = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            vida -= 1
            invencibilidade = True
            tempo_inven = 3
            num_vida = font1.render(str(vida), True, PRETO)



    #Textos
    tela.blit(texto_vida, [32, 14])
    tela.blit(num_vida, [230, 14])
    tela.blit(texto_round, [360, 14])
    tela.blit(num_round, [530, 14])
    tela.blit(texto_tempo, [660, 14])
    tela.blit(num_tempo, [830, 14])
    num_tempo = font1.render(str(segundos), True, PRETO)

    #Tela de GameOver
    if gameover:
        tela.blit(game_over, [280, 140])
        tela.blit(game_over2, [180, 340])

    
    #Contador de segundos
    if mili_temp == 60:
        if not gameover:
            segundos += 1
            tempo_round += 1
            mili_temp = 0

    #Mili segundos    
    mili_temp += 1
    
    #Atualização da tela
    pygame.display.flip()
