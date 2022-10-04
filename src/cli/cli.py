import os

from rich.text import Text
from rich import print
from rich.layout import Layout
from rich.panel import Panel


class Cli:
    def __init__(self) -> None:
        self.layout = self.init_layout()

    def init_layout(self):
        layout = Layout()
        layout.split_column(
            Layout(name="top"), Layout(name="center"), Layout(name="bottom")
        )
        layout["top"].split_row(
            Layout(name="top_right"),
            Layout(name="top_center"),
            Layout(name="top_left"),
        )
        layout["center"].split_row(
            Layout(name="center_right"),
            Layout(name="center_center"),
            Layout(name="center_left"),
        )
        layout["bottom"].split_row(
            Layout(name="bottom_right"),
            Layout(name="bottom_center"),
            Layout(name="bottom_left"),
        )
        # layout["top_center"].size = 45
        return layout

    def print_layout(self):
        print(self.layout)

    def update_layout(self, players: list):
        """data format: [{position: str, content:str}, {...}]"""
        for player in players:
            self.layout[player.position].update(
                Panel(
                    player.hand_image,
                    title=f"[red]Player:{player.id}[/red]",
                    subtitle=f"[magenta]{player.role}[/]",
                )
            )

    def clear_console(self):
        os.system("cli")
