from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.padding import Padding


class Outils:
    def __init__(self) -> None:
        pass

    def get_player_hand_image(self, card_list: list):
        CARD_PER_ROW = 6
        table = Table(
            show_header=False, box=None, collapse_padding=True, expand=True, leading=1
        )
        condition = True
        counter = 1
        while condition:
            row_list = []

            for _ in range(CARD_PER_ROW):
                card = card_list.pop()
                row_list.append(
                    Panel(
                        Padding(
                            f"{card['value']} {self.suit_to_symbol(card['suit'])} ",
                            (1, 0),
                            expand=True,
                        ),
                        subtitle=f"[blue]{counter}[/blue]",
                    ),
                )
                if len(card_list) == 0:
                    condition = False
                counter += 1

            table.add_row(*row_list)
        return table

    def suit_to_symbol(self, suit):
        data = {
            "clubs": "♣",
            "spades": "♤",
            "hearts": "♥",
            "diamonds": "♦",
            "meta": "M",
            "joker": "J",
        }
        return data[suit]
