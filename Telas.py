from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *



class Telas():
    def __init__(self):
        self.janela = Window(1000,500)
        self.janela.set_title("Invaders")

        self.mouse = Window.get_mouse()
        self.teclado = Window.get_keyboard()
        self.fundo = GameImage("fundo.png")
    
    def addBotao(self, posInicialX, *nomeSprites):
        lista = list()
        
        for botao in nomeSprites:
            bot = Sprite(botao)
            bot.set_position(self.janela.width/2-100, posInicialX)
            posInicialX += bot.height + 20
            lista.append(bot)
        return lista
