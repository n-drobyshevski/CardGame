from typing import Tuple
from .Section import Section

from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from ...Card import Card
from ...Player import Player
from ...config.constants import CARD_BORDER_COLOR


class TableSection(Section):
    def __init__(self, data):
        super().__init__(data)

    def render(self):
        res = ""
        if isinstance(self.data, str):
            res = self.data

        # if self.data == list[Tuple[Card, Player]]
        elif isinstance(self.data, list) and all(
            isinstance(x, Tuple) for x in self.data
        ):
            # if all first elements of all tuples are instances of Card class
            if all(isinstance(y[0], Card) for y in self.data):
                hand = self.data

                cards_list = []
                table = Table.grid(expand=True)  # table used for layout
                table.add_column()

                for tuple in hand:
                    card = tuple[0]
                    cards_list.append(
                        Panel.fit(
                            str(card),
                            padding=(2, 1),
                            border_style=CARD_BORDER_COLOR,
                            subtitle=(
                                tuple[1].name[:2]
                                if isinstance(tuple[1], Player)
                                else ""
                            ),
                        )
                    )

                table.add_row(*cards_list)

                res = table

        else:
            res = str(self.data)
        return Panel(Align.center(res), padding=(4, 0))
