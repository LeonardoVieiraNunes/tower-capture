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

        self.backgroundImage = pygame.image.load("./images/mapaBackground.png")
        self.backgroundImageShop = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/shopBackground.png"),(180,500)), (180,500))
        self.game = game
        self.estadoJogada = 0
        self.posicoesValidas = None
        self.posicoesValidasAtaque = None
        self.personagemSelecionado = None
        self.posicaoSelecionadaAndar = None
        self.posicaoSelecionadaAtaque = None

        self.configPosicoes()
    
    def resetPosicoesValidas(self, posicao = None):
        self.posicoesValidas = None
        self.posicoesValidasAtaque = None


    def getValidPositionsForMovement(self):
        posicaoTemp = self.personagemSelecionado
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


    def validaAndar(self, fromTarget, toTarget):
        warningText = ""
        
        if not self.estadoJogada > 1:
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
    
    def configPosicoes(self):
        # self.game.WINDOW.blit(self.backgroundImage, (0, 0))
        self.game.WINDOW.fill((107,107,107))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tempConfig = self.gridConfig.copy()
                tempConfig["x"] += j*tempConfig["size"][0]
                tempConfig["y"] += i*tempConfig["size"][1]
                self.grid[i][j] = Posicao(tempConfig, (i, j), self.game)
        return

    def drawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].draw()

    def draw(self):
        self.game.WINDOW.fill((107,107,107))

        self.mousePos = pygame.mouse.get_pos()

        self.game.drawSideBar()
        self.game.drawHUD()
        self.drawGrid()

    def handle_click(self, mousepos):
        posicao_x = int((mousepos[0]-self.gridConfig['x']) / 70)
        posicao_y = int((mousepos[1]-self.gridConfig['y']) / 70)
        posicao_selecionada = (posicao_y, posicao_x)
        if self.estadoJogada == 0:
            self.selecionarPersonagem(posicao_selecionada)
        elif self.estadoJogada == 1:
            self.selecionarPosicao(posicao_selecionada)
        elif self.estadoJogada == 2:
            self.atacar(posicao_selecionada)

    def atacar(self, posicao):
        self.posicaoSelecionadaAtaque = self.grid[posicao[0]][posicao[1]]
        if self.validarAtaque(self.posicaoSelecionadaAndar, self.posicaoSelecionadaAtaque):
            self.game.control.calcular_dano(self.posicaoSelecionadaAndar.entidade, self.posicaoSelecionadaAtaque.entidade)
            self.game.control.trocar_turno()
        else:
            self.posicaoSelecionadaAtaque = None
            return

    def getPosicoesAtaque(self):
        posicaoTemp = self.game.mapaAtual.posicaoSelecionadaAndar
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

    def validarAtaque(self, fromTarget, toTarget):
        warningText = ""

        if self.posicoesValidasAtaque[toTarget.matrixLocation[0]][toTarget.matrixLocation[1]] <= fromTarget.entidade.range_ataque:
            if toTarget.entidade == None:
                warningText = "Não existe um alvo a ser atacado nesta posição!"
            else:
                if toTarget.entidade.idJogador != self.game.control.get_vez_jogador():
                    return True
                else:
                    warningText = "A posição de ataque selecionada é seu aliado!"
        else:
            warningText = "Ataque não realizado, FORA DO SEU ALCANCE!"

        self.game.currentWarning = warningText
        self.game.shouldWarningInLoop = True
        return False

    def selecionarPersonagem(self, posicao):
        entidade = self.grid[posicao[0]][posicao[1]].getEntidade()
        if entidade is not None:
            if entidade.idJogador == self.game.control.get_vez_jogador():
                self.personagemSelecionado = self.grid[posicao[0]][posicao[1]]
                self.getValidPositionsForMovement()
                self.estadoJogada += 1
            else:
                warningText = "Esse personagem nao é válido"
                self.game.currentWarning = warningText
                self.game.shouldWarningInLoop = True

    def selecionarPosicao(self, posicao):
        posicao_alvo = self.grid[posicao[0]][posicao[1]]

        if self.grid[posicao[0]][posicao[1]] == self.personagemSelecionado:
            # acao de cancelar
            self.resetPosicoesValidas()
            self.personagemSelecionado = None
            self.estadoJogada = 0

        elif self.validaAndar(self.personagemSelecionado, posicao_alvo):
            self.andar(posicao_alvo)

        else:
            return None


    def andar(self, posicaoAlvo):
        self.posicaoSelecionadaAndar = posicaoAlvo
        self.personagemSelecionado.entidade, self.posicaoSelecionadaAndar.entidade = self.posicaoSelecionadaAndar.entidade, self.personagemSelecionado.entidade
        if self.personagemSelecionado.entidade:
            self.personagemSelecionado.entidade.gridConfig = self.personagemSelecionado.dimensions
        if self.posicaoSelecionadaAndar.entidade:
            self.posicaoSelecionadaAndar.entidade.gridConfig = self.posicaoSelecionadaAndar.dimensions

        self.resetPosicoesValidas()
        self.getPosicoesAtaque()
        self.estadoJogada += 1



    def adicionarEntidadeEmPosicao(self, pos:tuple, entity):
        self.grid[pos[0]][pos[1]].setEntidade(entity)

    def removerEntidadePorID(self, id):
        for indexI, line in enumerate(self.grid):
            for indexJ, entity in enumerate(line):
                if entity.entidade != None and entity.entidade.id == id:
                    self.grid[indexI][indexJ].entidade = None

