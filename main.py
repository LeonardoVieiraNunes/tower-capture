from Controladora import Controladora
from Game import Game

if __name__ == "__main__":
    Controladora.GAME = Game()
    Controladora.GAME.setup()