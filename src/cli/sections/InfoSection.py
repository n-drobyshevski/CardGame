from .Section import Section
from rich.panel import Panel
from rich.align import Align


class InfoSection(Section):
    def __init__(self, data):
        super().__init__(data)

    def render(self):
        res = ""
        if isinstance(self.data, str):
            res = self.data
        else:
            res = str(self.data)

        return Panel(Align.center(res))
