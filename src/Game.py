from random import randint
from .Player import Player
from .Card import Card, MetaCard
from .Deck import Deck

from .config.constants import (
    CARD_SUITS,
    CARD_VALUES,
    METACARD_VALUES,
    CARD_QUANTITY,
    CARD_ID,
    PLAYER_POSITIONS,
)
from .config.types import CardDataType, PlayerHandType


class Game:
    def __init__(self) -> None:
        self.players_count = 4
        self.deck = Deck()
        self.players = self.create_players()

    def get_random_card(self) -> int:
        card_index = randint(0, self.deck.length - 1)
        card = self.deck.get_card_by_id(card_index)
        return card

    def create_player_hand(self) -> PlayerHandType:
        return [self.get_random_card() for _ in range(18)]

    def compare_cards(self):
        pass

    def create_players(self) -> list:
        return [
            Player(self.create_player_hand(), position=PLAYER_POSITIONS[i])
            for i in range(4)
        ]
