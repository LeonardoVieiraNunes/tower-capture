import pygame

class Controladora:
    GAME = None

    def __init__(self, game):
        self.vez_jogador = 1  # 1 para jogador da esquerda, 2 para jogador da direita
        self.nro_turno = 1
        self.game = game

    def trocar_turno(self):
        self.vez_jogador = 3 - self.vez_jogador
        self.nro_turno += 1


    def get_vez_jogador(self):
        return self.vez_jogador

    def get_turno(self):
        return self.nro_turno




