import pygame
from Controladora import Controladora
from random import randint

class Entidade():
    def __init__(self, gridConfig, id):
        self.id = id
        self.gridConfig = gridConfig
        self.originalColor = (randint(0,255),randint(0,255),randint(0,255))
        self.color = self.originalColor
    
    def draw(self):
        pygame.draw.rect(Controladora.GAME.WINDOW,self.color,(self.gridConfig["x"],self.gridConfig["y"],self.gridConfig["size"][0],self.gridConfig["size"][1]),10)

    def getId(self):
        return self.id
    
    def handleHover(self,reset):
        if reset == "notHover":
            self.color = self.originalColor
        elif reset == "hover":
            self.color = (255,255,255)
        else:
            self.color = (0,0,0)