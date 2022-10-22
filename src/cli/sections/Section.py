from rich.panel import Panel
from typing import Optional, Any


class Section:
    def __init__(self, data=""):
        self.data = data

    def set_data(self, data):
        self.data = data

    def render(self) -> Panel:
        if self.data:
            res = Panel(str(self.data))
        else:
            raise Exception("None was passed to section data arg")
        return res
