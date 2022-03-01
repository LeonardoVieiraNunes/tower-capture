import pygame
from Entidade import Entidade

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
        self.vencedor = None
        self.score = {
            1:3,
            2:3
        }

    def trocar_turno(self):
        if self.game.mapaAtual.estadoJogada > 1:
            self.vez_jogador = 3 - self.vez_jogador
            self.nro_turno += 1
            self.game.mapaAtual.estadoJogada = 0
            self.game.mapaAtual.resetPosicoesValidas()
        else:
            warningText = "Você precisa realizar alguma ação antes de passar turno!"
            self.game.currentWarning = warningText
            self.game.shouldWarningInLoop = True

        if self.partida_com_vencedor:
            self.game.tela_final({"vencedor":3 - self.vez_jogador,"turno":self.nro_turno})

    def removerEntidade(self,entidade):
        self.game.mapaAtual.removerEntidadePorID(entidade.id)
        if entidade.tipo == 'torre':
            self.partida_com_vencedor = True
        else:
            self.score[3 - self.get_vez_jogador()] -=1
            if self.score[3 - self.get_vez_jogador()] ==0:
                self.partida_com_vencedor = True

    def get_vez_jogador(self):
        return self.vez_jogador

    def get_turno(self):
        return self.nro_turno

    def handle_click(self, mousepos):
        if not self.partida_em_andamento and self.btn_iniciar_jogo.collidepoint(mousepos):
            self.game.setup()
            self.partida_em_andamento = True

        elif self.partida_em_andamento and self.btn_passar_turno.collidepoint(mousepos):
            self.trocar_turno()

    def calcular_dano(self, atacante:Entidade, defensor:Entidade):
        dano_em_defesa = defensor.defesa - atacante.ataque
        if dano_em_defesa < 0:
            defensor.defesa = 0
            defensor.vida -= abs(dano_em_defesa)
        else:
            defensor.defesa = dano_em_defesa

        if defensor.vida <= 0:
            self.removerEntidade(defensor)



