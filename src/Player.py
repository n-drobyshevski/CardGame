from random import randint
from .Card import Card
from .config.types import CardSuitsType, CardValuesType, PlayerRoles


class Player:
    def __init__(self, init_hand: list[Card], name: str) -> None:
        self.hand = init_hand
        self.name = name  # not used
        self.id = self.create_id()

        self.role: PlayerRoles = ""  # not used

    def put_card_from_hand(self, index: int) -> Card:
        """get card from 'index' position in player hand"""
        if index <= len(self.hand):
            return self.hand.pop(index)
        else:
            raise Exception("given position is outside of player hand")

    def put_card_by_id(self, card_id):
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
        return f"Player: id-{self.id}, name-{self.name}"

    def __str__(self) -> str:
        return f"Player: id-{self.id}, name-{self.name}"
