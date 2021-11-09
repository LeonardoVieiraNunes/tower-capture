import pygame
from Game import Game
from Entidade import Entidade

class Mapa:
    def __init__(self):
        self.grid = []
        self.gridConfig = {"x":225,"y":135,"size":70}
        self.mousePos = (0,0)
        self.backgroundImage = pygame.image.load("./images/mapaBackground.png")
        self.backgroundImageSideBar = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),(180,500)), (180,500))
        self.setup()
    
    def setup(self):
        for i in range(9):
            tempList = []
            for j in range(5):
                tempList.append(Entidade({"x":self.gridConfig["x"]+(i*self.gridConfig["size"]),"y":self.gridConfig["y"]+(j*self.gridConfig["size"])},{"width":self.gridConfig["size"],"height":self.gridConfig["size"]}))
            self.grid.append(tempList)
    
    def drawSideBar(self):
        Game.WINDOW.blit(self.backgroundImageSideBar, (0, 0))
        # pygame.draw.rect(Game.WINDOW, (0,0,0), pygame.Rect(0, 0, 180, 500), 1)

    def drawGrid(self):
        for i in self.grid:
            for j in i:
                j.draw()

    def draw(self):
        self.mousePos = pygame.mouse.get_pos()
        # Game.WINDOW.fill((255,255,255))
        Game.WINDOW.blit(self.backgroundImage, (0,0))

        self.drawSideBar()
        self.drawGrid()
    
    def mouseClick(self):
        for i in self.grid:
            for j in i:
                j.checkClick(self.mousePos)
    
    def mouseHover(self):
        for i in self.grid:
            for j in i:
                j.checkHover(self.mousePos)