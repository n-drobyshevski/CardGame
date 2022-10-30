from random import randint
from time import sleep

from src.cli.Console import Console
from src.Player import Player
from src.Game import Game


def initialize():
    game = Game(player_names=["first", "second", "third", "fourth"])
    console = Console()

    # choose first playing player
    index = randint(0, 3)  # only exemple, needs to be changed
    game.first_playing_player = game.players[index]

    return game, console


def main(game, console):
    console.clear()
    # ---------------------------------------- just some test things, change it

    # ------------------- GAME LOGIC -----------------------
    current_player = game.get_next_player()
    # ------------------ SET NEW DATA -----------------------
    console.set_info_data(data=game.round)
    console.set_table_data(data=game.table)
    console.set_current_player_data(
        data=current_player.hand, player_name=current_player.name
    )

    # ------------------ UPDATE LAYOUT ---------------------
    console.update()

    # ------------------ USER INPUT ------------------------
    card_index = console.askInt("choose a card")

    # ------------------ GAME LOGIC ------------------------

    # remove card from player hand and add it to game.table
    game.table.append(
        (current_player.put_card_from_hand(card_index - 1), current_player)
    )

    return True, game, console


if __name__ == "__main__":
    # INITIALIZING GAME
    game, console = initialize()

    # MAIN LOOP

    condition = True
    while condition:
        condition, game, console = main(game, console)
