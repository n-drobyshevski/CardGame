from .config.types import CardSuitsType, CardValuesType
from .config.constants import CARD_BORDER_COLOR, CARD_VALUE_COLOR


class Card:
    def __init__(
        self, value: CardValuesType, suit: CardSuitsType, card_id: int
    ) -> None:
        # try to toggle type for suits
        self.suit: CardSuitsType = suit
        self.value: CardValuesType = value
        self.id: int = card_id

    # do we really need this method?
    # def get_data(self) -> CardDataType:
    #     res: CardDataType = {"id": self.card_id, "value": self.value, "suit": self.suit}
    #     return res

    def suit_to_symbol(self) -> str:
        """returns symbol of card suit"""
        data = {
            "clubs": "♣",
            "spades": "♤",
            "hearts": "[red]♥[/red]",
            "diamonds": "[red]♦[/red]",
            "metacard": "[magenta]M[/magenta]",
            "joker": "[magenta]J[/magenta]",
        }
        return data[self.suit]

    def __repr__(self) -> str:
        res = f" {self.suit_to_symbol()}[{CARD_VALUE_COLOR}]{self.value}[/{CARD_VALUE_COLOR}]"
        if len(self.value) > 1:
            res = res[1:]
        return res

    def __str__(self) -> str:
        res = f" {self.suit_to_symbol()}[{CARD_VALUE_COLOR}]{self.value}[/{CARD_VALUE_COLOR}]"
        if len(self.value) > 1:
            res = res[1:]
        return res


class MetaCard(Card):
    def __init__(self, value: str, card_id: int) -> None:
        super().__init__(value=value, card_id=card_id, suit="metacard")
