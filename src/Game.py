from random import randint
from .Player import Player
from .Card import Card, MetaCard


from .config.constants import (
    CARD_TYPES,
    CARD_VALUES,
    METACARD_VALUES,
    CARD_QUANTITY,
    CARD_ID,
)
from .config.types import CardDataType
from .config.types import PlayerHandType


class Game:
    def __init__(self) -> None:
        self.players_count = 4
        self.deck = self.create_deck()
        self.players = self.create_players()

    def create_deck(self) -> list:
        current_card_id = 0
        deck = []
        for tp in CARD_TYPES[:4]:
            for vl in CARD_VALUES:
                card = Card(value=vl, card_type=tp, card_id=CARD_ID[current_card_id])
                current_card_id += 1
                deck.append(card.get_data())

        for vl in METACARD_VALUES:
            card = MetaCard(value=vl, card_id=CARD_ID[current_card_id])
            current_card_id += 1
            deck.append(card.get_data())

        joker = Card(value="JOKER", card_type="JOKER", card_id=CARD_ID[current_card_id])
        deck.append(joker.get_data())
        return deck

    def get_random_card(self) -> CardDataType:
        card_index = randint(0, len(self.deck) - 1)
        card = self.deck[card_index]
        self.deck.pop(card_index)
        return card

    def create_player_hand(self) -> PlayerHandType:
        return [self.get_random_card() for _ in range(18)]

    def compare_cards(self):
        pass

    def create_players(self) -> list:
        return [Player(self.create_player_hand()) for _ in range(4)]