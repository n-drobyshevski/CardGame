from random import randint
from .Card import Card
from .config.types import (
    CardDataType,
    CardSuitsType,
    CardValuesType,
    PlayerDataType,
)


class Player:
    def __init__(self, init_hand: list[Card], position: str) -> None:
        self.hand = init_hand
        self.position = position
        self.id = self.create_id()
        self.role = "player-role"

    def get_data(self) -> PlayerDataType:
        """Returns player data"""
        return {"id": self.id, "hand": self.hand}

    def take_card(self, deck):
        pass

    def put_card(self, card_id):
        """delete card from self.hand and returns it"""
        for i in range(len(self.hand)):
            if self.hand[i].id == card_id:
                return self.hand.pop(i)
        return None

    def has_card(self, value: CardValuesType, suit: CardSuitsType) -> bool:
        """checks if provided card is in the player hand"""
        for i in range(len(self.hand)):
            current_card = self.hand[i]
            if current_card.value == value and current_card.suit == suit:
                return True
        else:
            return False

    def create_id(self) -> int:
        return randint(0, 9999)

    def __repr__(self) -> str:
        return f"Player: {self.id}"

    def __str__(self) -> str:
        return f"Player: {self.id}"
