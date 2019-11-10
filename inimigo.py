from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from Telas import Telas
import random

jogo=Telas()

class Inimigo():
    def __init__(self):
        self.matriz=[]
        self.lista=[]
        self.vet_tiro = [] 
    
    def criar_inimigo(self):
        #colocando os inimigos na matriz
        for i in range(2):
            self.lista = []
            for j in range(4):
                self.lista.append(Sprite("imagens/inimigo.png"))
            self.matriz.append(self.lista)
      #Posicionando os inimigos um em baixo do outro
        y=0
        x=10
        for i in range(2):
            x=10
            for j in range(4):
                self.matriz[i][j].set_position(x,y)
                self.matriz[i][j].draw()
             
                x += self.matriz[i][j].width + 10
            y += self.matriz[i][j].height + 10
        return 1

    def descer_inimigo(self,y,janela,nave):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j].y+50 >= janela-nave:
                    return 'menu'
                self.matriz[i][j].y = y
                self.matriz[i][j].draw()
            y +=50
        return y



    def mover_inimigo(self,velox, hit,y_descer,janela,nave):
        #fazendo eles se moverem de fato (apenas pros lados)
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j].x += velox
                self.matriz[i][j].draw()
                
                #limitando movimento ao tamanho da tela e fazendo inimigos descerem sempre que tocarem nos estremos
                if self.matriz[i][j].x >= jogo.janela.width - self.matriz[i][j].width and not hit:
                    hit = 1
                    velox = velox * -1
                    y_descer = self.descer_inimigo(y_descer,janela,nave)
                    

                #limite dos inimigos na esquerda
                elif self.matriz[i][j].x <= 0 and hit:
                    hit = 0
                    velox = velox * -1
                    y_descer = self.descer_inimigo(y_descer,janela,nave)
        return velox, hit, y_descer
        
    def atirar(self):
        if len(self.matriz[1]) == 0:
            alen = random.choice(self.matriz[0])
        else:
            alen = random.choice(self.matriz[random.randint(0,1)])
        
        tiro = Sprite("imagens/tiro_inimigo.png")
        tiro.set_position(alen.x, alen.y+alen.height-10)
        self.vet_tiro.append(tiro)


        