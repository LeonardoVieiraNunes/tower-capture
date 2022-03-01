import pygame
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Escudeiro import Escudeiro
from Mapa import Mapa
from Menu import Menu
from MenuFinal import MenuFinal
from Torre import Torre
from Jogador import Jogador
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
        self.menu = Menu(self)
        self.menuFinal = MenuFinal(self)
        self.partida_em_andamento = False
        self.partida_com_vencedor = False
        self.control = Controladora(self)
        self.currentWarning = None
        self.shouldWarningInLoop = None
        self.fontWarning = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.lastWarning = None
        self.jogadores = []

    def config_entidades(self):
        jogador1 = Jogador(1)
        jogador2 = Jogador(2)
        
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
        
        jogador1.setEntidades([arqueiro_p1,escudeiro_p1,guerreiro_p1,torre_p1])


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
        
        jogador2.setEntidades([arqueiro_p2,escudeiro_p2,guerreiro_p2,torre_p2])


        # Adiciona personagens ao mapa
        self.mapaAtual.addEntityToPosition(pos_arqueiro_p1, arqueiro_p1)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p1, escudeiro_p1)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p1, guerreiro_p1)
        self.mapaAtual.addEntityToPosition(pos_torre_p1, torre_p1)

        self.mapaAtual.addEntityToPosition(pos_arqueiro_p2, arqueiro_p2)
        self.mapaAtual.addEntityToPosition(pos_escudeiro_p2, escudeiro_p2)
        self.mapaAtual.addEntityToPosition(pos_guerreiro_p2, guerreiro_p2)
        self.mapaAtual.addEntityToPosition(pos_torre_p2, torre_p2)
        
        self.jogadores.append(jogador1)
        self.jogadores.append(jogador2)

    def setup(self):
        self.mapaAtual = Mapa(self)
        self.config_entidades()


    def game_loop(self):
        pygame.display.set_caption("Tower Capture!")
        display_warning = False

        while self.run:
            self.CLOCK.tick(self.FPS)
            
            if self.currentWarning != None and self.shouldWarningInLoop == True:
                display_warning = True
                self.shouldWarningInLoop = False
                self.lastWarning = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                exit = self.interface.click(event)
                # jogado handle de exit aqui
                if exit:
                    pygame.quit()
                    return

            if self.control.partida_em_andamento and not self.control.partida_com_vencedor:
                self.mapaAtual.draw()
            
            if display_warning:
                text_surface = self.fontWarning.render(f"{self.currentWarning}", True, (120,0,0))
                self.WINDOW.blit(text_surface, (225, 15))
                
                if pygame.time.get_ticks() - self.lastWarning > 3000:
                    display_warning = False
                    self.currentWarning = None
                    self.shouldWarningInLoop = None

                
            pygame.display.update()
