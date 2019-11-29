from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
import random

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

    def movimentarTiro_e_TestarColisao(self,matriz_inimigo,score,boss,tem_superinimigo,segundos2):
        velox=0.5
        for tiro in self.vet_tiro:
            try:
                if tiro.y<= matriz_inimigo[1][random.randint(0,4)].y:
                    velox= 3
            except:
                pass    
            tiro.y -= velox
            if tiro.y < 0:
                self.vet_tiro.remove(tiro)
            else:
                tiro.draw()
            for i in range(len(matriz_inimigo)):
                for alen in matriz_inimigo[i]:
                    if (tiro.collided(alen)): #se o tiro encostou no alien, eu removo o tiro da tela
                        try:
                            self.vet_tiro.remove(tiro)
                        except:
                            pass
                        matriz_inimigo[i].remove(alen) 
                        score+=1

            if (tiro.collided(boss)): #se o tiro encostou no boss, eu removo o tiro da tela
                try:
                    self.vet_tiro.remove(tiro)
                except:
                    pass
                tem_superinimigo=0
                boss.set_position(800,800)
                score+=4
                segundos2 = 0

        return score, tem_superinimigo,segundos2   
                        