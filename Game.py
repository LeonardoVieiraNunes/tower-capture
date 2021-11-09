import pygame

class Game:
    SCREENSIZE = {"width":900,"height":500}
    WINDOW = pygame.display.set_mode((SCREENSIZE["width"],SCREENSIZE["height"]))
    CLOCK = pygame.time.Clock()
    FPS = 24
    
    def __init__(self):
        self.run = True
        self.mapaAtual = Mapa()

    def setup(self):
        pygame.display.set_caption("Tower Capture!")

        while self.run:
            Game.CLOCK.tick(Game.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mapaAtual.mouseClick()

            self.mapaAtual.mouseHover()
            self.mapaAtual.draw()

            pygame.display.update()
            
        pygame.quit()

from Mapa import Mapa