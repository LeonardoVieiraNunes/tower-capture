import pygame
# from Personagem import Personagem
from Entidade import Entidade

class Torre(Entidade):
    def __init__(self, gridConfig, id, owner):
        super().__init__(gridConfig, id, owner)
        image_path ='images/shaded grid.png'

        self.vida = 99
        self.ataque = 99
        self.defesa = 99
        self.range_movimentacao = 2
        self.range_ataque = 4

        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))
        self.draw()
