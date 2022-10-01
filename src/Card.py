from .config.types import CardDataType


class Card:
    # Ajoute ID
    def __init__(self, value: str, card_suit: str, card_id: int) -> None:
        self.card_suit = card_suit
        self.value = value
        self._card_id = card_id

    # def get_card(self):
    def __repr__(self) -> str:
        return f"id : {self._card_id} value: {self.value}, suit:{self.card_suit}"

    def __str__(self) -> str:
        return f"id: {self._card_id} value: {self.value}, suit:{self.card_suit}"

    def get_data(self) -> CardDataType:
        return {"id": self._card_id, "value": self.value, "suit": self.card_suit}

    def get_id(self) -> int:
        return self._card_id


class MetaCard(Card):
    def __init__(self, value: str, card_id: int) -> None:
        super().__init__(value=value, card_id=card_id, card_suit="meta")
