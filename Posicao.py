import pygame
import random
from Controladora import Controladora
from Entidade import Entidade

class Posicao():

    def __init__(self,dimensions, matrixLocation, game):
        super().__init__()
        self.dimensions = dimensions
        self.matrixLocation = matrixLocation
        self.id = "C-"+str((matrixLocation[0]*9)+matrixLocation[1])
        self.entidade = None
        self.colorNotOcupied = (100,100,100)
        self.colorOcupied = (0,0,255)
        self.color = self.colorNotOcupied
        self.angles = [0,90,180]
        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.transform.scale(
                    pygame.image.load(
                        "./images/tile3.png"),
                    dimensions["size"]), 
                    dimensions["size"]
                ),
                random.choice(self.angles)
            )
        self.rect = self.image.get_rect()
        self.rect.x = dimensions["x"]
        self.rect.y = dimensions["y"]
        self.clicked = False
        self.game = game

    def draw(self):
        if self.game.mapaAtual.posicoesValidas:
            if self.game.mapaAtual.posicoesValidas[self.matrixLocation[0]][self.matrixLocation[1]] != 9:
                self.color = (0,255,0)
            else:
                self.color = (100,100,100)
        else:
            self.color = (100,100,100)
        
        if self.entidade:
            if self.game.control.get_vez_jogador() == self.entidade.idJogador:
                self.color = (182,182,182)

        self.game.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        pygame.draw.rect(self.game.WINDOW,self.color,(self.dimensions["x"],self.dimensions["y"],self.dimensions["size"][0],self.dimensions["size"][1]),1)
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
                if self.game.mapaAtual.posicaoSelecionada:
                    if self.game.mapaAtual.posicaoSelecionada.id == self.id:
                        self.clicked = False
                        Posicao.casaSelecionada = None
                        self.game.mapaAtual.resetPosicoesValidas()
                    else:
                        if self.game.mapaAtual.validForSwapPositions(self.game.mapaAtual.posicaoSelecionada,self):
                            self.game.mapaAtual.posicaoSelecionada.entidade.movimentar(self)
                else:
                    if self.entidade and self.entidade.range_movimentacao:
                        self.clicked = True
                        if self.entidade.idJogador == self.game.control.get_vez_jogador():
                            self.game.mapaAtual.posicaoSelecionada = self
                            self.game.mapaAtual.getValidPositionsForMovement()
                        else:
                            warningText = "Esse personagem nao eh seu, seu vagabundo!"
                            self.game.currentWarning = warningText
                            self.game.shouldWarningInLoop = True

    
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