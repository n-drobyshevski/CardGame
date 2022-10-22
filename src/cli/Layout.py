from rich.layout import Layout
from rich import print

TABLE_HEIGHT = 15
PLAYER_HEIGHT = 25
INFO_HEIGHT = 5


class GameLayout:
    def __init__(self) -> None:
        self.layout = self._initialize_layout()

    def _initialize_layout(self) -> Layout:
        layout = Layout()
        layout.size = 100
        # print(layout)
        layout.split_column(
            Layout(name="info"),
            Layout(name="table"),
            Layout(name="player"),
        )
        layout["info"].size = INFO_HEIGHT
        layout["table"].size = TABLE_HEIGHT
        layout["player"].size = PLAYER_HEIGHT
        return layout
