from .Section import Section

from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from ...Card import Card
from ...config.constants import CARD_BORDER_COLOR


class TableSection(Section):
    def __init__(self, data):
        super().__init__(data)

    def render(self):
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

            for card in hand:
                cards_list.append(
                    Panel.fit(
                        str(card),
                        padding=(2, 1),
                        border_style=CARD_BORDER_COLOR,
                    )
                )

            table.add_row(*cards_list)

            res = table
        else:
            res = str(self.data)
        return Panel(Align.center(res), padding=(4, 0))
