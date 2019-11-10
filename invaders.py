from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from Telas import Telas
from time import sleep
from Jogador import Jogador
from inimigo import Inimigo
from auxiliar import *

temp = frame = frames = 0

pts = dec = 0

def Menu():
    sleep(.5)
    menu = Telas()
    botoesMenu = menu.addBotao(50, 'imagens/Jogar.png', 'imagens/dificuldade.png', 'imagens/Rank.png', 'imagens/sair.png')


    while True:
        menu.fundo.draw()
        for i in botoesMenu:
            i.draw()
        
        #Dificuldade
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

def Ranking():
    sleep(.5)
    ranking = Telas()

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
        if ranking.mouse.is_button_pressed(1) and ranking.mouse.is_over_object(botoesMenu[0]):
            ranking.janela.close()
        #jogar
        if ranking.mouse.is_button_pressed(1) and ranking.mouse.is_over_object(botoesMenu[1]):  
            Jogo() 





        ranking.janela.update()

def Dificuldade():
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
            pass
        elif dificuldade.mouse.is_button_pressed(1) and dificuldade.mouse.is_over_object(botoesDif[1]):
            pass
        elif dificuldade.mouse.is_button_pressed(1) and dificuldade.mouse.is_over_object(botoesDif[2]):
            pass
        else:
            dificuldade.janela.update()



def Jogo():
 

    jogo = Telas()
    jogador = Jogador()
    inimigo = Inimigo()
    

    jogador.nave.set_position(jogo.janela.width/2-jogador.nave.width,jogo.janela.height-jogador.nave.height)

    teclado = Window.get_keyboard()

   
    segundo = fps = fps2 = 0

    existe_inimigo = 0
    temporizador = 0
    hit = 0
    velox = 0.3
    y_descer=50
    vidas=5
    score=0
 

    while True:       
        temporizador += 1
        jogo.fundo.draw()
        tempo = jogo.janela.delta_time()
        segundo+=tempo
        fps+=1
        if segundo>=1:
            fps2=fps
            fps=0
            segundo=0

        score+=tempo
            
        jogo.janela.draw_text(str(fps2), 0, jogo.janela.height - 50, 50, (178, 102, 255), "Calibri")
                    
        
    
        jogador.saude(vidas)#desenha a vida do jogador na tela

        if not existe_inimigo:
            existe_inimigo = inimigo.criar_inimigo()
      

        jogador.nave_movimentar(jogo.janela.width) #classe para movimentar a nave

        if(teclado.key_pressed("space")) and temporizador > 200:  # Atirar
            jogador.atirar()
            temporizador = 0
    
        if temporizador > 200:
            temporizador = 0
            inimigo.atirar()


        for tiro in jogador.vet_tiro:#########################
            tiro.y -= 0.5
            if tiro.y < 0:
                jogador.vet_tiro.remove(tiro)
            else:
                tiro.draw()
            for i in range(len(inimigo.matriz)):
                for alen in inimigo.matriz[i]:
                    if (tiro.collided(alen)):
                        jogador.vet_tiro.remove(tiro)
                        inimigo.matriz[i].remove(alen)
                        
                        
                        ################################
        
        for tiro in inimigo.vet_tiro:#########################
            tiro.y += 0.2
            if tiro.y > jogo.janela.height- jogador.nave.height :
                inimigo.vet_tiro.remove(tiro)
            else:
                tiro.draw()

            if (tiro.collided(jogador.nave)):
                inimigo.vet_tiro.remove(tiro)
                vidas -= 1

        
        velox ,hit, y_descer = inimigo.mover_inimigo(velox, hit,y_descer,jogo.janela.height,jogador.nave.height)
        
        if y_descer == 'menu' or len(inimigo.matriz[0]) == 0 or vidas == 0:

            Menu()
    
    
        
        jogador.nave.draw()
        jogo.janela.update()  

Menu()