import pygame

class Controladora:


    def __init__(self, game):
        self.vez_jogador = 1  # 1 para jogador da esquerda, 2 para jogador da direita
        self.nro_turno = 1
        self.game = game
        self.rect_sidebar = pygame.Rect(0, 0, 225, 600)
        self.btn_passar_turno = pygame.Rect(10,440,140,50)
        self.btn_iniciar_jogo = pygame.Rect(0,0,900,600)
        self.partida_em_andamento = False
        self.partida_com_vencedor = False

    def trocar_turno(self):
        # self.game.jogadores[self.vez_jogador-1].resetStatus()
        self.vez_jogador = 3 - self.vez_jogador
        self.nro_turno += 1
        self.game.mapaAtual.estadoJogada = 0

        if self.game.jogadores[self.vez_jogador-1].getAndou() or self.game.jogadores[self.vez_jogador-1].getAtacou():
            self.game.jogadores[self.vez_jogador-1].resetStatus()
            self.vez_jogador = 3 - self.vez_jogador
            self.nro_turno += 1
            self.game.mapaAtual.resetPosicoesValidas()
        else:
            warningText = "Você precisa realizar alguma ação antes de passar turno!"
            self.game.currentWarning = warningText
            self.game.shouldWarningInLoop = True

        if self.game.mapaAtual.checkIfPlayerLost(self.vez_jogador):
            self.partida_com_vencedor = True

            self.game.menuFinal.setup({"vencedor":self.game.jogadores[3 - self.vez_jogador-1],"turno":self.nro_turno})

    def removerEntidade(self,entidade):
        self.game.mapaAtual.removeEntityByID(entidade.id)

    def get_vez_jogador(self):
        return self.vez_jogador

    def get_turno(self):
        return self.nro_turno

    def handle_click(self, mousepos):
        print("Input passado para controladora")
        if not self.partida_em_andamento and self.btn_iniciar_jogo.collidepoint(mousepos):
            self.game.setup()
            self.partida_em_andamento = True
            print('Iniciar partida')

        elif self.partida_em_andamento and self.btn_passar_turno.collidepoint(mousepos):
            self.trocar_turno()
            print('trocar turno')


