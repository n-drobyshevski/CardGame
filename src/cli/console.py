import os
from typing import Optional

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
        self.gameLayout = GameLayout()
        self.layout = self.gameLayout.layout

        self.info_section: Section = InfoSection("")
        self.table_section: Section = TableSection("")
        self.current_player_section: Section = CurrentPlayerSection("")

    # --------------------------------------------------------------------------------------
    def clear(self) -> None:
        os.system("cls")

    # --------------------------------------------------------------------------------------
    # METHODS FOR USER INTERACTION
    def ask(
        self,
        msg: str,
        choices: Optional[list[str]] = None,
        default: str = "",
        show_default=False,
        show_choices=True,
    ) -> str:
        """Method to ask user for input, returns str"""

        res = Prompt.ask(
            msg,
            choices=choices,
            default=default,
            show_default=show_default,
            show_choices=show_choices,
        )
        return res

    def askInt(
        self,
        msg: str,
        choices: Optional[list[str]] = None,
        default: int = 0,
        show_default=False,
        show_choices=True,
    ) -> int:
        """method to ask user for input returns int"""

        res = IntPrompt.ask(
            msg,
            choices=choices,
            default=default,
            show_default=show_default,
            show_choices=show_choices,
        )
        return res

    # ---------------------------------------------------------------------------------------
    # METHODS TO SET DATA

    def set_info_data(self, data):
        """set data for display in info section"""
        self.info_section.set_data(data)

    def set_table_data(self, data):
        """set data for display in table section"""
        self.table_section.set_data(data)

    def set_current_player_data(self, data, player_name: Optional[str] = None):
        """set data for display in current player section"""
        self.current_player_section.set_data(data, player_name=player_name)  # type: ignore

    # ----------------------------------------------------------------------------------------
    def update(self, info: bool = True, table: bool = True, player: bool = True):
        """
        prints layout composed of sections
        to change content, use set_[]_data() methods
        """
        self.layout["info"].update(self.info_section.render())
        self.layout["info"].visible = info

        self.layout["table"].update(self.table_section.render())
        self.layout["table"].visible = table

        self.layout["player"].update(self.current_player_section.render())
        self.layout["player"].visible = player
        print(self.layout)
