import pygame
from Mapa import Mapa
from Entidade import Entidade
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
        self.partida_em_andamento = False
        self.control = Controladora(self)
        self.currentWarning = None
        self.shouldWarningInLoop = None
        self.fontWarning = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.lastWarning = None
        self.btn_iniciar_jogo = pygame.Rect(269, 317, 346, 91)
        self.backgroundImage = pygame.image.load("./images/back-menu.png")
        self.WINDOW.blit(self.backgroundImage, (0, 0))
        self.fontShop = pygame.font.Font(pygame.font.get_default_font(), 13)
        self.fontGrid = pygame.font.Font(pygame.font.get_default_font(), 18)
        self.tileImage = pygame.transform.scale(
            pygame.transform.scale(pygame.image.load("./images/tile3.png"), (140, 140)), (140, 140))

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
        arqueiro_p1 = Entidade(config_arqueiro_p1, 1, 1, self, 'arqueiro')
        escudeiro_p1 = Entidade(config_escudeiro_p1, 2, 1, self, "escudeiro")
        guerreiro_p1 = Entidade(config_guerreiro_p1, 3, 1, self, "guerreiro")
        torre_p1 = Entidade(config_torre_p1, 4, 1, self, "torre")

        pos_arqueiro_p2 = (1, 6)
        config_arqueiro_p2 = {"x": 225 + pos_arqueiro_p2[1] * 70, "y": 135 + pos_arqueiro_p2[0] * 70, "size": (70, 70)}
        pos_escudeiro_p2 = (2, 5)
        config_escudeiro_p2 = {"x": 225 + pos_escudeiro_p2[1] * 70, "y": 135 + pos_escudeiro_p2[0] * 70, "size": (70, 70)}
        pos_guerreiro_p2 = (3, 6)
        config_guerreiro_p2 = {"x": 225 + pos_guerreiro_p2[1] * 70, "y": 135 + pos_guerreiro_p2[0] * 70, "size": (70, 70)}
        pos_torre_p2 = (2, 7)
        config_torre_p2 = {"x": 225 + pos_torre_p2[1] * 70, "y": 135 + pos_torre_p2[0] * 70, "size": (70, 70)}

        arqueiro_p2 = Entidade(config_arqueiro_p2, 5, 2, self, 'arqueiro')
        escudeiro_p2 = Entidade(config_escudeiro_p2, 6, 2, self, 'escudeiro')
        guerreiro_p2 = Entidade(config_guerreiro_p2, 7, 2, self, 'guerreiro')
        torre_p2 = Entidade(config_torre_p2, 8, 2, self, 'torre')

        # Adiciona personagens ao mapa
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_arqueiro_p1, arqueiro_p1)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_escudeiro_p1, escudeiro_p1)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_guerreiro_p1, guerreiro_p1)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_torre_p1, torre_p1)

        self.mapaAtual.adicionarEntidadeEmPosicao(pos_arqueiro_p2, arqueiro_p2)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_escudeiro_p2, escudeiro_p2)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_guerreiro_p2, guerreiro_p2)
        self.mapaAtual.adicionarEntidadeEmPosicao(pos_torre_p2, torre_p2)


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
                exit = self.click(event)
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

    def drawHUD(self):
        text_surface = self.fontGrid.render(f"Turno do jogador: {self.control.get_vez_jogador()}", True,
                                            (255, 255, 255))
        self.WINDOW.blit(text_surface, (225, 115))

        text_surface = self.fontGrid.render(f"Turno: {self.control.get_turno()}", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (770, 115))

    def drawSideBar(self):
        self.WINDOW.blit(self.mapaAtual.backgroundImageShop, (0, 0))

        text_surface = self.fontShop.render("Posição selecionada:", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (10, 12))
        self.WINDOW.blit(self.tileImage, (10, 30))

        if self.mapaAtual.personagemSelecionado and self.mapaAtual.personagemSelecionado.entidade is not None:
            text_surface = self.fontShop.render(f"Vida: {self.mapaAtual.personagemSelecionado.entidade.vida}", True,
                                                (255, 255, 255))
            self.WINDOW.blit(text_surface, (10, 180))

            text_surface = self.fontShop.render(f"Defesa: {self.mapaAtual.personagemSelecionado.entidade.defesa}", True,
                                                (255, 255, 255))
            self.WINDOW.blit(text_surface, (10, 195))

            text_surface = self.fontShop.render(
                f"Movimentação: {self.mapaAtual.personagemSelecionado.entidade.range_movimentacao}", True, (255, 255, 255))
            self.WINDOW.blit(text_surface, (10, 210))

            text_surface = self.fontShop.render(f"Ataque: {self.mapaAtual.personagemSelecionado.entidade.ataque}", True,
                                                (255, 255, 255))
            self.WINDOW.blit(text_surface, (10, 225))

            text_surface = self.fontShop.render(
                f"Alcance de ataque: {self.mapaAtual.personagemSelecionado.entidade.range_ataque}", True, (255, 255, 255))
            self.WINDOW.blit(text_surface, (10, 240))

            self.WINDOW.blit(pygame.transform.scale(
                self.mapaAtual.personagemSelecionado.entidade.image,
                (self.mapaAtual.personagemSelecionado.entidade.size[0] * 3.5, self.mapaAtual.personagemSelecionado.entidade.size[1] * 3.5)
            ), (14, 40))

        pygame.draw.rect(self.WINDOW, (107, 107, 107), (10, 440, 140, 50))
        text_surface = self.fontGrid.render(f"Passar turno", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (25, 457))

    def tela_final(self, content):
        backgroundImage = pygame.image.load("./images/back-end.png")
        fontMain = pygame.font.Font(pygame.font.get_default_font(), 65)
        fontText = pygame.font.Font(pygame.font.get_default_font(), 35)

        self.WINDOW.blit(backgroundImage, (0, 0))

        text_surface = fontMain.render("Fim de jogo!", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (100, 150))

        jogadorId = content["vencedor"]
        turno = content["turno"]
        text_surface = fontText.render(f"Jogador {jogadorId} no turno {turno}", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (100, 250))

        text_surface = fontText.render("Reinicie para uma nova partida!", True, (255, 255, 255))
        self.WINDOW.blit(text_surface, (100, 290))

    def click(self, event:pygame.event):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3 or event.button == 2):
            mouse_pos = pygame.mouse.get_pos()

            if not self.control.partida_em_andamento:
                if self.btn_iniciar_jogo.collidepoint(mouse_pos):
                    self.control.handle_click(mouse_pos)
            else:
                if self.control.rect_sidebar.collidepoint(mouse_pos):
                    self.control.handle_click(mouse_pos)

                elif self.mapaAtual.rect.collidepoint(mouse_pos) and self.control.partida_em_andamento:
                    self.mapaAtual.handle_click(mouse_pos)


