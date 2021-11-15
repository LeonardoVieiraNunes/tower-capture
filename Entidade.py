import pygame
from Controladora import Controladora

class Entidade():
    def __init__(self, gridConfig, id, owner):
        super().__init__()
        self.owner = owner
        self.id = id
        self.gridConfig = gridConfig
        self.originalColor = (0,0,255)
        self.color = self.originalColor

        # usa imagem de fundo transparente como default ( não fica totalmente transparente mas blz)
        image_path = "images/shaded grid.png"
        self.image = pygame.image.load(image_path)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))

    def draw(self):
        Controladora.GAME.WINDOW.blit(self.image, (self.gridConfig["x"],self.gridConfig["y"]))

    def getId(self):
        return self.id
    
    # def handleHover(self,reset):
    #     if reset == "notHover":
    #         self.color = self.originalColor
    #     elif reset == "hover":
    #         self.color = (255,255,255)
    #     else:
    #         self.color = (0,0,0)