import pygame
from Controladora import Controladora
from Entidade import Entidade

class Posicao():

    def __init__(self,dimensions, matrixLocation):
        super().__init__()
        self.dimensions = dimensions
        self.matrixLocation = matrixLocation
        self.id = "C-"+str((matrixLocation[0]*9)+matrixLocation[1])
        self.entidade = None
        self.colorNotOcupied = (100,100,100)
        self.colorOcupied = (0,0,255)
        self.color = self.colorNotOcupied
        self.image = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile2.png"),dimensions["size"]), dimensions["size"])
        self.rect = self.image.get_rect()
        self.rect.x = dimensions["x"]
        self.rect.y = dimensions["y"]
        self.clicked = False

    def draw(self):
        if Controladora.GAME.mapaAtual.posicoesValidas:
            if Controladora.GAME.mapaAtual.posicoesValidas[self.matrixLocation[0]][self.matrixLocation[1]] != 9:
                self.color = (0,255,0)
            else:
                self.color = (100,100,100)
        else:
            self.color = (100,100,100)

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
            if event.button == 2:
                if self.entidade:
                    print(f"{self.entidade.id} ", end="")
                print(self.id)
            elif event.button == 1:
                if Controladora.GAME.mapaAtual.posicaoSelecionada:
                    if Controladora.GAME.mapaAtual.posicaoSelecionada.id == self.id:
                        self.clicked = False
                        Posicao.casaSelecionada = None
                        Controladora.GAME.mapaAtual.resetPosicoesValidas()
                    else:
                        if Controladora.GAME.mapaAtual.validForSwapPositions(Controladora.GAME.mapaAtual.posicaoSelecionada,self):
                            Controladora.GAME.mapaAtual.posicaoSelecionada.entidade.movimentar(self)
                else:
                    if self.entidade:
                        self.clicked = True
                        Controladora.GAME.mapaAtual.posicaoSelecionada = self
                        Controladora.GAME.mapaAtual.getValidPositionsForMovement()
    
    def checkHover(self, mousePos):
        # if self.entidade:
        #     if not self.clicked:
        #         if(self.checkCollision(mousePos)):
        #             self.entidade.handleHover("hover")
        #         else:
        #             self.entidade.handleHover("notHover")
        #     else:
        #         self.entidade.handleHover("clicked")
        # else:
        #     if(self.checkCollision(mousePos)):
        #         self.color = (255,255,255)
        #     else:
        #         self.color = (100,100,100)
        pass