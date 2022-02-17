import pygame
from Jogador import Jogador
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Escudeiro import Escudeiro
from Mapa import Mapa
from Torre import Torre
from Controladora import Controladora


class InterfaceJogador:

    def __init__(self):
        pygame.init()
        self.SCREENSIZE = {"width": 900, "height": 500}
        self.WINDOW = pygame.display.set_mode((self.SCREENSIZE["width"], self.SCREENSIZE["height"]))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 24
        self.run = True
        self.control = None
        self.mapaAtual = None

        self.arqueiro_p1 = None
        self.escudeiro_p1 = None
        self.guerreiro_p1 = None
        self.torre_p1 = None

        self.arqueiro_p2 = None
        self.escudeiro_p2 = None
        self.guerreiro_p2 = None
        self.torre_p2 = None

    def config_entidade_jogador1(self):
        pos_arqueiro_p1 = (1, 2)
        config_arqueiro_p1 = {"x": 225 + pos_arqueiro_p1[1] * 70, "y": 135 + pos_arqueiro_p1[0] * 70, "size": (70, 70)}
        pos_escudeiro_p1 = (2, 3)
        config_escudeiro_p1 = {"x": 225 + pos_escudeiro_p1[1] * 70, "y": 135 + pos_escudeiro_p1[0] * 70,
                               "size": (70, 70)}
        pos_guerreiro_p1 = (3, 2)
        config_guerreiro_p1 = {"x": 225 + pos_guerreiro_p1[1] * 70, "y": 135 + pos_guerreiro_p1[0] * 70,
                               "size": (70, 70)}
        pos_torre_p1 = (2, 1)
        config_torre_p1 = {"x": 225 + pos_torre_p1[1] * 70, "y": 135 + pos_torre_p1[0] * 70, "size": (70, 70)}

        # instancias de personagens
        self.arqueiro_p1 = Arqueiro(config_arqueiro_p1, 1, 1, self)
        self.escudeiro_p1 = Escudeiro(config_escudeiro_p1, 2, 1, self)
        self.guerreiro_p1 = Guerreiro(config_guerreiro_p1, 3, 1, self)
        self.torre_p1 = Torre(config_torre_p1, 4, 1, self)

        self.mapaAtual.addEntityToPosition(pos_arqueiro_p1, self.arqueiro_p1)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p1, self.escudeiro_p1)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p1, self.guerreiro_p1)
        self.mapaAtual.addEntityToPosition(pos_torre_p1, self.torre_p1)

    def config_entidade_jogador2(self):
        pos_arqueiro_p2 = (1, 2)
        config_arqueiro_p2 = {"x": 225 + pos_arqueiro_p2[1] * 70, "y": 135 + pos_arqueiro_p2[0] * 70, "size": (70, 70)}
        pos_escudeiro_p2 = (2, 3)
        config_escudeiro_p2 = {"x": 225 + pos_escudeiro_p2[1] * 70, "y": 135 + pos_escudeiro_p2[0] * 70,
                               "size": (70, 70)}
        pos_guerreiro_p2 = (3, 2)
        config_guerreiro_p2 = {"x": 225 + pos_guerreiro_p2[1] * 70, "y": 135 + pos_guerreiro_p2[0] * 70,
                               "size": (70, 70)}
        pos_torre_p2 = (2, 1)
        config_torre_p2 = {"x": 225 + pos_torre_p2[1] * 70, "y": 135 + pos_torre_p2[0] * 70, "size": (70, 70)}

        # instancias de personagens
        self.arqueiro_p2 = Arqueiro(config_arqueiro_p2, 1, 1, self)
        self.escudeiro_p2 = Escudeiro(config_escudeiro_p2, 2, 1, self)
        self.guerreiro_p2 = Guerreiro(config_guerreiro_p2, 3, 1, self)
        self.torre_p2 = Torre(config_torre_p2, 4, 1, self)

        self.mapaAtual.addEntityToPosition(pos_arqueiro_p2, self.arqueiro_p2)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p2, self.escudeiro_p2)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p2, self.guerreiro_p2)
        self.mapaAtual.addEntityToPosition(pos_torre_p2, self.torre_p2)


    def setup(self):
        pygame.display.set_caption("Tower Capture!")
        # instancia Mapa e Controladora
        self.mapaAtual = Mapa(self)
        self.control = Controladora(self)

        # configura entidades dos jogadores
        self.config_entidade_jogador1()
        self.config_entidade_jogador2()

        self.loop_jogo()

        pygame.quit()

    def loop_jogo(self):
        while True:
            self.CLOCK.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and (
                        event.button == 1 or event.button == 3 or event.button == 2):
                    mouse_pos = pygame.mouse.get_pos()
                    if self.mapaAtual.rect.collidepoint(mouse_pos):
                        print('pog?')
                        self.mapaAtual.mouseClick(event)


            self.mapaAtual.mouseHover()
            self.mapaAtual.draw()

            pygame.display.update()


