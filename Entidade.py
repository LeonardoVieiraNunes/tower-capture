import pygame
from Game import Game
from random import randint

class Entidade:
    def __init__(self, posicao, tamanho):
        self.vida = randint(10,100)
        self.tamanho = tamanho
        self.posicao = posicao
        self.color = (0, 0, 0)
        self.sprite = pygame.Rect(
            self.posicao["x"], self.posicao["y"], 
            self.tamanho["width"], self.tamanho['height'])
        self.backgroundImage = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),(70,70)), (70,70))

    def draw(self):
        Game.WINDOW.blit(self.backgroundImage, (self.posicao["x"], self.posicao["y"]))
        pygame.draw.rect(Game.WINDOW, self.color, self.sprite, 1)
    
    def checkCollision(self,mousePos):
        if(self.sprite.collidepoint(mousePos)):
            return True
        return False
    
    def checkClick(self,mousePos):
        if(self.checkCollision(mousePos)):
            print(self.vida)
    
    def checkHover(self, mousePos):
        if(self.checkCollision(mousePos)):
            self.color = (255,255,255)
        else:
            self.color = (0, 0, 0)

            