from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from Telas import Telas
from time import sleep
from Jogador import Jogador
from inimigo import Inimigo


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

        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[0]):  
            Jogo() 
        
        #Sair
        if menu.mouse.is_button_pressed(1) and menu.mouse.is_over_object(botoesMenu[3]):
            menu.janela.close()
        
        if menu.teclado.key_pressed('esc'):
            menu.janela.close()


        else:        
            menu.janela.update()

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

    existe_inimigo = 0
    temporizador = 0
    hit = 0
    velox = 0.3
    y_descer=50
    
  
    while True:

        temporizador += 1
        jogo.fundo.draw()

        if not existe_inimigo:
            existe_inimigo = inimigo.criar_inimigo()
      

        jogador.nave_movimentar(jogo.janela.width) #classe para movimentar a nave

        if(teclado.key_pressed("space")) and temporizador > 200:  # Atirar
            jogador.atirar()
            temporizador = 0
    
        for tiro in jogador.vet_tiro:
            tiro.y -= 0.5
            if tiro.y < 0:
                jogador.vet_tiro.remove(tiro)
            else:
                tiro.draw()

        
        velox ,hit, y_descer = inimigo.mover_inimigo(velox, hit,y_descer,jogo.janela.height,jogador.nave.height)
        if y_descer == 'menu':
            Menu()

        jogador.nave.draw()
        jogo.janela.update()  

Menu()