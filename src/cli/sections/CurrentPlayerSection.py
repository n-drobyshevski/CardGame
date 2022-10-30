from .Section import Section
from typing import Optional
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.align import Align
from ...Card import Card

from ...config.constants import CARD_BORDER_COLOR

# from ...config.types import is_card_list


class CurrentPlayerSection(Section):
    def __init__(self, data):
        super().__init__(data)
        self.data = data
        self.player_name: Optional[str] = None

    def set_data(self, data, player_name=None):
        # self.data = data
        self.player_name = player_name
        super().set_data(data)

    def render(self):

        # check if passed data is player_hand
        res = ""
        if isinstance(self.data, str):
            res = self.data
        elif isinstance(self.data, list) and all(
            isinstance(x, Card) for x in self.data
        ):
            hand = self.data

            cards_list = []
            table = Table.grid(expand=True)  # table used for layout
            table.add_column()

            card_index = 0
            for card in hand:
                card_index += 1
                cards_list.append(
                    Panel.fit(
                        str(card),
                        padding=(2, 1),
                        subtitle=f"{card_index}",
                        border_style=CARD_BORDER_COLOR,
                    )
                )

            table.add_row(*cards_list[: len(cards_list) // 2])
            table.add_row(*cards_list[len(cards_list) // 2 :])

            res = table
        else:
            res = str(self.data)

        return Align.center(
            Panel.fit(
                res,
                title=f"Player: {self.player_name}",
                padding=(2, 0),
                box=box.SIMPLE_HEAD,
            )
        )
