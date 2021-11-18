import pygame
# from Personagem import Personagem
from Entidade import Entidade

class Escudeiro(Entidade):
    def __init__(self, gridConfig, id, idJogador):
        super().__init__(gridConfig, id, idJogador)

        self.vida = 30
        self.ataque = 20
        self.defesa = 30
        self.range_movimentacao = 2
        self.range_ataque = 2

        image_path ='images/escudeiro_idle.png'
        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))

        self.draw()
