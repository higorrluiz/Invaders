from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from Telas import Telas

jogo=Telas()

class Inimigo():
    def __init__(self):
        self.matriz=[]
        self.lista=[]
    
    def criar_inimigo(self):
        for i in range(2):
            self.lista = []
            for j in range(4):
                self.lista.append(Sprite("inimigo.png"))
            self.matriz.append(self.lista)
      
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

    def mover_inimigo(self,velox, hit):
        for i in range(2):
            for j in range(4):
                self.matriz[i][j].x += velox
                self.matriz[i][j].draw()
                

                if self.matriz[i][j].x >= jogo.janela.width - self.matriz[i][j].width and not hit:
                    hit = 1
                    velox = velox * -1
                    
                    
                elif self.matriz[i][j].x <= 0 and hit:
                    hit = 0
                    velox = velox * -1
        return velox, hit