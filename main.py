from time import sleep

from src.cli.console import Console
from src.Player import Player
from src.Game import Game


def main(game: Game, console: Console):
    console.clear()

    current_player = game.players[0]
    game.round += 1

    # set new data
    console.set_info_data(game.round)
    console.set_table_data("table")
    console.set_current_player_data(current_player.hand)
    # Updated layout
    console.update()

    # remove card from player hand and add it to game.table
    # card_index = console.askInt("choose a card (by index)")
    # if card_index <= len(current_player.hand):
    #     game.table.append(current_player.hand[card_index])

    return False


if __name__ == "__main__":
    # Initializing game
    game = Game()
    console = Console()
    game.create_players()

    condition = True
    while condition:
        condition = main(game, console)
