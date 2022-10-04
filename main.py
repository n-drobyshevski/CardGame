from rich.pretty import pprint
from src.cli.cardsOutils import Outils
from src.cli.cli import Cli
from src.Game import Game

game = Game()
cli = Cli()
outils = Outils()


game.create_players()
cli.update_layout(game.players)
cli.print_layout()
