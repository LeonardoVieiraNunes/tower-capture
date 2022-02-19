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
            return
        elif event.type == pygame.MOUSEBUTTONDOWN and (
                event.button == 1 or event.button == 3 or event.button == 2):
            mouse_pos = pygame.mouse.get_pos()
            if self.game.mapaAtual.rect.collidepoint(mouse_pos):
                print('pog?')
                self.game.mapaAtual.mouseClick(event)
            elif self.game.control.rect_sidebar.collidepoint(mouse_pos):
                print('cog!')

            self.game.mapaAtual.mouseHover()
            self.game.mapaAtual.draw()

            pygame.display.update()


