import pygame
from Controladora import Controladora
from Posicao import Posicao

class Mapa():
    def __init__(self):
        self.grid = [[None for i in range(9)] for j in range(5)]
        self.gridConfig = {"x":225,"y":135,"size":(70,70)}
        self.mousePos = (0,0)
        self.tileImage = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile3.png"),(140,140)), (140,140))
        self.backgroundImage = pygame.image.load("./images/mapaBackground.png")
        self.backgroundImageShop = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/shopBackground.png"),(180,500)), (180,500))
        self.posicoesValidas = None
        self.posicaoSelecionada = None
        self.fontShop = pygame.font.Font(pygame.font.get_default_font(), 13)
        self.fontGrid = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.setup()
    
    def resetPosicoesValidas(self, posicao = None):
        Controladora.GAME.mapaAtual.posicaoSelecionada.clicked = False
        Controladora.GAME.mapaAtual.posicaoSelecionada = None
        if posicao:
            posicao.clicked = False
        self.posicoesValidas = None

    def getValidPositionsForMovement(self):
        posicaoTemp = Controladora.GAME.mapaAtual.posicaoSelecionada
        posicoesValidas = [[9 for i in range(9)] for j in range(5)]
        for moviRange in range(1,posicaoTemp.entidade.range_movimentacao+1):
            posicoesValidasTemp = posicoesValidas.copy()
            posicoesValidasTemp[posicaoTemp.matrixLocation[0]][posicaoTemp.matrixLocation[1]] = 0
            for indexI,i  in enumerate(posicoesValidasTemp):
                for indexJ,j  in enumerate(i):
                    if j == moviRange-1:
                        try:
                            if indexI+1 < 5 and posicoesValidasTemp[indexI+1][indexJ]:
                                posicoesValidasTemp[indexI+1][indexJ] = moviRange
                            if indexI-1 >= 0 and posicoesValidasTemp[indexI-1][indexJ]:
                                posicoesValidasTemp[indexI-1][indexJ] = moviRange
                            if indexJ+1 < 9 and posicoesValidasTemp[indexI][indexJ+1]:
                                posicoesValidasTemp[indexI][indexJ+1] = moviRange
                            if indexJ-1 >= 0 and posicoesValidasTemp[indexI][indexJ-1]:
                                posicoesValidasTemp[indexI][indexJ-1] = moviRange
                        except Exception:
                            print("Exception")
            posicoesValidas = posicoesValidasTemp

        self.posicoesValidas = posicoesValidas              


    def validForSwapPositions(self,fromTarget,toTarget):
        if self.posicoesValidas[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_movimentacao:           
            return True
        return False
    
    def swapPositions(self,fromTarget,toTarget):
        if self.posicoesValidas[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_movimentacao and toTarget.entidade is None:
            fromTarget.entidade, toTarget.entidade = toTarget.entidade, fromTarget.entidade

            if fromTarget.entidade:
                fromTarget.entidade.gridConfig = fromTarget.dimensions
            if toTarget.entidade:
                toTarget.entidade.gridConfig = toTarget.dimensions
            
            return True
        return False

    def setup(self):
        # Controladora.GAME.WINDOW.blit(self.backgroundImage, (0, 0))
        Controladora.GAME.WINDOW.fill((107,107,107))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tempConfig = self.gridConfig.copy()
                tempConfig["x"] += j*tempConfig["size"][0]
                tempConfig["y"] += i*tempConfig["size"][1]
                self.grid[i][j] = Posicao(tempConfig, (i, j))
        return
    def drawSideBar(self):
        Controladora.GAME.WINDOW.blit(self.backgroundImageShop, (0, 0))
        
        text_surface = self.fontShop.render("Posição selecionada:", True, (255,255,255))
        Controladora.GAME.WINDOW.blit(text_surface, (10, 12))
        Controladora.GAME.WINDOW.blit(self.tileImage, (10, 30))
        
        if self.posicaoSelecionada:
            text_surface = self.fontShop.render(f"Vida: {self.posicaoSelecionada.entidade.vida}", True, (255,255,255))
            Controladora.GAME.WINDOW.blit(text_surface, (10, 180))
            
            text_surface = self.fontShop.render(f"Defesa: {self.posicaoSelecionada.entidade.defesa}", True, (255,255,255))
            Controladora.GAME.WINDOW.blit(text_surface, (10, 195))
            
            text_surface = self.fontShop.render(f"Movimentação: {self.posicaoSelecionada.entidade.range_movimentacao}", True, (255,255,255))
            Controladora.GAME.WINDOW.blit(text_surface, (10, 210))
            
            text_surface = self.fontShop.render(f"Ataque: {self.posicaoSelecionada.entidade.ataque}", True, (255,255,255))
            Controladora.GAME.WINDOW.blit(text_surface, (10, 225))
            
            Controladora.GAME.WINDOW.blit(pygame.transform.scale(
                self.posicaoSelecionada.entidade.image, 
                (self.posicaoSelecionada.entidade.size[0]*3.5,self.posicaoSelecionada.entidade.size[1]*3.5)
            ), (14, 40))
        
        pygame.draw.rect(Controladora.GAME.WINDOW, (107,107,107), (10,440,140,50))
        text_surface = self.fontGrid.render(f"Passar turno", True, (255,255,255))
        Controladora.GAME.WINDOW.blit(text_surface, (25, 457))

        

    def drawGrid(self):
        text_surface = self.fontGrid.render("Turno do jogador: 1", True, (255,255,255))
        Controladora.GAME.WINDOW.blit(text_surface, (225, 115))
        
        text_surface = self.fontGrid.render("Turno: 3", True, (255,255,255))
        Controladora.GAME.WINDOW.blit(text_surface, (770, 115))
        
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].draw()

    def draw(self):
        self.mousePos = pygame.mouse.get_pos()

        self.drawSideBar()
        self.drawGrid()

    def mouseClick(self,event):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].checkClick(self.mousePos,event)

    def mouseHover(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].checkHover(self.mousePos)

    def addEntityToPosition(self,pos:tuple,entity):
        self.grid[pos[0]][pos[1]].setEntidade(entity)
