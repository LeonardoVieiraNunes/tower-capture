import pygame
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Escudeiro import Escudeiro
from Mapa import Mapa
from Torre import Torre
from Controladora import Controladora

class Game:

    def __init__(self, interface_jogador):
        self.interface = interface_jogador
        pygame.init()
        self.SCREENSIZE = {"width":900,"height":500}
        self.WINDOW = pygame.display.set_mode((self.SCREENSIZE["width"],self.SCREENSIZE["height"]))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 24
        self.run = True
        self.control = None
        self.mapaAtual = None
        self.partida_em_andamento = False
        self.control = Controladora(self)

    def config_entidades(self):
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
        arqueiro_p1 = Arqueiro(config_arqueiro_p1, 1, 1, self)
        escudeiro_p1 = Escudeiro(config_escudeiro_p1, 2, 1, self)
        guerreiro_p1 = Guerreiro(config_guerreiro_p1, 3, 1, self)
        torre_p1 = Torre(config_torre_p1, 4, 1, self)

        pos_arqueiro_p2 = (1, 6)
        config_arqueiro_p2 = {"x": 225 + pos_arqueiro_p2[1] * 70, "y": 135 + pos_arqueiro_p2[0] * 70, "size": (70, 70)}
        pos_escudeiro_p2 = (2, 5)
        config_escudeiro_p2 = {"x": 225 + pos_escudeiro_p2[1] * 70, "y": 135 + pos_escudeiro_p2[0] * 70, "size": (70, 70)}
        pos_guerreiro_p2 = (3, 6)
        config_guerreiro_p2 = {"x": 225 + pos_guerreiro_p2[1] * 70, "y": 135 + pos_guerreiro_p2[0] * 70, "size": (70, 70)}
        pos_torre_p2 = (2, 7)
        config_torre_p2 = {"x": 225 + pos_torre_p2[1] * 70, "y": 135 + pos_torre_p2[0] * 70, "size": (70, 70)}

        arqueiro_p2 = Arqueiro(config_arqueiro_p2, 5, 2, self)
        escudeiro_p2 = Escudeiro(config_escudeiro_p2, 6, 2, self)
        guerreiro_p2 = Guerreiro(config_guerreiro_p2, 7, 2, self)
        torre_p2 = Torre(config_torre_p2, 8, 2, self)

        # Adiciona personagens ao mapa
        self.mapaAtual.addEntityToPosition(pos_arqueiro_p1, arqueiro_p1)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p1, escudeiro_p1)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p1, guerreiro_p1)
        self.mapaAtual.addEntityToPosition(pos_torre_p1, torre_p1)

        self.mapaAtual.addEntityToPosition(pos_arqueiro_p2, arqueiro_p2)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p2, escudeiro_p2)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p2, guerreiro_p2)
        self.mapaAtual.addEntityToPosition(pos_torre_p2, torre_p2)

    def setup(self):
        self.mapaAtual = Mapa(self)
        self.config_entidades()


    def game_loop(self):
        pygame.display.set_caption("Tower Capture!")


        while self.run:
            self.CLOCK.tick(self.FPS)

            for event in pygame.event.get():
                exit = self.interface.click(event)
                # jogado handle de exit aqui
                if exit:
                    pygame.quit()
                    return

            if self.control.partida_em_andamento:
                self.mapaAtual.mouseHover()
                self.mapaAtual.draw()

            pygame.display.update()
