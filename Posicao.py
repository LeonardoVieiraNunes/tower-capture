import pygame
from Controladora import Controladora
from Entidade import Entidade
from random import randint

class Posicao(pygame.sprite.Sprite):
    casaSelecionada = None

    def __init__(self,dimensions,id):
        super().__init__()
        self.dimensions = dimensions
        self.id = "C-"+str(id)
        self.entidade = None
        self.color = (100,100,100)
        self.image = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),dimensions["size"]), dimensions["size"])
        self.rect = self.image.get_rect()
        self.rect.x = dimensions["x"]
        self.rect.y = dimensions["y"]
        self.clicked = False

    def draw(self):
        Controladora.GAME.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        pygame.draw.rect(Controladora.GAME.WINDOW,self.color,(self.dimensions["x"],self.dimensions["y"],self.dimensions["size"][0],self.dimensions["size"][1]),1)
        if self.entidade:
            self.entidade.draw()

    def checkCollision(self,mousePos):
        if(self.rect.collidepoint(mousePos)):
            return True
        return False

    def setEntidade(self,entidade:Entidade):
        self.entidade = entidade

    def checkClick(self,mousePos,event):
        if(self.checkCollision(mousePos)):
            if(event.button == 3):
                if not self.entidade:
                    self.entidade = Entidade(self.dimensions,"E-"+str(randint(0,1000)))
            elif(event.button == 2):
                if self.entidade:
                    print(f"{self.entidade.getId()} ", end="")
                print(self.id)
            elif(event.button == 1):
                if Posicao.casaSelecionada:
                    if Posicao.casaSelecionada.id == self.id:
                        print(f"Repetiu clique em {self.id}, desativou")
                        self.clicked = False
                        Posicao.casaSelecionada = None
                    else:

                        Controladora.GAME.mapaAtual.swapPositions(Posicao.casaSelecionada,self)

                        Posicao.casaSelecionada.clicked = False
                        print(f"Ativar mudanca de rota de {Posicao.casaSelecionada.id} para {self.id}")
                        Posicao.casaSelecionada = None
                        self.clicked = False
                else:
                    print(f"Clique inicial em {self.id}")
                    self.clicked = True
                    Posicao.casaSelecionada = self
    
    def checkHover(self, mousePos):
        if self.entidade:
            if not self.clicked:
                if(self.checkCollision(mousePos)):
                    self.entidade.handleHover("hover")
                else:
                    self.entidade.handleHover("notHover")
            else:
                self.entidade.handleHover("clicked")
        else:
            if(self.checkCollision(mousePos)):
                self.color = (255,255,255)
            else:
                self.color = (100,100,100)