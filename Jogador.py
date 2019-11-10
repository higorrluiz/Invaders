from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *

class Jogador():
    def __init__(self):
        self.nave = Sprite("imagens/nave.png")
        self.vet_tiro= []
        self.vidas = []

    def nave_movimentar(self,janela_largura):
        self.nave.move_key_x(1)
        #IFs para limitar espaço de locomoção da nave
        if self.nave.x >= janela_largura-self.nave.width: 
            self.nave.x = janela_largura-self.nave.width
        if self.nave.x <=0 :
            self.nave.x=0
    
    def atirar(self):
        tiro = Sprite("imagens/tiro.png")
        tiro.set_position(self.nave.x+27, self.nave.y-self.nave.height+10)
        self.vet_tiro.append(tiro)

    def saude(self,vidas):
        x=0
        y=0
        for i in range(vidas):
            self.vidas.append(GameImage("imagens/coração.png"))
        for i in range(vidas):
            self.vidas[i].set_position(x,y)
            self.vidas[i].draw()
            x += 30

    def movimentarTiro_e_TestarColisao(self,matriz_inimigo):
        for tiro in self.vet_tiro:#########################
            tiro.y -= 0.5
            if tiro.y < 0:
                self.vet_tiro.remove(tiro)
            else:
                tiro.draw()
            for i in range(len(matriz_inimigo)):
                for alen in matriz_inimigo[i]:
                    if (tiro.collided(alen)):
                        self.vet_tiro.remove(tiro)
                        matriz_inimigo[i].remove(alen)       







    
