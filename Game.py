import pygame
from Jogador import Jogador
class Game:
    def __init__(self):
        self.SCREENSIZE = {"width":900,"height":500}
        self.WINDOW = pygame.display.set_mode((self.SCREENSIZE["width"],self.SCREENSIZE["height"]))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 24
        self.run = True
        self.mapaAtual = None

    def setup(self):
        pygame.display.set_caption("Tower Capture!")

        self.mapaAtual = Mapa()

        while self.run:
            self.CLOCK.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3 or event.button == 2):
                    self.mapaAtual.mouseClick(event)

            self.mapaAtual.mouseHover()
            self.mapaAtual.draw()



            self.jogador1 = Jogador([],1)
            self.jogador2 = Jogador([],2)



            pygame.display.update()
            
        pygame.quit()

from Mapa import Mapa