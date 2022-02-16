import pygame
from Jogador import Jogador
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Escudeiro import Escudeiro
from Mapa import Mapa
from Torre import Torre
from Controladora import Controladora

class Game:

    def __init__(self):
        pygame.init()
        self.SCREENSIZE = {"width":900,"height":500}
        self.WINDOW = pygame.display.set_mode((self.SCREENSIZE["width"],self.SCREENSIZE["height"]))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 24
        self.run = True
        self.control = None
        self.mapaAtual = None
        self.jogador1 = None
        self.jogador2 = None

    def setup(self):
        pygame.display.set_caption("Tower Capture!")

        self.mapaAtual = Mapa(self)
        self.control = Controladora()

        self.jogador1 = Jogador(1)
        self.jogador2 = Jogador(2)

        # posicoes iniciais e configs
        # modelo de posicao: (linha,coluna)
        pos_arqueiro_p1 = (1, 2)
        config_arqueiro_p1 = {"x": 225 + pos_arqueiro_p1[1] * 70, "y": 135 + pos_arqueiro_p1[0] * 70, "size": (70, 70)}
        pos_escudeiro_p1 = (2, 3)
        config_escudeiro_p1 = {"x": 225 + pos_escudeiro_p1[1] * 70, "y": 135 + pos_escudeiro_p1[0] * 70, "size": (70, 70)}
        pos_guerreiro_p1 = (3, 2)
        config_guerreiro_p1 = {"x": 225 + pos_guerreiro_p1[1] * 70, "y": 135 + pos_guerreiro_p1[0] * 70, "size": (70, 70)}
        pos_torre_p1 = (2, 1)
        config_torre_p1 = {"x": 225 + pos_torre_p1[1] * 70, "y": 135 + pos_torre_p1[0] * 70, "size": (70, 70)}

        # instancias de personagens
        arqueiro_p1 = Arqueiro(config_arqueiro_p1, 1, self.jogador1.id, self)
        escudeiro_p1 = Escudeiro(config_escudeiro_p1, 2, self.jogador1.id, self)
        guerreiro_p1 = Guerreiro(config_guerreiro_p1, 3, self.jogador1.id, self)
        # Classe de torre ainda não implementada
        torre_p1 = Torre(config_torre_p1, 4, self.jogador1.id, self)

        # Adiciona personagens ao mapa
        self.mapaAtual.addEntityToPosition(pos_arqueiro_p1, arqueiro_p1)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p1, escudeiro_p1)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p1, guerreiro_p1)
        self.mapaAtual.addEntityToPosition(pos_torre_p1, torre_p1)

        self.jogador1.setEntidades([arqueiro_p1, escudeiro_p1, guerreiro_p1, torre_p1])

        pos_arqueiro_p2 = (1, 6)
        config_arqueiro_p2 = {"x": 225 + pos_arqueiro_p2[1] * 70, "y": 135 + pos_arqueiro_p2[0] * 70, "size": (70, 70)}
        pos_escudeiro_p2 = (2, 5)
        config_escudeiro_p2 = {"x": 225 + pos_escudeiro_p2[1] * 70, "y": 135 + pos_escudeiro_p2[0] * 70, "size": (70, 70)}
        pos_guerreiro_p2 = (3, 6)
        config_guerreiro_p2 = {"x": 225 + pos_guerreiro_p2[1] * 70, "y": 135 + pos_guerreiro_p2[0] * 70, "size": (70, 70)}
        pos_torre_p2 = (2, 7)
        config_torre_p2 = {"x": 225 + pos_torre_p2[1] * 70, "y": 135 + pos_torre_p2[0] * 70, "size": (70, 70)}

        arqueiro_p2 = Arqueiro(config_arqueiro_p2, 5, self.jogador2.id, self)
        escudeiro_p2 = Escudeiro(config_escudeiro_p2, 6, self.jogador2.id, self)
        guerreiro_p2 = Guerreiro(config_guerreiro_p2, 7, self.jogador2.id, self)
        torre_p2 = Torre(config_torre_p2, 8, self.jogador2.id, self)

        self.mapaAtual.addEntityToPosition(pos_arqueiro_p2, arqueiro_p2)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p2, escudeiro_p2)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p2, guerreiro_p2)
        self.mapaAtual.addEntityToPosition(pos_torre_p2, torre_p2)

        self.jogador2.setEntidades([arqueiro_p2, escudeiro_p2, guerreiro_p2, torre_p2])


        while self.run:
            self.CLOCK.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3 or event.button == 2):
                    self.mapaAtual.mouseClick(event)

            self.mapaAtual.mouseHover()
            self.mapaAtual.draw()

            pygame.display.update()
            
        pygame.quit()