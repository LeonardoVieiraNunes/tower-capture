import pygame

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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mapaAtual.mouseClick(event)

            self.mapaAtual.mouseHover()
            self.mapaAtual.draw()

            pygame.display.update()
            
        pygame.quit()

from Mapa import Mapa