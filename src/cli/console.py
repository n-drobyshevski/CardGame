import os
from ..Card import Card

# layout objects
from .Layout import GameLayout
from .sections.Section import Section
from .sections.TableSection import TableSection
from .sections.CurrentPlayerSection import CurrentPlayerSection
from .sections.InfoSection import InfoSection


from rich import print
from rich.prompt import Prompt, IntPrompt


class Console:
    """_summary_
    class for working with command line interface
    """

    def __init__(self) -> None:
        self.width: int = os.get_terminal_size()[0]
        self.height: int = os.get_terminal_size()[1]

        self.gameLayout = GameLayout()
        self.layout = self.gameLayout.layout

        self.info_section: Section = InfoSection("")
        self.table_section: Section = TableSection("")
        self.current_player_section: Section = CurrentPlayerSection("", "")

    # --------------------------------------------------------------------------------------
    def clear(self) -> None:
        os.system("cls")

    # --------------------------------------------------------------------------------------
    # METHODS FOR USER INTERACTION
    def ask(
        self, msg: str, choices: list = [], default: str = "", show_default=False
    ) -> str:
        res = Prompt.ask(
            msg, choices=choices, default=default, show_default=show_default
        )
        return res

    def askInt(
        self, msg: str, choices: list = [], default: int = 0, show_default=False
    ) -> int:
        res = IntPrompt.ask(
            msg, choices=choices, default=default, show_default=show_default
        )
        return res

    # ---------------------------------------------------------------------------------------
    # METHODS TO SET DATA

    def set_info_data(self, data):
        self.info_section.set_data(data)

    def set_table_data(self, data):
        self.table_section.set_data(data)

    def set_current_player_data(self, data):
        self.current_player_section.set_data(data)

    # ----------------------------------------------------------------------------------------
    def update(self):
        self.layout["info"].update(self.info_section.render())

        self.layout["table"].update(self.table_section.render())

        self.layout["player"].update(self.current_player_section.render())

        print(self.layout)
