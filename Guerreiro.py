import pygame
# from Personagem import Personagem
from Entidade import Entidade

class Guerreiro(Entidade):
    def __init__(self, gridConfig, id, idJogador, game):
        super().__init__(gridConfig, id, idJogador, game)
        image_path ='images/guerreiro_idle.png'

        self.vida = 40
        self.ataque = 30
        self.defesa = 15
        self.range_movimentacao = 4
        self.range_ataque = 2

        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))
        self.draw()
