from rich.pretty import pprint
from src.Game import Game
from src.cli import test

game = Game()


# pprint(game.deck)

# print(game.get_random_card())
pprint([player.get_data() for player in game.players])
test.test()
