from rich.pretty import pprint
from Game import Game

game = Game


# pprint(game.deck)

# print(game.get_random_card())
pprint([player.get_data() for player in game.players])
