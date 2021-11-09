import pygame
from Controladora import Controladora

class Mapa:
    def __init__(self):
        self.grid = pygame.sprite.Group()
        self.gridConfig = {"x":225,"y":135,"size":(70,70)}
        self.mousePos = (0,0)
        self.backgroundImage = pygame.image.load("./images/mapaBackground.png")
        self.backgroundImageShop = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),(180,500)), (180,500))
        self.setup()
    
    def swapPositions(self):
        pass
    
    def setup(self):
        Controladora.GAME.WINDOW.blit(self.backgroundImage, (0, 0))
        for i in range(9):
            for j in range(5):
                tempConfig = self.gridConfig.copy()
                tempConfig["x"] += i*tempConfig["size"][0]
                tempConfig["y"] += j*tempConfig["size"][1]
                self.grid.add(Entidade(tempConfig,(i*9)+j))
    
    def drawSideBar(self):
        Controladora.GAME.WINDOW.blit(self.backgroundImageShop, (0, 0))

    def drawGrid(self):
        for i in self.grid.sprites():
            i.draw()

    def draw(self):
        self.mousePos = pygame.mouse.get_pos()

        self.drawSideBar()
        self.drawGrid()
    
    def mouseClick(self,event):
        for i in self.grid.sprites():
            i.checkClick(self.mousePos,event)
    
    def mouseHover(self):
        for i in self.grid.sprites():
            i.checkHover(self.mousePos)

from Entidade import Entidade