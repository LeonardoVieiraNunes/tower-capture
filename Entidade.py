import pygame

config_personagens = {
        'arqueiro': {'vida':20, 'ataque':15, 'defesa':10, 'rangeAtaque':3, 'rangeMovimentacao':2},
        "guerreiro":{'vida':25, 'ataque':20, 'defesa':10, 'rangeAtaque':1, 'rangeMovimentacao':3},
        "escudeiro":{'vida':30, 'ataque':10, 'defesa':30, 'rangeAtaque':1, 'rangeMovimentacao':2},
        'torre':{'vida':100, 'ataque':0, 'defesa':0, 'rangeAtaque':0, 'rangeMovimentacao':0}

    }

class Entidade():
    def __init__(self, gridConfig, id, idJogador, game, tipo_personagem):
        super().__init__()
        self.idJogador = idJogador
        self.id = id
        self.gridConfig = gridConfig
        self.game = game
        self.originalColor = (0,0,255)
        self.color = self.originalColor

        # usa imagem de fundo transparente como default ( não fica totalmente transparente mas blz)
        self.image_path = "images/shaded grid.png"

        self.vida = None
        self.ataque = None
        self.defesa = None
        self.range_movimentacao = None
        self.range_ataque = None
        self.tipo = tipo_personagem
        self.get_atributos(tipo_personagem)

        self.image = pygame.image.load(self.image_path)
        self.size = self.image.get_size()
        if 'torre' in self.image_path:
            self.image = pygame.transform.scale(self.image, (int(self.size[0] * 4.3), int(self.size[1] * 4.4)))
        else:
            self.image = pygame.transform.scale(self.image, (int(self.size[0] * 2.1), int(self.size[1] * 2)))

    def get_atributos(self, tipo):
        self.image_path = f'images/{tipo}.png'

        self.vida = config_personagens[tipo]['vida']
        self.ataque = config_personagens[tipo]['ataque']
        self.defesa = config_personagens[tipo]['defesa']
        self.range_movimentacao = config_personagens[tipo]['rangeMovimentacao']
        self.range_ataque = config_personagens[tipo]['rangeAtaque']
    
    def draw(self):
        self.game.WINDOW.blit(self.image, (self.gridConfig["x"],self.gridConfig["y"]))            
        
    def getId(self):
        return self.id