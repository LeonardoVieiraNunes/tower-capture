import pygame
from Controladora import Controladora
from random import randint

class Entidade(pygame.sprite.Sprite):
    def __init__(self, gridConfig, id):
        super().__init__()
        self.id = id
        self.gridConfig = gridConfig
        self.originalColor = (randint(0,255),randint(0,255),randint(0,255))
        self.color = self.originalColor

        references = {
            0: 'images/arqueiro_idle.png',
            1: 'images/escudeiro_idle.png',
            2: 'images/guerreiro_idle.png',
        }
        index = randint(0,2)
        self.image = pygame.image.load(references[index])
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*2.1), int(self.size[1]*2)))


    def draw(self):
        Controladora.GAME.WINDOW.blit(self.image, (self.gridConfig["x"],self.gridConfig["y"]))
        # pygame.draw.rect(Controladora.GAME.WINDOW,self.color,(self.gridConfig["x"],self.gridConfig["y"],self.gridConfig["size"][0],self.gridConfig["size"][1]),10)


    def getId(self):
        return self.id
    
    def handleHover(self,reset):
        if reset == "notHover":
            self.color = self.originalColor
        elif reset == "hover":
            self.color = (255,255,255)
        else:
            self.color = (0,0,0)