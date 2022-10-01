from .config.types import CardDataType


class Card:
    # Ajoute ID
    def __init__(self, value: str, card_type: str, card_id: int) -> None:
        self.card_type = card_type
        self.value = value
        self.card_id = card_id

    # def get_card(self):
    def __repr__(self) -> str:
        return f"value: {self.value}, type:{self.card_type}"

    def __str__(self) -> str:
        return f"value: {self.value}, type:{self.card_type}"

    def get_data(self) -> CardDataType:
        return {self.card_id: {"value": {self.value}, "type": {self.card_type}}}


class MetaCard(Card):
    def __init__(self, value: str, card_id: int) -> None:
        super().__init__(value=value, card_id=card_id, card_type="META")
