from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from Telas import Telas
import random

jogo=Telas()

class Inimigo():
    def __init__(self):
        self.lista=[]
        self.vet_tiro = [] 
        self.super_inimigo = Sprite("imagens/boss.png")
    
    def criar_inimigo(self,linha,coluna):
        self.matriz=[]
        #colocando os inimigos na matriz
        for i in range(linha):
            self.lista = []
            for j in range(coluna):
                self.lista.append(Sprite("imagens/inimigo.png"))
            self.matriz.append(self.lista)
      #Posicionando os inimigos um em baixo do outro
        y=30
        x=0
        for i in range(linha):
            x=0
            for j in range(coluna):
                self.matriz[i][j].set_position(x,y)
                self.matriz[i][j].draw()
             
                x += self.matriz[i][j].width + 10
            y += self.matriz[i][j].height + 10
        return 1


    def mover_inimigo(self,velox, hit, janela,nave):
        #fazendo eles se moverem de fato (apenas pros lados)
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j].x += velox
        
        #limite dos inimigos na esquerda
                if self.matriz[i][j].x <= 0:
                    hit = 1
                    velox = velox * -1
               
        #limitando movimento ao tamanho da tela e fazendo inimigos descerem sempre que tocarem nos estremos
                elif self.matriz[i][j].x >= jogo.janela.width - self.matriz[i][j].width:
                    hit = 1
                    velox = velox * -1         
        
        if hit:
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[i])):
                    self.matriz[i][j].y+=40
            hit = 0
        
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j].draw()


        return velox, hit
        
    def atirar(self):
        if len(self.matriz[1]) == 0:
            alen = random.choice(self.matriz[0])
        else:
            alen = random.choice(self.matriz[random.randint(0,1)])
        
        tiro = Sprite("imagens/tiro_inimigo.png")
        tiro.set_position(alen.x, alen.y+alen.height-10)
        self.vet_tiro.append(tiro)


    def movimentarTiro_e_TestarColisao(self,nave,vidas,janela,speed_tiro):
        for tiro in self.vet_tiro:
            tiro.y += speed_tiro
            if tiro.y > janela.height- nave.height :
                self.vet_tiro.remove(tiro)
            else:
                tiro.draw()

            if (tiro.collided(nave)): #se o tiro encostou na nave eu tiro o tiro 
                self.vet_tiro.remove(tiro)
                vidas -= 1

        return vidas

    def Criar_SuperInimigo(self, especial):
        self.super_inimigo.set_position(0,50)
        self.super_inimigo.draw()
        especial = 1 
        return especial
    
    def mover_SuperInimigo(self,velox2,janela):
        
        self.super_inimigo.x += velox2
        if self.super_inimigo.x >= janela.width - self.super_inimigo.width:
            velox2 = velox2 * -1     
        elif self.super_inimigo.x <= 0:
            velox2 = velox2 * -1

      
        
        self.super_inimigo.draw()

        return velox2

        