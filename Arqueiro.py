import pygame
# from Personagem import Personagem
from Entidade import Entidade

class Arqueiro(Entidade):
    def __init__(self, gridConfig, id, idJogador, game):
        super().__init__(gridConfig, id, idJogador, game)
        image_path ='images/arqueiro_idle.png'

        self.vida = 20
        self.ataque = 30
        self.defesa = 25
        self.range_movimentacao = 2
        self.range_ataque = 4

        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))
        self.draw()
