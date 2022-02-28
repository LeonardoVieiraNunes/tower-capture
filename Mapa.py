from logging import warning
import pygame
from Controladora import Controladora
from Posicao import Posicao
from Entidade import Entidade

class Mapa():
    def __init__(self, game):
        self.grid = [[None for i in range(9)] for j in range(5)]
        self.gridConfig = {"x":225,"y":135,"size":(70,70)}
        self.rect = pygame.Rect(225, 135, 70*9, 70*5)
        self.mousePos = (0,0)
        self.tileImage = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile3.png"),(140,140)), (140,140))
        self.backgroundImage = pygame.image.load("./images/mapaBackground.png")
        self.backgroundImageShop = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/shopBackground.png"),(180,500)), (180,500))
        self.game = game
        self.posicoesValidas = None
        self.posicoesValidasAtaque = None
        self.posicaoSelecionada = None
        self.posicaoSelecionadaTempAtaque = None
        self.fontShop = pygame.font.Font(pygame.font.get_default_font(), 13)
        self.fontGrid = pygame.font.Font(pygame.font.get_default_font(), 18)
        self.setup()
    
    def resetPosicoesValidas(self, posicao = None):
        self.game.mapaAtual.posicaoSelecionada.clicked = False
        self.game.mapaAtual.posicaoSelecionada = posicao
        
        self.posicoesValidas = None
        self.posicoesValidasAtaque = None
                
        if posicao:
            self.game.mapaAtual.getValidPositionsForAttack()

    def getValidPositionsForMovement(self):
        posicaoTemp = self.game.mapaAtual.posicaoSelecionada
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
    
    def getValidPositionsForAttack(self):
        posicaoTemp = self.game.mapaAtual.posicaoSelecionada
        posicoesValidas = [[9 for i in range(9)] for j in range(5)]
        for moviRange in range(1,posicaoTemp.entidade.range_ataque+1):
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

        self.posicoesValidasAtaque = posicoesValidas           


    def validForSwapPositions(self,fromTarget,toTarget):
        warningText = ""
        
        if not self.game.jogadores[self.game.control.get_vez_jogador()-1].getAndou():
            if self.posicoesValidas[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_movimentacao:           
                if toTarget.entidade is None:
                    return True
                else:
                    if toTarget.entidade.idJogador != self.game.jogadores[self.game.control.get_vez_jogador()-1].id:
                        fromTarget.entidade.atacar(toTarget)
                    else:
                        warningText = "A posição selecionada se encontra OCUPADA!"
            else:
                warningText = "A posição selecionada se encontra FORA DO SEU ALCANCE!"
        else:
            warningText = "Você ja se movimentou, não é possivel escolher outro personagem!"

        self.game.currentWarning = warningText
        self.game.shouldWarningInLoop = True
        return False
    
    def validForAttack(self,fromTarget,toTarget):
        warningText = ""
        
        if not self.game.jogadores[self.game.control.get_vez_jogador()-1].getAtacou():
            if self.posicoesValidasAtaque[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_ataque:           
                if toTarget.entidade == None:
                    warningText = "Não existe um alvo a ser atacado nesta posição!"
                else:
                    if toTarget.entidade.idJogador != self.game.jogadores[self.game.control.get_vez_jogador()-1].id:
                        return True
                    else:
                        warningText = "A posição de ataque selecionada é seu aliado!"
            else:
                warningText = "Ataque não realizado, FORA DO SEU ALCANCE!"
        else:
            warningText = "Não é possivel realizar novos ataques, PASSAR TURNO!"

        self.game.currentWarning = warningText
        self.game.shouldWarningInLoop = True
        return False
    
    def swapPositions(self,fromTarget,toTarget):
        if self.posicoesValidas[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_movimentacao:
            fromTarget.entidade, toTarget.entidade = toTarget.entidade, fromTarget.entidade

            if fromTarget.entidade:
                fromTarget.entidade.gridConfig = fromTarget.dimensions
            if toTarget.entidade:
                toTarget.entidade.gridConfig = toTarget.dimensions
            
            self.game.jogadores[self.game.control.get_vez_jogador()-1].setAndou()
            return True
        return False
    
    def realizarAtaque(self,posicao):        
        posicao.entidade.receberDano(self.posicaoSelecionada.entidade.ataque)
        self.game.jogadores[self.game.control.get_vez_jogador()-1].setAtacou()
        self.game.control.trocar_turno()

    def setup(self):
        # self.game.WINDOW.blit(self.backgroundImage, (0, 0))
        self.game.WINDOW.fill((107,107,107))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tempConfig = self.gridConfig.copy()
                tempConfig["x"] += j*tempConfig["size"][0]
                tempConfig["y"] += i*tempConfig["size"][1]
                self.grid[i][j] = Posicao(tempConfig, (i, j), self.game)
        return
    def drawSideBar(self):
        self.game.WINDOW.blit(self.backgroundImageShop, (0, 0))
        
        text_surface = self.fontShop.render("Posição selecionada:", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (10, 12))
        self.game.WINDOW.blit(self.tileImage, (10, 30))
        
        if self.posicaoSelecionada:
            text_surface = self.fontShop.render(f"Vida: {self.posicaoSelecionada.entidade.vida}", True, (255,255,255))
            self.game.WINDOW.blit(text_surface, (10, 180))
            
            text_surface = self.fontShop.render(f"Defesa: {self.posicaoSelecionada.entidade.defesa}", True, (255,255,255))
            self.game.WINDOW.blit(text_surface, (10, 195))
            
            text_surface = self.fontShop.render(f"Movimentação: {self.posicaoSelecionada.entidade.range_movimentacao}", True, (255,255,255))
            self.game.WINDOW.blit(text_surface, (10, 210))
            
            text_surface = self.fontShop.render(f"Ataque: {self.posicaoSelecionada.entidade.ataque}", True, (255,255,255))
            self.game.WINDOW.blit(text_surface, (10, 225))
            
            text_surface = self.fontShop.render(f"Alcance de ataque: {self.posicaoSelecionada.entidade.range_ataque}", True, (255,255,255))
            self.game.WINDOW.blit(text_surface, (10, 240))
            
            self.game.WINDOW.blit(pygame.transform.scale(
                self.posicaoSelecionada.entidade.image, 
                (self.posicaoSelecionada.entidade.size[0]*3.5,self.posicaoSelecionada.entidade.size[1]*3.5)
            ), (14, 40))
        
        pygame.draw.rect(self.game.WINDOW, (107,107,107), (10,440,140,50))
        text_surface = self.fontGrid.render(f"Passar turno", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (25, 457))

        

    def drawGrid(self):
        text_surface = self.fontGrid.render(f"Turno do jogador: {self.game.control.get_vez_jogador()}", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (225, 115))
        
        text_surface = self.fontGrid.render(f"Turno: {self.game.control.get_turno()}", True, (255,255,255))
        self.game.WINDOW.blit(text_surface, (770, 115))
        
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].draw()

    def draw(self):
        self.game.WINDOW.fill((107,107,107))

        self.mousePos = pygame.mouse.get_pos()

        self.drawSideBar()
        self.drawGrid()

    def handle_click(self, mousepos, event):
        self.mouseClick(mousepos, event)
        self.mouseHover(mousepos)

    def mouseClick(self,mousepos,event):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].checkClick(mousepos,event)

    def mouseHover(self,mousepos):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].checkHover(mousepos)

    def addEntityToPosition(self,pos:tuple,entity):
        self.grid[pos[0]][pos[1]].setEntidade(entity)
    
    def removeEntityByID(self,id):
        for indexI, line in enumerate(self.grid):
            for indexJ, entity in enumerate(line):
                if entity.entidade != None and entity.entidade.id == id:
                    self.grid[indexI][indexJ].entidade = None
                    
    def checkIfPlayerLost(self, playerId):
        count = 0
        for indexI, line in enumerate(self.grid):
            for indexJ, entity in enumerate(line):
                if entity.entidade != None and (entity.entidade.id % 4 != 0) and entity.entidade.idJogador == playerId:
                    count += 1
        # return True
        if count > 0:
            return False
        else:
            return True