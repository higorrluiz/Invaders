from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from Telas import Telas
from time import sleep
from Jogador import Jogador
from inimigo import Inimigo
from auxiliar import *
import random

speed_tiro = 0.6
speed_shoot = 500

def Menu():
    sleep(.5)
    menu = Telas()
    botoesMenu = menu.addBotao(50, 'imagens/Jogar.png', 'imagens/dificuldade.png', 'imagens/Rank.png', 'imagens/sair.png')


    while True:
        menu.fundo.draw()
        for i in botoesMenu:
            i.draw()
        
        #MODO/DIFICULDADE
        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[1]):
            Dificuldade()

        #Ranking
        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[2]):
            Ranking()
        #jogar
        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[0]):  
            Jogo() 
        
        #Sair
        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[3]):
            menu.janela.close()
        
        if menu.teclado.key_pressed('esc'):
            menu.janela.close()


        else:        
            menu.janela.update()

def Ranking(): #tela que mostra os nomes dos jogadores em ordem do melhor para o pior
    sleep(.5)
    ranking = Telas()
    ordenar_ranking()

    while True:
        ranking.fundo.draw()
        jogadores = contar_pessoas()
        y = ranking.janela.height/6

        for jogador in jogadores:
            ranking.janela.draw_text( jogador.strip(), ranking.janela.width/2 - 80, y, 50, (178, 102, 255), "Calibri")
            y += 50

        botoesMenu = ranking.addBotao(y,'imagens/Jogar.png','imagens/sair.png')
        for i in botoesMenu:
            i.draw()
        
        #Sair
        if ranking.mouse.is_button_pressed(1) and ranking.mouse.is_over_object(botoesMenu[1]):
            ranking.janela.close()
        #jogar
        if ranking.mouse.is_button_pressed(1) and ranking.mouse.is_over_object(botoesMenu[0]):  
            Jogo() 
        ranking.janela.update()

def Dificuldade():
    global speed_tiro, speed_shoot
    sleep(.5)
    dificuldade = Telas()
    botoesDif = dificuldade.addBotao(50, 'imagens/facil.png', 'imagens/medio.png', 'imagens/dificil.png')

    while True:
        dificuldade.fundo.draw()
        for i in botoesDif:
            i.draw()

        if dificuldade.teclado.key_pressed('esc'):
            Menu()
            
        if dificuldade.mouse.is_button_pressed(1) and dificuldade.mouse.is_over_object(botoesDif[0]): #Facil foi pressionado
            speed_tiro = 0.6
            speed_shoot = 500
            Jogo()
        elif dificuldade.mouse.is_button_pressed(1) and dificuldade.mouse.is_over_object(botoesDif[1]):
            speed_tiro = 0.8
            speed_shoot = 300
            Jogo()
        elif dificuldade.mouse.is_button_pressed(1) and dificuldade.mouse.is_over_object(botoesDif[2]):
            speed_tiro = 1
            speed_shoot = 200
            Jogo()
        else:
            dificuldade.janela.update()

def Jogo():
    global speed_tiro, speed_shoot
    jogo = Telas()
    jogador = Jogador()
    inimigo = Inimigo()
    
    jogador.nave.set_position(jogo.janela.width/2-jogador.nave.width,jogo.janela.height-jogador.nave.height)

    teclado = Window.get_keyboard()

    segundo = fps = fps2 = 0
    

    existe_inimigo = 0
    especial = 0

    temporizador = temp = 0
    hit = 0
    velox = 0.3
    y_descer=50

    velox2=0.3

    score = 0
    
    vidas=5

    linha=2
    coluna=4
    cont=0

    while True:       
        temporizador += 1
        temp +=1

        jogo.fundo.draw()

        #desenhando fps
        tempo = jogo.janela.delta_time()
        segundo+=tempo
        fps+=1
        if segundo>=1:
            fps2=fps
            fps=0
            segundo=0
            

        jogo.janela.draw_text(str(fps2), 0, jogo.janela.height - 50, 50, (178, 102, 255), "Calibri")
        
    
        jogador.saude(vidas)#desenha a vida do jogador na tela

        if not existe_inimigo:#criando inimigos caso eles nao existam
            existe_inimigo = inimigo.criar_inimigo(linha,coluna)
      

        jogador.nave_movimentar(jogo.janela.width) #movimentar a nave

        if(teclado.key_pressed("space")) and temporizador > 200:  # Atirar
            jogador.atirar()
            temporizador = 0
    
        if temp > speed_shoot: #tiro do inimigo
            temp = 0
            inimigo.atirar()

        
        score = jogador.movimentarTiro_e_TestarColisao(inimigo.matriz,score,inimigo.super_inimigo)#movimenta o tiro e testa colisão com inimigo
        vidas = inimigo.movimentarTiro_e_TestarColisao(jogador.nave,vidas,jogo.janela,speed_tiro)#movimenta o tiro e testa colisão com a nave

        
        velox ,hit= inimigo.mover_inimigo(velox, hit, jogo.janela.height,jogador.nave)#faz os inimigos se moverem
        
        if especial == 0:
            if random.choice(inimigo.matriz[0]).y > 160:
                especial = inimigo.Criar_SuperInimigo(especial)
        
        if especial and inimigo.super_inimigo.x<800:
            velox2 = inimigo.mover_SuperInimigo(velox2,jogo.janela)
        
        
        if len(inimigo.matriz[0]) == 0:
            existe_inimigo = 0
            y_descer=0
            linha += 1
            cont += 10
            

        if y_descer == 'menu' or vidas == 0:#tenho que mudar
            adicionar_jogador(score)
            Menu()
    

        jogador.nave.draw()
        jogo.janela.update()  

Menu()