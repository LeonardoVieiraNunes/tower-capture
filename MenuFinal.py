import pygame
from Controladora import Controladora
from Posicao import Posicao
from Entidade import Entidade

class MenuFinal():
    def __init__(self, game):
        self.game = game
        self.backgroundImage = pygame.image.load("./images/back-end.png")
        self.fontMain = pygame.font.Font(pygame.font.get_default_font(), 65)
        self.fontText = pygame.font.Font(pygame.font.get_default_font(), 35)

    def setup(self, content):
        self.game.WINDOW.blit(self.backgroundImage, (0, 0))
        print(content["vencedor"].id)
        
        text_surface = self.fontMain.render("Fim de jogo!", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (100, 150))
        
        jogadorId = content["vencedor"].id
        turno = content["turno"]
        text_surface = self.fontText.render(f"Jogador {jogadorId} no turno {turno}", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (100, 250))
        
        text_surface = self.fontText.render("Reinicie para uma nova partida!", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (100, 290))

    def handle_click(self, mousepos):
        pass
