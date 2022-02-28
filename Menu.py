import pygame
from Controladora import Controladora
from Posicao import Posicao
from Entidade import Entidade

class Menu():
    def __init__(self, game):
        self.game = game
        self.btn_iniciar_jogo = pygame.Rect(269,317,346,91)
        self.backgroundImage = pygame.image.load("./images/back-menu.png")
        self.fontShop = pygame.font.Font(pygame.font.get_default_font(), 13)
        self.fontGrid = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.setup()

    def setup(self):
        self.game.WINDOW.blit(self.backgroundImage, (0, 0))

    def handle_click(self, mousepos):
        pass
