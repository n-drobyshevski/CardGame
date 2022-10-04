from random import randint
from .Card import Card
from .cli.cardsOutils import Outils
from .config.types import (
    CardDataType,
    CardSuitsType,
    CardValuesType,
    PlayerDataType,
    PlayerHandType,
)

outils = Outils()


class Player:
    def __init__(self, init_hand: PlayerHandType, position: str) -> None:
        self.hand = init_hand
        self.position = position
        self.id = self.create_id()
        self.role = "player-role"
        self.hand_image = outils.get_player_hand_image(self.hand)

    def get_data(self) -> PlayerDataType:
        """Returns player data"""
        return {"id": self.id, "hand": self.hand}

    def take_card(self, deck):
        pass

    def put_card(self, card_id):
        """delete card from self.hand and returns it"""
        for i in len(self.hand):
            if self.hand[i].card_id == card_id:
                return self.hand.pop(i)
        return None

    def has_card(self, value: CardValuesType, suit: CardSuitsType) -> bool:
        """checks if provided card is in the player hand"""
        for i in len(self.hand):
            if self.hand[i].value == value and self.hand[i].suit == suit:
                return True
        else:
            return False

    def create_id(self) -> int:
        return randint(0, 9999)

    def __repr__(self) -> str:
        return f"Player: {self.id}"

    def __str__(self) -> str:
        return f"Player: {self.id}"
