import pygame
# from Personagem import Personagem
from Entidade import Entidade

class Torre(Entidade):
    def __init__(self, gridConfig, id, idJogador, game):
        super().__init__(gridConfig, id, idJogador, game)
        image_path ='images/test_tower.png'

        self.vida = 99
        self.ataque = 0
        self.defesa = 0
        self.range_movimentacao = 0
        self.range_ataque = 0

        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 4.3), int(self.size[1] * 4.4)))
        self.draw()
