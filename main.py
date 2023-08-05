from src.game_setup import GameSetup
from src.game import Game


if __name__ == '__main__':
	players = GameSetup()
	game = Game(players.nicknames)

