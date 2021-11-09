import pygame
from Controladora import Controladora
from random import randint

class Entidade(pygame.sprite.Sprite):
    entidadeSelecionada = None

    def __init__(self, gridConfig, id):
        super().__init__()
        self.id = id
        self.originalColor = (randint(0,255),randint(0,255),randint(0,255))
        self.color = self.originalColor
        self.image = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),gridConfig["size"]), gridConfig["size"])
        self.rect = self.image.get_rect()
        self.rect.x = gridConfig["x"]
        self.rect.y = gridConfig["y"]
        self.clicked = False
    
    def draw(self):
        Controladora.GAME.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        pygame.draw.rect(Controladora.GAME.WINDOW,self.color,self.rect,10)
    
    def checkCollision(self,mousePos):
        if(self.rect.collidepoint(mousePos)):
            return True
        return False
    
    def checkClick(self,mousePos,event):
        if(self.checkCollision(mousePos)):
            if Entidade.entidadeSelecionada:
                if Entidade.entidadeSelecionada.id == self.id:
                    print(f"Repetiu clique em {self.id}, desativou")
                    self.clicked = False
                    Entidade.entidadeSelecionada = None
                else:
                    Entidade.entidadeSelecionada.clicked = False
                    print(f"Ativar mudanca de rota de {Entidade.entidadeSelecionada.id} para {self.id}")
                    Entidade.entidadeSelecionada = None
                    self.clicked = False
                    pass
            else:
                print(f"Clique inicial em {self.id}")
                self.clicked = True
                Entidade.entidadeSelecionada = self
                    

    
    def checkHover(self, mousePos):
        if not self.clicked:
            if(self.checkCollision(mousePos)):
                self.color = (255,255,255)
            else:
                self.color = self.originalColor
        else:
            self.color = (0, 0, 0)
