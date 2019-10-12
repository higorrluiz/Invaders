from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *

class Jogador():
    def __init__(self):
        self.nave = Sprite("imagens/nave.png")
        self.vet_tiro= []

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
        
        #return 1






    
