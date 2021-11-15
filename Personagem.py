import pygame
from Controladora import Controladora
from random import randint
from Entidade import Entidade

class Personagem(Entidade):
    def __init__(self, gridConfig, id):
        super().__init__(gridConfig, id)
        self.ataque = 10
        self.defesa = 10
        self.vantagem = ''
        self.range_movimentacao = 1
        self.range_ataque = 1


