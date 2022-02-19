import pygame
from Game import Game
from Jogador import Jogador
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Escudeiro import Escudeiro
from Mapa import Mapa
from Torre import Torre
from Controladora import Controladora


class InterfaceJogador:

    def __init__(self):
        self.game = Game(self)

    def click(self, event:pygame.event):
        if event.type == pygame.QUIT:
            return True

        elif event.type == pygame.MOUSEBUTTONDOWN and (
                event.button == 1 or event.button == 3 or event.button == 2):
            mouse_pos = pygame.mouse.get_pos()
            if self.game.mapaAtual.rect.collidepoint(mouse_pos):
                self.game.mapaAtual.handle_click(mouse_pos)
            elif self.game.control.rect_sidebar.collidepoint(mouse_pos):
                self.game.control.handle_click(mouse_pos)




